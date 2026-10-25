# From Watrous to the classification theorems

The selected anchor is **John Watrous, The Theory of Quantum Information, Cambridge University Press, 2018**. The reference version for this bridge is the author's **2018 standard-layout manuscript**, available through his [books page](https://jhwatrous.github.io/books-and-courses.html). Section and theorem numbers below refer to that manuscript; page numbers are its printed page numbers.

The book supplies the operational language of states, measurements, channels, and symmetry. The project adds the representation formulas and decision calculations needed for an unknown flat-spectrum source. This page connects those ingredients to the canonical proofs and to the [30 project milestones](milestones.md). It links to the author-hosted chapters and does not redistribute the manuscript.

## Targeted passages

| Project use | Verified passage in the anchor | Milestones |
|---|---|---|
| Positive operators, projectors, spectral decompositions, and matrix norms | [Chapter 1](https://jhwatrous.github.io/TQI.1.pdf), §§1.1.2–1.1.3, pp. 8, 24; the Schatten-norm discussion is on pp. 32–34 | [M01](milestones.md#m01), [M05](milestones.md#m05) |
| Density operators, product states, and partial traces | [Chapter 2](https://jhwatrous.github.io/TQI.2.pdf), §§2.1.2–2.1.3, pp. 61, 67 | [M01–M02](milestones.md#m01), [M04](milestones.md#m04) |
| Channels and their operator representations | [Chapter 2](https://jhwatrous.github.io/TQI.2.pdf), §§2.2.1–2.2.2, pp. 72, 77 | [M04](milestones.md#m04), [M23–M24](milestones.md#m23) |
| Measurement effects and outcome probabilities | [Chapter 2](https://jhwatrous.github.io/TQI.2.pdf), §2.3.1, p. 100; Definition 2.34 and equation (2.201), p. 101 | [M03](milestones.md#m03) |
| Optimal binary discrimination | [Chapter 3](https://jhwatrous.github.io/TQI.3.pdf), §3.1.1, p. 125; Theorem 3.4 and its proof, pp. 128–129 | [M06](milestones.md#m06), [M13–M16](milestones.md#m13) |
| Channel error with a reference system | [Chapter 3](https://jhwatrous.github.io/TQI.3.pdf), §3.3.2, p. 166; Definition 3.43, p. 170, and Proposition 3.44, p. 171 | [M07](milestones.md#m07), [M24–M25](milestones.md#m24) |
| Register permutations and their commutants | [Chapter 7](https://jhwatrous.github.io/TQI.7.pdf), §7.1.1, equation (7.3), p. 391; §7.1.2, p. 400, especially Theorem 7.15, p. 407 | [M09–M10](milestones.md#m09), [M20](milestones.md#m20) |
| Haar averaging and evaluation by symmetry | [Chapter 7](https://jhwatrous.github.io/TQI.7.pdf), §7.2.1, p. 408; Definition 7.18, p. 411, Proposition 7.20, p. 413, and Lemma 7.24, pp. 416–417 | [M08](milestones.md#m08), [M13](milestones.md#m13) |

Theorem 7.15 identifies operators commuting with every collective unitary as linear combinations of register permutations. The partition labels, one-box branching, dimension formulas, and content moments used below are additional representation inputs recorded in the project proofs. The pure-state integral in Lemma 7.24 is a useful special case; mixed flat states require more than the symmetric-vector sector.

## Notation and the exact experiment

| Anchor notation or convention | Project notation or use |
|---|---|
| $`A^*`$ | $`A^\dagger`$, the adjoint |
| $`\mathrm{Pos}(\mathcal X)`$ and $`\mathrm D(\mathcal X)`$ | Positive semidefinite operators and density operators on a finite-dimensional register |
| A measurement $`\mu(a)`$ | An effect such as $`T`$, $`E_y`$, or $`M_y`$; probabilities are traces against the state |
| Schatten $`2`$-norm | $`\lVert X\rVert_F`$, the Frobenius norm |
| Schatten $`1`$-norm | $`\lVert X\rVert_1`$; normalized trace distance is half the norm of a state difference |
| The completely bounded trace norm, written with triple bars in the book | $`\lVert\Phi\rVert_\diamond`$ |
| $`W_\pi`$ for a register permutation | $`V_\pi`$ in the exact-classifier proof |
| The prior parameter $`\lambda`$ in Theorem 3.4 | Set to $`1/2`$ here; the project's later $`\lambda`$ labels a partition |

The assumptions are those of the [model](../science/model.md), consolidated in [M12](milestones.md#m12):

- The source fixes an unknown rank-$`r`$ projector $`P`$ on $`\mathbb C^d`$, and supplies $`N`$ independent copies of $`\rho_P=P/r`$.
- One test arrives after training. With equal prior probability it is $`\rho_P`$ or $`\tau_d=I_d/d`$. Conditional on $`P`$ and the label, the training systems and test are independent.
- Access consists of the supplied copies. There is no description, purification, or preparation oracle for the unknown state, and no additional source access after the test arrives.
- A coherent learner can retain the training systems. A classical compiler must measure them before the test arrives and retain only a classical record, with arbitrary collective training measurements and unrestricted classical computation allowed.
- The output is one label. The test can be destroyed, both kinds of error are allowed, and the model has no reuse requirement.

The exact formulas use $`1\le r<d`$. The dimension-uniform precision statements use $`1\le r\le d/2`$ and $`0<\varepsilon\le1/8`$. Risk includes averaging over the equal label prior and measurement randomness, followed by the worst case over $`P`$.

## 1. From the experiment to binary state discrimination

**Milestones:** [M02–M06](milestones.md#m02), [M08](milestones.md#m08), [M13](milestones.md#m13).  
**Canonical proofs:** [model](../science/model.md) and [exact classifier, §1](../science/exact_classifier.md#1-reduction-to-two-averaged-states).

An arbitrary procedure ending in a binary label induces a positive effect $`0\le T\le I `$ on the supplied systems. This includes an ancilla-assisted circuit: the adjoint of its channel pulls the final measurement effect back to the original registers. For a fixed source,

```math
p(T,P)=\frac12\mathrm{Tr}\!\left(T\rho_P^{\otimes(N+1)}\right)
+\frac12\mathrm{Tr}\!\left[(I-T)
 \left(\rho_P^{\otimes N}\otimes\tau_d\right)\right].
```

When $`P`$ is known, $`\rho_P-\tau_d`$ is positive on the support of $`P`$ and negative on its orthogonal complement. Theorem 3.4 therefore selects the support measurement. Its risk and advantage over guessing are

```math
R_*(d,r)=\frac{r}{2d},
\qquad
A_{d,r}=\frac12-R_*=\frac{1-r/d}{2}.
```

The unknown-source problem becomes a pair of known averaged operators by integrating over $`P=UP_0U^\dagger`$ with normalized Haar measure:

```math
A_n=\mathbb E_P\rho_P^{\otimes n},
\qquad
H_1=A_{N+1},
\qquad
H_0=A_N\otimes\tau_d.
```

The same projector occurs in every tensor factor before averaging. Replacing $`A_n`$ by $`(\mathbb E_P\rho_P)^{\otimes n}`$ would discard the shared-source correlations that make learning possible.

For $`\Delta=H_1-H_0`$, the equal-prior specialization of the discrimination theorem is

```math
\overline p(T)=\frac12+\frac12\mathrm{Tr}(T\Delta),
\qquad
\sup_{0\le T\le I}\overline p(T)
=\frac12+\frac14\lVert\Delta\rVert_1.
```

The remaining task is to identify the positive eigenspaces of $`\Delta`$. Haar averaging is used to analyze the fixed-source experiment. Once an optimal effect is invariant under collective unitary rotations, its success is constant over all rank-$`r`$ projectors. The inequality

```math
\inf_Pp(T,P)\le\mathbb E_Pp(T,P)
```

then converts its optimal average value into the minimax value.

## 2. Permutation invariance and partition blocks

**Milestones:** [M09–M11](milestones.md#m09), [M13–M14](milestones.md#m13).  
**Canonical proof:** [exact classifier, §§2–3](../science/exact_classifier.md#2-haar-moments-and-their-support).

### Invariant operators need not be supported on symmetric vectors

Watrous distinguishes two actions. A symmetric vector satisfies $`V_\pi v=v`$. An invariant operator satisfies $`V_\pi X V_\pi^\dagger=X`$. The second condition allows weight in several representation sectors.

This distinction already matters for two mixed copies. Let $`S`$ swap them and let $`\Pi_-=(I-S)/2`$ project onto antisymmetric vectors. The swap trace identity gives

```math
\mathrm{Tr}\!\left(\Pi_-\rho_P^{\otimes2}\right)
=\frac{1-\mathrm{Tr}(\rho_P^2)}2
=\frac{1-1/r}{2}.
```

This is positive whenever $`r>1`$, although $`\rho_P^{\otimes2}`$ commutes with the swap. The mixed-state proof must therefore retain the full partition decomposition.

### The representation input used by the project

A partition $`\lambda\vdash n`$ is a nonincreasing list of nonnegative integers summing to $`n`$. Its diagram has $`\lambda_i`$ boxes in row $`i`$. Write $`\ell(\lambda)`$ for the number of nonempty rows. The Schur-Weyl decomposition is

```math
(\mathbb C^k)^{\otimes n}
\cong
\bigoplus_{\substack{\lambda\vdash n\\\ell(\lambda)\le k}}
U_\lambda^{(k)}\otimes V_\lambda.
```

Collective unitaries act on $`U_\lambda^{(k)}`$, while permutations act on $`V_\lambda`$. Their dimensions are $`D_\lambda(k)`$ and $`f_\lambda`$. For a box $`b=(i,j)`$, its content is $`c(b)=j-i`$, and its hook length $`h_\lambda(b)`$ counts that box and the boxes directly to its right and below. The needed dimension identities are

```math
f_\lambda=\frac{n!}{\prod_{b\in\lambda}h_\lambda(b)},
\qquad
D_\lambda(k)
=\frac{f_\lambda}{n!}\prod_{b\in\lambda}(k+c(b)).
```

The unitary representation is absent when $`\ell(\lambda)>k`$. Adding one tensor factor corresponds to adding one box. On restriction from $`S_{N+1}`$ to $`S_N`$,

```math
V_\mu\!\downarrow_{S_N}
\cong\bigoplus_{\lambda:\lambda\nearrow\mu}V_\lambda.
```

Each allowed branch occurs once. Conversely, the representation induced from a fixed $`V_\lambda`$ has dimension $`(N+1)f_\lambda`$ and decomposes over its one-box successors. Thus

```math
q_{\lambda\mu}:=\frac{f_\mu}{(N+1)f_\lambda},
\qquad
\sum_{\mu:\lambda\nearrow\mu}q_{\lambda\mu}=1,
\qquad
\frac{D_\mu(k)}{D_\lambda(k)}
=(k+c(\mu/\lambda))q_{\lambda\mu}.
```

These standard representation identities are stated in the [exact-classifier proof](../science/exact_classifier.md#3-hook-content-ratio-and-the-likelihood-operator), with their role distinguished from the new decision calculation. The project's [representation-source discussion](../references/RELATED_WORK.md#odonnell2015) records the relevant antecedents. They supplement the commutant statement in Watrous.

### Why the averaged state is scalar in each block

The tensor power $`\rho_P^{\otimes n}`$ commutes with every permutation. Haar averaging also makes it commute with every collective unitary. The two actions on the decomposition therefore force

```math
A_n
=\bigoplus_\lambda a_\lambda^{(n)}
 I_{U_\lambda^{(d)}}\otimes I_{V_\lambda},
\qquad
a_\lambda^{(n)}
=\frac{D_\lambda(r)}{r^nD_\lambda(d)}.
```

The numerator comes from tracing the tensor power on the $`r`$-dimensional support, and the denominator divides that trace among the $`D_\lambda(d)`$ unitary directions. Exactly the diagrams with at most $`r`$ rows have positive coefficient. Their training probabilities are

```math
w_{N,r}(\lambda)=\frac{f_\lambda D_\lambda(r)}{r^N}.
```

Normalization is the dimension identity for $`(\mathbb C^r)^{\otimes N}`$.

## 3. From one-box branching to the exact classifier

**Milestones:** [M14–M16](milestones.md#m14).  
**Canonical proof:** [exact classifier, §§3–5](../science/exact_classifier.md#3-hook-content-ratio-and-the-likelihood-operator).

On the common block labeled by $`\lambda\nearrow\mu`$, the eigenvalues of $`H_0`$ and $`H_1`$ are $`a_\lambda^{(N)}/d`$ and $`a_\mu^{(N+1)}`$. Dividing them and using the dimension ratio twice gives

```math
L(c)=\frac{a_\mu^{(N+1)}}{a_\lambda^{(N)}/d}
=\frac dr\,\frac{r+c}{d+c}.
```

This ratio is used only on the support of $`H_0`$. Every active diagram has at most $`r`$ rows, so $`c\ge-r`$ and $`d+c>0`$. A successor with a new $`(r+1)`$st row has $`c=-r`$ and zero likelihood, consistent with the support of $`H_1`$. Outside those training sectors, the diagram and every successor have more than $`r`$ rows, so both hypotheses vanish.

To identify the corresponding measurement, define the central transposition sum

```math
Z_n=\sum_{1\le i\lt j\le n}(ij).
```

Its action on $`V_\lambda`$ is the scalar $`\theta_\lambda=\sum_{b\in\lambda}c(b)`$. The [canonical derivation](../science/exact_classifier.md#3-hook-content-ratio-and-the-likelihood-operator) obtains that scalar by comparing the next-to-leading coefficient of the dimension polynomial with its character expansion. The difference $`Z_{N+1}-Z_N`$ is the sum of training–test swaps,

```math
J_N=\sum_{i=1}^N V_{(i,N+1)},
```

and its eigenvalue on a branch is $`\theta_\mu-\theta_\lambda=c`$. Consequently,

```math
L(c)-1=\frac{(d-r)c}{r(d+c)}.
```

Its sign is the sign of $`c`$. The positive spectral projector of $`J_N`$ is therefore the Helstrom effect for the averaged hypotheses. It is invariant under collective unitaries, so the argument in §1 gives minimax optimality. The effect depends on the supplied registers but not on the rank.

### The two branch distributions

The physical branch distribution under $`H_0`$ is

```math
p_0(\mu\mid\lambda)
=\frac{D_\mu(d)}{dD_\lambda(d)}
=\frac{d+c}{d}\,q_{\lambda\mu}.
```

The growth probabilities $`q_{\lambda\mu}`$ enter after cancellation with the likelihood:

```math
p_0(\mu\mid\lambda)(1-L(c))_+
=\left(1-\frac rd\right)
q_{\lambda\mu}\frac{(-c)_+}{r}.
```

Draw $`\lambda`$ with probability $`w_{N,r}(\lambda)`$, then a successor with probability $`q_{\lambda\mu}`$, and let $`C`$ be its content. The exact learning curve becomes

```math
F_{N,r}=\mathbb E\frac{(-C)_+}{r},
\qquad
p_{\mathrm Q}(N;d,r)=\frac12+A_{d,r}F_{N,r},
\qquad
E_{\mathrm Q}(N;d,r)=A_{d,r}(1-F_{N,r}).
```

This auxiliary growth law is independent of $`d`$. The cancellation, together with the oracle factor $`A_{d,r}`$, explains the exact separation of dimension and rank in the learning curve.

## 4. From content moments to the precision converse

**Milestones:** [M17–M19](milestones.md#m17), [M25](milestones.md#m25).  
**Canonical proof:** [quantum precision, §§1–4](../science/quantum_precision.md#1-the-transition-content-distribution).

The distribution just defined satisfies

```math
C\ge-r,
\qquad
\mathbb E[C\mid\lambda]=0,
\qquad
\mathbb E[C^2\mid\lambda]=N.
```

The moment identities are representation statements. Their finite proof in the project uses an induced representation, rather than an asymptotic distributional approximation.

Here is the calculation connecting the branching rule to those moments. Put $`W_\lambda=\mathrm{Ind}_{S_N}^{S_{N+1}}V_\lambda`$. In its decomposition over successors, the normalized trace weights are precisely $`q_{\lambda\mu}`$. The eigenvalues of $`Z_{N+1}-\theta_\lambda I `$ are the added contents.

A permutation moving $`m`$ points fixes $`N+1-m`$ cosets. For $`m\le N`$, its normalized induced character is its normalized character at size $`N`$, multiplied by $`(N+1-m)/(N+1)`$. For $`m=N+1`$, no coset is fixed and the induced character is zero. Summing over transpositions gives normalized trace $`\theta_\lambda`$ for $`Z_{N+1}`$. For the second moment, the identity

```math
Z_n^2=\binom n2 I
+3\sum_{\text{3-cycles }g}g
+2\sum_{\text{disjoint transposition pairs }g}g
```

separates the possible ordered products of two transpositions. For each nonidentity cycle type, its count and the induced-character factor cancel because

```math
\binom{N+1}{m}\frac{N+1-m}{N+1}=\binom Nm.
```

Only the identity coefficient changes, by $`N`$. Thus the first two normalized traces of $`Z_{N+1}`$ are $`\theta_\lambda`$ and $`\theta_\lambda^2+N`$. Centering by $`\theta_\lambda`$ proves the displayed moments. Absent cycle types contribute zero; the empty diagram is handled directly. The [full moment proof](../science/quantum_precision.md#2-proof-of-the-two-content-moments) spells out these boundary cases.

### Two consequences of the same moments

Mean zero makes the positive and negative parts of $`C`$ have equal expectations. Cauchy–Schwarz then gives

```math
F_{N,r}=\frac{\mathbb E|C|}{2r}
\le\frac{\sqrt N}{2r}.
```

For $`N\le r^2`$, at least half the oracle advantage remains unrecovered.

For $`N\ge r^2`$, use the quadratic

```math
Q(c)=\frac{r^2(c-N/r)^2}{(N+r^2)^2}.
```

It bounds $`(-c)_+/r`$ from above on $`c\ge-r`$. For nonnegative $`c`$ this is immediate. On $`[-r,0]`$, the difference $`g(c)=Q(c)+c/r`$ is convex, vanishes at $`-r`$, and has nonnegative derivative there:

```math
g'(-r)=\frac{N-r^2}{r(N+r^2)}\ge0.
```

Taking expectations uses only the two moments:

```math
F_{N,r}\le\mathbb E Q(C)=\frac{N}{N+r^2},
\qquad
E_{\mathrm Q}(N;d,r)\ge A_{d,r}\frac{r^2}{N+r^2}.
```

Because $`F_{N,r}`$ is the exact optimum, this is a converse for every allowed coherent learner. The construction below supplies the matching upper order. Combining the small-budget and precision regimes yields

```math
\left\lceil\frac{r^2}{8\varepsilon}\right\rceil
\le N_{\mathrm Q}(d,r,\varepsilon)
\le\left\lceil\frac{2\pi^2r^2}{\varepsilon}\right\rceil
\quad
\left(1\le r\le d/2,\quad0<\varepsilon\le1/8\right).
```

## 5. What changes when training leaves only a classical record

**Milestones:** [M04](milestones.md#m04), [M20–M22](milestones.md#m20), [M26](milestones.md#m26).  
**Canonical proof:** [classical compilation](../science/classical_compilation.md).

If training produces outcome $`y`$ and the later test uses effect $`M_y`$, the joint decision effect is

```math
T_{\mathrm C}=\int E(dy)\otimes M_y.
```

The tensor-product form follows from the order of access: the test is absent when the training measurement is made. A record-dependent ancilla prepared later can be absorbed into $`M_y`$. This argument allows a collective training POVM; it does not require separately measured copies.

The converse needs an additional positivity fact. Average each training effect over register permutations. This preserves its outcome probabilities for every tensor-power input. The averaged effect commutes with $`A_N`$, since $`A_N`$ is scalar on each full Schur block. Using a positive density $`e_y`$ for the POVM, the operators

```math
F_y=e_yA_N
```

are consequently positive and satisfy $`\int\mathrm{Tr}(F_y)\,d\mu(y)=1`$. Commutation is essential here: positivity of the factors alone would not justify positivity of their product. The [continuous-outcome argument](../science/classical_compilation.md#22-continuous-outcomes-and-permutation-symmetrization) gives the measure and operator density explicitly.

The likelihood formula and the scalar inequality

```math
\frac{x}{d}-\frac{x}{d+x}
=\frac{x^2}{d(d+x)}\ge0
\quad(x>-d)
```

give the operator bound

```math
H_1-H_0
\preceq\frac{d-r}{rd^2}(A_N\otimes I)J_N.
```

For each swap in $`J_N`$, partial tracing reduces the contribution to

```math
\mathrm{Tr}\!\left[(F_y\otimes M_y)V_{(i,N+1)}\right]
=\mathrm{Tr}\!\left(F_y^{(i)}M_y\right)
\le\mathrm{Tr}(F_y).
```

Summing the $`N`$ terms and integrating proves

```math
p_{\mathrm C}(N;d,r)-\frac12
\le A_{d,r}\frac{N}{rd}.
```

This is the decision converse C1. It applies without requiring the record to be an estimated state.

### The separate constructive role of tomography

For the upper bound C2, a state estimate is useful. O'Donnell–Wright's collective tomography theorem supplies

```math
\mathbb E\lVert\widehat\rho-\rho_P\rVert_F^2
\le\frac{4d-3}{N}.
```

This input is [Theorem 1.2 of the cited tomography paper](../references/RELATED_WORK.md#odonnell2016). The project then takes the top-$`r`$ projector $`\widehat P`$ of $`\widehat\rho`$. Because $`\widehat P/r`$ is a nearest flat rank-$`r`$ state, the triangle inequality gives

```math
\lVert\widehat P-P\rVert_F
\le2r\lVert\widehat\rho-P/r\rVert_F.
```

The classifier using effect $`\widehat P`$ has the exact regret

```math
R_P(\widehat P)-R_*
=\frac{r-\mathrm{Tr}(P\widehat P)}{2r}
=\frac{\lVert P-\widehat P\rVert_F^2}{4r}.
```

Thus $`E_{\mathrm C}\le(4d-3)r/N`$. The use of squared Frobenius loss is what makes this an $`O(rd/\varepsilon)`$ construction for excess classification error $`\varepsilon`$. The lower and upper bounds give $`\Theta(rd)`$ copies at fixed nontrivial accuracy. The general-rank classical precision converse remains unmatched; the [combined bounds and proportional-rank corollary](../science/classical_compilation.md#corollary-c3-combined-lower-bound-and-proportional-rank) state exactly what follows.

## 6. A reflection built from the supplied copies

**Milestones:** [M07](milestones.md#m07), [M23–M25](milestones.md#m23), [M27](milestones.md#m27).  
**Canonical proof:** [constructions and resource account](../science/constructions.md).

The optimal spectral measurement establishes the statistical value. To attain its sample order with explicit operations, the project specializes sample-based Hamiltonian simulation.

Append a known qubit in state $`|1\rangle`$ to each training example, forming

```math
\sigma_P=|1\rangle\langle1|\otimes\frac{P}{r}.
```

At time $`t=\pi r`$, its exponential is

```math
e^{-it\sigma_P}
=|0\rangle\langle0|\otimes I
+|1\rangle\langle1|\otimes(I-2P).
```

The known program qubit therefore turns an ordinary simulation target on dimension $`2d`$ into the required controlled reflection. Each program state uses one supplied example and a known ancilla. A Hadamard readout of the control measures the test effect $`P`$ in the ideal limit.

For one independent program copy of state $`\sigma`$, a partial swap produces

```math
\Phi_\delta(X)
=\mathrm{Tr}_{\mathrm{prog}}\!\left[
e^{-i\delta S}(X\otimes\sigma)e^{i\delta S}
\right],
\qquad
\left.\frac{d}{d\delta}\Phi_\delta(X)\right|_{\delta=0}
=-i[\sigma,X].
```

The derivative agrees with the target unitary channel, including when the data is correlated with a reference. The commutator generators have diamond norm at most two. Bounding each second-order integral remainder gives

```math
\lVert\Phi_\delta-\mathcal U_\delta\rVert_\diamond
\le4\delta^2,
\qquad
\mathcal U_\delta(X)=e^{-i\delta\sigma}Xe^{i\delta\sigma}.
```

Every step uses a fresh program copy. Channel norm one, as in Watrous's Proposition 3.44, makes the errors telescope under composition:

```math
\lVert\Phi_{t/m}^{\,m}-\mathcal U_t\rVert_\diamond
\le m\,4(t/m)^2
=\frac{4t^2}{m}.
```

A binary outcome probability changes by at most half the trace norm of the state difference. Preparation and readout are channels, so the resulting excess classification risk is at most

```math
\frac{2t^2}{m}=\frac{2\pi^2r^2}{m}.
```

This proves the constructive side of Q2. The rank enters the chosen simulation time and budget; Q1's exact decision measurement remains independent of rank.

The resource count follows the experiment's access order. The examples arrive before the test, so all unused program copies require storage until prediction. For $`d=2^n`$, the direct construction stores $`mn`$ unknown-state qubits even though each interaction has active width $`2n+O(1)`$. Source preparation and gate synthesis have their own charged costs, specified in the [resource table](../science/constructions.md#gates-active-width-and-stored-data). Small active width does not change the initial training storage.

## 7. Proof connections across the milestone map

| Milestones | Connection established by this bridge | Canonical destination |
|---|---|---|
| [M01–M07](milestones.md#m01) | States and effects define the experiment; norm conventions fix risk and simulation constants | [Model](../science/model.md), [constructions](../science/constructions.md) |
| [M08–M12](milestones.md#m08) | Haar symmetry and the two commuting actions lead to the partition data needed by the model | [Exact classifier, §§1–3](../science/exact_classifier.md#1-reduction-to-two-averaged-states) |
| [M13–M16](milestones.md#m13) | Averaged hypotheses, one-box likelihood, rank-independent decision, and exact factorization | [Theorem Q1](../science/exact_classifier.md#theorem-q1-exact-minimax-decision-and-value) |
| [M17–M19](milestones.md#m17) | Content moments give both the rank-squared threshold and the precision majorant | [Quantum precision, §§1–4](../science/quantum_precision.md#1-the-transition-content-distribution) |
| [M20–M22](milestones.md#m20) | A classical record yields the C1 positivity argument; squared estimation error yields C2 | [Classical compilation](../science/classical_compilation.md) |
| [M23–M25](milestones.md#m23) | Augmented program copies and channel-error composition attain the lower-bound order | [Construction](../science/constructions.md), [Theorem Q2](../science/quantum_precision.md#theorem-q2-finite-sample-risk-and-copy-complexity) |
| [M26–M28](milestones.md#m26) | Copy complexity, retained storage, and rank determine the operational comparison | [Classical comparison](../science/classical_compilation.md#4-a-precise-fixed-accuracy-comparison), [interpretation](../science/interpretation.md) |
| [M29–M30](milestones.md#m29) | The full argument combines inherited tools with the project's exact decision and converse calculations | [Attribution](../references/RELATED_WORK.md), [verification scope](../verification/README.md) |

At fixed excess risk $`1/16`$ and $`r\le d/2`$, the resulting copy orders are $`\Theta(r^2)`$ for coherent prediction and $`\Theta(rd)`$ for classical compilation. The coherent precision order is $`\Theta(r^2/\varepsilon)`$ throughout $`0<\varepsilon\le1/8`$. When $`cd\le r\le d/2`$ for a fixed positive $`c`$, inclusion of the classical class in the quantum class also gives $`\Theta_c(d^2/\varepsilon)`$ for classical compilation. The remaining general-rank classical precision gap is part of the stated theorem boundary.
