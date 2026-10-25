"""Independent permutation-Gram Haar twirls and compiler matrix checks.

The twirl construction uses only permutation matrices and the moments
Tr[rho^tensor k U_pi] = r^(cycles(pi)-k).  It does not use Schur eigenvalues.
The Gram system is solved over Fraction, including its singular cases k>d.
NumPy is used only to assemble finite matrices and check their spectra.
"""

from __future__ import annotations

from fractions import Fraction
from functools import cache
from itertools import permutations, product

import numpy as np

from exact_schur import exact_statistics, fraction_text, require

TOLERANCE = 2e-10
RECORDED_RESIDUALS: list[float] = []


def check_close(actual, expected, label: str) -> float:
    residual = float(np.max(np.abs(np.asarray(actual) - np.asarray(expected))))
    RECORDED_RESIDUALS.append(residual)
    require(residual <= TOLERANCE, f"{label}: residual={residual:.3e}")
    return residual


def cycle_count(permutation: tuple[int, ...]) -> int:
    unseen = set(range(len(permutation)))
    count = 0
    while unseen:
        count += 1
        current = min(unseen)
        while current in unseen:
            unseen.remove(current)
            current = permutation[current]
    return count


@cache
def permutation_indices(permutation: tuple[int, ...], dimension: int):
    k = len(permutation)
    if k == 0:
        return np.array([0], dtype=np.int64)
    coordinates = np.array(list(product(range(dimension), repeat=k)))
    return np.ravel_multi_index(coordinates[:, permutation].T,
                                (dimension,) * k)


def permutation_matrix(permutation: tuple[int, ...], dimension: int):
    indices = permutation_indices(permutation, dimension)
    result = np.zeros((len(indices), len(indices)))
    result[indices, np.arange(len(indices))] = 1
    return result


def rational_solve(matrix: list[list[int]], rhs: list[Fraction]):
    """Consistent square system; free variables are set to zero.

    Permutations become linearly dependent when k>d.  A singular Gram matrix
    is therefore expected, and must not be silently treated as an error.
    """
    size = len(rhs)
    augmented = [[Fraction(value) for value in row] + [value_rhs]
                 for row, value_rhs in zip(matrix, rhs)]
    pivots = []
    row = 0
    for column in range(size):
        pivot = next((i for i in range(row, size)
                      if augmented[i][column]), None)
        if pivot is None:
            continue
        augmented[row], augmented[pivot] = augmented[pivot], augmented[row]
        scale = augmented[row][column]
        augmented[row] = [entry / scale for entry in augmented[row]]
        for i in range(size):
            if i != row and augmented[i][column]:
                scale = augmented[i][column]
                augmented[i] = [entry - scale * pivot_entry
                                for entry, pivot_entry
                                in zip(augmented[i], augmented[row])]
        pivots.append(column)
        row += 1
        if row == size:
            break
    for entries in augmented:
        require(any(entries[:-1]) or entries[-1] == 0,
                "inconsistent permutation-Gram system")
    solution = [Fraction(0)] * size
    for i, column in enumerate(pivots):
        solution[column] = augmented[i][-1]
    require(all(sum(a * x for a, x in zip(entries, solution)) == value
                for entries, value in zip(matrix, rhs)),
            "exact Gram solve residual")
    return solution, len(pivots)


@cache
def twirl(k: int, rank: int, dimension: int):
    group = tuple(permutations(range(k)))
    indices = [permutation_indices(p, dimension) for p in group]
    # Hilbert-Schmidt products computed from the actual permutation action.
    gram = [[int(np.count_nonzero(a == b)) for b in indices] for a in indices]
    moments = [Fraction(rank ** cycle_count(p), rank ** k) for p in group]
    coefficients, gram_rank = rational_solve(gram, moments)
    size = dimension ** k
    result = np.zeros((size, size))
    columns = np.arange(size)
    for coefficient, rows in zip(coefficients, indices):
        result[rows, columns] += float(coefficient)
    check_close(result, result.T, "twirl Hermiticity")
    check_close(np.trace(result), 1, "twirl trace")
    for rows, moment in zip(indices, moments):
        check_close(np.sum(result[columns, rows]), float(moment),
                    "twirl permutation moment")
    require(np.linalg.eigvalsh(result)[0] >= -TOLERANCE, "twirl is not positive")
    result.setflags(write=False)
    return result, gram_rank, len(group)


@cache
def jucys_murphy(n: int, dimension: int):
    size = dimension ** (n + 1)
    result = np.zeros((size, size))
    for i in range(n):
        permutation = list(range(n + 1))
        permutation[i], permutation[n] = permutation[n], permutation[i]
        result += permutation_matrix(tuple(permutation), dimension)
    result.setflags(write=False)
    return result


def positive_projector(matrix):
    values, vectors = np.linalg.eigh(matrix)
    selected = vectors[:, values > TOLERANCE]
    return selected @ selected.conj().T


def tensor_power(matrix, exponent: int):
    result = np.ones((1, 1), dtype=matrix.dtype)
    for _ in range(exponent):
        result = np.kron(result, matrix)
    return result


def matrix_case(n: int, rank: int, dimension: int):
    training, training_gram_rank, _ = twirl(n, rank, dimension)
    h1, joint_gram_rank, permutation_count = twirl(n + 1, rank, dimension)
    h0 = np.kron(training, np.eye(dimension) / dimension)
    j = jucys_murphy(n, dimension)
    identity = np.eye(len(j))
    residuals = {}
    residuals["commutator"] = check_close(h0 @ j, j @ h0, "[H0,J]")
    require(np.linalg.eigvalsh(dimension * identity + j)[0] > 0,
            "dI+J is not positive on the physical tensor space")
    numerator = h0 @ ((dimension / rank) * (rank * identity + j))
    predicted = np.linalg.solve((dimension * identity + j).T, numerator.T).T
    residuals["likelihood"] = check_close(h1, predicted, "matrix likelihood")
    delta = h1 - h0
    success = 0.5 + np.sum(np.abs(np.linalg.eigvalsh(delta))) / 4
    expected = exact_statistics(n, rank, dimension)
    residuals["success"] = check_close(success, float(expected["success"]),
                                       "twirl versus Schur success")
    effect = positive_projector(j)
    sign_success = 0.5 + np.trace(effect @ delta).real / 2
    residuals["rank_blind"] = check_close(sign_success, success,
                                          "positive-J Helstrom rule")
    null_values, null_vectors = np.linalg.eigh(h0)
    kernel_vectors = null_vectors[:, null_values < TOLERANCE]
    residuals["support"] = check_close(kernel_vectors.conj().T @ h1, 0,
                                       "H1 supported inside H0") \
        if kernel_vectors.shape[1] else 0.0
    check_close(np.trace(h0 @ j), float(expected["null_mean_content"]),
                "matrix null first moment")
    check_close(np.trace(h0 @ j @ j), float(expected["null_second_content"]),
                "matrix null second moment")
    rhs = ((dimension - rank) / (rank * dimension ** 2)
           * np.kron(training, np.eye(dimension)) @ j)
    slack = (rhs - delta + (rhs - delta).T) / 2
    slack_min = float(np.linalg.eigvalsh(slack)[0])
    require(slack_min >= -TOLERANCE, "classical operator slack has negative eigenvalue")
    if rank == dimension:
        check_close(h1, h0, "identical full-rank hypotheses")
    # Covariance spot check: two actual fixed subspaces, not only the Haar mean.
    diagonal_state = np.diag([1 / rank] * rank + [0] * (dimension - rank))
    positions = np.arange(dimension)
    fourier = np.exp(2j * np.pi * np.outer(positions, positions) / dimension)
    fourier /= np.sqrt(dimension)
    rotated_state = fourier @ diagonal_state @ fourier.conj().T
    for state in (diagonal_state, rotated_state):
        fixed_difference = np.kron(tensor_power(state, n),
                                   state - np.eye(dimension) / dimension)
        fixed_success = 0.5 + np.trace(effect @ fixed_difference).real / 2
        check_close(fixed_success, success, "fixed-subspace covariant risk")
    return ({"N": n, "r": rank, "d": dimension,
             "joint_matrix_dimension": len(j),
             "training_gram_rank": training_gram_rank,
             "joint_gram_rank": joint_gram_rank,
             "joint_permutation_count": permutation_count,
             "success": fraction_text(expected["success"])},
            max(residuals.values()), min(0.0, slack_min))


def training_basis(n: int, dimension: int):
    if n == 1:
        return np.eye(dimension)
    require(n == 2, "compiler example supports one or two training copies")
    result = np.eye(dimension ** 2)
    # Orthogonal rotations of |00>,|11> and |01>,|10> give informative,
    # genuinely entangled training effects, without random-number generation.
    for a, b, angle in ((0, dimension + 1, np.pi / 6),
                         (1, dimension, np.pi / 8)):
        rotation = np.array([[np.cos(angle), -np.sin(angle)],
                             [np.sin(angle), np.cos(angle)]])
        result[:, [a, b]] = result[:, [a, b]] @ rotation
    return result


def one_body_marginal(matrix, keep: int, n: int, dimension: int):
    labels = list(range(n)) + list(range(n, 2 * n))
    for i in range(n):
        if i != keep:
            labels[n + i] = labels[i]
    return np.einsum(matrix.reshape((dimension,) * (2 * n)), labels,
                     [labels[keep], labels[n + keep]])


def compiler_case(n: int, rank: int, dimension: int):
    training, _, _ = twirl(n, rank, dimension)
    h1, _, _ = twirl(n + 1, rank, dimension)
    h0 = np.kron(training, np.eye(dimension) / dimension)
    delta = h1 - h0
    size = dimension ** n
    reshaped = delta.reshape(size, dimension, size, dimension)
    basis = training_basis(n, dimension)
    train_permutations = [permutation_matrix(p, dimension)
                          for p in permutations(range(n))]
    sum_f = np.zeros_like(training)
    objective = 0.0
    marginal_sum = 0.0
    largest_unsymmetrized_commutator = 0.0
    for vector in basis.T:
        effect = np.outer(vector, vector)
        largest_unsymmetrized_commutator = max(
            largest_unsymmetrized_commutator,
            float(np.max(np.abs(effect @ training - training @ effect))))
        symmetric = sum(p @ effect @ p.T for p in train_permutations)
        symmetric /= len(train_permutations)
        before = np.einsum("ji,iajb->ab", effect, reshaped)
        after = np.einsum("ji,iajb->ab", symmetric, reshaped)
        check_close(before, after, "training symmetrization preserves posterior")
        check_close(symmetric @ training, training @ symmetric,
                    "symmetrized effect commutes with A_N")
        f = symmetric @ training
        check_close(f, f.T, "F_y Hermiticity")
        require(np.linalg.eigvalsh(f)[0] >= -TOLERANCE, "F_y is not positive")
        sum_f += f
        test_effect = positive_projector(after)
        objective += float(np.trace(test_effect @ after).real)
        for i in range(n):
            permutation = list(range(n + 1))
            permutation[i], permutation[n] = permutation[n], permutation[i]
            swap = permutation_matrix(tuple(permutation), dimension)
            left = np.trace(np.kron(f, test_effect) @ swap).real
            right = np.trace(one_body_marginal(f, i, n, dimension)
                             @ test_effect).real
            check_close(left, right, "swap/partial-trace identity")
            require(-TOLERANCE <= right <= np.trace(f) + TOLERANCE,
                    "one-body positivity upper bound")
            marginal_sum += float(right)
    check_close(sum_f, training, "compiler F_y normalization")
    coefficient = Fraction(dimension - rank, rank * dimension ** 2)
    require(objective <= float(coefficient) * marginal_sum + TOLERANCE,
            "compiler trace bound from operator inequality")
    require(marginal_sum <= n + TOLERANCE, "sum of compiler marginal traces")
    require(objective <= float(coefficient * n) + TOLERANCE,
            "classical success advantage bound")
    result = {"N": n, "r": rank, "d": dimension,
              "linear_advantage_bound": fraction_text(coefficient * n / 2)}
    if n == 1:
        exact_advantage = Fraction(dimension - rank,
                                   2 * rank * dimension * (dimension + 1))
        check_close(objective / 2, float(exact_advantage),
                    "one-copy compiled classifier fixture")
        result["compiled_advantage"] = fraction_text(exact_advantage)
    else:
        require(largest_unsymmetrized_commutator > 1e-5,
                "collective example failed to exercise symmetrization")
        require(objective > 1e-5, "collective compiler example is uninformative")
        result["collective_training_effects"] = True
    return result


def rank_mixture_case():
    n, dimension = 3, 3
    weights = ((1, Fraction(1, 5)), (2, Fraction(2, 5)), (3, Fraction(2, 5)))
    delta = np.zeros((dimension ** (n + 1),) * 2)
    for rank, weight in weights:
        training, _, _ = twirl(n, rank, dimension)
        joint, _, _ = twirl(n + 1, rank, dimension)
        delta += float(weight) * (joint - np.kron(training, np.eye(dimension) / dimension))
    effect = positive_projector(jucys_murphy(n, dimension))
    sign_success = 0.5 + np.trace(effect @ delta).real / 2
    optimal_success = 0.5 + np.sum(np.abs(np.linalg.eigvalsh(delta))) / 4
    check_close(sign_success, optimal_success, "rank-mixture optimality")
    expected_success = sum(weight * exact_statistics(n, rank, dimension)["success"]
                           for rank, weight in weights)
    check_close(sign_success, float(expected_success), "rank-mixture risk")
    return {"N": n, "d": dimension,
            "weights": {str(rank): fraction_text(weight) for rank, weight in weights},
            "success": fraction_text(expected_success)}


def run():
    RECORDED_RESIDUALS.clear()
    cases = ((0, 1, 2), (1, 1, 2), (2, 1, 2), (3, 1, 2),
             (2, 2, 3), (3, 2, 3), (2, 2, 4), (3, 2, 4),
             (2, 2, 2))
    fixtures = []
    residual = 0.0
    smallest_slack = 0.0
    for case in cases:
        fixture, case_residual, case_slack = matrix_case(*case)
        fixtures.append(fixture)
        residual = max(residual, case_residual)
        smallest_slack = min(smallest_slack, case_slack)
    compilers = [compiler_case(*case) for case in
                 ((1, 1, 2), (1, 2, 3), (1, 2, 4),
                  (2, 1, 2), (2, 2, 3), (2, 2, 4))]
    rank_mixture = rank_mixture_case()
    return ({"twirl_cases": fixtures, "compiler_cases": compilers,
             "rank_mixture": rank_mixture},
            {"largest_matrix_residual": max(RECORDED_RESIDUALS, default=residual),
             "smallest_operator_slack_eigenvalue": smallest_slack,
             "absolute_tolerance": TOLERANCE})
