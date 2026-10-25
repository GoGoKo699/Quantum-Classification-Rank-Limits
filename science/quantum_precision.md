# Quantum precision law

The exact classifier shows that the optimal excess risk factors as

```math
E_Q(N;d,r)=A_{d,r}(1-F_{N,r}),
\qquad
A_{d,r}=\frac{1-r/d}{2}.
```

This page proves finite-sample lower bounds on that risk and the resulting optimal copy complexity. The converse applies to every joint quantum procedure on the supplied training systems and the single test. The matching upper bound uses the sample-based reflection construction described in [Constructions](constructions.md).

## Theorem Q2: finite-sample risk and copy complexity

Let $`1\le r<d`$ and $`N\ge0`$ be integers. In the model of [Theorem Q1](exact_classifier.md),

```math
E_Q(N;d,r)\ge A_{d,r}
\begin{cases}
1-\dfrac{\sqrt N}{2r}, & 0\le N\le r^2,\\[6pt]
\dfrac{r^2}{N+r^2}, & N\ge r^2.
\end{cases}
```

Both bounds agree at $`N=r^2`$. In the ideal-operation model, for $`N\ge1`$,

```math
E_Q(N;d,r)
\le\min\left\{A_{d,r},\frac{2\pi^2r^2}{N}\right\}.
```

Define the minimum number of supplied training copies needed for uniform excess risk at most $`\epsilon`$ by

```math
N_Q(d,r,\epsilon)
=\min\{N\in\mathbb Z_{\ge0}:E_Q(N;d,r)\le\epsilon\}.
```

For every $`0<\epsilon\le A_{d,r}/2`$,

```math
\left\lceil r^2\left(\frac{A_{d,r}}{\epsilon}-1\right)\right\rceil
\le N_Q(d,r,\epsilon)
\le\left\lceil\frac{2\pi^2r^2}{\epsilon}\right\rceil.
```

In particular, the following constants and range are uniform in both dimensions:

```math
1\le r\le d/2,\qquad 0<\epsilon\le\frac18
\quad\Longrightarrow\quad
\left\lceil\frac{r^2}{8\epsilon}\right\rceil
\le N_Q(d,r,\epsilon)
\le\left\lceil\frac{2\pi^2r^2}{\epsilon}\right\rceil.
```

Thus $`N_Q(d,r,\epsilon)=\Theta(r^2/\epsilon)`$ throughout this range, with universal implicit constants. For $`\epsilon\ge A_{d,r}`$, no training is needed. For $`r=d`$, the hypotheses coincide and the excess risk is zero at every budget; this trivial boundary is outside the nonzero-advantage statement.

## 1. The transition-content distribution

Use the notation of [Theorem Q1](exact_classifier.md). First draw a training diagram

```math
\Pr\{\lambda\}=w_{N,r}(\lambda)
=\frac{f_\lambda D_\lambda(r)}{r^N},
```

then draw a successor using

```math
\Pr\{\mu\mid\lambda\}=q_{\lambda\mu}
=\frac{f_\mu}{(N+1)f_\lambda}.
```

Let $`C=c(\mu/\lambda)`$ be the added-box content under this probability distribution. The exact factorization is

```math
F_{N,r}=\mathbb E\frac{(-C)_+}{r}.
```

The growth probabilities $`q_{\lambda\mu}`$ are distinct from the physical conditional branch probabilities under $`H_0`$. The latter contain the additional factor $`(d+C)/d`$. That factor has already canceled against the likelihood in the formula for $`F_{N,r}`$.

The following moments hold even before averaging over the training diagram:

```math
\mathbb E[C\mid\lambda]=0,
\qquad
\mathbb E[C^2\mid\lambda]=N.
```

Moreover, every populated training diagram has at most $`r`$ rows, so $`C\ge-r`$. The support bound and these two moments are sufficient for the precision converse. We give a direct proof of the moment identities.

## 2. Proof of the two content moments

Fix an arbitrary partition $`\lambda\vdash N`$. Let $`V_\lambda`$ be its symmetric-group representation, and let

```math
W_\lambda=\operatorname{Ind}_{S_N}^{S_{N+1}}V_\lambda.
```

The branching rule gives

```math
W_\lambda\cong\bigoplus_{\mu:\lambda\nearrow\mu}V_\mu,
\qquad
\dim W_\lambda=(N+1)f_\lambda.
```

For a representation space $`W`$, write $`\tau_W(X)=\operatorname{Tr}_W(X)/\dim W`$ for normalized trace. Denote by

```math
Z_n=\sum_{1\le i<j\le n}(ij)
```

the central sum of transpositions in the group algebra of $`S_n`$. As stated in the exact-classifier proof, it acts on $`V_\nu`$ as the total content $`\theta_\nu=\sum_{b\in\nu}c(b)`$.

On the summand $`V_\mu\subset W_\lambda`$, the operator $`Z_{N+1}-\theta_\lambda I`$ therefore has eigenvalue $`c(\mu/\lambda)`$. Its normalized trace distribution is precisely $`q_{\lambda\mu}`$. Hence

```math
\mathbb E[C^k\mid\lambda]
=\tau_{W_\lambda}\!\left[(Z_{N+1}-\theta_\lambda I)^k\right],
\qquad k=1,2.
```

It remains to compute two traces of the central sum.

### Induced characters

The cosets of $`S_N`$ in $`S_{N+1}`$ are indexed by the $`N+1`$ possible images of the last point. A permutation $`g`$ that moves $`m`$ points fixes $`N+1-m`$ of these cosets. On each fixed coset its contribution to the induced character is the character of a permutation with the same nontrivial cycle type in $`S_N`$. Thus, if $`m\le N`$,

```math
\tau_{W_\lambda}(g)
=\frac{N+1-m}{N+1}\,
  \frac{\chi_\lambda(g_N)}{f_\lambda},
```

where $`g_N\in S_N`$ has that cycle type. If $`m=N+1`$, there are no fixed cosets and the induced character is zero.

For a transposition, $`m=2`$. Summing over all transpositions yields

```math
\tau_{W_\lambda}(Z_{N+1})
=\binom{N+1}{2}\frac{N-1}{N+1}
  \frac{\chi_\lambda((12))}{f_\lambda}
=\tau_{V_\lambda}(Z_N)
=\theta_\lambda.
```

The expression involving $`(12)\in S_N`$ is needed only when $`N\ge2`$. For $`N=0,1`$, the same equality follows directly: the relevant transposition sum is zero, or each transposition has induced character zero. This proves the first moment.

### Second moment

Expanding a square of the transposition sum gives the group-algebra identity

```math
Z_n^2
=\binom n2 I
+3\!\sum_{g\,\text{a 3-cycle in }S_n}\!g
+2\!\sum_{g\,\text{two disjoint transpositions in }S_n}\!g.
```

The coefficients follow by counting ordered products of two transpositions. Identical transpositions produce the identity; each 3-cycle has three such factorizations; and each product of two disjoint transpositions has two.

For each of the two nonidentity cycle types, the induced-character contribution at size $`N+1`$ equals the ordinary-character contribution at size $`N`$. Indeed, a cycle type moving $`m`$ points has a number of occurrences proportional to $`\binom nm`$, and

```math
\binom{N+1}{m}\frac{N+1-m}{N+1}=\binom Nm.
```

When the cycle type fills all $`N+1`$ points, its induced character and its count at size $`N`$ are both zero. Cycle types absent at smaller sizes contribute no term. The identity coefficient is the only difference, and increases by $`N`$. Consequently,

```math
\tau_{W_\lambda}(Z_{N+1}^2)
=\tau_{V_\lambda}(Z_N^2)+N
=\theta_\lambda^2+N.
```

Subtracting the mean proves

```math
\mathbb E[C^2\mid\lambda]
=\theta_\lambda^2+N
-2\theta_\lambda^2+\theta_\lambda^2
=N.
```

For $`N=0`$, the only content is zero, so both moment identities also hold directly. Averaging over $`w_{N,r}`$ now gives $`\mathbb EC=0`$ and $`\mathbb EC^2=N`$ for the distribution entering $`F_{N,r}`$.

## 3. The regime up to rank squared

Mean zero implies that the positive and negative parts of $`C`$ have equal expectations. Therefore

```math
F_{N,r}
=\frac{\mathbb E|C|}{2r}
\le\frac{\sqrt{\mathbb EC^2}}{2r}
=\frac{\sqrt N}{2r},
```

where the inequality is Cauchy-Schwarz. Combining this with $`E_Q=A_{d,r}(1-F_{N,r})`$ yields

```math
E_Q(N;d,r)
\ge A_{d,r}\left(1-\frac{\sqrt N}{2r}\right).
```

In particular, when $`N\le r^2`$, at least half of the available Bayes advantage remains unrecovered.

## 4. The precision converse

Assume $`N\ge r^2`$. Define the quadratic

```math
Q(c)=\frac{r^2(c-N/r)^2}{(N+r^2)^2}.
```

We claim that

```math
Q(c)\ge\frac{(-c)_+}{r}
\qquad\text{for every }c\ge-r.
```

For $`c\ge0`$, the claim is just $`Q(c)\ge0`$. On $`[-r,0]`$, put $`g(c)=Q(c)+c/r`$. This function is convex, and

```math
g(-r)=0,
\qquad
g'(-r)=\frac{N-r^2}{r(N+r^2)}\ge0.
```

Its derivative is nondecreasing, so $`g(c)\ge0`$ throughout that interval. This proves the majorization over the entire allowed support.

Taking expectations and using the two moments gives

```math
\begin{aligned}
F_{N,r}
&\le\mathbb EQ(C)\\
&=\frac{r^2}{(N+r^2)^2}
  \left(\mathbb EC^2-\frac{2N}{r}\mathbb EC+\frac{N^2}{r^2}\right)\\
&=\frac{r^2N+N^2}{(N+r^2)^2}
=\frac{N}{N+r^2}.
\end{aligned}
```

It follows that

```math
E_Q(N;d,r)
\ge A_{d,r}\frac{r^2}{N+r^2}.
```

The argument uses the exact optimal value from Theorem Q1. It is therefore a converse for all joint classifiers, including procedures with arbitrary ancillas and collective training operations. It does not assume that a classifier implements density-matrix exponentiation or any particular measurement circuit.

## 5. Matching upper bound and its constant

The [construction](constructions.md) uses the sample-based Hamiltonian-simulation method analyzed by [Kimmel et al.](https://www.nature.com/articles/s41534-017-0013-7), on program states

```math
\sigma_P=|1\rangle\langle1|\otimes\rho_P.
```

At time $`t=\pi r`$, the target evolution is the controlled reflection

```math
e^{-it\sigma_P}
=|0\rangle\langle0|\otimes I_d
+|1\rangle\langle1|\otimes(I_d-2P).
```

Preparing the control in $`|+\rangle`$ and reading it in the $`X`$ basis implements the ideal support decision. Appending $`|1\rangle`$ is a known operation; each program state consumes exactly one supplied copy of $`\rho_P`$.

For completeness, the error accounting needed here is the following. A partial-swap step of duration $`\delta`$ and the desired unitary channel have the same value and first derivative at $`\delta=0`$. Each second-order integral remainder has diamond norm at most $`2\delta^2`$, because its commutator generator has diamond norm at most two and its unitary channels have norm one. Thus the one-step difference is at most $`4\delta^2`$. Telescoping $`N`$ steps of duration $`t/N`$ gives channel error at most $`4t^2/N`$ in diamond norm. A binary outcome probability changes by at most half that norm, so the excess classification risk is at most

```math
\frac{2t^2}{N}=\frac{2\pi^2r^2}{N}.
```

The construction page gives the channels and the first-derivative calculation explicitly. The bound is for ideal elementary operations. Finite synthesis accuracy and the storage of the offline training systems are accounted for separately there.

Ignoring the training and guessing one class has excess risk $`A_{d,r}`$. Choosing the better of these two procedures proves the upper risk bound in Theorem Q2. Although this construction uses the known rank to choose its simulation time, the rank-independent measurement in Theorem Q1 is optimal at each budget and therefore satisfies the same upper bound on its decision risk.

## 6. Explicit copy-complexity range

Suppose $`0<\epsilon\le A_{d,r}/2`$. If $`N<r^2`$, the first lower bound is strictly greater than $`A_{d,r}/2`$, so such a budget cannot achieve the target. For $`N\ge r^2`$, the precision bound requires

```math
\epsilon\ge A_{d,r}\frac{r^2}{N+r^2},
\qquad\text{hence}\qquad
N\ge r^2\left(\frac{A_{d,r}}{\epsilon}-1\right).
```

Taking the integer ceiling gives the stated lower copy bound. Taking $`N=\lceil2\pi^2r^2/\epsilon\rceil`$ in the reflection construction gives the upper bound.

When $`r\le d/2`$, one has $`A_{d,r}\ge1/4`$. If additionally $`\epsilon\le1/8`$, then $`\epsilon\le A_{d,r}/2`$ and

```math
\frac{A_{d,r}}{\epsilon}-1
\ge\frac{1/4-\epsilon}{\epsilon}
\ge\frac{1}{8\epsilon}.
```

This establishes the uniform constants in Theorem Q2. The restriction on $`\epsilon`$ keeps the target a fixed distance below the success obtainable without training. It also prevents a vanishing known-projector advantage from being mistaken for a small learning cost.

## 7. Checks and consequences

For $`r=1`$, the exact formula from Theorem Q1 is

```math
E_Q(N;d,1)=\frac{A_{d,1}}{N+1}.
```

Thus the precision lower bound is an equality for every $`N\ge1`$ in the pure-state case. At $`N=0`$, the separate small-budget bound is also exact. For every $`r<d`$, the lower bounds are positive at finite budget, so exact attainment of the known-projector risk requires an unbounded supply of training copies.

At the opposite end of the stated uniform range, take even $`d`$ and $`r=d/2`$. The known-projector success is $`3/4`$, while

```math
N_Q(d,d/2,\epsilon)=\Theta(d^2/\epsilon)
\qquad(0<\epsilon\le1/8).
```

The two test classes therefore retain a constant available advantage, yet coherent retention does not remove the dimension dependence of learning from their mixed-state training source.

This is a copy-complexity statement for one future test. It does not determine the minimum quantum memory required to attain the bound, or the lifetime of a reusable quantum model. The [resource analysis](constructions.md) charges the stored training systems used by the stated construction. The fixed-accuracy classical-compiler comparison and the precise relationship to earlier quantum-reference advantages are described in [Related work](../references/RELATED_WORK.md) and the corresponding topic proofs.
