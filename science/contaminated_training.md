# Classification from a contaminated flat source

Suppose the training source supplies $`N`$ independent copies of $`\rho=aP/r+(1-a)\sigma`$, where $`P`$ is an unknown rank-$`r`$ projector in dimension $`d`$, $`0\lt a\le1`$ is known, and $`\sigma`$ is any density operator. The later test still comes with equal priors from the clean state $`P/r`$ or the known background $`I_d/d`$. The learner outputs one label. Write $`\eta=1-a`$, $`u=r\eta/a`$ and $`A_{d,r}=(1-r/d)/2`$. The known-$`P`$ risk remains $`r/(2d)`$.

The [flat-rank contamination proof](https://github.com/GoGoKo699/Quantum-Training-Contamination/blob/main/science/flat_rank_training.md) develops the new recognition results. The [contaminated reflection proof](https://github.com/GoGoKo699/Collective-Quantum-Programming/blob/main/science/contaminated_reflections.md) develops the channel results. This page explains how the two clean statistical converses apply under the contaminated training promise.

## The statistical cost of contaminated recognition

The subfamily $`\sigma=P/r`$ yields $`\rho=P/r`$ at every known $`a`$. Fixing $`a`$ yields an eligible strategy for the clean experiment, so the worst-case contaminated excess is at least the clean minimax excess of the same access class. [Q2](quantum_precision.md#theorem-q2-finite-sample-risk-and-copy-complexity) supplies the coherent lower bound, and [C3](classical_compilation.md#theorem-c3-uniform-classical-precision) supplies the distinct classical-record lower bound. The classical record can be arbitrary and continuous. It retains the full outcome of a collective measurement made before the test arrives.

At balanced rank $`d=2r`$, two projectors with principal angles $`\theta_i`$ can give the same training density exactly when $`\sum_i\sin\theta_i\le u`$. On the pair with equal weight, the positive test averages to $`(P+Q)/(2r)`$, while the negative test is unchanged. The resulting binary Helstrom rule bounds the excess risk of every learner below by $`\sum_i(1-\cos\theta_i)/(4r)`$. Choosing the number of disjoint rotated planes to fit the contamination budget yields the lower order $`\min\{u^2,u,r\}/r`$. For $`0\le u\lt1`$ the top-$`r`$ projection of the perfectly known $`\rho`$ attains the one-plane lower bound in the worst case. Thus the exact fixed-dimension infinite-training excess at balance is

```math
\frac{1-\sqrt{1-u^2}}{4r}.
```

Finite training adds the same order of risk for either access class at balance. For $`N\ge1`$, each has worst-case excess of order

```math
\min\!\left\{1,\,\frac{r^2}{N}+\frac{\min\{u^2,u,r\}}{r}\right\}.
```

Here the contamination lower bound uses compatibility and the finite-sample term uses Q2 or C3. On the upper side, a coherent learner simulates a controlled exponential of the supplied $`\rho`$ using fresh copies. A classical compiler may instead apply collective tomography before the test and retain a classical description of the estimated top-$`r`$ projector. In the clean low-rank regime the two approaches differ in their dimension dependence. Their noise-dependent extensions preserve that separation: for $`1\le r\le d/2`$ and $`0\lt\varepsilon\le1/8`$, the copy budgets have orders $`r^2/\varepsilon`$ and $`rd/\varepsilon`$ respectively when $`\min(u^2,u)/r`$ is at most a sufficiently small universal constant times $`\varepsilon`$. The [proof and resource discussion](https://github.com/GoGoKo699/Quantum-Training-Contamination/blob/main/science/flat_rank_training.md) give the coherent simulation and the tomography error estimate. At balance the factor $`d/r`$ is constant. For fixed rank and increasing $`d`$, it grows linearly in $`d`$.

## A classical-record converse for ordinary reflection programming

Now let $`D`$ be the programming dimension, $`r`$ the program rank and $`\epsilon`$ the unhalved diamond error. The programmer may collectively measure all training specimens and retain unlimited classical information before the data arrive. Its eventual action on the data can be any quantum channel selected using that record. Because $`\sigma=P/r`$ is admissible, it suffices to bound the program cost on clean specimens. The [anchored reduction](programming_application.md) then uses the same classical record to choose a later measurement. It reduces an $`\epsilon`$-accurate programmer to a classical-record classifier with excess at most $`A_{d,s}\epsilon`$ in classification dimension $`d`$ and rank $`s`$.

Use the finite-sample form (C3.1), which applies at every $`1\le s\lt d`$. Dividing by the positive contrast and using $`2\sqrt N\le N/s+s\le N/s+d`$ gives

```math
\epsilon\ \ge\ \frac{d}{d+N/s+2\sqrt N}\ \ge\ \frac{d}{2(d+N/s)},
\qquad N\ge sd\left(\frac{1}{2\epsilon}-1\right).
```

For $`D\ge r+2`$ a known vacuum uses $`(d,s)=(D-1,r)`$ and directly embeds each specimen. For $`D=r+1`$, $`r\ge2`$, a known occupied direction uses $`(d,s)=(D-1,r-1)`$ and prepares the exact flat program by independent, unconditional padding before the training measurement. All of the routing after the test arrives uses only known gates and the record-dependent channel. In both cases the hard specimen budget remains $`N`$, and $`sd`$ has order $`rD`$. When $`(D,r)=(2,1)`$, the clean two-program converse already gives order $`1/\epsilon`$. Thus the classical-record programming cost is at least $`\Omega(rD/\epsilon)`$ for all $`1\le r\lt D`$ and $`0\lt\epsilon\le1/8`$. The contaminated reflection account specifies the domains where coherent programming and classical tomography attain their respective upper bounds.

The anchored argument uses a known eigenstate to preserve a relative phase. At balanced rank the complementary projectors $`P`$ and $`I-P`$ induce identical ordinary channels, so the unrestricted channel alone cannot say which clean support to accept. In the other direction, the good prediction rule against $`I_d/d`$ is only a binary effect. For a fixed positive pure-state contamination fraction the single-test prediction error tends to zero with $`d`$, while the reflection channel on arbitrary data still has a positive error floor. The stronger channel loss accounts for that difference.
