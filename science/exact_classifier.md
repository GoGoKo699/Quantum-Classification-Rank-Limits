# Exact optimal classifier

An unknown rank-$`r`$ projector $`P`$ on $`\mathbb C^d`$ supplies $`N`$ training systems in $`\rho_P=P/r`$. One independent test system is then drawn, with equal prior probabilities, from $`\rho_P`$ or $`I_d/d`$. A quantum learner may retain all training systems and measure them jointly with the test. The [model](model.md) specifies the access order and the resources being counted.

The optimal decision has a particularly simple form: measure the sign of the sum of swaps between the training systems and the test. The same decision measurement is optimal for every flat rank. Its success probability admits an exact factorization that separates ambient dimension from the rank-dependent learning curve.

## Theorem Q1: exact minimax decision and value

Let $`N\ge 0`$ and $`1\le r<d`$ be integers. Define

```math
J_N=\sum_{i=1}^{N}V_{(i,N+1)},
\qquad
A_{d,r}=\frac{1-r/d}{2},
```

where $`V_{(i,N+1)}`$ swaps training system $`i`$ with the test. For $`N=0`$, the empty sum is zero. A positive decision means that the test is classified as $`\rho_P`$.

**Theorem Q1.** The effect

```math
T_N^\star=\mathbf 1_{(0,\infty)}(J_N)
```

is optimal both for the Haar-averaged problem and for worst-case success over rank-$`r`$ projectors. Any decision on the zero eigenspace has the same Haar-averaged value; the displayed invariant choice attains the minimax value. The measurement depends on $`N`$ and the register structure, and does not depend on $`r`$ or $`P`$.

Write $`p_Q(N;d,r)`$ for this optimal worst-case success probability. Then

```math
p_Q(N;d,r)=\frac12+A_{d,r}F_{N,r},
```

where

```math
F_{N,r}
=\sum_{\substack{\lambda\vdash N\\\ell(\lambda)\le r}}
  \frac{f_\lambda D_\lambda(r)}{r^N}
  \sum_{\mu:\lambda\nearrow\mu}
  \frac{f_\mu}{(N+1)f_\lambda}
  \frac{(-c(\mu/\lambda))_+}{r}.
```

Here:

- $`\lambda\vdash N`$ is a partition of $`N`$, and $`\ell(\lambda)`$ is its number of nonzero rows.
- $`f_\lambda`$ is the dimension of the irreducible $`S_N`$ representation with label $`\lambda`$.
- $`D_\lambda(k)=s_\lambda(1^k)`$ is the dimension of the polynomial $`U(k)`$ representation with that label. It is zero when $`\ell(\lambda)>k`$.
- $`\lambda\nearrow\mu`$ means that $`\mu`$ is obtained by adding one box to $`\lambda`$.
- The content of a box in row $`i`$ and column $`j`$ is $`c=j-i`$, and $`x_+=\max(x,0)`$.

All Young-diagram successors are included in the inner sum. Because $`\ell(\lambda)\le r<d`$, every such successor has at most $`d`$ rows and is physically present in the $`d`$-dimensional tensor space. The empty partition has $`f_\varnothing=D_\varnothing(k)=1`$.

For a known projector, the support measurement $`\{P,I-P\}`$ has optimal success

```math
p_*(d,r)=1-\frac{r}{2d}=\frac12+A_{d,r}.
```

Consequently, the optimal excess risk is

```math
E_Q(N;d,r)
:=p_*(d,r)-p_Q(N;d,r)
=A_{d,r}(1-F_{N,r}).
```

The quantity $`F_{N,r}`$ is the fraction of the available Bayes advantage recovered from training. It is independent of $`d`$, lies in $`[0,1]`$, and includes the uncertainty in the unknown subspace. The [precision theorem](quantum_precision.md) bounds this exact learning curve.

## 1. Reduction to two averaged states

Any binary joint procedure induces an effect $`0\le T\le I`$ on the supplied training and test systems. Its success for a fixed projector is

```math
p(T,P)
=\frac12\mathrm{Tr}\!\left[T\rho_P^{\otimes(N+1)}\right]
+\frac12\mathrm{Tr}\!\left[(I-T)
  \left(\rho_P^{\otimes N}\otimes\frac{I_d}{d}\right)\right].
```

Ancillas, intermediate operations, and classical records are absorbed into this effect. Conversely, every such effect is allowed by joint processing of retained training systems and the test.

Fix a rank-$`r`$ projector $`P_0`$, and let $`P=UP_0U^\dagger`$ with normalized Haar measure on $`U(d)`$. Define

```math
A_n=\mathbb E_P\left[\rho_P^{\otimes n}\right],
\qquad A_0=1,
```

and the two normalized averaged input states

```math
H_1=A_{N+1},
\qquad
H_0=A_N\otimes\frac{I_d}{d}.
```

The average success is

```math
\overline p(T)
=\frac12+\frac12\mathrm{Tr}[T(H_1-H_0)].
```

For a traceless Hermitian operator $`\Delta=H_1-H_0`$, maximizing over effects gives

```math
\sup_{0\le T\le I}\overline p(T)
=\frac12+\frac14\|\Delta\|_1.
```

Indeed, diagonalizing $`\Delta`$ shows that its positive eigenspaces should be accepted and its negative eigenspaces rejected. Its positive and negative parts have the same trace. We next find these eigenspaces explicitly.

## 2. Haar moments and their support

Schur-Weyl duality decomposes the $`n`$-system space as

```math
(\mathbb C^d)^{\otimes n}
\cong
\bigoplus_{\substack{\lambda\vdash n\\\ell(\lambda)\le d}}
U_\lambda^{(d)}\otimes V_\lambda,
```

with dimensions $`D_\lambda(d)`$ and $`f_\lambda`$. The unitary group acts on the first factor, while permutations act on the second. These are standard representation identities; the calculation below states the dimensions and branching relations needed for the proof.

The tensor power $`\rho_{P_0}^{\otimes n}`$ commutes with permutations. In its $`\lambda`$ sector, its trace over the unitary-group factor is

```math
s_\lambda(\underbrace{1/r,\ldots,1/r}_{r\text{ entries}},0,\ldots,0)
=\frac{D_\lambda(r)}{r^n}.
```

Haar averaging makes the operator scalar on each irreducible unitary-group factor. Therefore

```math
A_n
=\bigoplus_{\substack{\lambda\vdash n\\\ell(\lambda)\le d}}
a_\lambda^{(n)}
I_{U_\lambda^{(d)}}\otimes I_{V_\lambda},
\qquad
a_\lambda^{(n)}
=\frac{D_\lambda(r)}{r^nD_\lambda(d)}.
```

Exactly the sectors with $`\ell(\lambda)\le r`$ have positive coefficients. The probability of a training label $`\lambda`$ is accordingly

```math
w_{N,r}(\lambda)
=f_\lambda D_\lambda(d)a_\lambda^{(N)}
=\frac{f_\lambda D_\lambda(r)}{r^N}.
```

This is a probability distribution: applying the same decomposition to $`(\mathbb C^r)^{\otimes N}`$ gives $`\sum_\lambda f_\lambda D_\lambda(r)=r^N`$.

To compare the two hypotheses, restrict the last tensor decomposition from $`S_{N+1}`$ to the subgroup $`S_N`$ acting on the training systems. The branching rule is multiplicity-free:

```math
V_\mu\!\downarrow_{S_N}
\cong\bigoplus_{\lambda:\lambda\nearrow\mu}V_\lambda.
```

Thus a common block is labeled by $`\lambda\nearrow\mu`$ and has dimension $`D_\mu(d)f_\lambda`$. On it, $`H_0`$ has eigenvalue $`a_\lambda^{(N)}/d`$, while $`H_1`$ has eigenvalue $`a_\mu^{(N+1)}`$.

Only $`\ell(\lambda)\le r`$ contributes to $`H_0`$. If $`\ell(\lambda)>r`$, every successor also has more than $`r`$ rows, so $`H_1`$ vanishes there too. Hence

```math
\mathrm{supp}\,H_1\subseteq\mathrm{supp}\,H_0.
```

All likelihood ratios below are taken on $`\mathrm{supp}\,H_0`$, including blocks where $`H_1`$ has eigenvalue zero. No inverse of a zero training coefficient is used.

## 3. Hook-content ratio and the likelihood operator

For a box $`b=(i,j)`$, let $`h_\lambda(b)`$ be its hook length. The dimension formulas are

```math
f_\lambda=\frac{n!}{\prod_{b\in\lambda}h_\lambda(b)},
\qquad
D_\lambda(k)
=\prod_{b\in\lambda}\frac{k+c(b)}{h_\lambda(b)}.
```

Equivalently,

```math
D_\lambda(k)=\frac{f_\lambda}{n!}
\prod_{b\in\lambda}(k+c(b)).
```

For $`\lambda\nearrow\mu`$ with $`|\lambda|=N`$ and added content $`c`$, division gives

```math
\frac{D_\mu(k)}{D_\lambda(k)}
=(k+c)q_{\lambda\mu},
\qquad
q_{\lambda\mu}:=\frac{f_\mu}{(N+1)f_\lambda},
```

whenever $`D_\lambda(k)>0`$. This identity also covers $`D_\mu(k)=0`$: the new box in row $`k+1`$ then has $`c=-k`$.

The induction branching rule

```math
\mathrm{Ind}_{S_N}^{S_{N+1}}V_\lambda
\cong\bigoplus_{\mu:\lambda\nearrow\mu}V_\mu
```

has dimension $`(N+1)f_\lambda`$, so $`\sum_\mu q_{\lambda\mu}=1`$. These are the Plancherel growth probabilities for the fixed diagram $`\lambda`$.

Applying the dimension ratio at $`k=r`$ and $`k=d`$ gives the exact likelihood on each active block:

```math
L(c)
:=\frac{a_\mu^{(N+1)}}{a_\lambda^{(N)}/d}
=\frac dr\frac{r+c}{d+c}.
```

An active training diagram has at most $`r`$ rows, so every possible added content satisfies $`c\ge-r`$. Therefore $`d+c\ge d-r>0`$. A new $`(r+1)`$st row has $`c=-r`$ and likelihood zero, exactly as required by the support of $`H_1`$.

The central sum of transpositions in $`S_n`$ acts on $`V_\lambda`$ as the scalar

```math
\theta_\lambda=\sum_{b\in\lambda}c(b)
=\frac12\sum_i\lambda_i(\lambda_i-2i+1).
```

One can obtain this content identity directly from the same dimension formulas. Taking the trace of the central character projector, and using that a permutation with $`\kappa(\pi)`$ cycles has tensor-space trace $`k^{\kappa(\pi)}`$, gives

```math
D_\lambda(k)=\frac1{n!}\sum_{\pi\in S_n}
\chi_\lambda(\pi)k^{\kappa(\pi)}.
```

For $`n\ge2`$, comparing the coefficient of $`k^{n-1}`$ with the hook-content product gives $`\binom n2\chi_\lambda((12))/f_\lambda=\theta_\lambda`$. This is the scalar of the central transposition sum, since a central operator acts as a scalar and its trace is the sum of these transposition characters. For $`n=0,1`$, both sides are zero.

Since $`J_N`$ is the difference between the central transposition sums for $`S_{N+1}`$ and $`S_N`$, its eigenvalue on the branch $`\lambda\nearrow\mu`$ is $`\theta_\mu-\theta_\lambda=c`$. Thus the preceding scalar formula is an operator likelihood formula on $`\mathrm{supp}\,H_0`$:

```math
L=\frac dr(rI+J_N)(dI+J_N)^{-1}.
```

In particular,

```math
L(c)-1=\frac{(d-r)c}{r(d+c)}.
```

Equivalently, on that support,

```math
H_1-H_0=\frac{d-r}{r}\,H_0J_N(dI+J_N)^{-1}.
```

Both hypotheses vanish on the complementary support; no likelihood is required there.

Its sign is exactly the sign of $`c`$, establishing the Haar-optimal effect $`T_N^\star`$. The choice is independent of rank because the prefactor and denominator are positive for every $`r<d`$ on its populated blocks.

## 4. From Haar optimality to worst-case optimality

Every swap commutes with $`U^{\otimes(N+1)}`$. Hence $`T_N^\star`$ is invariant under applying the same unitary to all registers. Its success is the same for $`P`$ and $`UPU^\dagger`$. The unitary group acts transitively on rank-$`r`$ projectors, so this success is constant over the entire model.

For every effect $`T`$,

```math
\inf_P p(T,P)\le\mathbb E_P p(T,P)
\le\overline p(T_N^\star).
```

The invariant effect attains the last quantity for every $`P`$. It therefore attains the supremum of the worst-case success probabilities. This also explains why Haar integration is a proof method: the operational instance need not resample its unknown projector.

## 5. Exact success factorization

Under $`H_0`$, the conditional probability of the branch $`\mu`$ given training label $`\lambda`$ is

```math
p_0(\mu\mid\lambda)
=\frac{D_\mu(d)}{dD_\lambda(d)}
=\frac{d+c}{d}\,q_{\lambda\mu}.
```

The normalization follows either from tracing the corresponding training block tensored with $`I_d/d`$, or from the unitary-group branching identity $`\sum_{\mu:\lambda\nearrow\mu}D_\mu(d)=dD_\lambda(d)`$ for fixed $`\lambda`$.

Because the two averaged states have trace one and commute, their trace distance can be calculated from the negative part of the likelihood difference:

```math
\frac12\|H_1-H_0\|_1
=\sum_\lambda w_{N,r}(\lambda)
  \sum_{\mu:\lambda\nearrow\mu}
  p_0(\mu\mid\lambda)(1-L(c))_+.
```

The denominator in the likelihood cancels exactly:

```math
p_0(\mu\mid\lambda)(1-L(c))_+
=\left(1-\frac rd\right)
q_{\lambda\mu}\frac{(-c)_+}{r}.
```

Substitution yields

```math
\frac12\|H_1-H_0\|_1
=\left(1-\frac rd\right)F_{N,r},
```

and hence the success and excess-risk formulas in Theorem Q1. Since $`c\ge-r`$, the averaged integrand defining $`F_{N,r}`$ is between zero and one.

## 6. Boundary checks

**No training.** At $`N=0`$ the only branch is $`\varnothing\nearrow(1)`$, with content zero. Thus $`F_{0,r}=0`$, $`p_Q(0;d,r)=1/2`$, and $`E_Q(0;d,r)=A_{d,r}`$. In the averaged problem both test states are $`I_d/d`$.

**Pure training states.** For $`r=1`$, the training diagram is $`\lambda=(N)`$ with probability one. When $`N\ge1`$, its successors have contents $`N`$ and $`-1`$, with growth probabilities $`1/(N+1)`$ and $`N/(N+1)`$. Therefore, including $`N=0`$,

```math
F_{N,1}=\frac{N}{N+1},
\qquad
E_Q(N;d,1)=\frac{1-1/d}{2(N+1)}.
```

**Full rank.** If $`r=d`$, then $`P=I_d`$ and both hypotheses are identical. Every classifier has success $`1/2`$ and excess risk zero. This boundary is handled directly. In particular, one should not substitute $`r=d`$ into a branch ratio for a formal successor with $`d+1`$ rows; that successor is absent from the physical tensor space.

## Scope and provenance

The proof combines standard Schur-Weyl, branching, and hook-content identities with the likelihood calculation for this training-and-test experiment. These representation tools also underlie [O'Donnell and Wright's quantum spectrum testing](https://arxiv.org/abs/1501.05028). Related rank tests, programmable discriminators, and quantum-reference separations are compared in [Related work](../references/RELATED_WORK.md). The minimum-error claim here allows arbitrary joint procedures. No one-sided false-alarm constraint, returned-message condition, or restricted measurement model enters its converse.

The theorem determines the best decision statistics. The [construction and resource analysis](constructions.md) separately specifies an attainable sample bound, its elementary operations, and the storage of training systems.
