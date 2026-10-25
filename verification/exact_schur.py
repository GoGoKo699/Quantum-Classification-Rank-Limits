"""Exact finite-size formulas for flat-subspace classification.

All combinatorial quantities use integers or fractions.Fraction.  This module
does not construct the permutation-Gram twirl used by check_matrices.py.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import cache
from math import factorial, prod

Partition = tuple[int, ...]


def require(condition: bool, message: str) -> None:
    """Do not rely on assert, which Python can disable with -O."""
    if not condition:
        raise AssertionError(message)


@cache
def partitions(n: int, max_parts: int | None = None,
               max_first: int | None = None) -> tuple[Partition, ...]:
    if n < 0:
        raise ValueError("partition size must be nonnegative")
    if n == 0:
        return ((),)
    if max_parts is None:
        max_parts = n
    if max_parts <= 0:
        return ()
    if max_first is None:
        max_first = n
    return tuple(
        (first,) + tail
        for first in range(min(n, max_first), 0, -1)
        for tail in partitions(n - first, max_parts - 1, first)
    )


def cells(shape: Partition):
    for i, row in enumerate(shape):
        for j in range(row):
            hook = row - j + sum(length > j for length in shape[i + 1:])
            yield i, j, hook


@cache
def tableaux(shape: Partition) -> int:
    """f_lambda, from the hook-length formula."""
    numerator = factorial(sum(shape))
    denominator = prod(hook for _, _, hook in cells(shape))
    require(numerator % denominator == 0, "nonintegral tableau dimension")
    return numerator // denominator


@cache
def schur_dimension(shape: Partition, dimension: int) -> int:
    """s_lambda(1^dimension), including zero-dimensional sectors."""
    if dimension < 1:
        raise ValueError("dimension must be positive")
    if len(shape) > dimension:
        return 0
    value = prod((Fraction(dimension + j - i, hook)
                  for i, j, hook in cells(shape)), start=Fraction(1))
    require(value.denominator == 1, "nonintegral Schur dimension")
    return value.numerator


@cache
def successors(shape: Partition) -> tuple[tuple[Partition, int], ...]:
    """ALL Young-lattice successors; no ambient-dimension truncation."""
    result = []
    for i in range(len(shape)):
        if i == 0 or shape[i] < shape[i - 1]:
            child = list(shape)
            child[i] += 1
            result.append((tuple(child), shape[i] - i))
    result.append((shape + (1,), -len(shape)))
    return tuple(result)


def removable_contents(shape: Partition) -> tuple[int, ...]:
    return tuple(row - i - 1 for i, row in enumerate(shape)
                 if i + 1 == len(shape) or row > shape[i + 1])


def growth(shape: Partition) -> tuple[tuple[Partition, int, Fraction], ...]:
    n = sum(shape)
    return tuple((child, content,
                  Fraction(tableaux(child), (n + 1) * tableaux(shape)))
                 for child, content in successors(shape))


def growth_residue(shape: Partition, content: int) -> Fraction:
    """Independent corner-product formula for a transition probability."""
    addable = tuple(c for _, c in successors(shape))
    if content not in addable:
        raise ValueError("content is not an addable corner")
    numerator = prod(content - b for b in removable_contents(shape))
    denominator = prod(content - a for a in addable if a != content)
    return Fraction(numerator, denominator)


def schur_weight(shape: Partition, rank: int) -> Fraction:
    return Fraction(tableaux(shape) * schur_dimension(shape, rank),
                    rank ** sum(shape))


def twirl_eigenvalue(shape: Partition, rank: int,
                    dimension: int) -> Fraction:
    size = schur_dimension(shape, dimension)
    if size == 0:
        raise ValueError("unphysical Schur sector")
    return Fraction(schur_dimension(shape, rank),
                    rank ** sum(shape) * size)


def normalized_curve(n: int, rank: int) -> Fraction:
    if n < 0 or rank < 1:
        raise ValueError("n must be nonnegative and rank positive")
    return sum((schur_weight(shape, rank)
                * sum((probability * Fraction(max(-content, 0), rank)
                       for _, content, probability in growth(shape)),
                      start=Fraction(0))
                for shape in partitions(n, rank)), start=Fraction(0))


@dataclass(frozen=True)
class Branch:
    shape: Partition
    child: Partition
    content: int
    p0: Fraction
    p1: Fraction
    a_training: Fraction
    a_joint: Fraction

    @property
    def likelihood(self) -> Fraction:
        return self.p1 / self.p0


def branches(n: int, rank: int, dimension: int) -> tuple[Branch, ...]:
    if n < 0 or not 1 <= rank <= dimension:
        raise ValueError("require n >= 0 and 1 <= rank <= dimension")
    result = []
    for shape in partitions(n, rank):
        a_training = twirl_eigenvalue(shape, rank, dimension)
        for child, content in successors(shape):
            size = schur_dimension(child, dimension)
            if size == 0:
                continue  # In particular c=-d is absent when r=d.
            multiplicity = tableaux(shape) * size
            a_joint = twirl_eigenvalue(child, rank, dimension)
            result.append(Branch(
                shape, child, content,
                multiplicity * a_training / dimension,
                multiplicity * a_joint,
                a_training, a_joint,
            ))
    return tuple(result)


def exact_statistics(n: int, rank: int, dimension: int) -> dict[str, Fraction]:
    data = branches(n, rank, dimension)
    p0_total = sum((b.p0 for b in data), start=Fraction(0))
    p1_total = sum((b.p1 for b in data), start=Fraction(0))
    require(p0_total == p1_total == 1, "hypotheses are not normalized")
    variation = sum((abs(b.p1 - b.p0) for b in data),
                    start=Fraction(0)) / 2
    success = Fraction(1, 2) + variation / 2
    oracle_success = 1 - Fraction(rank, 2 * dimension)
    return {
        "F": normalized_curve(n, rank),
        "success": success,
        "oracle_success": oracle_success,
        "excess_error": oracle_success - success,
        "null_mean_content": sum((b.p0 * b.content for b in data),
                                 start=Fraction(0)),
        "null_second_content": sum((b.p0 * b.content ** 2 for b in data),
                                   start=Fraction(0)),
        "chi_squared": sum(((b.p1 - b.p0) ** 2 / b.p0 for b in data),
                           start=Fraction(0)),
    }


def majorant(content: Fraction, n: int, rank: int) -> Fraction:
    """Polynomial Q; its majorization assertion needs n >= rank**2."""
    return Fraction(rank ** 2, (n + rank ** 2) ** 2) * (
        content - Fraction(n, rank)) ** 2


def fraction_text(value: Fraction | int) -> str:
    return str(Fraction(value))
