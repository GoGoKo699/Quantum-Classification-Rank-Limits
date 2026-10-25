# Constructing the coherent classifier and charging its resources

The [exact optimal decision](exact_classifier.md) is a spectral measurement of the sum of training–test swaps. To attain its sample-complexity order, a simpler construction suffices: use the training copies to simulate a reflection about the unknown support, then read that reflection with a Hadamard test.

Sample-based Hamiltonian simulation is an established method of [Lloyd, Mohseni and Rebentrost](../references/RELATED_WORK.md#lloyd2014), with its sample complexity analyzed by [Kimmel et al.](../references/RELATED_WORK.md#kimmel2017). The construction here specializes that method to the flat-state classification experiment. The proof below keeps the controlled operation and its errors explicit.

## A controlled support reflection from copies

Let $`\rho_P=P/r`$. Introduce a control qubit $`C`$ for the test and attach a known qubit in state $`|1\rangle`$ to each training copy. Each augmented program state is

```math
\sigma_P=|1\rangle\langle1|\otimes\rho_P.
```

At time $`t=\pi r`$,

```math
e^{-it\sigma_P}
=|0\rangle\langle0|\otimes I
 +|1\rangle\langle1|\otimes(I-2P).
```

This is the controlled support reflection on $`C S`$. It is generated from copies of $`\sigma_P`$ by ordinary sample-based simulation on a $`2d`$-dimensional system. No controlled access to an unknown preparation unitary is assumed.

Prepare $`C`$ in $`|+\rangle`$, apply the simulated unitary, apply a Hadamard gate to $`C`$, and measure $`C`$ in the computational basis. For the ideal unitary, outcome $`1`$ has test effect $`P`$, while outcome $`0`$ has effect $`I-P`$. Predict the class state on outcome $`1`$. Its ideal error is $`R_*=r/(2d)`$.

## An explicit simulation bound

Let $`S_{\mathrm{swap}}`$ exchange one data register with one independent program register of state $`\sigma`$. One partial-swap step is the channel

```math
\Phi_\delta(X)
=\operatorname{tr}_{\mathrm{prog}}\!
 \left[
 e^{-i\delta S_{\mathrm{swap}}}
 (X\otimes\sigma)
 e^{i\delta S_{\mathrm{swap}}}
 \right].
```

Its derivative at zero is $`-i[\sigma,X]`$. This identity also holds with an untouched reference system. Write

```math
\mathcal L_{\mathrm{swap}}=-i[S_{\mathrm{swap}},\,\cdot\,],
\qquad
\mathcal L_\sigma=-i[\sigma,\,\cdot\,].
```

Both superoperators have diamond norm at most $`2`$, because $`\|S_{\mathrm{swap}}\|_\infty=1`$ and $`\|\sigma\|_\infty\le1`$. Their exponentials are unitary channels with diamond norm one. For either generator and $`\delta\ge0`$, the integral remainder gives

```math
\left\|e^{\delta\mathcal L}
 -I-\delta\mathcal L\right\|_\diamond
\le
\int_0^\delta(\delta-s)\|\mathcal L\|_\diamond^2\,ds
\le2\delta^2.
```

Preparing the program and tracing it out are channel contractions. The partial-swap and target channels have the same constant and linear terms. Consequently,

```math
\|\Phi_\delta-\mathcal U_\delta\|_\diamond
\le4\delta^2,
\qquad
\mathcal U_\delta(X)=e^{-i\delta\sigma}Xe^{i\delta\sigma}.
```

With $`m`$ fresh program copies and $`\delta=t/m`$, telescoping the channel composition yields

```math
\left\|\Phi_{t/m}^{\,m}-\mathcal U_t\right\|_\diamond
\le \frac{4t^2}{m}.
```

The bound does not require an additional small-step assumption. It can be loose when its right-hand side exceeds the maximum channel distance, which does not affect the upper bound.

Preparation and readout of the control preserve this bound. A binary outcome probability changes by at most half the trace norm of the output-state difference, hence at most half the displayed diamond-norm bound. The classification error therefore satisfies

```math
R_{\mathrm{constructed}}-R_*
\le \frac{2t^2}{m}
=\frac{2\pi^2r^2}{m}.
```

Thus, with ideal elementary operations,

```math
m=\left\lceil\frac{2\pi^2r^2}{\varepsilon}\right\rceil
```

suffices. This is the constructive half of [Theorem Q2](quantum_precision.md). The exact sign-of-swap classifier can only perform better at the same budget.

## Gates, active width and stored data

Assume $`d=2^n`$ for the qubit resource count. One program copy contains $`n`$ unknown-state qubits. Its known program-control qubit can be appended when that copy is used.

A partial swap of the two $`n+1`$-qubit augmented registers is $`e^{-i\delta S_{\mathrm{swap}}}`$. Since $`S_{\mathrm{swap}}^2=I`$, an ancillary qubit can coherently resolve its two eigenvalues using a controlled full-register swap, acquire the phase $`e^{\mp i\delta}`$, and uncompute. A controlled full-register swap consists of $`n+1`$ controlled swaps of qubit pairs. This gives $`O(n)`$ fixed-size gates plus a constant number of variable-angle rotations per partial-swap step. The ancillary work is returned.

| Resource | Direct implementation |
|---|---|
| Unknown-state examples | $`m`$ copies of $`P/r`$ |
| Training storage before the test | $`mn`$ qubits |
| Test | One $`n`$-qubit system |
| Active interaction width, excluding idle stored copies | $`2n+O(1)`$ qubits |
| Partial-swap interactions | $`m`$ |
| Gates with exact rotations | $`O(mn)`$ |
| Source preparation | $`m C_{\mathrm{prep}}`$ if one source copy costs $`C_{\mathrm{prep}}`$ |

The test arrives after training has been supplied. Every unused program copy must therefore remain stored until its interaction. Discarding a used copy reduces storage during prediction, but does not remove the initial $`mn`$ requirement.

For a finite gate set, use Clifford+T, so the fixed controlled-swap gates have exact constant-size decompositions. Allocate half the error budget to sample-based simulation by taking $`m=\lceil4\pi^2r^2/\varepsilon\rceil`$, and approximate the $`O(m)`$ variable rotations to channel error $`O(\varepsilon/m)`$ each. The [Solovay-Kitaev synthesis bound](../references/RELATED_WORK.md#dawson2005) then gives total cost

```math
O\!\left(
m\left[n+\operatorname{polylog}\!\left(\frac m\varepsilon\right)\right]
\right)
```

with the polylogarithmic exponent determined by the synthesis algorithm. For a different finite universal gate set, synthesizing the fixed gates as well can instead give $`O(mn\,\operatorname{polylog}(mn/\varepsilon))`$. These are gate-count bounds; no fault-tolerant hardware threshold or polynomial-time preparation guarantee for every unknown subspace is asserted.

For dimensions that are not powers of two, the systems can be embedded in $`\lceil\log_2d\rceil`$ qubits. The physical background remains $`I_d/d`$ on the specified $`d`$-dimensional subspace. Padding does not replace it by a maximally mixed state on the larger qubit space.

## Why coherence is used at prediction

The program systems interact with the still-unknown test. Measuring the entire program beforehand removes this resource, even if that measurement is collective. The [classical compilation converse](classical_compilation.md) quantifies the resulting copy cost.

The construction consumes program systems and performs one prediction. Its existence does not establish a reusable quantum model or optimal retained memory. The [exact measurement](exact_classifier.md) and [precision converse](quantum_precision.md) optimize classification success over all permitted coherent learners; the storage and gate counts above describe this particular attaining construction.

