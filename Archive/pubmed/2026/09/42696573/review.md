## Review setup
- **Input scope** Full manuscript (including abstract, introduction, results, discussion, materials and methods, and supplementary materials)
- **Assessment boundary** Scientific content only; editorial or formatting issues are not considered
- **Shared manuscript claim summary** The authors propose a stepwise molecular pathway for the recruitment of the ULK1 autophagy-initiating complex to membranes, mediated by WIPI proteins and the ATG13:ATG101 HORMA dimer, culminating in the positioning of the ULK1 kinase domain near the membrane surface.
- **Visible evidence base** Biochemical reconstitution assays, cell-based assays (autophagy and mitophagy), AlphaFold2 structural predictions, molecular dynamics simulations, GUV and SUV binding assays, mutagenesis, and microscopy.
- **Missing materials affecting confidence** None identified; the manuscript is comprehensive.

## Reviewer 1
- **Overall assessment** This is a thorough and well-executed study that addresses a long-standing question in the autophagy field: how the ULK1 complex is recruited to PI3P-containing membranes despite lacking a canonical PI3P-binding domain. The authors present a compelling stepwise model involving WIPI2, WIPI3, the ATG101 WF finger, and a novel ULK1 IDR-ATG13 HORMA interaction. The combination of in vitro reconstitution, cell-based assays, and computational modeling is a strength. However, several concerns regarding the quantitative rigor of the cellular data and the generalizability of the model to all forms of autophagy need to be addressed.
- **Who would be interested in the results, and why** Researchers in the fields of autophagy, membrane biology, and kinase signaling. The study provides a mechanistic framework for a central event in autophagy initiation, which has implications for understanding diseases linked to autophagy dysfunction, such as Parkinson's disease and cancer.
- **Major strengths** 1. The study elegantly solves a long-standing paradox in the field. 2. The use of a minimal reconstituted system to dissect the stepwise recruitment is powerful. 3. The combination of computational modeling (AlphaFold2 and MD simulations) with experimental validation is robust. 4. The identification of a novel ULK1 IDR-ATG13 HORMA interaction provides a mechanism for kinase positioning.
- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** No
    - **Axis** Quantitative rigor of cellular data
    - **Claim pointer** The authors claim that the ATG13(HF|DD) and ULK1(ADA) mutants significantly impair autophagy and mitophagy in cells.
    - **Evidence pointer** Figures 4, 6, and S6, S10
    - **Concern** The quantification of the autophagy and mitophagy assays (e.g., Halo-LC3 flux, mito-QC) relies on manual or semi-automated image analysis. The statistical power and the number of independent experiments for these key cellular phenotypes are not always clearly stated in the figure legends. For example, in Figure 4K-L, the Halo-LC3 flux assay shows a clear defect for the HF|DD mutant, but the error bars and statistical test are not fully described in the legend. Similarly, the mito-QC data in Figure 6A-B and S6A-B would benefit from a more detailed description of the quantification pipeline and the number of cells analyzed per replicate.
    - **Why it matters** The cellular validation is critical for establishing the physiological relevance of the proposed mechanism. Without rigorous and transparent quantification, the strength of the in vivo conclusions is weakened.
    - **Resolution test** Provide a clear statement in the figure legends for all cellular assays (Figures 4, 6, S6, S10) detailing: (1) the number of independent biological replicates (n), (2) the total number of cells analyzed per condition per replicate, (3) the specific statistical test used (e.g., two-way ANOVA with Šidák's multiple-comparison test), and (4) whether the data are presented as mean ± SD or SEM. For the mito-QC and LC3 flux assays, consider providing a more detailed description of the automated or semi-automated quantification pipeline in the Methods section.

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** No
    - **Axis** Generalizability of the model
    - **Claim pointer** The authors propose a stepwise pathway for ULK1 recruitment that is general to autophagy initiation.
    - **Evidence pointer** Discussion, Figure 7
    - **Concern** The model is built primarily on data from starvation-induced autophagy and DFP-induced mitophagy. The authors acknowledge that WIPI3 KO has been reported to have no effect on starvation-induced autophagy in HEK293 cells (reference 61). While they discuss this discrepancy, they do not provide a clear explanation or experimental data to resolve it. The model's generalizability to other forms of selective autophagy (e.g., xenophagy, aggrephagy) or to different cell types is not addressed.
    - **Why it matters** A central claim of the paper is that this is a unifying model for ULK1 recruitment. The existence of a contradictory report and the lack of testing in other contexts limits the scope of the claim.
    - **Resolution test** 1. Discuss the discrepancy with reference 61 in more detail. Is it possible that WIPI3 is redundant with WIPI2 in HEK293 cells, or that the KO was incomplete? 2. Add a sentence or two in the Discussion acknowledging that the model may be context-dependent and that further work is needed to test its generalizability to other cell types and autophagy-inducing conditions.

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Mechanistic detail of the ULK1 IDR-ATG13 interaction
    - **Claim pointer** The ULK1 IDR (residues 428-450) binds directly to the ATG13 HORMA domain, and this interaction is critical for kinase positioning and activity.
    - **Evidence pointer** Figures 5, S7, S8
    - **Concern** The evidence for the direct interaction is strong (AlphaFold2, GST pull-down). However, the functional consequence of this interaction is modeled as a reduction in the average distance of the ULK1 KD to the membrane (from 19 to 12 nm). The model is based on a single set of assumptions about the IDR conformation and the position of the palmitoylated cysteines. The authors should discuss the limitations of this model and whether other mechanisms (e.g., allosteric activation of ULK1 by the ATG13 HORMA domain) could also contribute to the observed increase in ATG16L1 phosphorylation.
    - **Why it matters** The paper's central conclusion is that the IDR-HD interaction positions the kinase. If the primary effect is allosteric, the model would need to be revised.
    - **Resolution test** 1. In the Discussion, explicitly state that the modeling data are consistent with a proximity-based mechanism but do not rule out additional allosteric effects. 2. Consider performing an in vitro kinase assay using a soluble substrate (e.g., a peptide) to test if the ADA mutation affects ULK1 catalytic activity directly, independent of membrane proximity.

- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity of presentation
    - **Affected element** Figure 1
    - **Evidence pointer** Figure 1A-B
    - **Issue** The sequence logo in Figure 1A is described as showing the "DHF motif," but the logo appears to show conservation of a broader region. The exact boundaries of the motif should be more clearly indicated.
    - **Required correction** Add a box or bracket to the sequence logo in Figure 1A to clearly delineate the DHF motif (residues D213, H214, F215).

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Data presentation
    - **Affected element** Figure 2
    - **Evidence pointer** Figure 2D-E
    - **Issue** The GUV binding data in Figure 2D-E show a linear, concentration-dependent relationship for the WF mutant. The authors state this is "primarily driven by the WIPI3-PI3P interaction." It would be helpful to show a control without WIPI3 for the WF mutant to confirm this.
    - **Required correction** Add a control condition for the ATG101(WF|DD) mutant in the absence of WIPI3 in Figure 2D-E to demonstrate that the residual binding is indeed WIPI3-dependent.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Statistical reporting
    - **Affected element** Figure 4
    - **Evidence pointer** Figure 4C
    - **Issue** The dot blot data in Figure 4C are quantified in Figure 4E. The statistical test used is not specified in the legend for Figure 4C.
    - **Required correction** Add the statistical test used (e.g., two-way ANOVA) to the legend of Figure 4C.

    - **Concern ID** R1-m4
    - **Severity** Minor
    - **Axis** Completeness of model
    - **Affected element** Discussion
    - **Evidence pointer** Discussion, Figure 7
    - **Issue** The model in Figure 7 is elegant but does not include the role of ATG9, which is mentioned in the Introduction as a binding partner for the ATG13:ATG101 dimer.
    - **Required correction** Add a brief note in the Discussion or a label in Figure 7 to indicate where ATG9 binding might fit into the stepwise pathway, even if it is not the focus of this study.

- **Technical failings that need to be addressed before the case is established** None identified. The technical quality of the work is high.
- **Assessment against Nature-style criteria**
    - **Originality**: High. The study provides a novel and unifying mechanism for a central, unresolved question in autophagy.
    - **Scientific importance**: High. The work explains a decade-old observation and has implications for understanding the molecular basis of autophagy-related diseases.
    - **Interdisciplinary readership**: Moderate. The topic is specialized, but the principles of membrane recruitment and kinase positioning are of broad interest to cell biologists and biochemists.
    - **Technical soundness**: High. The study uses a multi-pronged approach with appropriate controls and rigorous data analysis.
    - **Readability for nonspecialists**: Good. The abstract and introduction are clear, and the figures are well-designed. The discussion effectively contextualizes the findings.
- **Recommendation posture** Supportive if technical concerns are resolved. The major concerns are primarily about the quantitative rigor of the cellular data and the generalizability of the model, which can be addressed with clarifications and additional discussion.

## Risk / unsupported claims
- None identified. All major claims are supported by the provided evidence.