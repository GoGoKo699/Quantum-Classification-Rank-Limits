# Quantum Classification Rank Limits

**How does the mixture rank of quantum training data limit the advantage of retaining it coherently?**

A source supplies independent examples from an unknown state $`P/r`$, uniform on a rank-$`r`$ subspace of a $`d`$-dimensional system. One later test is drawn, with equal prior probabilities, from that same state or from the known background $`I/d`$. The learner must output one label.

This repository gives the exact optimal coherent classifier, a matching rank-and-precision law for its training cost, and a fixed-accuracy comparison with every strategy that converts the training data to a classical record before seeing the test. The coherent cost is governed by $`r^2`$; the classical cost at fixed accuracy is governed by $`rd`$. Their ratio decreases as the mixture rank grows.

## Principal results

Let $`N_{\mathrm Q}(d,r,\varepsilon)`$ and $`N_{\mathrm C}(d,r,\varepsilon)`$ be the minimum training-copy budgets required to bring the worst-case classification error within $`\varepsilon`$ of the known-subspace optimum $`R_*=r/(2d)`$. The [model](science/model.md) specifies the minimax risk and chronology.

| Result | Statement | Proof |
|---|---|---|
| Exact coherent decision | Predict the class state on the positive eigenspace of $`J=\sum_{i=1}^N\operatorname{SWAP}(i,S)`$. The same rule is optimal for every $`1\le r<d`$. | [Q1](science/exact_classifier.md) |
| Exact learning curve | $`p_{\mathrm Q}=1/2+A_{d,r}F_{N,r}`$, where $`A_{d,r}=(1-r/d)/2`$ and $`F_{N,r}`$ is independent of $`d`$. | [Q1](science/exact_classifier.md) |
| Quantum rank and precision | $`N_{\mathrm Q}=\Theta(r^2/\varepsilon)`$ uniformly for $`1\le r\le d/2`$ and $`0<\varepsilon\le1/8`$. | [Q2](science/quantum_precision.md) and [construction](science/constructions.md) |
| Classical compilation | $`N_{\mathrm C}(d,r,1/16)=\Theta(rd)`$ for $`1\le r\le d/2`$, even with arbitrary collective training measurements and unlimited classical storage. | [C1–C2](science/classical_compilation.md) |
| Rank proportional to dimension | For fixed $`c>0`$ and $`cd\le r\le d/2`$, both learner classes require $`\Theta_c(d^2/\varepsilon)`$ copies in the stated precision range. | [C3](science/classical_compilation.md#corollary-c3-combined-lower-bound-and-proportional-rank) |

The uniform quantum bounds include explicit constants:

```math
\left\lceil\frac{r^2}{8\varepsilon}\right\rceil
\le N_{\mathrm Q}(d,r,\varepsilon)
\le
\left\lceil\frac{2\pi^2r^2}{\varepsilon}\right\rceil.
```

For classical compilation, the general precision upper is

```math
N_{\mathrm C}(d,r,\varepsilon)
\le
\left\lceil\frac{(4d-3)r}{\varepsilon}\right\rceil.
```

The matching classical converse is established at fixed accuracy and for rank proportional to dimension. A matching $`\Theta(rd/\varepsilon)`$ law for all rank regimes is not claimed.

At fixed accuracy, fixed rank and $`d=2^n`$, coherent retention saves an exponential number of training copies in the number of qubits. At $`r=d/2`$, the oracle still succeeds with probability $`3/4`$, but both learner classes need order $`d^2/\varepsilon`$ copies. The loss of the copy advantage therefore occurs while the classification task retains constant observable contrast.

## What information the learner receives

All $`N`$ training copies arrive before the test. A coherent learner may retain them and perform any joint measurement at prediction. A classical compiler may perform any collective POVM during training, retain its full classical outcome, and choose any later test measurement from that record. It must discard the training quantum information before the test arrives.

The learner has no description of $`P`$, purification, inverse preparation, controlled preparation oracle or fresh post-test examples. The task permits both classification error types and destruction of the test. It concerns one prediction.

The exact optimal decision does not need the rank. The promised rank can still determine the sample budget and the explicit attaining construction. For $`d=2^n`$, that direct construction stores $`Nn`$ training qubits before prediction; its active interaction width is $`2n+O(1)`$. Source preparation and gate synthesis are charged in the [resource account](science/constructions.md).

## Read the scientific account

| Question | Start here |
|---|---|
| What is the prediction experiment, and what does each learner know? | [Model and operational assumptions](science/model.md) |
| Why is a rank-independent sign-of-swap measurement exactly optimal? | [Exact classifier and Schur likelihood](science/exact_classifier.md) |
| Why must every coherent learner use order $`r^2/\varepsilon`$ copies? | [Growth-content moments and the precision converse](science/quantum_precision.md) |
| How is the sample order attained, and what does it cost to implement? | [Controlled support reflection and resources](science/constructions.md) |
| Why does an arbitrary classical compiler require order $`rd`$ copies at fixed accuracy? | [Compiler converse and tomography construction](science/classical_compilation.md) |
| What changes between low and high rank? | [Physical interpretation and claim boundaries](science/interpretation.md) |
| Which ingredients and earlier advantages are inherited? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

For a continuous first reading, follow the table from the model through the interpretation. The exact-classifier page derives the averaged hypotheses and branch likelihood. The precision page proves the content moments and quadratic majorant. The classical page uses the same likelihood in an operator inequality that applies to all permitted compilers.

[llms.txt](llms.txt) provides a compact map from questions to authoritative files.

## Reproduce the finite checks

With Python 3.11 or newer, run from the repository root:

```sh
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

The [verification guide](verification/README.md) documents the pinned dependency, reference results, tolerances and failure behavior. The suite checks exact rational Schur formulas and content identities, then independently constructs small Haar-averaged density matrices to compare the decision rule with the Helstrom optimum. It also checks the classical operator inequality and informative collective-training examples.

Finite checks support the analytical derivations. They do not prove the universal rates, establish priority, or certify noisy hardware performance.

## Relation to earlier work and scope

Fixed-rank quantum-reference advantages and the collective classical-compilation comparator have precedents, particularly [An's rank-two leakage problem](references/RELATED_WORK.md#an2026) and [coherent quantum inference](references/RELATED_WORK.md#li2026). The result here is the unrestricted minimum-error decision for general flat rank, its exact learning curve, the matching quantum precision converse, and the rank-dependent compilation comparison.

The attaining quantum mechanism is established sample-based Hamiltonian simulation, specialized to a support reflection. The classical upper uses established collective tomography. Both are attributed alongside the new derivations in the scientific account.

The flat spectrum, independent training, equal class prior, maximally mixed background and single future test define the result. Arbitrary spectra, optimal retained quantum memory, model reuse and robustness to experimental noise require further arguments. The [interpretation](science/interpretation.md) also explains precisely how high rank obstructs a uniform dimension-independent training claim.

## Purpose

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
