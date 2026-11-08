# Applying the classification converse to reflection programming

The precision converse [Q2](quantum_precision.md) also limits a processor that consumes copies of a flat state to apply an ordinary support reflection. The classification theorem remains the statistical input. The authoritative operational reduction and programming theorem are developed in [Collective Quantum Programming](https://github.com/GoGoKo699/Collective-Quantum-Programming/blob/c6b5150ce0e7d4f6ac81d171bb7f136ad86a1358/science/classification_transfer.md). This page states the interface and its consequence for the classification account.

## Two tasks and their promises

Use $`d,s`$ for classification: the learner receives $`N`$ independent copies of $`Q/s`$, where $`Q`$ has rank $`1\le s\lt d`$, before one test from either $`Q/s`$ or $`I_d/d`$ with equal priors. It may retain the training systems and use any joint measurement. Its oracle risk and available contrast are

```math
R_*=\frac{s}{2d},\qquad A_{d,s}=\frac{1-s/d}{2}.
```

The all-rank form of Q2, rather than only its low-rank uniform corollary, gives

```math
0\lt\delta\le A_{d,s}/2
\quad\Longrightarrow\quad
N_{\mathrm Q}(d,s,\delta)
\ge\left\lceil s^2\left(\frac{A_{d,s}}{\delta}-1\right)\right\rceil.
```

Use $`D,r,k`$ for programming. The processor receives a hard budget of $`N`$ independent specimens of $`P/r`$, for an unknown rank-$`r`$ projector on $`\mathbb C^D`$. Define $`R_P=I_D-2P`$. Its target is the ordinary channel of $`R_P^{\otimes k}`$, uniformly over $`P`$ and all input states, including entangled references. Write $`N_*(D,r,k,\epsilon)`$ for the minimum budget at **unhalved diamond error** $`\epsilon`$. The processor is deterministic and unconditional; success conditioning and expected-copy budgets are different promises.

## Why the relative error is the useful one

A controlled support reflection followed by a Hadamard readout implements the ideal classification effect $`Q`$. If the implemented controlled channel has unhalved diamond error at most $`\epsilon`$, its actual effect $`M_Q`$ obeys

```math
\|M_Q-Q\|_\infty\le\epsilon/2.
```

This follows by bounding the binary outcome-probability error on every input state. The induced excess classification risk is therefore

```math
\begin{aligned}
R(M_Q,Q)-R_*
&=\frac12\operatorname{tr}\!\left[(Q-M_Q)
\left(\frac Qs-\frac{I_d}{d}\right)\right]\\
&\le\frac\epsilon4\left\|\frac Qs-\frac{I_d}{d}\right\|_1
=A_{d,s}\epsilon.
\end{aligned}
```

The factor $`A_{d,s}`$ is retained on both sides of the converse. Substituting $`\delta=A_{d,s}\epsilon`$ into Q2 yields

```math
N\ge\left\lceil s^2(\epsilon^{-1}-1)\right\rceil,
\qquad 0\lt\epsilon\le1/2.
```

The small-budget branch of Q2 excludes $`N\lt s^2`$ in this range, so the argument does not assume the large-budget regime without justification. Since $`s\lt d`$, the contrast is positive and cancels exactly. No lower bound on $`1-s/d`$ is needed for this relative-risk statement. It does not extend the original fixed **absolute** risk law to a vanishing-contrast regime.

## Obtaining control from an anchored ordinary reflection

An ordinary unitary channel does not generically supply a controlled version with a fixed phase. At $`D=2r`$, complementary projectors satisfy $`R_{I-P}=-R_P`$ and induce the same ordinary channel. The converse instead restricts the universal programming promise to a family with a known eigenstate. Known controlled swaps route either that eigenstate or the classification test through the same ordinary channel, then undo the routing. The eigenstate fixes the relative phase; a known control phase corrects a $`-1`$ eigenvalue. The circuit is a channel supermap independent of the unknown subspace, so its diamond error does not increase.

The exact dimension and source conversions are:

| Programming family | Classification parameters | Specimen conversion |
|---|---|---|
| $`D\ge r+2`$, $`P=0_v\oplus Q`$ with a known vacuum $`v`$ | $`d=D-1`$, $`s=r`$ | Embed each $`Q/r`$ copy; exactly $`N`$ supplied copies |
| $`D=r+1`$, $`r\ge2`$, $`P=\lvert v\rangle\langle v\rvert\oplus Q`$ with a known occupied direction | $`d=r`$, $`s=r-1`$ | An exact copy-local mixture produces $`P/r`$ from at most one $`Q/s`$ input per slot |
| Flagged projector $`\widehat P=\lvert1\rangle\langle1\rvert\otimes Q`$ in dimension $`D=2d`$ | Any $`1\le s\lt d`$, programming rank $`r=s`$ | Append one known flag to each $`Q/s`$ copy |

For the occupied-direction row, if $`V`$ is the known embedding into $`v^\perp`$, use the trace-preserving channel

```math
\Lambda(X)=\frac1r\operatorname{tr}(X)|v\rangle\langle v|
+\frac{r-1}{r}VXV^\dagger,
\qquad
\Lambda(Q/(r-1))=P/r.
```

Independent known coin flips implement $`\Lambda^{\otimes N}`$: either embed the input or discard it and prepare $`v`$. All $`N`$ supplied classification copies are charged, including discarded ones. This produces the exact independent programming state, without postselection, extra specimens or an expected-budget conversion. The classification background remains $`I_d/d`$ on the stated $`d`$-dimensional test space.

For the flagged row the ordinary reflection is already

```math
I_{2d}-2\widehat P
=|0\rangle\langle0|\otimes I_d
+|1\rangle\langle1|\otimes(I_d-2Q).
```

The programming dimension is explicitly $`2d`$, not $`d`$. The vacuum route uses programming dimension $`d+1`$ with a routing ancilla. In every route all training precedes the later test, no fresh examples are obtained after it arrives, and no preparation unitary, inverse or purification is supplied.

## Programming consequence and its limit

The first two rows give the single-target lower bounds

```math
N_*(D,r,1,\epsilon)\ge
\begin{cases}
\left\lceil r^2(\epsilon^{-1}-1)\right\rceil,&D\ge r+2,\\
\left\lceil(r-1)^2(\epsilon^{-1}-1)\right\rceil,&D=r+1,\ r\ge2,
\end{cases}
\qquad0\lt\epsilon\le1/2.
```

The remaining $`(D,r)=(2,1)`$ endpoint uses the programming account's existing pair-discrimination converse. Together with its constructive upper bound, this proves

```math
N_*(D,r,1,\epsilon)=\Theta(r^2/\epsilon),
\qquad1\le r\lt D,\quad0\lt\epsilon\le1/8,
```

with constants independent of the ambient dimension and rank. The full-rank endpoint $`r=D`$ has an identity ordinary channel and requires no specimens.

Any $`k`$-target programmer reduces to one target by fixing the other inputs and discarding their outputs. This preserves $`D,r,N`$ and does not increase the diamond error. Combining the transferred bound with the programming account's existing $`rk^2/\epsilon`$ converse gives, throughout $`1\le r\lt D`$, $`k\ge1`$, $`0\lt\epsilon\le1/8`$,

```math
\frac{9}{8\pi^2}\frac{\max\{r^2,rk^2\}}{\epsilon}
\le N_*(D,r,k,\epsilon)
\le\left\lceil\frac{4\pi^2rk(r+k-1)}{\epsilon}\right\rceil.
```

The upper constant assumes exact known rotations; the programming resource account charges finite synthesis separately. For $`1\lt k\lt r`$, the lower order is $`(r^2+rk^2)/\epsilon`$ and the upper order is $`(r^2k+rk^2)/\epsilon`$. Their ratio is within constants of $`\min\{k,r/k\}`$. Q2 is a single-test theorem: padding or summing marginal risks does not establish an additional factor $`k`$ in the rank-squared lower bound. Nor does the parallel channel promise provide a reusable oracle for future adaptive inputs.

The [full transfer proof](https://github.com/GoGoKo699/Collective-Quantum-Programming/blob/c6b5150ce0e7d4f6ac81d171bb7f136ad86a1358/science/classification_transfer.md) owns these operational reductions and the programming consequence. Q1, Q2 and the exact classification model remain authoritative here. The reflection construction already supplies the flagged controlled operation; the converse transfer uses it in the opposite direction with the promises above kept explicit.
