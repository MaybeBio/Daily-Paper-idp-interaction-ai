## Review setup
- **Input scope** Full manuscript text (abstract and main text, figures and tables not provided)
- **Assessment boundary** Claims and evidence as presented in the abstract and text description; no figures, tables, or supplementary materials were supplied
- **Shared manuscript claim summary** The authors claim that biomolecular condensates fundamentally alter the folding landscape of protein alpha-helices through a balance of multivalent interactions (unfolding) and crowding (folding), and that this process is kinetically frustrated due to coupling with condensate dynamics, leading to dual sequence dependence.
- **Visible evidence base** Atomistic simulations of helix-coil transitions; Bayesian optimization-derived residue-resolution model; application to TDP-43, Annexin A11, and Androgen Receptor helices in condensates of varying properties
- **Missing materials affecting confidence** All figures, tables, supplementary information, simulation details, model parameters, and quantitative results (e.g., free energy differences, kinetic rates, error bars) are absent. This severely limits the ability to evaluate the technical soundness of the claims.

## Reviewer 1
- **Overall assessment** The manuscript addresses a timely and important question—how biomolecular condensates reshape protein folding—and proposes a conceptually appealing framework. However, the provided text alone is insufficient to assess the validity of the core claims. The absence of quantitative data, simulation details, and validation metrics means that the evidence base is currently too thin to support the strong conclusions drawn. The work has potential, but the case is not yet established from the supplied material.

- **Who would be interested in the results, and why** Researchers in biophysics, protein folding, phase separation, and cellular organization will be interested. The work bridges condensate physics and protein structural biology, offering a framework that could inform understanding of condensate-mediated proteinopathies (e.g., ALS, cancer) and guide the design of condensates for synthetic biology. The dual sequence-dependence concept is particularly novel and could attract a broad readership.

- **Major strengths** 1. The question is fundamental and timely, addressing a gap in how condensates affect protein structure beyond simple crowding. 2. The proposed framework—balancing multivalent interactions (unfolding) and crowding (folding)—is conceptually elegant and testable. 3. The use of Bayesian optimization to develop a chemically specific model is a methodological strength. 4. The application to disease-associated proteins (TDP-43, Annexin A11, Androgen Receptor) adds translational relevance.

- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Evidence sufficiency
    - **Claim pointer** "Atomistic simulations suggest the helix-coil transition within condensates differs markedly from its behavior in dilute solution or in the presence of inert crowders."
    - **Evidence pointer** Text only; no figures, tables, or simulation details provided
    - **Concern** The claim is based on atomistic simulations, but no quantitative data (e.g., free energy profiles, melting temperatures, population shifts) are presented. The nature of the condensate model, force field, system size, and sampling methodology are not described. Without these, the reader cannot evaluate whether the observed differences are statistically significant or an artifact of the simulation setup.
    - **Why it matters** This is the foundational observation of the paper. If the simulation evidence is weak or non-robust, the entire framework built upon it collapses.
    - **Resolution test** Provide the free energy difference (ΔG) for helix-coil transition in dilute solution, inert crowder, and condensate conditions, with error bars. Report the simulation parameters (force field, box size, condensate composition, equilibration time, sampling method). Show that the differences are statistically significant (e.g., via bootstrapping or multiple independent runs).

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Model validation
    - **Claim pointer** "We then use Bayesian optimization to develop a chemically specific, residue-resolution model for quantification of alpha-helical folding and apply it to characterize diverse helices... within condensates of varying physicochemical properties."
    - **Evidence pointer** Text only; no model details, validation, or application results provided
    - **Concern** The Bayesian optimization model is central to the quantitative claims, but no information is given about its architecture, training data, feature space, or validation against known experimental or simulation data. The "residue-resolution" claim implies a level of detail that requires demonstration. The application to disease-associated helices is mentioned but no results (e.g., predicted folding propensities, comparison to experiments) are shown.
    - **Why it matters** Without model validation, the quantitative predictions are unsubstantiated. The reader cannot assess whether the model captures the physics correctly or is overfitted.
    - **Resolution test** Provide the model's training set, validation metrics (e.g., R², RMSE against known helix propensities), and a comparison of model predictions to independent simulation or experimental data. Show the predicted folding free energies for the three disease-associated helices in at least two condensate conditions, with uncertainty estimates.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Kinetic claim support
    - **Claim pointer** "helix folding transitions are kinetically frustrated inside condensates because they are coupled to the time scale of contact rearrangement with co-condensate proteins."
    - **Evidence pointer** Text only; no kinetic data provided
    - **Concern** The claim of kinetic frustration is a strong statement about dynamics, but no timescales, relaxation rates, or comparison to dilute solution kinetics are presented. The coupling to "contact rearrangement" is asserted but not demonstrated. The text does not specify how this was measured or simulated.
    - **Why it matters** Kinetic frustration is a key novelty of the paper. If unsupported, the claim of dual sequence dependence (from both helix and co-condensate proteins) is weakened.
    - **Resolution test** Provide the folding/unfolding rate constants (k_fold, k_unfold) in dilute solution and in condensates, with error bars. Show that the relaxation time in condensates is significantly longer than in dilute solution. Demonstrate that the timescale of contact rearrangement (e.g., from protein-protein contact lifetime analysis) is comparable to or slower than the folding timescale.

- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity
    - **Affected element** Abstract
    - **Evidence pointer** Text
    - **Issue** The phrase "dually sequence-dependent" is introduced without clear definition. It is not immediately obvious what "dual" refers to (helix sequence and co-condensate protein sequence).
    - **Required correction** Define "dual sequence dependence" explicitly in the abstract or early in the main text. For example: "the folding landscape depends on both the sequence of the alpha-helical domain and the sequences of co-condensate proteins."

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Terminology
    - **Affected element** Abstract
    - **Evidence pointer** Text
    - **Issue** The term "inert crowders" is used but not defined. In the context of condensates, "inert" is ambiguous—are these synthetic crowders (e.g., PEG, Ficoll) or a specific protein-based crowder?
    - **Required correction** Specify the nature of the inert crowders used in the simulations (e.g., "inert crowders such as PEG 8000" or "a model inert crowder with no specific interactions").

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Completeness
    - **Affected element** Abstract
    - **Evidence pointer** Text
    - **Issue** The implications for "condensate-mediated proteinopathies" and "targeting aberrant condensates" are stated but no specific examples or mechanisms are given.
    - **Required correction** Add a brief example or reference to a specific disease mechanism (e.g., "for example, the TDP-43 helix we studied is linked to ALS, and our results suggest that condensate composition could modulate its aggregation propensity").

- **Technical failings that need to be addressed before the case is established** R1-M1 (simulation evidence), R1-M2 (model validation), R1-M3 (kinetic support). All three are blocking because the core claims of the paper—altered folding landscape, quantitative model, and kinetic frustration—are unsupported by the provided material.

- **Assessment against Nature-style criteria**
    - **Originality**: High. The concept of condensates dictating folding landscapes through a balance of interactions and crowding, with kinetic frustration, is novel and goes beyond existing work on crowding or simple partitioning.
    - **Scientific importance**: High. If validated, the work would have broad implications for understanding protein function in cellular environments, disease mechanisms, and synthetic biology.
    - **Interdisciplinary readership**: High. The topic bridges biophysics, cell biology, and computational chemistry, and the disease connections broaden appeal.
    - **Technical soundness**: Currently not assessable. The absence of quantitative data, simulation details, and model validation means the technical foundation cannot be evaluated. This is the critical weakness.
    - **Readability for nonspecialists**: Good. The abstract is clearly written and the conceptual framework is accessible. However, terms like "Bayesian optimization" and "residue-resolution model" may require brief explanation for a general audience.

- **Recommendation posture** Currently not established from the provided evidence. The manuscript has strong potential and addresses an important question, but the evidence base is insufficient to support the claims. A revised version with full simulation data, model validation, and kinetic analysis could change this assessment. I am supportive if the technical concerns are resolved.