# What rank changes in quantum classification

The source state is uniform on an unknown subspace. Its support dimension $`r`$ measures how many equally weighted directions contribute to each example. The ambient dimension $`d`$ measures how much larger the surrounding Hilbert space can be.

The [exact solution](exact_classifier.md) separates these roles:

```math
p_{\mathrm Q}(N;d,r)-\frac12
=
\frac{1-r/d}{2}\,F_{N,r}.
```

The prefactor is the advantage available to a learner who already knows the subspace. The normalized learning curve $`F_{N,r}`$ depends on rank and training budget alone. Thus increasing the ambient dimension at fixed rank changes the available contrast with the maximally mixed background, but does not change the fraction of that contrast recovered by an optimal coherent learner.

## Why the rank-squared scale appears

The exact likelihood reduces the quantum classification problem to the content of one added Young-diagram box. Under the relevant growth distribution, that content has mean zero, second moment $`N`$, and a negative range bounded by $`-r`$. Recovering a fixed fraction of the oracle advantage requires fluctuations on the scale of $`r`$, which leads to the lower bound $`N=\Omega(r^2)`$.

The [precision proof](quantum_precision.md) turns this observation into a bound at large training budgets. A quadratic function majorizes the negative-content score and gives

```math
E_{\mathrm Q}(N;d,r)
\ge
\frac{1-r/d}{2}\frac{r^2}{N+r^2},
\qquad N\ge r^2.
```

The matching construction simulates the support reflection at time $`\pi r`$. Its accumulated sample-based simulation error is proportional to $`r^2/N`$. The exact decision problem therefore has the same order of training cost as this construction. The converse does not assume that the learner uses simulation.

## The cost of classicalizing the training data

A classical compiler can use entanglement during training. It can retain an unlimited record and apply any later test measurement. Nevertheless, the [compiler converse](classical_compilation.md) bounds its recovered advantage by $`N/(rd)`$ times the oracle advantage.

The proof does not require the compiler to estimate the entire state. It treats every permitted classical record and conditional test measurement at once. Tomography supplies an attaining order at fixed accuracy, but the lower bound is about prediction itself.

For a fixed accuracy target bounded away from random guessing and the oracle risk, the comparison is

| Rank regime, with $`d=2^n`$ | Coherent training | Classical compilation | Copy ratio |
|---|---:|---:|---:|
| Fixed $`r`$ | $`\Theta(1)`$ | $`\Theta(d)`$ | $`\Theta(d)`$ |
| $`r=\mathrm{poly}(n)`$ | $`\Theta(r^2)`$ | $`\Theta(rd)`$ | $`\Theta(d/r)`$ |
| $`r=d^\alpha`$, fixed $`0<\alpha<1`$ | $`\Theta(d^{2\alpha})`$ | $`\Theta(d^{1+\alpha})`$ | $`\Theta(d^{1-\alpha})`$ |
| $`r`$ proportional to $`d`$, with $`r\le d/2`$ | $`\Theta(d^2)`$ | $`\Theta(d^2)`$ | $`\Theta(1)`$ |

Integer rounding of ranks does not change these asymptotic orders. The fixed-rank exponential advantage is already present in quantum-reference work, especially [An's rank-two leakage result](../references/RELATED_WORK.md#an2026). The general-rank optimum quantifies how that advantage decreases with the mixture rank.

## High rank retains useful contrast but loses the copy advantage

Take even $`d`$ and $`r=d/2`$. A known-projector test succeeds with probability $`3/4`$, so the classes remain distinguishable with constant advantage. The difficult part is learning how to use that contrast from examples.

For every $`0<\varepsilon\le1/8`$,

```math
N_{\mathrm Q}(d,d/2,\varepsilon)
=\Theta(d^2/\varepsilon).
```

Every classical compiler is a coherent procedure with an additional restriction. It obeys the same lower bound. The collective tomography construction gives a classical upper of the same order in this regime. More generally, if $`c d\le r\le d/2`$ for a fixed $`c>0`$,

```math
N_{\mathrm C}(d,r,\varepsilon)
=
N_{\mathrm Q}(d,r,\varepsilon)
=
\Theta_c(d^2/\varepsilon),
```

where equality denotes equality of asymptotic orders, not equality of exact optimal budgets.

For arbitrary rank, the established classical bounds instead give

```math
\max\left\{
\frac{r^2}{8\varepsilon},
\;rd\left(1-\frac{\varepsilon}{A_{d,r}}\right)
\right\}
\le
N_{\mathrm C}(d,r,\varepsilon)
\le
\left\lceil\frac{(4d-3)r}{\varepsilon}\right\rceil
```

throughout $`1\le r\le d/2`$, $`0<\varepsilon\le1/8`$, with integer ceilings understood on necessary lower bounds. These inequalities establish the full quantum precision law and the fixed-accuracy classical comparison. They do not determine the complete classical precision law when $`r/d`$ vanishes.

## Rank-independent decisions and resource limits

The optimal effect is the positive spectral projector of

```math
J_N=\sum_{i=1}^{N}\mathrm{SWAP}(i,S).
```

Its definition contains no rank. Rank affects the amount of information available in the examples, rather than the form of the optimal fixed-budget decision. This separates the learning obstruction from a need to estimate rank before classifying.

The sample comparison assumes native quantum examples. If generating a copy costs $`C_{\mathrm{prep}}`$, that cost is multiplied by the required training budget. The theorem does not assert efficient preparation of arbitrary subspaces or an end-to-end speedup for classical datasets.

Coherent retention also has a storage cost. The direct construction holds $`N\log_2d`$ training qubits before prediction and can consume those systems during the one test. The [resource account](constructions.md) distinguishes this storage from active circuit width. Reusing a trained quantum model and compressing its retained memory are different resource questions.

## Reading the scope correctly

The sharp obstruction concerns flat-spectrum sources and a single test against a maximally mixed background. It covers all coherent classifiers within that experiment, including procedures that allow false alarms and discard the test. It is not a converse for every conceivable learning problem, source spectrum, or side-information model.

The high-rank family also rules out a dimension-uniform approximate-Helstrom training guarantee under this copy-only access. The precise comparison with the published phase-estimation argument is given in [Related work](../references/RELATED_WORK.md#banchi2024). The positive low-rank results and the high-rank limitation are compatible once the state family and the charged sample access are specified.

