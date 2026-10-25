# Thirty milestones for understanding the project

This map contains exactly 30 project-defined understanding targets. It follows the scientific dependencies of quantum classification from a flat unknown subspace, from the individual states and measurements to the complete comparison of coherent retention and classical compilation.

The single educational anchor is **John Watrous, *The Theory of Quantum Information* (2018)**. The [Watrous bridge](watrous_bridge.md) identifies the relevant portions of the book, translates notation, and explains which further arguments are supplied by this project. Chapter links below point to the author's [book materials](https://jhwatrous.github.io/books-and-courses.html). Research papers cited through the project supply particular mathematical or algorithmic ingredients; they are not additional educational anchors.

## Allocation and dependency structure

| Phase | Milestones | Why this allocation fits the science |
|---|---|---|
| Background / preliminaries | M01–M12: 12 targets | The problem joins quantum decision theory, channel error, and tensor-power symmetry. These foundations must be connected before the likelihood and resource comparison have a precise meaning. M12 integrates them into the full experiment. |
| Narrative / innovation | M13–M30: 18 targets | The scientific account combines an exact decision rule, quantum and classical converses, and attaining constructions. These components then support the rank comparison, resource account, and claim boundaries. M30 integrates the complete result. |

Prerequisites refer only to earlier milestone IDs. Their own prerequisites remain in force. This is a map of the main understanding dependencies, not an assertion that every lemma or neighboring topic is covered. Each phase progresses from its components to a global synthesis.

## Background / preliminaries

### M01

**States, support, and flat mixtures**

**Central question.** What do $`d`$ and $`r`$ describe physically?

**Understanding target.** Distinguish a density operator, its support projector, and the ambient Hilbert space. Explain why $`\rho_P=P/r`$ is a normalized state, why its nonzero eigenvalues are all $`1/r`$, and how it differs from $`I_d/d`$.

**Prerequisites and story role.** No earlier milestone. This establishes the local objects on which both the decision problem and its rank dependence rest.

**Conceptual connection.** The spectrum describes the mixture within the source, while the unknown orientation of its support creates the learning problem.

**Source pointers.** Watrous [§1.1.2](https://jhwatrous.github.io/TQI.1.pdf) and [§2.1.2](https://jhwatrous.github.io/TQI.2.pdf); [model, “Experiment and information access”](../science/model.md#experiment-and-information-access).

### M02

**Copies and the training/test experiment**

**Central question.** What does conditional independence give, and what access is absent?

**Understanding target.** Explain the tensor-product inputs for the two labels, with one unknown $`P`$ fixed throughout an instance. Distinguish supplied copies from a classical state description, a purification, or a preparation oracle, and identify the training-before-test order.

**Prerequisites and story role.** M01. This turns a single state into a physical experiment with a specified information supply.

**Conceptual connection.** Conditional independence determines the input states before averaging. Averaging over a shared unknown $`P`$ can create correlations in the analytical model without changing how the physical samples were supplied.

**Source pointers.** Watrous [§§2.1.2–2.1.3](https://jhwatrous.github.io/TQI.2.pdf); [model, “Experiment and information access”](../science/model.md#experiment-and-information-access).

### M03

**Effects and POVMs**

**Central question.** How does a quantum procedure produce a binary prediction?

**Understanding target.** Relate an effect $`0\le T\le I`$ to its outcome probability and complementary effect. Explain why ancillas and intermediate operations can be absorbed into a final binary effect on the supplied systems, while a training measurement may have many outcomes.

**Prerequisites and story role.** M01, M02. This supplies the operational language in which every permitted classifier can be compared.

**Conceptual connection.** The optimization variable is a quantum decision effect. It need not be a reconstructed state, an estimated subspace, or a particular learning circuit.

**Source pointers.** Watrous [§2.3.1, Definition 2.34 and the Born rule](https://jhwatrous.github.io/TQI.2.pdf); [model, “Two classes of learner”](../science/model.md#two-classes-of-learner).

### M04

**Channels and classical records**

**Central question.** What survives a measure-and-prepare stage?

**Understanding target.** Describe the roles of channels, partial trace, and a recorded measurement outcome. Explain the classical compiler form $`T_{\mathrm C}=\int E_y\otimes M_y\,dy`$, including why a known state prepared from $`y`$ can be absorbed into the later test procedure.

**Prerequisites and story role.** M02, M03. This identifies the access restriction separating the two learner classes.

**Conceptual connection.** Entangled operations during training are compatible with classical compilation. The decisive restriction is that quantum information about $`P`$ does not survive to interact with the later test.

**Source pointers.** Watrous [§2.1.3 and §§2.2.1–2.2.2](https://jhwatrous.github.io/TQI.2.pdf); [model, “Classical compiler”](../science/model.md#classical-compiler); [classical compilation, §1](../science/classical_compilation.md).

### M05

**Three operator norms**

**Central question.** Which errors are measured by trace, Frobenius, and operator norm?

**Understanding target.** Distinguish the three norms and their roles. Trace norm controls decision statistics, squared Frobenius norm measures the imported tomography error, and operator norm controls Hamiltonian commutators in the construction.

**Prerequisites and story role.** M01. This prepares the error conversions needed by both attaining constructions.

**Conceptual connection.** An estimation guarantee becomes a prediction guarantee only after the metric is related to the actual loss. Different bounds cannot be compared by treating their error parameters as interchangeable.

**Source pointers.** Watrous [§1.1.3, particularly the Schatten norms](https://jhwatrous.github.io/TQI.1.pdf); [classical compilation, Theorem C2](../science/classical_compilation.md); [construction, “An explicit simulation bound”](../science/constructions.md#an-explicit-simulation-bound).

### M06

**Discrimination and excess risk**

**Central question.** What is the known-$`P`$ benchmark and the actual learning target?

**Understanding target.** Connect binary state discrimination to the positive part of a difference of weighted states. Explain why the known-support error is $`R_*=r/(2d)`$, and distinguish total classification error, excess error, and recovered advantage over random guessing.

**Prerequisites and story role.** M03, M05. This specifies the loss against which every sample bound is measured.

**Conceptual connection.** Even perfect knowledge of $`P`$ leaves an unavoidable classification error because the background overlaps the source support. Learning precision is measured above that optimum.

**Source pointers.** Watrous [§3.1.1, Theorem 3.4](https://jhwatrous.github.io/TQI.3.pdf); [model, “Oracle benchmark and minimax quantities”](../science/model.md#oracle-benchmark-and-minimax-quantities).

### M07

**Channel error and composition**

**Central question.** Why does diamond distance control later binary statistics?

**Understanding target.** Explain why a channel approximation must remain valid when its input is accompanied by another system. Relate a diamond-norm bound to output-state trace distance, binary probability error, and a telescoping bound for composed channels.

**Prerequisites and story role.** M04, M05. This supplies the error framework for a physical classifier built from approximate operations.

**Conceptual connection.** A simulator's channel guarantee is a sufficient condition for prediction accuracy. The classification converse need not impose that stronger channel objective on competing learners.

**Source pointers.** Watrous [§3.3.2, Definition 3.43 and Proposition 3.44](https://jhwatrous.github.io/TQI.3.pdf); [construction, “An explicit simulation bound”](../science/constructions.md#an-explicit-simulation-bound).

### M08

**Symmetry and minimax risk**

**Central question.** When can Haar averaging certify worst-case performance?

**Understanding target.** Explain normalized Haar averaging over the orbit of one projector, its invariance, and the difference between average and worst-case risk. Identify why an invariant procedure with constant risk can make an averaged optimum attainable uniformly.

**Prerequisites and story role.** M02, M06. This connects the unknown orientation of the source to a tractable decision problem.

**Conceptual connection.** A Haar-average lower bound alone is a worst-case obstruction. Equality with the minimax value additionally requires an attaining procedure whose performance is the same across the orbit.

**Source pointers.** Watrous [§7.2.1, Definition 7.18 and Proposition 7.20](https://jhwatrous.github.io/TQI.7.pdf) for Haar measure; the local covariance-to-minimax argument in [exact classifier, §4](../science/exact_classifier.md).

### M09

**Permutations and swaps**

**Central question.** How do exchange operators encode multi-copy information?

**Understanding target.** Describe permutation operators on tensor factors and the swap between a training register and the test. Explain the swap trace identity and why permutations commute with applying the same unitary to every register.

**Prerequisites and story role.** M02, M05. This introduces the operators that will connect the exact quantum decision and the classical converse.

**Conceptual connection.** Swaps translate relations between quantum systems into traces of products. Their symmetry makes them useful even when the source basis is unknown.

**Source pointers.** Watrous [§7.1.1, including equation (7.3)](https://jhwatrous.github.io/TQI.7.pdf); [exact classifier, §3](../science/exact_classifier.md); [classical compilation, §2.3](../science/classical_compilation.md).

### M10

**Schur sectors and rank**

**Central question.** How do unitary and permutation symmetries organize tensor powers?

**Understanding target.** Distinguish the unitary-group and permutation multiplicity factors in a Schur sector. Explain why a unitary twirl of identical-copy inputs becomes scalar on the complete sector, and why a rank-$`r`$ source populates only diagrams with at most $`r`$ rows.

**Prerequisites and story role.** M08, M09. This provides the block structure needed to analyze many unknown training copies without estimating their orientation.

**Conceptual connection.** A commutant statement identifies the symmetry algebra. The partition-indexed decomposition and its dimensions turn that algebra into a concrete probability calculation.

**Source pointers.** Watrous [§7.1.2, especially Theorem 7.15](https://jhwatrous.github.io/TQI.7.pdf), for the commutant; the additional partition and dimension bridge in [exact classifier, §2](../science/exact_classifier.md) and [Watrous bridge](watrous_bridge.md).

### M11

**One-box branching and dimensions**

**Central question.** How do contents, hooks, and multiplicities enter a probability calculation?

**Understanding target.** Interpret adding the test register as a one-box branch. Distinguish $`f_\lambda`$, $`D_\lambda(k)`$, and the added content $`c`$, and explain how their dimension ratios produce normalized growth probabilities rather than uniform weights over diagram labels.

**Prerequisites and story role.** M10. This supplies the last algebraic ingredients before the full experiment can be reduced to one scalar branch label.

**Conceptual connection.** Dimension counting carries the probability mass. Omitting a multiplicity would change the optimal risk even if the list of allowed diagrams were correct.

**Source pointers.** The branching and hook-content formulas in [exact classifier, §§2–3](../science/exact_classifier.md); [O'Donnell–Wright spectrum-testing attribution](../references/RELATED_WORK.md#odonnell2015). Watrous [§7.1.2](https://jhwatrous.github.io/TQI.7.pdf) supplies the underlying symmetry setting; the explicit branching formulas are part of the local bridge.

### M12

**Integrated model**

**Central question.** How do access, loss, symmetry, and charged resources define a fair comparison?

**Understanding target.** Assemble the complete training-before-test experiment, both learner classes, the known-source benchmark, and the minimax criterion. Explain how the symmetry tools apply while all source copies and retained systems remain physical resources.

**Prerequisites and story role.** M04, M06, M07, M08, M11. This is the global synthesis of the background phase, integrating the quantum objects, risk, access boundary, and mathematical framework.

**Conceptual connection.** A useful sample-complexity comparison holds the task and supplied information fixed while changing which training information survives until prediction.

**Source pointers.** [Model](../science/model.md), especially its learner classes, risk definitions, and resource boundaries; [Watrous bridge](watrous_bridge.md).

## Narrative / innovation

### M13

**Averaged hypotheses and support**

**Central question.** Why are $`H_1=A_{N+1}`$ and $`H_0=A_N\otimes I/d`$ simultaneously tractable?

**Understanding target.** Reconstruct the two averaged inputs from the physical experiment and explain their common branching blocks. Identify the support of $`H_0`$, including branches on which $`H_1`$ is zero, and the origin of the training weight $`f_\lambda D_\lambda(r)/r^N`$.

**Prerequisites and story role.** M08, M10, M12. This begins the project-specific reduction with the actual input states and their populated sectors.

**Conceptual connection.** The shared unknown projector couples the averaged training and positive test. The resulting operator problem retains the full training/test experiment.

**Source pointers.** [Exact classifier, §§1–2](../science/exact_classifier.md); Watrous [§7.2.1](https://jhwatrous.github.io/TQI.7.pdf) for unitary averaging.

### M14

**The one-box likelihood**

**Central question.** Why does $`L(c)=d(r+c)/(r(d+c))`$ hold on the populated support?

**Understanding target.** Explain the cancellation of dimension factors in the likelihood ratio and why $`d+c\ge d-r>0`$ on every active branch. Interpret the zero likelihood at $`c=-r`$ as a support property of the positive hypothesis.

**Prerequisites and story role.** M11, M13. This obtains the scalar expression from which both the optimal decision and the compiler inequality follow.

**Conceptual connection.** Representation dimensions become likelihoods. The support restriction makes functional calculus legitimate and prevents division by a nonexistent or zero-probability block.

**Source pointers.** [Exact classifier, §3](../science/exact_classifier.md); [classical compilation, §2.1](../science/classical_compilation.md).

### M15

**A rank-independent optimal decision**

**Central question.** Why does the sign of $`J_N`$ solve the Haar and minimax problems at once?

**Understanding target.** Connect the added content to the eigenvalue of $`J_N=\sum_i\mathrm{SWAP}(i,S)`$, then explain why the sign of $`L(c)-1`$ is the sign of $`c`$. Combine this decision with covariance to establish optimality for every source orientation and every $`r<d`$.

**Prerequisites and story role.** M06, M08, M09, M14. This integrates the likelihood, state-discrimination rule, and symmetry into Theorem Q1's exact measurement.

**Conceptual connection.** Rank changes the information in the examples without changing the form of the optimal fixed-budget decision. That statement is distinct from selecting a sufficient sample budget without knowing rank.

**Source pointers.** [Exact classifier, Theorem Q1 and §§3–4](../science/exact_classifier.md); Watrous [§3.1.1, Theorem 3.4](https://jhwatrous.github.io/TQI.3.pdf), for binary discrimination.

### M16

**Exact learning-curve factorization**

**Central question.** What does $`p_Q-1/2=A_{d,r}F_{N,r}`$ separate, including $`N=0`$, $`r=1`$, and $`r=d`$?

**Understanding target.** Explain how physical branch weights cancel the denominator of the likelihood, leaving a rank-dependent growth average. Interpret $`F_{N,r}`$ as the recovered fraction of available advantage and distinguish its dimension independence from that of the entire task.

**Prerequisites and story role.** M15. This turns the optimal decision into an exact learning curve whose normalization has a physical meaning.

**Conceptual connection.** Ambient dimension changes the available source/background contrast. Rank and sample count govern the fraction recovered. The no-training, pure-state, and identical-hypothesis boundaries check those roles separately.

**Source pointers.** [Exact classifier, §§5–6](../science/exact_classifier.md); [interpretation, opening factorization](../science/interpretation.md).

### M17

**Transition-content moments**

**Central question.** Why are mean zero and second moment $`N`$ the right growth identities?

**Understanding target.** Distinguish the growth probabilities $`q_{\lambda\mu}`$ from the physical $`H_0`$ branch probabilities. Explain the induced-character calculation giving $`\mathbb E C=0`$ and $`\mathbb E C^2=N`$, together with the support bound $`C\ge-r`$.

**Prerequisites and story role.** M11, M16. This extracts the quantitative information from the exact curve that will control every coherent classifier.

**Conceptual connection.** Representation dimensions define a probability distribution whose moments can be proved by counting permutation cycle types. The moment argument is provided locally rather than assumed as a textbook conclusion.

**Source pointers.** [Quantum precision, §§1–2](../science/quantum_precision.md); the permutation foundations in Watrous [§7.1.1](https://jhwatrous.github.io/TQI.7.pdf).

### M18

**The rank-squared threshold**

**Central question.** Why do fixed-advantage predictions require $`N`$ of order $`r^2`$?

**Understanding target.** Explain the conversion from the content moments to $`F_{N,r}\le\sqrt N/(2r)`$ using the positive and negative parts of a mean-zero variable. Relate this inequality to the fraction of Bayes advantage that remains unrecovered when $`N\le r^2`$.

**Prerequisites and story role.** M05, M17. This identifies the first universal obstruction before addressing arbitrarily small excess error.

**Conceptual connection.** The typical exchange-content fluctuation is controlled by $`\sqrt N`$, while the available negative scale is $`r`$. The comparison produces a sample threshold for prediction, without requiring state reconstruction.

**Source pointers.** [Quantum precision, §3](../science/quantum_precision.md); [interpretation, “Why the rank-squared scale appears”](../science/interpretation.md#why-the-rank-squared-scale-appears).

### M19

**The precision converse**

**Central question.** How does a support-aware quadratic majorant force $`r^2/(N+r^2)`$ regret?

**Understanding target.** Explain why the quadratic used in the proof majorizes $`(-c)_+/r`$ on $`c\ge-r`$ when $`N\ge r^2`$. Combine its expectation with the exact risk factorization to obtain $`E_Q\ge A_{d,r}r^2/(N+r^2)`$ for unrestricted coherent classification.

**Prerequisites and story role.** M17, M18. This strengthens the fixed-advantage obstruction into a precision-dependent lower bound.

**Conceptual connection.** A bound on the exact optimal learning curve constrains every quantum procedure. The argument does not require a competitor to simulate a channel or to satisfy a one-sided error condition.

**Source pointers.** [Quantum precision, §4](../science/quantum_precision.md); [exact classifier, Theorem Q1](../science/exact_classifier.md).

### M20

**Classical compilation and positivity**

**Central question.** Why may an arbitrary collective POVM be symmetrized so that $`E_yA_N\ge0`$?

**Understanding target.** Explain why permuting training registers preserves each outcome probability for every $`P`$. Use the resulting commutant structure to establish $`[E_y,A_N]=0`$, and distinguish this valid positivity argument from the generally false assertion that a product of positive operators is positive.

**Prerequisites and story role.** M04, M10, M12, M13. This identifies the structural step needed to cover the entire classical compiler class.

**Conceptual connection.** Symmetry provides an analytical simplification of arbitrary collective measurements without restricting their decision performance or classical outcome space.

**Source pointers.** [Classical compilation, §2.2](../science/classical_compilation.md); Watrous [§7.1.2](https://jhwatrous.github.io/TQI.7.pdf), for the commutant framework.

### M21

**The compiler converse**

**Central question.** How do likelihood order and swap traces bound every classical record?

**Understanding target.** Follow the scalar inequality $`x/(d+x)\le x/d`$ through functional calculus and a positive decision effect. Explain how reduced positive operators and the swap trace identity yield recovered advantage at most $`A_{d,r}N/(rd)`$.

**Prerequisites and story role.** M09, M14, M20. This establishes the lower-bound side of the classical comparison at the level of prediction itself.

**Conceptual connection.** The same exact likelihood that solves coherent prediction also limits measurement-first prediction. The converse does not assume a particular estimator, separate-copy measurements, or bounded classical memory.

**Source pointers.** [Classical compilation, Theorem C1 and §§2.1–2.3](../science/classical_compilation.md); [exact classifier, operator likelihood](../science/exact_classifier.md).

### M22

**Tomography-to-prediction upper**

**Central question.** Why does Frobenius estimation error control the subspace classifier's regret?

**Understanding target.** Explain the use of the top-$`r`$ eigenspace of the classical estimate and its nearest-flat-state property. Relate the exact projector loss $`\lVert P-\widehat P\rVert_F^2/(4r)`$ to the imported expected Frobenius error and the resulting $`O(rd/\varepsilon)`$ upper bound.

**Prerequisites and story role.** M05, M06, M12, M21. This supplies an attainable classical performance against which the unrestricted converse can be compared.

**Conceptual connection.** Tomography is a sufficient construction for prediction. Its use in the upper bound does not turn the earlier prediction converse into a claim that every successful compiler must perform tomography.

**Source pointers.** [Classical compilation, Theorem C2](../science/classical_compilation.md); [O'Donnell–Wright tomography theorem and attribution](../references/RELATED_WORK.md#odonnell2016).

### M23

**Controlled reflection from copies**

**Central question.** How do known program ancillas avoid a free controlled oracle?

**Understanding target.** Explain the augmented program state $`|1\rangle\langle1|\otimes P/r`$ and why simulation time $`t=\pi r`$ generates a controlled support reflection. Relate the control readout to the ideal effect $`P`$ and identify the consumption of one supplied state per program copy.

**Prerequisites and story role.** M04, M07, M12. This starts the attaining coherent construction using only the source access already present in the experiment.

**Conceptual connection.** Known ancillas can provide control through an enlarged Hamiltonian. They do not provide a description of the unknown support or controlled access to an unknown preparation circuit.

**Source pointers.** [Construction, “A controlled support reflection from copies”](../science/constructions.md#a-controlled-support-reflection-from-copies); [Lloyd2014](../references/RELATED_WORK.md#lloyd2014) and [Kimmel2017](../references/RELATED_WORK.md#kimmel2017) for the inherited simulation mechanism.

### M24

**Simulation error to prediction error**

**Central question.** Why are $`O(r^2/\varepsilon)`$ copies sufficient with explicit constants?

**Understanding target.** Explain the matched first derivatives of the partial-swap and target channels, the second-order remainder bound, and telescoping over fresh programs. Track the factor of one-half converting diamond-norm error into binary probability error, giving excess risk at most $`2\pi^2r^2/N`$.

**Prerequisites and story role.** M07, M23. This turns an ideal physical operation into a quantitative sample upper bound.

**Conceptual connection.** The reflection time grows with rank. Keeping that time in the simulation error explains why this construction retains the same rank-squared scale as the unrestricted converse.

**Source pointers.** [Construction, “An explicit simulation bound”](../science/constructions.md#an-explicit-simulation-bound); [quantum precision, §5](../science/quantum_precision.md); Watrous [§3.3.2](https://jhwatrous.github.io/TQI.3.pdf).

### M25

**Complete quantum precision theorem**

**Central question.** How do converse and construction combine, and on which error and rank domain?

**Understanding target.** State the uniform $`\Theta(r^2/\varepsilon)`$ law with $`1\le r\le d/2`$ and $`0<\varepsilon\le1/8`$, and explain the explicit lower and upper constants. Distinguish that domain from the exact decision's broader domain and from targets attainable with no training.

**Prerequisites and story role.** M19, M24. This integrates necessity and attainability into Theorem Q2.

**Conceptual connection.** Optimality of a sample order requires a converse for all permitted procedures and one allowed construction achieving that order. It does not require the construction to attain the exact finite-budget optimum or optimal constants.

**Source pointers.** [Quantum precision, Theorem Q2 and §6](../science/quantum_precision.md); [model, “Principal results and proof route”](../science/model.md#principal-results-and-proof-route).

### M26

**Classical comparison and its precision gap**

**Central question.** What is matched at fixed accuracy and proportional rank, and what remains unproved?

**Understanding target.** Combine the compiler converse, tomography upper, and inclusion of classical compilers among quantum procedures. Distinguish $`\Theta(rd)`$ at excess error $`1/16`$ for $`r\le d/2`$ from $`\Theta_c(d^2/\varepsilon)`$ for fixed $`0<c\le1/2`$, $`cd\le r\le d/2`$, and $`0<\varepsilon\le1/8`$. Identify the remaining gap for general classical precision.

**Prerequisites and story role.** M21, M22, M25. This assembles the two learner classes under common risk and access conventions.

**Conceptual connection.** Matching quantum precision does not automatically imply matching classical precision. The high-rank classical law follows because the inherited quantum lower becomes strong enough to meet the classical construction there.

**Source pointers.** [Classical compilation, §4 and Corollary C3](../science/classical_compilation.md); [interpretation, classical and high-rank comparisons](../science/interpretation.md).

### M27

**Resource accounting**

**Central question.** How do source copies, stored qubits, active width, gates, and one-use prediction differ?

**Understanding target.** Explain why the direct construction stores $`N\lceil\log_2d\rceil`$ unknown-state qubits before prediction despite its small active width. Account separately for source preparation, known ancillas, partial-swap gates, rotation synthesis, and the consumption of training systems for one test.

**Prerequisites and story role.** M02, M23, M24, M25. This translates sample attainability into the charged physical implementation described in the project.

**Conceptual connection.** A copy advantage is not automatically an end-to-end speedup or a memory saving. The stored program, source cost, and specified gate model determine what the construction physically requires.

**Source pointers.** [Construction, “Gates, active width and stored data”](../science/constructions.md#gates-active-width-and-stored-data); [model, “Boundaries and resources”](../science/model.md#boundaries-and-resources).

### M28

**Rank regimes and observable contrast**

**Central question.** Why does the copy advantage disappear at high rank while Bayes contrast stays finite?

**Understanding target.** Interpret the fixed-accuracy ratio $`d/r`$ across fixed, intermediate, and proportional ranks. Explain why $`r=d/2`$ leaves oracle success $`3/4`$ while both classes require order $`d^2/\varepsilon`$ copies in the stated range, and what this implies for a dimension-uniform learning claim under this access model.

**Prerequisites and story role.** M16, M26, M27. This connects the separate theorems to the physical meaning of rank and coherent retention.

**Conceptual connection.** Small individual spectral gaps can carry a constant aggregate decision advantage. Maintaining observable contrast does not ensure that the orientation needed to use it can be learned from few examples.

**Source pointers.** [Interpretation](../science/interpretation.md); [quantum precision, §7](../science/quantum_precision.md); the scoped [Banchi2024 comparison](../references/RELATED_WORK.md#banchi2024).

### M29

**Evidence and attribution**

**Central question.** Which ingredients are inherited, which statements are new derivations here, and what do finite checks establish?

**Understanding target.** Separate the project's exact likelihood and classification converses from established fixed-rank advantages, symmetry tools, simulation, and tomography. Compare operational objectives before transferring a previous theorem, and distinguish finite consistency checks from analytical proof or a priority guarantee.

**Prerequisites and story role.** M15, M19, M21, M22, M24, M28. This integrates the result with its primary-source context and the actual evidentiary support.

**Conceptual connection.** Similar access orders or asymptotic expressions do not make different tasks equivalent. Attribution and verification are strongest when their scope matches the precise claim being assessed.

**Source pointers.** [Related work](../references/RELATED_WORK.md), especially the An2026, Li2026, O'Donnell–Wright, and Kimmel comparisons; [verification guide](../verification/README.md). The source comparison is bounded and does not certify exhaustive priority.

### M30

**Global synthesis and claim boundaries**

**Central question.** How do optimal decision, unavoidable cost, access order, and physical resources fit into one result?

**Understanding target.** Explain the complete scientific story from the flat-state training experiment to the rank-independent optimal measurement, sharp quantum precision law, classical comparison, and high-rank limit. Keep the uniform domains, one-test objective, charged construction, and unresolved classical precision and memory questions explicit.

**Prerequisites and story role.** M12, M25, M26, M27, M28, M29. This is the global synthesis of the narrative phase and of the whole project.

**Conceptual connection.** The central result concerns how much prediction-relevant information survives in coherent examples compared with a classical record. Its exact decision, sample laws, implementation, and limitations answer different parts of that single operational question.

**Source pointers.** [Model](../science/model.md), [exact classifier](../science/exact_classifier.md), [quantum precision](../science/quantum_precision.md), [classical compilation](../science/classical_compilation.md), [construction](../science/constructions.md), and [interpretation](../science/interpretation.md); [Watrous bridge](watrous_bridge.md) for the connection to the selected anchor.
