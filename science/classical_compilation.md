# Classical compilation of the training examples

A classical compiler may perform an arbitrary collective measurement on all training examples. Its restriction is that only a classical record remains when the test arrives. Even with unlimited classical memory, computation, and record-dependent test measurements, recovering a fixed positive fraction of the known-projector advantage requires at least order $`rd`$ training examples, where $`r`$ is the rank and $`d`$ is the ambient dimension.

This section proves the converse for that entire class and gives an explicit construction based on collective state tomography. The [model](model.md) specifies the access order and risk. The [exact classifier](exact_classifier.md) supplies the likelihood identity used below; the [quantum precision theorem](quantum_precision.md) and [constructions](constructions.md) give the corresponding coherent results.

## 1. Task and compiler class

Let $`P`$ be an unknown rank-$`r`$ orthogonal projector on $`\mathbb C^d`$, with $`1\le r<d`$, and put

```math
\rho_P=\frac{P}{r}.
```

The learner receives $`N`$ independent training copies of $`\rho_P`$. One test system then arrives, equally likely to be in state $`\rho_P`$ or $`I/d`$. The training systems are independent of the test conditional on $`P`$ and the test label. The learner has no classical description of $`P`$.

A classical compiler first measures the training systems and retains a record $`y`$. When the test arrives, that record determines a binary effect $`M_y`$, with $`0\preceq M_y\preceq I`$; outcome $`M_y`$ means that the test is predicted to be $`\rho_P`$. The training measurement may be collective, adaptive within the training stage, and assisted by arbitrary independent ancillas. Its outcome space may be continuous. Unlimited classical storage and computation are allowed. These operations are represented by one POVM $`E(dy)`$ on the training registers and the family $`\{M_y\}`$.

Any intermediate quantum systems correlated with $`P`$ must be discarded before test arrival. Ancillas prepared from the classical record at test time are already included in the effect $`M_y`$. A protocol using at most $`N`$ training copies on every branch can be supplied with all $`N`$ initially and ignore unused copies, so the same description covers a maximum-budget convention.

Write $`R_P(\mathcal C)`$ for the misclassification probability, including the training measurement randomness, of a compiler $`\mathcal C`$. If $`P`$ were known, the optimal test would be $`\{P,I-P\}`$, with

```math
R_\star=\frac{r}{2d},
\qquad
A_{d,r}:=\frac12-R_\star=\frac{1-r/d}{2}.
```

Thus $`A_{d,r}`$ is the oracle's advantage over random guessing. Define the optimal worst-case excess risk within the compiler class by

```math
E_{\mathrm C}(N;d,r)
:=
\inf_{\mathcal C}
\sup_{\mathrm{rank}\,P=r}
\bigl(R_P(\mathcal C)-R_\star\bigr).
```

The error criterion is expected classification risk, not a high-probability guarantee for each individual training record.

## 2. Theorem C1: converse for every collective compiler

**Theorem C1.** For every $`1\le r<d`$, every integer $`N\ge0`$, and every classical compiler in the class above, its Haar-averaged success probability satisfies

```math
\overline p_{\mathrm C}
\le
\frac12+
\frac{N(d-r)}{2rd^2}.
\tag{C1.1}
```

Consequently,

```math
E_{\mathrm C}(N;d,r)
\ge
A_{d,r}\left(1-\frac{N}{rd}\right)_+.
\tag{C1.2}
```

Equivalently, the compiler's average fraction of the oracle advantage is at most $`\min\{1,N/(rd)\}`$. In particular, achieving a fixed positive fraction of that advantage requires $`\Omega(rd)`$ training copies.

### 2.1 Averaged hypotheses and the operator inequality

Let $`P`$ have the normalized Haar distribution on the rank-$`r`$ Grassmannian, and define

```math
A_N=\mathbb E_P\rho_P^{\otimes N},
\qquad
H_1=A_{N+1},
\qquad
H_0=A_N\otimes\frac{I}{d},
\qquad
\Delta=H_1-H_0.
```

Haar averaging is a device for proving a worst-case lower bound. The source need not resample the subspace during a classification instance.

Let $`S_{i,t}`$ swap training register $`i`$ with the test register, and set

```math
J=\sum_{i=1}^{N}S_{i,t}.
```

The exact likelihood identity, proved in [Exact classifier](exact_classifier.md), is

```math
H_1=H_0\,L(J),
\qquad
L(J)=\frac{d}{r}\frac{r+J}{d+J}.
\tag{C1.3}
```

All fractions in (C1.3) are evaluated on the support of $`H_0`$. On that support $`J\succeq-rI`$, so $`d+J`$ is strictly positive. Also $`H_0`$ commutes with $`J`$. Both hypotheses vanish outside this support, so extending the resulting operators by zero causes no ambiguity.

For a real number $`x>-d`$,

```math
\frac{x}{d}-\frac{x}{d+x}
=\frac{x^2}{d(d+x)}\ge0.
```

Functional calculus, followed by multiplication by the commuting positive operator $`H_0`$, therefore gives

```math
\begin{aligned}
\Delta
&=\frac{d-r}{r}
   \left(A_N\otimes\frac{I}{d}\right)
   \frac{J}{d+J}\\
&\preceq
\frac{d-r}{rd^2}(A_N\otimes I)J.
\end{aligned}
\tag{C1.4}
```

The right-hand side need not be positive. Only its difference from $`\Delta`$ is asserted to be positive; that is sufficient for taking its trace against a decision effect.

### 2.2 Continuous outcomes and permutation symmetrization

For a finite outcome space, the compiler's joint positive-decision effect is $`T=\sum_y E_y\otimes M_y`$. The same argument applies to arbitrary measurable outcome spaces. To make the integral notation precise, let $`D=d^N`$ and choose the scalar probability measure

```math
\mu(B)=\frac{\mathrm{Tr}E(B)}{D}.
```

Finite dimensionality gives a positive operator-valued density $`e_y`$ such that

```math
E(dy)=e_y\,\mu(dy),
\qquad
\int e_y\,\mu(dy)=I.
```

The compiler effect is consequently

```math
T=\int e_y\otimes M_y\,\mu(dy),
\qquad
0\preceq T\preceq I.
\tag{C1.5}
```

Every state $`\rho_P^{\otimes N}`$ is invariant under permutations of its training registers. We may therefore replace each density $`e_y`$ by

```math
\widetilde e_y
=\frac{1}{N!}\sum_{\pi\in S_N}
 V_\pi e_yV_\pi^\dagger.
\tag{C1.6}
```

This replacement preserves positivity, normalization, and the probability of every outcome for every $`P`$. It therefore leaves the compiler's risk unchanged, even before Haar averaging. For $`N=0`$ the averaging is trivial.

It remains essential to justify a positivity step: a product of two positive operators is not generally positive. Here the symmetrized densities commute with $`A_N`$. Indeed, in Schur–Weyl coordinates,

```math
(\mathbb C^d)^{\otimes N}
\cong
\bigoplus_{\lambda\vdash N}
 U_\lambda^{(d)}\otimes V_\lambda,
```

the commutant of the training permutation representation has the form

```math
\widetilde e_y
=\bigoplus_\lambda e_{y,\lambda}\otimes I_{V_\lambda},
```

whereas $`A_N`$ is scalar on each complete $`\lambda`$ block:

```math
A_N
=\bigoplus_\lambda
 a_\lambda I_{U_\lambda^{(d)}}\otimes I_{V_\lambda}.
```

Thus $`[\widetilde e_y,A_N]=0`$. Dropping the tilde, define

```math
F_y=e_yA_N.
```

Then

```math
F_y\succeq0,
\qquad
\int F_y\,\mu(dy)=A_N,
\qquad
\int\mathrm{Tr}F_y\,\mu(dy)=1.
\tag{C1.7}
```

These properties hold without requiring the training measurement to be a state estimator, a tensor product measurement, or a finite-outcome measurement.

### 2.3 Trace bound and risk consequence

Let $`F_y^{(i)}`$ denote the reduced operator of $`F_y`$ on training register $`i`$. The swap trace identity gives

```math
\mathrm{Tr}\bigl[(F_y\otimes M_y)S_{i,t}\bigr]
=\mathrm{Tr}\bigl[F_y^{(i)}M_y\bigr].
\tag{C1.8}
```

Because $`F_y^{(i)}\succeq0`$ and $`0\preceq M_y\preceq I`$,

```math
0\le
\mathrm{Tr}\bigl[F_y^{(i)}M_y\bigr]
\le\mathrm{Tr}F_y.
```

Taking the trace of (C1.4) against the positive effect (C1.5), and then using (C1.7)–(C1.8), yields

```math
\begin{aligned}
\mathrm{Tr}(T\Delta)
&\le
\frac{d-r}{rd^2}
\int\sum_{i=1}^{N}
\mathrm{Tr}\bigl[F_y^{(i)}M_y\bigr]\,\mu(dy)\\
&\le
\frac{d-r}{rd^2}
\int N\mathrm{Tr}F_y\,\mu(dy)\\
&=\frac{N(d-r)}{rd^2}.
\end{aligned}
\tag{C1.9}
```

All integrands in the second line are nonnegative and integrable, with their total trace fixed by (C1.7). The finite sum and integral therefore introduce no convergence issue.

For equal priors, success is

```math
\overline p_{\mathrm C}
=\frac12\mathrm{Tr}(TH_1)
 +\frac12\mathrm{Tr}((I-T)H_0)
=\frac12+\frac12\mathrm{Tr}(T\Delta).
```

Equation (C1.9) proves (C1.1). Subtracting this success bound from the known-$`P`$ optimum gives (C1.2), since worst-case risk is at least Haar-average risk and excess risk is nonnegative. The independent oracle bound also caps the success advantage at $`A_{d,r}`$. This completes the proof.

The Haar-average and minimax optima agree for this covariant family. To see this within the compiler class, randomize a compiler by a Haar unitary applied to all training registers and to the later test, retaining the unitary as part of the classical record. The resulting risk is the original compiler's Haar-average risk for every $`P`$. This observation is compatible with unrestricted continuous classical outcomes; the converse itself only needs the simpler average-to-worst-case implication.

## 3. Theorem C2: constructive upper bound

The upper bound uses the collective measurement analyzed by O'Donnell and Wright. Their Theorem 1.2 gives, for every $`d`$-dimensional state $`\rho`$ and every $`N\ge1`$, a classical Hermitian matrix estimate $`\widehat\rho`$ satisfying

```math
\mathbb E_\rho
\|\widehat\rho-\rho\|_F^2
\le\frac{4d-3}{N}.
\tag{C2.1}
```

Here $`\|X\|_F^2=\mathrm{Tr}(X^\dagger X)`$. The expectation is over the measurement record. The statement is uniform in the state and has no dimension logarithm. [C-OW]

**Theorem C2.** For known rank $`r`$, there is a classical compiler using $`N\ge1`$ training copies such that, for every rank-$`r`$ projector $`P`$,

```math
R_P(\mathcal C)-R_\star
\le\frac{(4d-3)r}{N}.
\tag{C2.2}
```

Consequently,

```math
E_{\mathrm C}(N;d,r)
\le
\min\left\{A_{d,r},\frac{(4d-3)r}{N}\right\}.
\tag{C2.3}
```

### Proof

During training, perform the collective measurement that produces $`\widehat\rho`$ in (C2.1). From that classical record, let $`\widehat P`$ be a projector onto the $`r`$ largest eigenvalues of $`\widehat\rho`$. Resolve eigenvalue ties by any fixed measurable convention. At test time, apply the binary measurement $`\{\widehat P,I-\widehat P\}`$, predicting $`\rho_P`$ on the first outcome. All training systems have already been measured and discarded.

The state $`\widehat P/r`$ is a closest normalized rank-$`r`$ projector to $`\widehat\rho`$ in Frobenius norm. Indeed, for any rank-$`r`$ projector $`Q`$,

```math
\left\|\widehat\rho-\frac{Q}{r}\right\|_F^2
=\|\widehat\rho\|_F^2+\frac1r
 -\frac{2}{r}\mathrm{Tr}(\widehat\rho Q),
```

and the top-$`r`$ eigenspace maximizes the last trace. Since the true $`P/r`$ belongs to this comparison class, the triangle inequality implies

```math
\left\|\frac{\widehat P}{r}-\frac{P}{r}\right\|_F
\le
\left\|\frac{\widehat P}{r}-\widehat\rho\right\|_F
 +\left\|\widehat\rho-\frac{P}{r}\right\|_F
\le
2\left\|\widehat\rho-\frac{P}{r}\right\|_F.
\tag{C2.4}
```

For a fixed training record, the classifier's error is

```math
R_P(\widehat P)
=\frac12\left(1-\frac{\mathrm{Tr}(P\widehat P)}{r}\right)
 +\frac12\frac{\mathrm{Tr}\widehat P}{d}.
```

Both projectors have rank $`r`$. Therefore its excess risk has the exact expression

```math
\begin{aligned}
R_P(\widehat P)-R_\star
&=\frac{r-\mathrm{Tr}(P\widehat P)}{2r}\\
&=\frac{\|P-\widehat P\|_F^2}{4r}\\
&\le r\left\|\widehat\rho-\frac{P}{r}\right\|_F^2.
\end{aligned}
\tag{C2.5}
```

Taking the expectation and applying (C2.1) proves (C2.2). The additional option of guessing the label uniformly at random has excess risk $`A_{d,r}`$, which proves (C2.3).

This construction concerns sample complexity. It allows the collective tomography measurement and a classical matrix record of unrestricted size, exactly as the compiler model permits. It requires neither a state-preparation oracle nor quantum random access to classical training data.

## 4. A precise fixed-accuracy comparison

Define

```math
N_{\mathrm C}(d,r,\varepsilon)
:=\min\{N:E_{\mathrm C}(N;d,r)\le\varepsilon\}.
```

Take the numerical target $`\varepsilon_0=1/16`$ and restrict $`1\le r\le d/2`$. In this range $`A_{d,r}\ge1/4`$. Theorem C1 implies

```math
N_{\mathrm C}(d,r,1/16)
\ge
\left\lceil rd\left(1-\frac{1}{16A_{d,r}}\right)\right\rceil
\ge
\left\lceil\frac34rd\right\rceil.
\tag{C3.1}
```

Theorem C2 supplies the sufficient budget

```math
N_{\mathrm C}(d,r,1/16)
\le
\left\lceil16r(4d-3)\right\rceil.
\tag{C3.2}
```

Hence, with universal constants and with the same excess-risk target for every admissible rank and dimension,

```math
\boxed{N_{\mathrm C}(d,r,1/16)=\Theta(rd).}
\tag{C3.3}
```

The [quantum precision theorem](quantum_precision.md) gives $`N_{\mathrm Q}(d,r,1/16)=\Theta(r^2)`$. The fixed-accuracy sample advantage from retaining the training systems is therefore of order $`d/r`$. It is large at low rank and becomes a constant factor when rank is proportional to the ambient dimension.

For general precision, the statements proved here are

```math
N_{\mathrm C}(d,r,\varepsilon)
\ge
\left\lceil rd\left(1-\frac{\varepsilon}{A_{d,r}}\right)\right\rceil
\quad(0<\varepsilon<A_{d,r}),
```

and

```math
N_{\mathrm C}(d,r,\varepsilon)
\le
\left\lceil\frac{(4d-3)r}{\varepsilon}\right\rceil.
```

The first bound alone does not establish an inverse-$`\varepsilon`$ classical lower bound. A second lower bound follows from the inclusion of classical compilers in the unrestricted quantum class.

### Corollary C3: combined lower bound and proportional rank

For $`1\le r\le d/2`$ and $`0<\varepsilon\le1/8`$, the [quantum precision theorem](quantum_precision.md) gives

```math
N_{\mathrm C}(d,r,\varepsilon)
\ge N_{\mathrm Q}(d,r,\varepsilon)
\ge\left\lceil\frac{r^2}{8\varepsilon}\right\rceil.
```

Combining this with Theorems C1 and C2 yields

```math
\left\lceil
\max\left\{
\frac{r^2}{8\varepsilon},
rd\left(1-\frac{\varepsilon}{A_{d,r}}\right)
\right\}
\right\rceil
\le N_{\mathrm C}(d,r,\varepsilon)
\le
\left\lceil\frac{(4d-3)r}{\varepsilon}\right\rceil.
\tag{C3.4}
```

In particular, fix any constant $`c\in(0,1/2]`$ and take $`cd\le r\le d/2`$. The first lower bound in (C3.4) is at least $`c^2d^2/(8\varepsilon)`$, while its upper bound is at most $`2d^2/\varepsilon`$ before integer rounding. Therefore, uniformly over $`0<\varepsilon\le1/8`$,

```math
N_{\mathrm C}(d,r,\varepsilon)
=\Theta_c\!\left(\frac{d^2}{\varepsilon}\right)
,\qquad N_{\mathrm Q}(d,r,\varepsilon)
=\Theta_c\!\left(\frac{d^2}{\varepsilon}\right).
\tag{C3.5}
```

The constants may depend on $`c`$. Both access models thus have the same sample-complexity order throughout the precision range when rank is a fixed fraction of dimension. For general rank, (C3.4) leaves a gap between the lower and upper precision bounds. The fixed-accuracy $`\Theta(rd)`$ result therefore does not assert a general $`\Theta(rd/\varepsilon)`$ law.

## 5. Relation to existing work

The tomography measurement and its quantitative bound (C2.1) are inherited from O'Donnell–Wright. Theorem C2 applies that bound to the present flat-spectrum classification loss; equation (C2.5) is the explicit link between subspace estimation error and prediction regret. [C-OW]

For rank two, An studies the same training-first classicalization order in leakage detection, allowing arbitrary collective reference measurements. Its posterior converse concerns the decision effect independently of the returned-message constraint. Consequently the fixed-rank-two dimension separation is already present there. Theorem C1 gives the displayed bound uniformly in rank and connects it to the minimum-error prediction problem studied here. [C-An]

Li, Theil, Harrow, and Chuang likewise allow collective reference measurements followed by operations on independent quantum data controlled by the classical record. In the second version of their coherent-inference paper, the density-matrix-exponentiation converse requires approximation of a unitary channel uniformly over auxiliary inputs, measured in induced trace norm. Its proof uses a local family of pure program states. That channel task supplies relevant context for the access order but does not by itself prove the promised single-test classification converse (C1.1). [C-CQI]

## References

**[C-OW]** Ryan O'Donnell and John Wright, *Efficient quantum tomography*, Proceedings of STOC 2016, pp. 899–912. [arXiv:1508.01907v2](https://arxiv.org/html/1508.01907v2). Theorem 1.2 is the expected squared-Frobenius bound used in Theorem C2; Corollary 1.4 separately states the trace-distance sample bound without a logarithmic factor.

**[C-An]** Zheng An, *Exponential Advantage of Quantum over Classical References in Leakage Detection*, [arXiv:2609.36541v1](https://arxiv.org/html/2609.36541v1), 2026. See the End Matter, supplemental Section III, and Section IX for the collective measurement-first posterior inequality and its scope.

**[C-CQI]** Zhaoyi Li, Elias Theil, Aram W. Harrow, and Isaac Chuang, *An Exponential Sample-Complexity Advantage for Coherent Quantum Inference*, [arXiv:2605.21457v2](https://arxiv.org/html/2605.21457v2), 2026. See supplemental Section S5, particularly equation (S110), Lemma S5.1, and Theorem S5.3.
