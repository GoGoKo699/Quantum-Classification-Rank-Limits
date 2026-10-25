"""Deterministic exact-arithmetic checks of the Schur formulas."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations, product

from exact_schur import (
    branches, exact_statistics, fraction_text, growth, growth_residue,
    majorant, normalized_curve, partitions, require, schur_dimension,
    schur_weight, successors, tableaux,
)


def rsk_shape(word: tuple[int, ...]) -> tuple[int, ...]:
    """Row insertion, independent of hook/content arithmetic."""
    rows: list[list[int]] = []
    for symbol in word:
        current = symbol
        for row in rows:
            position = next((i for i, entry in enumerate(row)
                             if entry > current), len(row))
            if position == len(row):
                row.append(current)
                break
            row[position], current = current, row[position]
        else:
            rows.append([current])
    return tuple(map(len, rows))


def check_shapes() -> int:
    checked = 0
    # Includes nonrectangular diagrams, repeated rows, empty shape and hooks.
    for n in range(13):
        for shape in partitions(n):
            distribution = growth(shape)
            require(sum(q for _, _, q in distribution) == 1,
                    f"growth normalization: {shape}")
            require(sum(q * c for _, c, q in distribution) == 0,
                    f"growth first moment: {shape}")
            require(sum(q * c * c for _, c, q in distribution) == n,
                    f"growth second moment: {shape}")
            for _, content, q in distribution:
                require(q > 0 and q == growth_residue(shape, content),
                        f"hook versus corner-residue probability: {shape}")
            checked += 1
        # Branching dimension follows independently by counting paths.
        if n:
            path_counts: Counter = Counter()
            for parent in partitions(n - 1):
                for child, _ in successors(parent):
                    path_counts[child] += tableaux(parent)
            require(all(path_counts[s] == tableaux(s) for s in partitions(n)),
                    f"tableau dimension recurrence: n={n}")
    return checked


def check_word_distribution() -> int:
    checked = 0
    for rank, n in ((1, 5), (2, 5), (3, 4)):
        counts = Counter(rsk_shape(word)
                         for word in product(range(rank), repeat=n))
        for shape in partitions(n, rank):
            require(Fraction(counts[shape], rank ** n)
                    == schur_weight(shape, rank),
                    f"RSK word distribution: rank={rank}, n={n}, {shape}")
        checked += rank ** n
    return checked


def check_central_square() -> int:
    """Check the group-algebra identity used by the induced-character proof."""
    for n in range(6):
        identity = tuple(range(n))
        transpositions = []
        for i, j in combinations(range(n), 2):
            transposition = list(identity)
            transposition[i], transposition[j] = transposition[j], transposition[i]
            transpositions.append(tuple(transposition))
        coefficients = Counter(tuple(left[right[i]] for i in range(n))
                               for left in transpositions for right in transpositions)
        for permutation in permutations(range(n)):
            unseen = set(range(n))
            cycles = []
            while unseen:
                current = min(unseen)
                length = 0
                while current in unseen:
                    unseen.remove(current)
                    current = permutation[current]
                    length += 1
                if length > 1:
                    cycles.append(length)
            kind = tuple(sorted(cycles))
            expected = {(): n * (n - 1) // 2, (3,): 3, (2, 2): 2}.get(kind, 0)
            require(coefficients[permutation] == expected,
                    f"central transposition square: n={n}, permutation={permutation}")
    return 6


def check_likelihood(n: int, rank: int, dimension: int) -> None:
    stats = exact_statistics(n, rank, dimension)
    advantage = Fraction(dimension - rank, 2 * dimension)
    require(stats["success"] == Fraction(1, 2) + advantage * stats["F"],
            f"dimension factorization: {(n, rank, dimension)}")
    require(stats["null_mean_content"] == Fraction(n, dimension),
            "null-weighted first moment")
    require(stats["null_second_content"]
            == n + Fraction(n * (n - 1), rank * dimension),
            "null-weighted second moment")
    require(0 <= stats["excess_error"] <= advantage,
            "risk lies outside chance/oracle endpoints")
    if 2 * rank <= dimension:
        for epsilon in (Fraction(1, 8), Fraction(1, 16), Fraction(1, 64)):
            precise_bound = rank ** 2 * (advantage / epsilon - 1)
            uniform_bound = Fraction(rank ** 2, 8) / epsilon
            precise_ceiling = -(-precise_bound.numerator // precise_bound.denominator)
            uniform_ceiling = -(-uniform_bound.numerator // uniform_bound.denominator)
            require(precise_ceiling >= uniform_ceiling, "uniform copy-bound constant")
            if stats["excess_error"] <= epsilon:
                require(n >= precise_ceiling, "integer precision converse")
    if rank < dimension:
        require(stats["chi_squared"]
                <= Fraction(n, rank ** 2)
                + Fraction(n * (n - 1), rank ** 3 * dimension),
                "chi-squared converse")
    for b in branches(n, rank, dimension):
        predicted = Fraction(dimension * (rank + b.content),
                             rank * (dimension + b.content))
        require(b.likelihood == predicted, "Schur eigenvalue likelihood")
        require(b.content > -dimension, "unphysical denominator included")
        require(b.likelihood >= 0, "negative likelihood")
        if rank < dimension:
            require((b.likelihood > 1) == (b.content > 0),
                    "rank-blind positive decision")
            require((b.likelihood == 1) == (b.content == 0),
                    "zero-content tie")
        # Verify the exact operator slack on every supported Schur branch.
        rhs = (Fraction(dimension - rank, rank * dimension ** 2)
               * b.a_training * b.content)
        delta = b.a_joint - b.a_training / dimension
        expected_slack = (
            Fraction(dimension - rank, rank * dimension ** 2)
            * b.a_training * Fraction(b.content ** 2,
                                      dimension + b.content))
        require(rhs - delta == expected_slack >= 0,
                "classical-compiler operator inequality")


def check_majorants() -> dict:
    rectangles = []
    for rank in range(1, 6):
        for n in (rank ** 2, rank ** 2 + 1, 2 * rank ** 2, 5 * rank ** 2):
            t = Fraction(n, rank ** 2)
            # Polynomial identity in x=-c/r: compare all three coefficients.
            actual = (t * t / (1 + t) ** 2,
                      2 * t / (1 + t) ** 2 - 1,
                      1 / (1 + t) ** 2)
            factored = (t * t / (1 + t) ** 2,
                        -(1 + t * t) / (1 + t) ** 2,
                        1 / (1 + t) ** 2)
            require(actual == factored, "majorant factorization")
            for x in (Fraction(0), Fraction(1, 7), Fraction(1, 2), Fraction(1)):
                c = -rank * x
                require(majorant(c, n, rank) - x
                        == (x - 1) * (x - t * t) / (1 + t) ** 2 >= 0,
                        "majorant on negative-content interval")
            require(majorant(Fraction(n, rank), n, rank) == 0,
                    "majorant positive-content contact")
        # The condition is essential: construct an exact counterexample below it.
        n = rank ** 2 - 1
        t = Fraction(n, rank ** 2)
        x = (1 + t * t) / 2
        require(majorant(-rank * x, n, rank) < x,
                "majorant used outside its valid regime")
        for width in (rank, 2 * rank):
            shape = (width,) * rank
            n = rank * width
            value = sum(q * Fraction(max(-c, 0), rank)
                        for _, c, q in growth(shape))
            require(value == Fraction(n, n + rank ** 2),
                    "rectangular equality case")
            rectangles.append({"rank": rank, "width": width,
                               "conditional_F": fraction_text(value)})
    return {"rectangular_contacts": rectangles,
            "invalid_regime_counterexamples": 5}


def run() -> dict:
    shape_count = check_shapes()
    word_count = check_word_distribution()
    central_sizes = check_central_square()
    cases = {
        1: (0, 1, 2, 5, 12),
        2: (0, 1, 2, 3, 4, 5, 8, 12, 16),
        3: (0, 1, 3, 8, 9, 10, 18),
        4: (0, 1, 4, 15, 16, 17, 32),
    }
    likelihood_cases = 0
    fixtures = []
    for rank, sizes in cases.items():
        previous = Fraction(-1)
        for n in sizes:
            f = normalized_curve(n, rank)
            require(0 <= f <= 1 and f >= previous, "curve range/monotonicity")
            previous = f
            if rank == 1:
                require(f == Fraction(n, n + 1), "pure-rank exact curve")
            if n == 0:
                require(f == 0, "no-training curve")
            if n == 1:
                require(f == Fraction(1, 2 * rank), "one-training-copy curve")
            if n <= rank ** 2:
                require(4 * rank ** 2 * f * f <= n,
                        "small-sample moment bound")
            if n >= rank ** 2:
                require(f <= Fraction(n, n + rank ** 2),
                        "precision lower bound")
            for dimension in sorted({rank + 1, 2 * rank, 2 * rank + 3}):
                check_likelihood(n, rank, dimension)
                likelihood_cases += 1
            stats = exact_statistics(n, rank, 2 * rank)
            fixtures.append({"N": n, "r": rank, "d": 2 * rank,
                             **{key: fraction_text(value)
                                for key, value in stats.items()}})
    # Degenerate full rank is outside the nontrivial precision theorem.
    for dimension, n in ((1, 0), (1, 4), (2, 3), (3, 4)):
        check_likelihood(n, dimension, dimension)
        require(exact_statistics(n, dimension, dimension)["success"]
                == Fraction(1, 2), "identical hypotheses at full rank")
        likelihood_cases += 1
    return {"shape_moment_checks": shape_count,
            "enumerated_words": word_count,
            "central_square_group_sizes": central_sizes,
            "likelihood_cases": likelihood_cases,
            "fixtures": fixtures,
            "precision_majorant": check_majorants()}
