## Review setup
- **Input scope** Abstract
- **Assessment boundary** Claims and evidence presented in the abstract only
- **Shared manuscript claim summary** The authors systematically evaluate the impact of pre-trained protein language model (PLM) embeddings on drug-target affinity (DTA) prediction, comparing them to classical 1D convolution methods across multiple backbones and datasets. They find that simple architectural modifications to convolution methods may be sufficient to bridge the performance gap to large pre-trained PLMs.
- **Visible evidence base** Abstract text only; no figures, tables, or methods section provided
- **Missing materials affecting confidence** Full manuscript (methods, results, figures, tables, code, data splits, hyperparameters, statistical tests)

## Reviewer 1
- **Overall assessment** The abstract presents a timely and potentially impactful benchmarking study on the use of protein language model embeddings for drug-target affinity prediction. The research question is well-motivated, and the experimental design—spanning multiple PLM families, representation backbones, and datasets—is commendable in scope. However, the abstract lacks critical quantitative results, statistical rigor, and methodological detail necessary to evaluate the strength of the central claim. The conclusion that simple architectural modifications may bridge the gap to PLMs is intriguing but currently unsupported by any numerical evidence in the provided material. The study's value to the field is clear, but the case is not established from the abstract alone.

- **Who would be interested in the results, and why** Computational drug discovery researchers, machine learning practitioners working on protein representation learning, and bioinformaticians developing DTA prediction models. The systematic comparison of PLM embeddings against simpler convolution methods addresses a practical question of resource allocation: whether the computational cost of large PLMs is justified for DTA tasks.

- **Major strengths** 1. Systematic evaluation across four PLM families with distinct architectures and training objectives (structure prediction, function prediction, sequence unmasking). 2. Use of multiple molecular representation backbones (four) and two benchmark datasets (Davis, KIBA) with standard metrics (CI, MSE). 3. Inclusion of cold-start train/test splits to assess generalization, which is a more realistic and challenging evaluation scenario. 4. Per-protein contribution analysis to understand model behavior at the protein level.

- **Major Concerns**
    - **Concern ID** R1-M1
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Evidence sufficiency
    - **Claim pointer** "The results indicate simple architectural modifications to traditional convolution methods may be sufficient to bridge the gap to large pre-trained PLMs."
    - **Evidence pointer** Abstract; location not provided
    - **Concern** The central claim of the abstract—that simple architectural modifications can match PLM performance—is presented without any quantitative support. No numerical results (CI values, MSE values, or effect sizes) are reported for any model or dataset. The reader cannot assess the magnitude of the performance gap, the statistical significance of any differences, or whether the claim holds across all datasets and backbones.
    - **Why it matters** This is the primary conclusion of the study. Without quantitative evidence, the claim is an unsupported assertion. The field needs to know, for example, whether the modified convolution method achieves CI within 0.01 of the best PLM-based model, or whether the gap is larger but still "bridged" in a practical sense.
    - **Resolution test** Provide key numerical results in the abstract, including at least: (i) the best CI and MSE for each dataset for both the PLM-based and modified convolution methods, (ii) the performance of the baseline convolution method for comparison, and (iii) a statement of whether differences are statistically significant (e.g., via bootstrapped confidence intervals).

    - **Concern ID** R1-M2
    - **Severity** Major
    - **Blocking** Yes
    - **Axis** Methodological transparency
    - **Claim pointer** "We design multiple experiments across four different molecular representation backbones and assess the effect of incorporating PLM embeddings, comparing their performance to classical 1D convolution methods."
    - **Evidence pointer** Abstract; location not provided
    - **Concern** The abstract does not specify what the "four different molecular representation backbones" are, nor what the "simple architectural modifications" to the convolution method entail. Without this information, the reader cannot evaluate the fairness of the comparison or the novelty of the proposed modifications.
    - **Why it matters** The claim that simple modifications suffice depends entirely on what those modifications are. If the modifications are non-trivial (e.g., adding attention mechanisms or residual connections), the conclusion may be less surprising. The field needs to know the specific architectural changes to assess their simplicity and reproducibility.
    - **Resolution test** Briefly name the four backbones (e.g., GCN, GAT, GIN, MPNN) and describe the key architectural modification (e.g., "adding a 2-layer MLP with residual connections to the 1D convolution branch").

    - **Concern ID** R1-M3
    - **Severity** Major
    - **Blocking** No
    - **Axis** Generalizability and robustness
    - **Claim pointer** "We further evaluate the generalization power of each model using cold-start train and test splits, and analyze the per-protein contribution to total CI."
    - **Evidence pointer** Abstract; location not provided
    - **Concern** The abstract reports that cold-start evaluation was performed but provides no results. Cold-start splits (where test proteins or drugs are unseen during training) are known to be much harder than random splits. The claim about bridging the gap to PLMs may not hold under cold-start conditions, which would significantly weaken the conclusion.
    - **Why it matters** The practical value of DTA models depends on their ability to generalize to new proteins and drugs. If PLMs show a clear advantage under cold-start conditions, the conclusion that simple modifications suffice would be misleading.
    - **Resolution test** Report at least one key cold-start result (e.g., "Under cold-start protein splits, the modified convolution method achieved CI of X vs. Y for the best PLM model, compared to Z for the baseline").

- **Minor Comments**
    - **Concern ID** R1-m1
    - **Severity** Minor
    - **Axis** Clarity
    - **Affected element** Model naming
    - **Evidence pointer** Abstract; location not provided
    - **Issue** The abstract introduces "PLM-GraphDTA" and "DeepGraphDTA" but does not clearly define how these relate to the four PLM families and four backbones. It is unclear whether PLM-GraphDTA is a single model or a family of models.
    - **Required correction** Clarify the naming convention: e.g., "We integrate each PLM into GraphDTA to create PLM-GraphDTA variants (e.g., ESM-GraphDTA, ProtBERT-GraphDTA)."

    - **Concern ID** R1-m2
    - **Severity** Minor
    - **Axis** Completeness
    - **Affected element** PLM families
    - **Evidence pointer** Abstract; location not provided
    - **Issue** The abstract states "four families of PLMs" but does not name them. For a benchmarking study, the specific PLMs are essential information.
    - **Required correction** List the four PLM families (e.g., ESM-1b, ProtBERT, ProtT5, Ankh) in the abstract.

    - **Concern ID** R1-m3
    - **Severity** Minor
    - **Axis** Reproducibility
    - **Affected element** Evaluation metrics
    - **Evidence pointer** Abstract; location not provided
    - **Issue** The abstract uses CI and MSE but does not specify whether MSE is computed on log-transformed or raw Kd/Ki values, which is a common source of variability in DTA benchmarks.
    - **Required correction** Specify the MSE target (e.g., "MSE on log-transformed binding affinity values").

- **Technical failings that need to be addressed before the case is established** R1-M1 (lack of quantitative results for the central claim) and R1-M2 (insufficient methodological detail on backbones and modifications) are blocking. Without these, the abstract does not provide enough evidence to evaluate the study's conclusions.

- **Assessment against Nature-style criteria**
    - **Originality**: Moderate. The systematic comparison of PLM embeddings for DTA is not entirely novel, but the specific focus on whether simple modifications can match PLMs is a useful and practical question.
    - **Scientific importance**: High. If the claim holds, it could reduce the computational burden of DTA prediction and make high-performance models more accessible.
    - **Interdisciplinary readership**: Moderate. The topic is of primary interest to computational biologists and machine learning researchers; the abstract is accessible to a broader audience but lacks the quantitative hook to draw in nonspecialists.
    - **Technical soundness**: Cannot be assessed from the abstract alone. The experimental design appears sound in scope, but the lack of results and methodological detail prevents evaluation.
    - **Readability for nonspecialists**: Good. The abstract is clearly written and avoids unnecessary jargon, though the model names could be better explained.

- **Recommendation posture** Currently not established from the provided evidence. The abstract presents an interesting research question and a well-structured experimental plan, but the central claim is unsupported by quantitative results. The authors should provide key numerical findings and clarify the methodological details before the study can be properly evaluated.

## Risk / unsupported claims
- "The results indicate simple architectural modifications to traditional convolution methods may be sufficient to bridge the gap to large pre-trained PLMs." — Unsupported; no quantitative results provided.
- Any implied superiority of the modified convolution method over PLMs or vice versa — Unsupported; no comparative results given.
- The effectiveness of cold-start evaluation or per-protein analysis — Unsupported; no results reported.