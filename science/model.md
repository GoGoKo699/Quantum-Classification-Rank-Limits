# Classification from quantum training data

A source supplies examples from an unknown quantum state. The prediction task is to decide whether one later system came from that source or from a known maximally mixed background. Keeping the examples coherent allows a joint prediction. Measuring the examples first produces a classical model that must act on the later test through its recorded information.

This project solves the coherent decision problem for states that are uniform on an unknown subspace. The mixture rank determines the coherent training cost; the ambient dimension enters the cost of classical compilation.

## Experiment and information access

Let $`d\ge2`$ and $`1\le r<d`$ be integers. An unknown rank-$`r`$ orthogonal projector $`P`$ acts on $`\mathbb C^d`$. Define

```math
\rho_P=\frac{P}{r},
\qquad
\tau_d=\frac{I_d}{d}.
```

Training consists of $`N`$ independent copies of $`\rho_P`$. After training has arrived, a single test register $`S`$ is supplied. Its label $`h\in\{0,1\}`$ has equal prior probabilities, and its conditional state is

```math
h=1:\ \rho_P,
\qquad
h=0:\ \tau_d.
```

The copies and test are independent conditional on $`P`$ and $`h`$. The source fixes one unknown $`P`$ throughout the experiment. Haar averaging is a proof device, not a requirement to physically resample the source.

The learner receives quantum copies. It receives no description of $`P`$, purification, inverse preparation, controlled preparation oracle, or further source copies after the test arrives. Known ancillas and operations independent of $`P`$ are permitted. Every supplied example is charged. No QRAM or free loading of a classical dataset is assumed.

The output is one classical label. The test may be destroyed, and either type of classification error is allowed. The claim concerns one prediction, without a requirement to preserve the test or reuse the training data.

## Two classes of learner

### Coherent learner

A coherent learner may retain the training systems and perform any joint measurement when the test arrives. Ancillas, intermediate operations and randomness can be absorbed into a binary effect $`0\le T\le I`$ on the supplied systems. The effect $`T`$ means “predict $`h=1`$.”

Its success at a fixed source is

```math
p(T,P)=\frac12\operatorname{tr}\!\left(T\rho_P^{\otimes(N+1)}\right)
+\frac12\operatorname{tr}\!\left[(I-T)
  \left(\rho_P^{\otimes N}\otimes\tau_d\right)\right].
```

### Classical compiler

A classical compiler performs any collective POVM $`\{E_y\}`$ on all training copies before the test arrives. It retains an unrestricted classical record $`y`$, discards all training quantum systems, and applies a record-dependent binary test effect $`0\le M_y\le I`$. Its positive-decision effect has the form

```math
T_{\mathrm C}=\int E_y\otimes M_y\,dy,
\qquad
E_y\ge0,\qquad \int E_y\,dy=I.
```

Sums are the discrete special case. This class includes arbitrary entanglement and adaptive operations during training, unbounded classical storage, and arbitrary later test measurements. It also includes general entanglement-breaking preprocessing: a state prepared from the classical record can be absorbed into the subsequent test procedure.

The distinction is whether quantum information about the training source survives until prediction. It is not a restriction to separately measured examples or to tomography followed by a fixed classifier.

## Oracle benchmark and minimax quantities

If $`P`$ is known, the optimal positive effect is $`P`$. The class state is always accepted, while the maximally mixed state is accepted with probability $`r/d`$. Therefore

```math
p_*(d,r)=1-\frac{r}{2d},
\qquad
R_*(d,r)=\frac{r}{2d},
\qquad
A_{d,r}=p_*-\frac12=\frac{1-r/d}{2}.
```

For $`\mathcal L\in\{\mathrm Q,\mathrm C\}`$, define

```math
p_{\mathcal L}(N;d,r)
=\sup_{T\in\mathcal L}\inf_{\operatorname{rank}P=r}p(T,P),
\qquad
E_{\mathcal L}(N;d,r)
=p_*(d,r)-p_{\mathcal L}(N;d,r).
```

Thus $`E_{\mathcal L}`$ is the excess classification error above the known-source optimum. The training complexity is

```math
N_{\mathcal L}(d,r,\varepsilon)
=\min\{N\ge0:E_{\mathcal L}(N;d,r)\le\varepsilon\}.
```

All risks average over training measurement outcomes, internal randomness and the equal label prior, and take the worst case over $`P`$. There is no separate high-probability requirement on each realized training record.

For a dimension-uniform fixed-accuracy comparison, it is also useful to require recovery of half the available advantage:

```math
p_{\mathcal L}(N;d,r)\ge \frac12+\frac{A_{d,r}}2.
```

The statements below use $`1\le r\le d/2`$, so the oracle advantage is at least $`1/4`$.

## Principal results and proof route

| Result | Precise content | Authoritative proof |
|---|---|---|
| Q1: exact optimum | The positive spectral projector of $`J=\sum_{i=1}^{N}\operatorname{SWAP}(i,S)`$ is minimax optimal for every flat rank $`r<d`$. | [Exact classifier](exact_classifier.md) |
| Learning-curve factorization | $`p_{\mathrm Q}=1/2+A_{d,r}F_{N,r}`$, with $`F_{N,r}`$ independent of $`d`$. | [Exact classifier](exact_classifier.md) |
| Q2: quantum precision | For $`1\le r\le d/2`$ and $`0<\varepsilon\le1/8`$, $`r^2/(8\varepsilon)\le N_{\mathrm Q}(d,r,\varepsilon)\le\lceil2\pi^2r^2/\varepsilon\rceil`$. | [Quantum precision](quantum_precision.md) and [construction](constructions.md) |
| C1: all classical compilers | $`p_{\mathrm C}-1/2\le A_{d,r}N/(rd)`$. | [Classical compilation](classical_compilation.md) |
| C2: classical construction | $`E_{\mathrm C}\le(4d-3)r/N`$ for $`N\ge1`$. | [Classical compilation](classical_compilation.md) |

At fixed nontrivial accuracy, the training orders are $`\Theta(r^2)`$ and $`\Theta(rd)`$. The quantum dependence on $`\varepsilon`$ is matched. The classical bounds establish an $`O(rd/\varepsilon)`$ upper and a fixed-accuracy converse; they do not establish a matching classical converse for every $`\varepsilon`$.

The exact quantum decision rule does not require $`r`$. The sample budget and the explicit reflection construction may use the promised rank. Rank-independent decision-making does not imply an adaptive stopping or memory-compression theorem.

## Boundaries and resources

At $`N=0`$, the minimax success is $`1/2`$. At $`r=d`$, the two classes coincide and the task is trivial. Exact formulas for $`r<d`$ remain valid beyond $`r\le d/2`$, but the constant-accuracy complexity statements require an oracle advantage bounded away from zero.

The direct coherent construction stores $`N\log_2d`$ training qubits when $`d`$ is a power of two. Its small active interaction width does not reduce that offline storage. Source preparation adds its actual per-copy cost. The [construction and resource account](constructions.md) specify these charges.

The [interpretation](interpretation.md) explains the high-rank obstruction and the relation to dimension-independent learning claims. [Related work](../references/RELATED_WORK.md) separates the new decision and precision laws from inherited fixed-rank advantages, representation tools, simulation and tomography. [Verification](../verification/README.md) documents finite checks and their limits.

