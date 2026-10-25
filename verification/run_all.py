#!/usr/bin/env python3
"""Run the reproducible suite; return nonzero on failure or fixture mismatch."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import sys

# Small dense matrices are faster and more reproducible without BLAS oversubscription.
# These settings affect this verification process only.
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
sys.dont_write_bytecode = True

import check_exact
import check_matrices


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        help="also write the actual results and numerical diagnostics as JSON")
    arguments = parser.parse_args()
    directory = Path(__file__).resolve().parent
    try:
        exact = check_exact.run()
        matrices, diagnostics = check_matrices.run()
        actual = {"schema_version": 1, "exact": exact, "matrices": matrices}
        expected = json.loads((directory / "expected.json").read_text())
        if actual != expected:
            raise AssertionError("computed exact fixtures differ from verification/expected.json")
        if arguments.output:
            report = {**actual, "numerical_diagnostics": diagnostics}
            arguments.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    except Exception as error:
        print(f"FAIL: {type(error).__name__}: {error}", file=sys.stderr)
        return 1
    print("PASS: exact Schur likelihoods, normalized curves, content moments and precision bounds")
    print("PASS: independent permutation-Gram Haar twirls, rank-blind decisions and support edges")
    print("PASS: classical operator inequality and collective-training compiler examples")
    print("PASS: committed exact reference results match expected.json")
    print(f"Largest matrix residual: {diagnostics['largest_matrix_residual']:.3e} "
          f"(tolerance {diagnostics['absolute_tolerance']:.1e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
