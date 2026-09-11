## Review setup
- **Input scope** Full manuscript (abstract only provided)
- **Assessment boundary** Claims and evidence presented in the abstract
- **Shared manuscript claim summary** The authors claim that membrane phase, charge, and curvature cooperatively regulate alpha-synuclein binding dynamics, with gel-phase membranes and anionic lipids promoting kinetically stabilized states, and that curvature-induced defect formation is amplified in gel-phase but insensitive to charge.
- **Visible evidence base** Abstract only; no figures, tables, methods, or simulation details provided
- **Missing materials affecting confidence** Full text, all figures, experimental protocols, simulation parameters, statistical analyses, and supplementary information

## Reviewer
- **Overall assessment** The abstract presents a potentially important advance in understanding the multi-parameter regulation of alpha-synuclein–membrane interactions. The claim that membrane phase, charge, and curvature act cooperatively, rather than independently, is timely and could have implications for both physiological function and disease mechanisms. However, the abstract alone provides insufficient detail to evaluate the rigor of the experimental design, the robustness of the data, or the validity of the conclusions. Key methodological choices (e.g., vesicle size distributions, lipid compositions, FRAP analysis) and simulation validation are not described. The work appears technically sound in principle, but the evidence base is too limited for a definitive assessment.

- **Who would be interested in the results, and why** Researchers in membrane biophysics, protein–lipid interactions, and neurodegenerative disease (particularly Parkinson’s disease) would be interested. The cooperative regulation of binding by phase, charge, and curvature addresses a gap in the field, and the kinetic stabilization finding could inform models of alpha-synuclein aggregation on membranes.

- **Major strengths**
  - Addresses a clear gap: the combined effects of membrane phase, charge, and curvature on alphaSyn binding dynamics have not been systematically studied.
  - Integrates multiple experimental techniques (fluorescence microscopy, CD, FRAP) with coarse-grained simulations, providing complementary perspectives.
  - Identifies a specific mechanistic insight: curvature-dependent packing defects in gel-phase membranes drive binding under zwitterionic conditions.
  - Distinguishes between thermodynamic and kinetic contributions, which is conceptually important for understanding protein–membrane interactions.

- **Major Concerns**
  - **Concern ID** R1-M1
    **Severity** Major
    **Blocking** Yes
    **Axis** Experimental design and data completeness
    **Claim pointer** "alphaSyn preferentially binds highly curved gel-phase membranes, driven by curvature-dependent enrichment of packing defects arising from faceted vesicle morphologies."
    **Evidence pointer** Abstract; no figure or table specified
    **Concern** The abstract does not provide any quantitative data (e.g., binding isotherms, FRAP recovery curves, or simulation snapshots) to support this claim. The existence of "faceted vesicle morphologies" in gel-phase vesicles is asserted but not demonstrated. Without evidence of actual faceting or defect quantification, the mechanistic link remains speculative.
    **Why it matters** This claim is central to the paper’s novelty. If the faceted morphology is not experimentally confirmed or if the defect density is not measured, the proposed mechanism is unsubstantiated.
    **Resolution test** Provide experimental evidence (e.g., cryo-EM or AFM images) showing faceted gel-phase vesicles, and quantify defect density (e.g., via molecular dynamics or fluorescence probe partitioning) as a function of curvature.

  - **Concern ID** R1-M2
    **Severity** Major
    **Blocking** Yes
    **Axis** Data interpretation and control experiments
    **Claim pointer** "Incorporation of anionic lipids selectively enhances binding in liquid-phase membranes while attenuating curvature-dependent partitioning in gel-phase membranes."
    **Evidence pointer** Abstract; no figure or table specified
    **Concern** The abstract does not specify the anionic lipid fraction used, the range of curvatures tested, or whether the attenuation in gel-phase is statistically significant. The phrase "selectively enhances" implies a differential effect that requires direct comparison under identical conditions. Without these details, the claim is ambiguous.
    **Why it matters** The interplay between charge and phase is a key finding. If the effect is small or not properly controlled (e.g., for vesicle size distribution), the conclusion may be overstated.
    **Resolution test** Report the full dataset (binding affinity vs. curvature for multiple anionic lipid fractions) with error bars and statistical tests. Include control experiments with charge-neutral gel-phase vesicles to isolate charge effects.

  - **Concern ID** R1-M3
    **Severity** Major
    **Blocking** Yes
    **Axis** Simulation validation
    **Claim pointer** "Simulations show that curvature-induced defect formation is strongly amplified in gel-phase membranes but largely insensitive to charge."
    **Evidence pointer** Abstract; no figure or table specified
    **Concern** The abstract does not describe the coarse-grained model, force field, system size, or simulation timescales. It is unclear whether the simulations reproduce the experimental conditions (e.g., lipid composition, temperature, vesicle curvature). Without validation against experimental data (e.g., defect density from fluorescence), the simulation results are unverified.
    **Why it matters** The simulation claim directly supports the experimental mechanism. If the model is not validated, the entire mechanistic narrative is weakened.
    **Resolution test** Provide simulation details (model, parameters, convergence) and show direct comparison between simulated defect densities and experimental proxies (e.g., dye partitioning or binding data).

- **Minor Comments**
  - **Concern ID** R1-m1
    **Severity** Minor
    **Axis** Clarity and terminology
    **Affected element** Abstract text
    **Evidence pointer** Abstract
    **Issue** The term "kinetically stabilized states" is used but not defined. Does this refer to slower off-rates, longer residence times, or reduced exchange? The abstract should clarify the kinetic parameter being measured.
    **Required correction** Define "kinetically stabilized" in terms of specific FRAP or exchange measurements (e.g., mobile fraction, half-time of recovery).

  - **Concern ID** R1-m2
    **Severity** Minor
    **Axis** Scope and generalizability
    **Affected element** Abstract text
    **Evidence pointer** Abstract
    **Issue** The abstract focuses on gel-phase and liquid-phase membranes but does not mention whether the findings apply to physiologically relevant membrane compositions (e.g., with cholesterol or raft-like domains).
    **Required correction** Add a sentence acknowledging the limitations of the model membrane system or state whether the findings are expected to generalize.

  - **Concern ID** R1-m3
    **Severity** Minor
    **Axis** Readability
    **Affected element** Abstract text
    **Evidence pointer** Abstract
    **Issue** The phrase "curvature-dependent enrichment of packing defects arising from faceted vesicle morphologies" is dense and may be difficult for nonspecialists to parse.
    **Required correction** Consider rephrasing to: "curvature-dependent packing defects, which are enriched in faceted gel-phase vesicles."

- **Technical failings that need to be addressed before the case is established**
  - R1-M1: Lack of experimental evidence for faceted vesicle morphologies and defect quantification.
  - R1-M2: Insufficient detail on anionic lipid fraction, curvature range, and statistical significance.
  - R1-M3: Unvalidated simulation results without model description or experimental comparison.

- **Assessment against Nature-style criteria**
  - **Originality**: High. The cooperative regulation of phase, charge, and curvature on alphaSyn binding dynamics is a novel angle that goes beyond previous independent studies.
  - **Scientific importance**: Moderate to high. Understanding alphaSyn–membrane interactions is relevant to Parkinson’s disease, but the physiological relevance of gel-phase membranes (which are rare in cells) may limit immediate impact.
  - **Interdisciplinary readership**: Moderate. The work bridges biophysics, cell biology, and neurochemistry, but the focus on model membranes may reduce appeal to clinical or systems-level audiences.
  - **Technical soundness**: Cannot be fully assessed from the abstract. The combination of techniques is appropriate, but the lack of data and simulation details prevents evaluation of rigor.
  - **Readability for nonspecialists**: Fair. The abstract is concise but uses specialized terminology (e.g., "faceted vesicle morphologies," "kinetically stabilized states") without sufficient explanation.

- **Recommendation posture** Currently not established from the provided evidence. The abstract presents an interesting hypothesis and a plausible experimental approach, but the absence of quantitative data, control experiments, and simulation validation means the core claims cannot be evaluated. A full manuscript with figures, methods, and statistical analyses is required for a definitive assessment. Supportive if technical concerns are resolved.