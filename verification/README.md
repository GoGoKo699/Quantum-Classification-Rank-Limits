# Reproduce the finite-size checks

This suite checks consequential finite cases of the [exact classifier](../science/exact_classifier.md), [quantum precision bound](../science/quantum_precision.md), and classical compiler argument. It combines exact rational calculations with an independent construction of small Haar-averaged density matrices. The proofs in `science/` establish the general statements; passing these checks does not replace those proofs.

## Run

Use Python 3.11 or newer and the pinned NumPy dependency. From the repository root:

```sh
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

The suite was run with Python 3.12.14 and NumPy 2.3.5. NumPy is the only external dependency. The exact calculations use Python's standard-library `Fraction`; no symbolic algebra package or quantum simulator is required. A normal run completes in approximately one second on the development environment, uses no network, and does not modify the reference results.

To save the actual exact results and floating-point diagnostics:

```sh
python verification/run_all.py --output /tmp/quantum-classification-checks.json
```

Every check uses explicit exceptions rather than disableable Python `assert` statements. A failed mathematical check, missing reference file, or mismatch with `expected.json` returns a nonzero exit status. A successful run returns zero. The runner sets single-thread BLAS execution for these small matrices and suppresses bytecode-file creation.

## What is checked

| Component | Calculation | Failure mode addressed |
|---|---|---|
| Exact Schur branches | Integer hook-length dimensions, rational hook-content dimensions, and both hypothesis weights computed separately | Missing multiplicities, reversed likelihood, or a factor of two in Helstrom success |
| Normalized learning curve | Exact `F(N,r)` and success for several ambient dimensions at each selected training budget | A false claim of dimension independence or inconsistent risk normalization |
| Growth probabilities and moments | Hook-length probabilities compared with an independent corner-residue formula for every partition of sizes 0 through 12 | Confusing ordinary Young-diagram growth with the physical null branch distribution |
| Schur-Weyl weights | Exhaustive row insertion for small alphabets, compared with the rational Schur-Weyl distribution | An erroneous rank-dependent weight or partition enumeration |
| Transposition-square identity | Exact permutation multiplication for group sizes 0 through 5 | Incorrect coefficients of the identity, 3-cycles, or double transpositions in the moment proof |
| Precision majorant | Rational polynomial coefficients, contact points, rectangular equality cases, and exact learning-curve inequalities | A sign error or use of the large-budget bound below `N=r²` |
| Haar twirls | Independent permutation-Gram construction, with the linear system solved over rational numbers | Circular validation of Schur formulas by another implementation of the same formulas |
| Rank-blind decision | Direct matrix Helstrom value compared with the positive spectral projector of `J`, including a prior mixture of ranks | Incorrect sign convention or an unjustified rank-independent decision rule |
| Classical compiler inequality | Exact branch slacks, full matrix positivity, and informative collective-training examples | Missing symmetrization, invalid positivity of `E_y A_N`, or an incorrect swap/partial-trace identity |
| Reference results | Exact rational outputs compared with the committed JSON | Unnoticed changes in formulas, fixtures, or the checked regime |

### Exact arithmetic and boundary cases

The exact branch cases include pure training states, mixed ranks up to four, and budgets immediately below, at, and above `N=r²`. Their largest training budget is 32. These cases check the identities

```math
L(c)=\frac dr\frac{r+c}{d+c},\qquad
p_Q=\frac12+\frac{1-r/d}{2}F_{N,r}.
```

The ordinary transition law is checked against

```math
\mathbb E_q C=0,\qquad \mathbb E_q C^2=N,
```

while the distinct null-hypothesis law is checked against

```math
\mathbb E_0 C=\frac Nd,\qquad
\mathbb E_0 C^2=N+\frac{N(N-1)}{rd}.
```

The suite includes `N=0`, the exact pure-state curve `F(N,1)=N/(N+1)`, and the one-copy identity `F(1,r)=1/(2r)`. The degenerate case `r=d` is handled by identical hypotheses. Formal successors with `d+1` rows are excluded from physical likelihood calculations, so a zero-dimensional sector never introduces a spurious denominator `d+c=0`.

For the precision polynomial, the checks verify its factored slack on the negative-content interval and its exact contact with `(-c)_+/r` at the required points. They also construct a rational counterexample when `N<r²`; the threshold is an essential assumption. The exact risk fixtures check the integer lower-bound implication and the uniform constant in `N_Q ≥ ceil(r²/(8 epsilon))` for the stated range `r≤d/2`, `epsilon≤1/8`.

### Independent matrix construction

For `k` registers, let `U_pi` be their permutation matrices. The Haar twirl of the flat state belongs to their linear span. Its coefficients are found from

```math
G_{\pi\sigma}=\operatorname{Tr}(U_\pi^\dagger U_\sigma),\qquad
b_\pi=\operatorname{Tr}(\rho^{\otimes k}U_\pi)
=r^{\#\mathrm{cycles}(\pi)-k},\qquad G\alpha=b.
```

`check_matrices.py` builds `G` from the explicit action on tensor basis indices and solves this system over `Fraction`. It does not call the Schur dimension formula to construct the twirl. The permutation span can be linearly dependent when `k>d`; exact elimination handles this case by setting free coefficients to zero. The resulting operator is unique even when its coefficient representation is not.

The largest density matrix is `256 × 256`, and the largest Gram system has 24 permutations. The checks compare the independent twirl with the likelihood operator, the exact Schur success probability, and the rank-blind decision effect. They also check support inclusion, positivity, the classical operator inequality, and the decision risk for two explicit fixed subspaces related by a Fourier unitary. The latter are finite covariance checks; the proof establishes the full minimax conclusion.

All floating matrix comparisons use absolute tolerance `2e-10`. The runner reports the largest observed comparison residual. Tiny negative operator-slack eigenvalues within the same tolerance are treated as floating-point roundoff. Exact combinatorial identities and reference fractions have no numerical tolerance.

### Classical compiler examples

The compiler checks include a one-training-copy computational-basis measurement with the exact achieved advantage

```math
\frac{d-r}{2rd(d+1)}.
```

For two training copies, deterministic rotations of basis states produce a training POVM with genuinely entangled effects and nonzero classification information. Its effects need not commute with `A_N` before permutation averaging. The checks verify that averaging leaves the decision statistics unchanged, makes `E_y A_N` positive, preserves normalization, and permits the swap/partial-trace estimate in the proof. The later test measurement is optimized for each resulting classical record.

These examples check the algebra for collective training measurements. They are not an optimization over every possible compiler, and do not numerically prove the all-compiler converse.

## Files and reference values

- `exact_schur.py` contains the rational formulas and partition operations.
- `check_exact.py` performs the exact identities, independent small-word checks, and precision checks.
- `check_matrices.py` constructs independent Haar twirls and checks finite matrix/compiler examples.
- `run_all.py` is the single entry point and compares the results with `expected.json`.
- `expected.json` stores the exact rational fixtures, case parameters, and structural results. Fractions are strings such as `"3/8"`; it contains no timings or machine-dependent residuals.
- `requirements.txt` pins the only external package actually used.

The reference JSON is a regression record, not an independent proof oracle. The independent matrix construction, special-case analytic formulas, and separate combinatorial identities supply the cross-checks. Changing a formula should require reviewing the resulting reference diff against those checks and the scientific proof; the normal runner never refreshes expectations automatically.

## Limits of verification

The suite checks finite instances of the exact curve and the load-bearing algebra. It does not prove the asymptotic rates from numerical scaling, certify priority, verify experimental noise resilience, or simulate the full sample-based reflection construction. Its diamond-norm error bound and the tomography upper bound are analytical results discussed and attributed in the scientific pages.

No result here establishes the minimum retained quantum memory, reusable-model lifetime, arbitrary-spectrum classification, or a matching classical precision converse. The selected comparison remains unrestricted coherent classification versus classical compilation for one future test drawn from the flat-subspace experiment.
