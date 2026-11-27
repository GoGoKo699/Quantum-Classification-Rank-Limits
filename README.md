# Quantum Classification Rank Limits

**How does the mixture rank of quantum training data limit the advantage of retaining it coherently?**

A source supplies independent examples from an unknown state $`P/r`$, uniform on a rank-$`r`$ subspace of a $`d`$-dimensional system. One later test is drawn, with equal prior probabilities, from that same state or from the known background $`I/d`$. The learner must output one label.

This repository gives the exact optimal coherent classifier and matching training-copy laws for coherent retention and classical compilation. At excess error $`\varepsilon`$, the coherent cost scales as $`r^2/\varepsilon`$ and the cost of measuring all training data before the test scales as $`rd/\varepsilon`$ throughout the precision range below.

## Run one classification

1. Store the labeled training specimens until the test arrives. For the clean model, the rank and dimension are known, and the test is equally likely to come from the class source or the maximally mixed background. Use the [copy and precision allocation](science/constructions.md#gates-active-width-and-stored-data) for the desired excess risk.
2. Prepare the test control with a Hadamard on a zero qubit. For each stored specimen, append a flag in state one, partially swap the flagged specimen with the control–test pair at an angle of pi times the rank divided by the allocated copy count, then discard the used specimen. A separate zero work qubit implements each partial swap with a Hadamard, controlled full-register swap and Hadamard, followed by a Z rotation at twice the swap angle and the inverse of the first three gates. This returns the work qubit to zero with exact rotations.
3. Apply a Hadamard to the test control and measure it in the computational basis. Output the class label on one and the background label on zero. This uses one test and consumes the training specimens. Every outcome produces a label.

This [copy-based construction](science/constructions.md#a-controlled-support-reflection-from-copies) uses inherited sample-based simulation to attain the clean sample order. The [exact optimal decision](science/exact_classifier.md) instead measures the sign of the sum of training–test swaps. The resource account charges all early specimen storage, active registers, source preparation and finite gate synthesis. The [classical-record route](science/classical_compilation.md#3-theorem-c2-constructive-upper-bound) performs collective tomography before the test and measures the estimated top-rank projector at prediction. For contaminated training, the test source remains clean and the [noise-dependent conditions](science/contaminated_training.md#the-statistical-cost-of-contaminated-recognition) govern the copy requirements.

## Principal results

Let $`N_{\mathrm Q}(d,r,\varepsilon)`$ and $`N_{\mathrm C}(d,r,\varepsilon)`$ be the minimum training-copy budgets required to bring the worst-case classification error within $`\varepsilon`$ of the known-subspace optimum $`R_*=r/(2d)`$. The [model](science/model.md) specifies the minimax risk and chronology.

| Result | Statement | Proof |
|---|---|---|
| Exact coherent decision | Predict the class state on the positive eigenspace of $`J=\sum_{i=1}^N\mathrm{SWAP}(i,S)`$. The same rule is optimal for every $`1\le r\lt d`$. | [Q1](science/exact_classifier.md) |
| Exact learning curve | $`p_{\mathrm Q}=1/2+A_{d,r}F_{N,r}`$, where $`A_{d,r}=(1-r/d)/2`$ and $`F_{N,r}`$ is independent of $`d`$. | [Q1](science/exact_classifier.md) |
| Quantum rank and precision | $`N_{\mathrm Q}=\Theta(r^2/\varepsilon)`$ uniformly for $`1\le r\le d/2`$ and $`0\lt \varepsilon\le1/8`$. | [Q2](science/quantum_precision.md) and [construction](science/constructions.md) |
| Classical rank and precision | $`N_{\mathrm C}=\Theta(rd/\varepsilon)`$ in the same range, even with arbitrary collective training measurements and unlimited classical storage. | [C3](science/classical_compilation.md#theorem-c3-uniform-classical-precision) |

The uniform quantum bounds include explicit constants:

```math
\left\lceil\frac{r^2}{8\varepsilon}\right\rceil
\le N_{\mathrm Q}(d,r,\varepsilon)
\le
\left\lceil\frac{2\pi^2r^2}{\varepsilon}\right\rceil.
```

The classical precision bounds are

```math
\left\lceil\frac{rd}{20\varepsilon}\right\rceil
\le N_{\mathrm C}(d,r,\varepsilon)
\le \left\lceil\frac{(4d-3)r}{\varepsilon}\right\rceil.
```

The copy ratio $`N_{\mathrm C}/N_{\mathrm Q}`$ is $`\Theta(d/r)`$ throughout this range. For fixed rank and $`d=2^n`$, coherent retention saves an exponential number of copies in the number of qubits. At $`r=d/2`$, the oracle still succeeds with probability $`3/4`$, while both learner classes need order $`d^2/\varepsilon`$ copies.

## Converse application: ordinary reflection programming

[Collective Quantum Programming](https://github.com/GoGoKo699/Collective-Quantum-Programming) studies the same flat source as a program for an ordinary reflection channel on a batch of data registers. The all-rank finite-sample form of Q2 transfers through a known vacuum or occupied eigenstate: channel error $`\epsilon`$ gives classification excess at most the available contrast times $`\epsilon`$, so that contrast cancels in the lower bound. This establishes the single-target programming law $`N_* = \Theta(r^2/\epsilon)`$ uniformly over every nontrivial programming dimension and rank for $`0\lt\epsilon\le1/8`$.

The [application and exact promise mapping](science/programming_application.md) keep the classification and programming dimensions, hard specimen budget and unhalved diamond error separate. The [authoritative transfer proof](https://github.com/GoGoKo699/Collective-Quantum-Programming/blob/c6b5150ce0e7d4f6ac81d171bb7f136ad86a1358/science/classification_transfer.md) is in the programming account. For intermediate batches it strengthens the lower bound to order $`(r^2+rk^2)/\epsilon`$; it does not establish the missing $`r^2k/\epsilon`$ term. Q2 remains the statistical theorem supplied by this repository.

## When training is contaminated

[Quantum Training Contamination](https://github.com/GoGoKo699/Quantum-Training-Contamination/blob/main/science/flat_rank_training.md) extends the source to $`\rho=aP/r+(1-a)\sigma`$ while keeping the later test clean. The admissible choice $`\sigma=P/r`$ preserves the Q2 and C3 statistical lower bounds. At balanced rank, the two learner classes retain the same copy-error order and face the same contamination floor. For $`r\le d/2`$ their copy ratio stays of order $`d/r`$ when $`\min(u^2,u)/r`$ is at most a sufficiently small constant times the target excess, where $`u=r(1-a)/a`$.

The same contrast-normalized reduction also carries C3 to a copy lower bound of order $`rD/\epsilon`$ for a programmer in dimension $`D`$ that retains only a classical record. The [classification bridge](science/contaminated_training.md) gives the two clean-subfamily arguments. [Collective Quantum Programming](https://github.com/GoGoKo699/Collective-Quantum-Programming/blob/main/science/contaminated_reflections.md) proves the stronger channel-error floor for the contaminated batch itself.

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
| What does Q2 imply for ordinary reflection programming? | [Anchored converse application and exact promise mapping](science/programming_application.md) |
| Why does an arbitrary classical compiler require order $`rd/\varepsilon`$ copies? | [Posterior bound and matching tomography construction](science/classical_compilation.md) |
| Which clean classification limits survive when training is contaminated? | [Statistical and classical-record programming converses](science/contaminated_training.md) |
| What changes between low and high rank? | [Physical interpretation and claim boundaries](science/interpretation.md) |
| Which ingredients and earlier advantages are inherited? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |

For a continuous first reading, follow the table from the model through the interpretation. The exact-classifier page derives the averaged hypotheses and branch likelihood. The precision page proves the content moments and quadratic majorant. The classical page uses the same likelihood to bound the information available after any collective training measurement and derives the precision law from the first row of the recorded Schur diagram.

[llms.txt](llms.txt) provides a compact map from questions to authoritative files.

## Learn the project

The educational anchor is **John Watrous, [The Theory of Quantum Information](https://jhwatrous.github.io/books-and-courses.html) (Cambridge University Press, 2018)**, using the author's standard-layout manuscript and its printed section and page numbers.

Start with the [30-milestone map](learning/milestones.md). Its 12 background milestones connect states, measurements, risk, channels and symmetry into the prediction experiment. Its 18 research milestones build the exact likelihood and decision, both learning-cost converses, the attaining constructions, and the rank-dependent physical interpretation.

The [Watrous-to-project bridge](learning/watrous_bridge.md) identifies the relevant sections, translates notation and supplies the additional steps needed for this problem. Watrous provides the foundations of discrimination, channel norms and invariant operators. The bridge explains how those foundations lead into the partition, branching and content calculations developed in the scientific pages.

The map follows this project's logical dependencies. Use its understanding targets and proof links to choose a starting point; reading the entire textbook is unnecessary.

## Reproduce the finite checks

With Python 3.11 or newer, run from the repository root:

```sh
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

The [verification guide](verification/README.md) documents the pinned dependency, reference results, tolerances and failure behavior. The suite checks exact rational Schur formulas and content identities, then independently constructs small Haar-averaged density matrices to compare the decision rule with the Helstrom optimum. It also checks the classical operator inequality and informative collective-training examples.

Finite checks support the analytical derivations. They do not prove the universal rates, establish priority, or certify noisy hardware performance.

## Relation to earlier work and scope

[An's rank-two leakage analysis](references/RELATED_WORK.md#an2026) already implies the rank-two classical precision scaling. [Coherent quantum inference](references/RELATED_WORK.md#li2026) gives a related measurement-first comparator for quantum outputs. The contribution here is the unrestricted minimum-error decision for a flat source, its exact coherent learning curve, and the matched copy laws uniform in the stated rank and precision range.

The attaining quantum mechanism is established sample-based Hamiltonian simulation, specialized to a support reflection. The classical upper uses established collective tomography. Both are attributed alongside the new derivations in the scientific account.

The flat spectrum, independent training, equal class prior, maximally mixed background and single future test define the result. Arbitrary spectra, optimal retained quantum memory, model reuse and robustness to experimental noise require further arguments. The [interpretation](science/interpretation.md) also explains precisely how high rank obstructs a uniform dimension-independent training claim.

## Purpose

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
