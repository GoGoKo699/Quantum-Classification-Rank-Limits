# Related work and attribution

The contribution is an exact minimum-error classifier for a flat unknown subspace, a matching quantum rank-and-precision law, and a fixed-accuracy comparison with arbitrary classical compilation. Quantum-reference advantages, the compilation comparator, Schur-Weyl methods, sample-based simulation and collective tomography have established predecessors.

The comparisons below specify the source versions and the operational distinction. They are a bounded primary-source comparison, not an exhaustive priority certificate. Bibliographic records are in [references.bib](references.bib).

The single educational anchor is John Watrous, *The Theory of Quantum Information* (Cambridge University Press, 2018), using the [author's standard-layout manuscript](https://jhwatrous.github.io/books-and-courses.html). The [educational bridge](../learning/watrous_bridge.md) gives the relevant sections and distinguishes their foundations from the project's additional representation calculations and research-level ingredients.

| Ingredient or result | Attribution and role |
|---|---|
| Coherent-versus-classical reference advantage at fixed rank | Already established in [An2026](#an2026); not a new claim here |
| Arbitrary collective measurement of a program before independent data processing | Present in [Li2026](#li2026) and [An2026](#an2026) |
| Schur-Weyl reduction, branching and hook-content identities | Standard representation theory; used throughout [OW2015](#odonnell2015) and universal quantum learning |
| Sample-based Hamiltonian simulation | [Lloyd2014](#lloyd2014), with sample bounds and extensions in [Kimmel2017](#kimmel2017) |
| Collective tomography risk | [OW2016](#odonnell2016), Theorem 1.2 and Corollary 1.4 |
| Finite-gate approximation of variable rotations | [Dawson2005](#dawson2005), used only for the constructive gate-count upper |
| This experiment's exact likelihood and rank-independent optimum | [Theorem Q1](../science/exact_classifier.md) |
| Unrestricted classification precision lower bound | [Theorem Q2](../science/quantum_precision.md) |
| General-rank classical compilation converse | [Theorem C1](../science/classical_compilation.md) |
| Specialization of known constructions to the stated task | [Coherent construction](../science/constructions.md) and [Theorem C2](../science/classical_compilation.md) |

## Dawson2005

**Christopher M. Dawson and Michael A. Nielsen, “The Solovay-Kitaev algorithm,” arXiv:quant-ph/0505030v2 (23 August 2005).** [Primary text](https://arxiv.org/abs/quant-ph/0505030v2).

The algorithm compiles a single-qubit rotation over a fixed finite universal gate set with a sequence length polynomial in the logarithm of inverse approximation error. The [resource account](../science/constructions.md) uses this conservative synthesis bound for the variable rotations and specifies Clifford+T so that the fixed controlled-swap gates have exact constant-size decompositions. The argument does not require a claim of optimal synthesis.

## An2026

**Zheng An, “Exponential Advantage of Quantum over Classical References in Leakage Detection,” arXiv:2609.36541v1 (29 September 2026).** [Primary text](https://arxiv.org/html/2609.36541v1).

This is the closest precedent. It supplies independent references $`(P/2)^{\otimes M}`$ for an unknown rank-two projector, then one message. Its measurement-first class allows arbitrary collective reference POVMs. It derives an exact coherent leakage-detection law under zero false alarms, and a classical cost $`\Theta(d/\eta)`$ under small false-alarm and disturbance tolerance $`\eta`$.

The fixed-rank separation transfers to a classical label-only task. Writing $`Q=I-P`$,

```math
\frac{I}{d}=\frac2d\frac P2+\frac{d-2}{d}\frac Q{d-2}.
```

If a detector has normal rejection $`\alpha`$ and orthogonal-leakage detection $`D`$, its induced classification excess is $`A_{d,2}(1+\alpha-D)`$. Thus the rank-two advantage is inherited even after its quantum output is discarded.

Supplement Theorem 1 explicitly restricts coherent optimality to zero false alarms. Section III's “general-dimensional” posterior remains rank two. The present minimum-error theorem allows both error types, varies rank, and proves the unrestricted precision converse.

## Li2026

**Zhaoyi Li, Elias Theil, Aram W. Harrow and Isaac Chuang, “An Exponential Sample-Complexity Advantage for Coherent Quantum Inference,” arXiv:2605.21457v2 (29 September 2026).** [Primary text](https://arxiv.org/html/2605.21457v2).

This work studies quantum-output inference, including purity amplification, random purification, cloning and density-matrix exponentiation. Section S5, Lemma S5.1 already allows a collective measurement of all program copies followed by a classically selected channel on independent quantum data.

The v2 DME comparison uses a uniform channel approximation criterion in induced trace norm, bounded above by diamond-norm error. Its lower bound restricts the program to a local pure-state family. A single classical classification label for the flat mixed-state promise does not reconstruct such a channel, so that converse does not directly establish Theorem Q2 or C1. The comparator and the broader coherence-versus-classicalization question are nevertheless inherited.

## Lloyd2014

**Seth Lloyd, Masoud Mohseni and Patrick Rebentrost, “Quantum principal component analysis,” Nature Physics 10, 631–633 (2014).** [Publisher](https://www.nature.com/articles/nphys3029); [preprint](https://arxiv.org/abs/1307.0401).

The density-matrix-exponentiation idea uses copies of an unknown state to simulate the unitary generated by that state. It is the constructive mechanism used here. The support reflection for a flat rank-$`r`$ state requires simulation time proportional to $`r`$, which must be retained when counting samples.

## Kimmel2017

**Shelby Kimmel, Cedric Yen-Yu Lin, Guang Hao Low, Maris Ozols and Theodore J. Yoder, “Hamiltonian simulation with optimal sample complexity,” npj Quantum Information 3, 13 (2017).** [Publisher](https://www.nature.com/articles/s41534-017-0013-7); [full preprint](https://arxiv.org/html/1608.00281v1).

This paper supplies the $`O(t^2/\delta)`$ sample-based simulation bound and extensions, including controlled simulation. The [construction](../science/constructions.md) gives a self-contained, conservative constant for the reflection specialization and constructs its control from known program ancillas.

Their general simulator lower bound concerns channel simulation and includes hard states with varying qubit eigenvalues. It does not imply a converse for the weaker flat-spectrum, single-test prediction task. The matching quantum upper mechanism is attributed to this line of work; the classification converse is proved separately.

## ODonnell2016

**Ryan O'Donnell and John Wright, “Efficient quantum tomography,” STOC 2016; arXiv:1508.01907v2 (13 September 2015).** [Primary text](https://arxiv.org/html/1508.01907v2).

Theorem 1.2 gives expected squared Frobenius error at most $`(4d-3)/N`$. Projecting its estimator onto the closest flat rank-$`r`$ state gives the [classical classification upper](../science/classical_compilation.md) $`E_{\mathrm C}\le(4d-3)r/N`$.

Corollary 1.4 directly states $`O(rd/\delta^2)`$ copies for trace-distance accuracy $`\delta`$. No logarithmic dimension factor is needed for the fixed-accuracy upper used here. Section 1.3 distinguishes this result from the concurrent tomography bound of Haah and coauthors, whose stated form includes a logarithm.

## ODonnell2015

**Ryan O'Donnell and John Wright, “Quantum Spectrum Testing,” arXiv:1501.05028v1 (21 January 2015).** [Primary text](https://arxiv.org/html/1501.05028v1).

The paper develops spectrum testing with Schur methods. Its rank-testing results include one-sided testing and distinguishing states uniform on subspaces of rank $`r`$ or $`r+\Delta`$, with a related rank-squared scale.

Those experiments supply i.i.d. copies of one state under either hypothesis. Here the training state remains rank $`r`$ under both hypotheses, and only one subsequent test changes. The rank-testing oracle does not immediately supply this conditional training/test family. Its theorem also imposes no classical compilation boundary. The common representation theory and rank scale are antecedents; a lower bound is not transferred solely because the formulas have similar orders.

## Fanizza2019

**Marco Fanizza, Andrea Mari and Vittorio Giovannetti, “Optimal universal learning machines for quantum state discrimination,” IEEE Transactions on Information Theory 65, 5931–5944 (2019).** [Primary preprint, v3](https://arxiv.org/abs/1805.03477v3); [DOI](https://doi.org/10.1109/TIT.2019.2916646).

The general mixed-state classification analysis concerns qubits and finite training sizes. Its arbitrary-dimensional extension is for pure states with known overlap. It establishes important programmable-discrimination precedents, but does not state the growing-rank, growing-dimension result of this experiment.

## Fanizza2022

**Marco Fanizza, Michalis Skotiniotis, John Calsamiglia, Ramon Muñoz-Tapia and Gael Sentís, “Universal algorithms for quantum data learning,” Europhysics Letters 140, 28001 (2022).** [Primary text](https://arxiv.org/html/2210.11850v1); [DOI](https://doi.org/10.1209/0295-5075/ac9c29).

This perspective explains the established reduction of reference-frame-independent learning tasks by group representations. Sections V.1–V.2 discuss supervised classification and the distinction between joint learning and measurement-first strategies. The use of symmetry here belongs to that framework. The task-specific likelihood, exact decision and precision bound supply the present result.

## Sentis2012

**Gael Sentís, John Calsamiglia, Ramon Muñoz-Tapia and Emilio Bagan, “Quantum learning without quantum memory,” Scientific Reports 2, 708 (2012).** [Publisher](https://www.nature.com/articles/srep00708).

In its binary pure-qubit classification setting, a learning machine can attain the optimal performance without retaining quantum memory from training. This prevents a blanket assertion that quantum training retention is always necessary or always advantageous. The present high-dimensional subspace family has a different sample-complexity comparison.

## Banchi2024

**Leonardo Banchi, Jason Luke Pereira, Sharu Theresa Jose and Osvaldo Simeone, “Statistical Complexity of Quantum Learning,” Advanced Quantum Technologies, article 2300311.** [DOI](https://doi.org/10.1002/qute.202300311); [arXiv v2](https://arxiv.org/html/2309.11617v2); [publisher's version in the institutional repository](https://pure-oai.bham.ac.uk/ws/portalfiles/portal/261676557/Adv_Quantum_Tech_-_2024_-_Banchi_-_Statistical_Complexity_of_Quantum_Learning.pdf).

Section 4.5, page 25 of the published article, states a dimension-independent $`O(-\log(\varepsilon)\varepsilon^{-3})`$ training-copy bound for approximate Helstrom classification. The displayed phase-estimation argument infers the sign from the first phase bit.

A uniform interpretation over arbitrary unknown states fails in the present copy-only model. For $`r=d/2`$,

```math
H=\frac{\rho_P-\tau_d}{2}
```

has eigenvalues $`\pm1/(2d)`$, yet the oracle advantage is $`1/4`$. Theorem Q2 requires $`\Omega(d^2/\varepsilon)`$ coherent examples. Constant numerical phase resolution does not guarantee the correct leading bit near the phase-wrap boundary; the small eigenvalues carry constant aggregate classification advantage.

This comparison is scoped to that uniform statement, not to every result in the article. Known copies of $`I/d`$ carry no information about $`P`$ and do not remove the obstruction.

## Lloyd2020

**Seth Lloyd, Maria Schuld, Aroosa Ijaz, Josh Izaac and Nathan Killoran, “Quantum embeddings for machine learning,” arXiv:2001.03622v2.** [Primary text](https://arxiv.org/html/2001.03622v2).

The quantum-embedding approach explicitly invokes low-rank conditions for efficient spectral classification and has regenerable embeddings of classical data. Those conditions differ from a dimension-uniform guarantee for arbitrary unknown mixed-state sources. The high-rank obstruction here does not contradict an explicitly low-rank result.

## Representation and implementation sources

**Dave Bacon, Isaac L. Chuang and Aram W. Harrow, “Efficient Quantum Circuits for Schur and Clebsch-Gordan Transforms,” Physical Review Letters 97, 170502 (2006).** [Primary preprint](https://arxiv.org/abs/quant-ph/0407082); [DOI](https://doi.org/10.1103/PhysRevLett.97.170502).

This provides a circuit-level precedent for Schur processing. The original general transform's cost is polynomial in register number and local dimension; it is not invoked here as a free gate-efficient implementation for exponentially large local dimension. The sample-attaining circuit used in this project is instead the explicit partial-swap reflection construction.

