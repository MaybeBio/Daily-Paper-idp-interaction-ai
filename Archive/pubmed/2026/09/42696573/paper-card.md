## 01 基本信息
- **标题**: Reconstitution of multistep recruitment of ULK1 to membranes in autophagy
- **作者与单位**: Duan, Yongjia (UC Berkeley); Lu, Ye (UC Berkeley); Paul, Sanjoy (Max Planck Institute of Biophysics); Betz, Johannes (Max Planck Institute of Biophysics); Wilhelm, Lea P (Max Planck Institute of Biophysics); Cook, Annan S I (University of Dundee); Ren, Xuefeng (UC Berkeley); Adriaenssens, Elias (University of Dundee); Martens, Sascha (University of Vienna); Ganley, Ian G (University of Dundee); Hummer, Gerhard (Max Planck Institute of Biophysics); Hurley, James H (UC Berkeley)
- **期刊/预印本平台**: Science Advances
- **年份**: 2026
- **论文类型**: 研究论文
- **领域**: 细胞生物学/生物化学/结构生物学
- **关键词**: 自噬, ULK1, ATG13, ATG101, WIPI, 相分离, 膜招募, 无序蛋白, 分子动力学模拟, AlphaFold
- **DOI/arXiv 号**: 10.1126/sciadv.aeg3201
- **代码、数据**: 代码: https://doi.org/10.5281/zenodo.20076398; 数据: https://doi.org/10.5281/zenodo.18778578
- **阅读日期**: 2024-05-24
- **该文在「无序蛋白/相分离 × 蛋白互作 × AI 方法」方向中的位置**: 本文是研究IDP/IDR介导的蛋白复合物膜招募的典范。它利用AlphaFold2预测IDR与折叠蛋白的互作，结合分子动力学(MD)模拟验证，并通过生化重建和细胞实验确认功能。核心发现是ULK1的IDR中的PVP基序与ATG13的HORMA结构域互作，将激酶结构域定位到膜附近。这为理解IDR如何通过短线性基序(SLiM)调控蛋白定位和活性提供了机制性框架，并展示了AI预测与物理模拟结合解决复杂生物学问题的强大能力。

## 02 一句话总结
本文通过生化重建、AlphaFold2预测和分子动力学模拟，揭示了ULK1自噬起始复合物通过WIPI蛋白和ATG101的WF指协同锚定到含PI3P的膜上，并发现ULK1 IDR中的PVP基序与ATG13 HORMA结构域互作，将ULK1激酶结构域定位到膜附近以磷酸化底物。

## 03 研究问题
- **具体问题**: PI3P如何招募不含PI3P结合结构域的ULK1复合物(ULK1C)到自噬体膜上？ULK1的激酶结构域(KD)如何接近其膜结合底物？
- **为什么重要**: ULK1C的膜招募是自噬起始的关键事件，但其机制长期未知。PI3P依赖的ULK1C稳定化是自噬领域的核心问题，而ULK1 KD与膜的距离调控对于理解其底物特异性至关重要。
- **现有方法为何不足**: 先前认为ATG13 N端碱性残基簇结合PI3P，但晶体结构不支持，且更严格的GUV结合实验无法重复。ULK1 KD通过长IDR与膜锚定部分连接，其如何接近膜底物也不清楚。
- **精确的「Can ... ?」研究问题**: Can the intrinsically disordered regions (IDRs) of ATG13 and ULK1, through short linear interaction motifs (SLiMs), mediate the stepwise recruitment and membrane-proximal positioning of the ULK1 kinase domain?

## 04 背景与发展脉络
- **阶段1: 发现PI3P依赖的ULK1C招募 (约2010年)**: 发现PI3P合成对ULK1C在自噬体形成位点的稳定化至关重要，但机制未知。**优点**: 建立了关键联系。**局限**: 机制假说(ATG13直接结合PI3P)未被后续结构生物学和严格生化实验支持。
- **阶段2: 发现WIPI蛋白在BNIP3/NIX介导线粒体自噬中招募ULK1C (2023年)**: 发现WIPI2通过结合ATG13 IDR中的W2IR基序招募ULK1C。**优点**: 提供了WIPI-ULK1C互作的线索。**局限**: 该机制是否适用于一般自噬尚不清楚。
- **阶段3: 本文的工作**: 系统性地阐明了ULK1C通过WIPI2/WIPI3和ATG101 WF指协同锚定到PI3P膜上，并发现ULK1 IDR中的PVP基序与ATG13 HORMA结构域互作，将KD定位到膜附近。**本文主张的位置**: 填补了PI3P依赖的ULK1C招募和KD定位的机制空白，提出了一个多步骤、协同的膜招募和激活模型。
- **注**: 此脉络是「经外部核验」的，基于文中引用的文献。

## 05 核心痛点
| 痛点 | 表现 | 成因或作者解释 | 文中证据 |
| :--- | :--- | :--- | :--- |
| PI3P依赖的ULK1C招募机制缺失 | 已知PI3P对ULK1C稳定化至关重要，但ULK1C亚基不含PI3P结合结构域。 | 先前认为ATG13 N端碱性残基簇结合PI3P，但晶体结构不支持，且GUV结合实验无法重复。 | Results节: "the crystal structure of the human ATG13:ATG101 HORMA dimer did not show evidence of a PI3P-binding pocket... nor... has it been possible to replicate the finding of PI3P binding using more stringent... GUV binding assays." |
| ULK1激酶结构域(KD)与膜距离过远 | ULK1 KD通过~500残基的IDR与膜锚定部分连接，难以接近膜结合底物。 | 缺乏将KD拉近膜的额外机制。 | Results节: "Even when the ATG13:ATG101 HORMA dimer is tightly engaged with membranes, the ULK1 KD is tethered only distantly from the membrane by the ULK1 IDR and a further >150 residues of ATG13 IDR." |
| ATG101 WF指功能未知 | ATG101的WF指对自噬至关重要，但其结合伙伴和功能长期未知。 | WF指不参与已知的ATG9 IDR结合。 | Discussion节: "The identity of the ATG101 WF binding partner has been unresolved for the past decade." |

## 06 核心思想
1.  **表面方法**: 结合AlphaFold2结构预测、分子动力学(MD)模拟、体外生化重建(GUV/脂质体结合、激酶活性测定)和细胞实验(自噬/线粒体自噬通量测定、免疫共沉淀、免疫荧光)，系统性地解析ULK1C的膜招募和激活机制。
2.  **核心洞察**: ULK1C的膜招募是一个多步骤、协同的过程：(1) PI3P结合WIPI2/WIPI3；(2) WIPI3通过结合ATG13 IDR中的DHF基序，WIPI2通过结合ATG13 IDR中的W2IR基序，共同将ATG13:ATG101 HORMA二聚体招募到膜上；(3) ATG101的WF指和CTH直接插入膜，稳定复合物；(4) ULK1 IDR中的PVP基序与ATG13 HORMA结构域结合，将ULK1 KD拉近到膜表面，使其能够磷酸化膜结合底物(如ATG16L1)。
3.  **可能的普适教训 [Analysis]**: 长IDR不仅是连接子，其内部包含的多个短线性基序(SLiMs)可以介导多步骤、可调控的蛋白-蛋白和蛋白-膜互作，从而精确控制远端功能结构域(如激酶结构域)的空间定位和活性。这种“IDR介导的纳米级定位”机制可能广泛存在于其他信号通路中。

## 07 方法总览
- **输入**: 人源ULK1、FIP200、ATG13、ATG101、WIPI2、WIPI3、ATG16L1的序列信息；PI3P脂质。
- **输出**: ULK1C膜招募和激活的多步骤分子模型；关键互作基序(DHF, WF, PVP)的功能验证。
- **模块**:
    1.  **结构预测模块**: 使用AlphaFold2 (ColabFold) 预测ATG13:ATG101与WIPI3、ULK1 IDR与ATG13 HORMA的复合物结构。
    2.  **分子动力学(MD)模拟模块**: 使用GROMACS和CHARMM36m力场，模拟复合物在磷脂双分子层上的稳定性，验证关键残基的作用。
    3.  **体外生化重建模块**:
        - GUV结合实验: 观察ATG13:ATG101在WIPI3和PI3P存在下对GUV的招募。
        - 激酶活性测定: 在脂质体上重建ULK1C对ATG16L1的磷酸化，检测关键突变的影响。
    4.  **细胞功能验证模块**: 在ATG13或ATG101敲除细胞中回补野生型或突变体，通过Halo-LC3 flux、mito-QC、免疫印迹(p-ATG16L1)和免疫荧光(ULK1 puncta)检测自噬和线粒体自噬。
- **训练**: 不适用(AlphaFold2为预训练模型)。
- **工具**: AlphaFold2 (ColabFold), GROMACS, CHARMM-GUI, UCSF ChimeraX, Fiji, GraphPad Prism。
- **反馈回路**: MD模拟结果与生化实验(如突变体结合/活性)相互验证；细胞表型与体外重建结果一致。
- **假设**: AlphaFold2预测的复合物结构是可靠的；MD模拟的力场和膜模型能反映生理状态；体外重建条件能模拟体内环境。
- **文字流程**: 首先，通过序列比对和AlphaFold2预测，发现ATG13 IDR中的DHF基序与WIPI3互作，以及ULK1 IDR中的PVP基序与ATG13 HORMA互作。然后，通过GUV结合实验和MD模拟验证ATG13:ATG101-WIPI3复合物在膜上的协同锚定，并证明ATG101 WF指和CTH直接插入膜。接着，在体外重建ULK1C对膜结合底物ATG16L1的磷酸化，证明WIPI2、WIPI3、DHF基序和WF指对激酶活性至关重要。最后，在细胞中验证这些互作对自噬和线粒体自噬的必要性，并证明PVP基序对ULK1 puncta形成、底物磷酸化和自噬功能至关重要。

## 08 核心模块拆解
| 模块 | 功能 | 为何需要 | 输入输出 | 支撑证据 | 移除后的已知或预期影响 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **AlphaFold2结构预测** | 预测ATG13:ATG101与WIPI3、ULK1 IDR与ATG13 HORMA的复合物结构。 | 为实验提供结构假说，指导突变设计。 | 输入: 蛋白序列；输出: 预测的复合物三维结构。 | 500次AlphaFold2运行显示高收敛性(97%模型属于同一簇)；MD模拟验证了预测界面的稳定性。 | 无法获得初始的结构假说，实验设计将缺乏针对性。 |
| **分子动力学(MD)模拟** | 模拟复合物在膜上的动态行为，验证关键残基(如WF指、DHF基序)对膜结合和复合物稳定性的贡献。 | 提供原子级别的动态证据，补充静态结构预测和生化实验。 | 输入: AlphaFold2预测结构、膜模型；输出: 轨迹、RMSD、距离等分析。 | 模拟显示WF指突变导致膜锚定丧失和复合物界面扰动；DHF基序与WIPI3的互作稳定。 | 对突变效应的理解停留在生化层面，缺乏动态和结构基础。 |
| **体外生化重建(激酶活性)** | 在脂质体上重建ULK1C对ATG16L1的磷酸化，直接检验膜招募和KD定位机制对激酶活性的影响。 | 在受控环境中直接证明分子机制的功能后果。 | 输入: 纯化蛋白、脂质体、ATP；输出: ATG16L1磷酸化水平。 | 去除WIPI2/WIPI3或突变DHF/WF/ADA均显著降低磷酸化。 | 无法将分子互作与激酶活性直接关联，结论停留在结合层面。 |
| **细胞功能验证(自噬/线粒体自噬)** | 在细胞水平验证关键互作对自噬和线粒体自噬的必要性。 | 确认体外发现的生理相关性。 | 输入: 敲除细胞系、回补质粒；输出: LC3 flux、mito-QC、p-ATG16L1水平、ULK1 puncta。 | ATG13(HF|DD)和ULK1(ADA)突变体均显著降低自噬和线粒体自噬通量。 | 无法确定体外发现的机制在复杂细胞环境中的重要性。 |

## 09 关键公式符号
不适用。本文未使用需要公式推导的数学模型。

## 10 实验设计与证据链
- **数据集/群体**: 纯化蛋白(HEK293F GnTi细胞表达)、GUV/脂质体、HeLa/ARPE-19/MEF细胞系(WT, KO, 回补)。
- **规模**: 每组实验至少3次生物学重复。
- **指标**: 荧光强度(GUV结合)、磷酸化信号(激酶活性)、LC3 flux、mito-QC(红/绿 puncta比率)、ULK1 puncta数量、免疫共沉淀信号。
- **基线**: WT蛋白/细胞；阴性对照: 空载体、GST alone、无脂质体/无WIPI条件。
- **骨干/仪器**: 共聚焦显微镜(Nikon A1, Ti2-E)、流式细胞仪(LSRFortessa)、凝胶成像系统。
- **oracle 输入**: 不适用。
- **评测协议**: 统计显著性通过one-way/two-way ANOVA或Student's t检验确定。

| 实验 | 检验的claim | 对比与条件 | 结果 | 支持的结论 | 不支持更强的结论 | 来源 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| GUV结合实验 | ATG101 WF指和CTH介导膜结合。 | WT vs. ATG101(WF|DD), ATG101ΔCTH, 双突变体，在WIPI3和PI3P存在下。 | WF|DD突变体膜结合显著降低，CTH缺失也有缺陷，双突变体与WF|DD类似。 | ATG101 WF指是膜结合的主要贡献者，CTH有辅助作用。 | 不能排除WF指和CTH通过影响蛋白构象间接影响膜结合。 | Results 图2 |
| 体外激酶活性测定 | WIPI2, WIPI3, DHF基序, WF指对ULK1活性至关重要。 | 去除WIPI2或WIPI3 vs. 全组分；ATG13(HF|DD) vs. WT；ATG101(WF|DD) vs. WT。 | 去除任一WIPI或突变DHF/WF均显著降低ATG16L1磷酸化。 | 协同膜招募是ULK1活性的必要条件。 | 不能排除这些突变影响ULK1C组装或底物结合。 | Results 图4 |
| 细胞自噬通量(Halo-LC3) | ATG13-WIPI3互作对自噬重要。 | ATG13 KO + Halo-LC3 回补 WT vs. ATG13(HF|DD)。 | HF|DD突变体自噬通量显著低于WT。 | ATG13-WIPI3互作对自噬至关重要。 | 不能排除HF|DD突变影响其他ATG13功能。 | Results 图4 |
| 细胞线粒体自噬(mito-QC) | ULK1-ATG13 HORMA互作对线粒体自噬重要。 | ULK1 KO + mito-QC 回补 WT vs. ULK1(ADA)。 | ADA突变体线粒体自噬显著低于WT。 | ULK1-ATG13 HORMA互作对线粒体自噬至关重要。 | 不能排除ADA突变影响ULK1稳定性或与其他蛋白互作。 | Results 图6 |

## 11 结论正确解读
- **任务范围**: 本文聚焦于ULK1C在自噬起始阶段的膜招募和激酶定位机制，不涉及自噬后期事件或ULK1C的其他功能。
- **oracle/真值输入**: 结构预测依赖AlphaFold2，其准确性受限于MSA质量和训练数据。MD模拟使用简化膜模型和力场。
- **端到端状态**: 从分子机制到细胞表型建立了完整的证据链，但未在动物模型中验证。
- **算力成本**: MD模拟需要大量计算资源，但未提供具体成本。
- **历史数据依赖**: 依赖于先前对ULK1C、WIPI、PI3P在自噬中作用的研究。
- **模型依赖**: 结论强烈依赖于AlphaFold2预测的结构模型和MD模拟结果。
- **最难情形**: 在WIPI3 KO细胞中，自噬表型存在争议(文中提及)，本文未完全解决此矛盾。
- **群体/领域边界**: 结论基于人源蛋白和细胞系，在其它物种中的普适性未知。
- **不确定性**: 虽然证据充分，但无法完全排除其他未知的互作或调控机制参与ULK1C的膜招募。
- **有边界的复述**: 在人源细胞和体外重建系统中，ULK1C通过WIPI2/WIPI3与ATG13 IDR的互作、ATG101 WF指的膜插入，以及ULK1 IDR的PVP基序与ATG13 HORMA的互作，实现多步骤、协同的膜锚定和激酶结构域定位，这对自噬和线粒体自噬至关重要。

## 12 作者自认局限
| 局限 | 具体表现 | 作者提出的未来方向 | 来源 |
| :--- | :--- | :--- | :--- |
| WIPI3在自噬中的作用存在争议 | WIPI3 KO在HEK293细胞中对饥饿诱导的自噬通量无影响，与本文和其他研究矛盾。 | 需要进一步研究。 | Discussion节: "WIPI3 KO by CRISPR was found to have no effect on starvation-induced autophagy flux in human embryonic kidney (HEK) 293 cells. The reason for this difference is unclear and will require further study." |
| 其他膜招募机制的相互作用 | ULK1C的膜招募可能还涉及与PI3KC3-C1的超级复合物、RAB1A、ATG8蛋白等。 | 需要进一步研究这些机制之间的相互作用。 | Discussion节: "The interplay between these various mechanisms will require further investigation." |

## 13 批判性分析
| [Analysis] 观察 | 潜在问题或替代解释 | 为何重要 | 如何检验 | 依据 |
| :--- | :--- | :--- | :--- | :--- |
| AlphaFold2预测的ATG13-WIPI3和ULK1-ATG13 HORMA互作界面高度依赖保守残基，但未在非保守残基上进行系统突变扫描。 | 可能存在其他未被AlphaFold2预测到的、更动态或条件依赖的互作界面。 | 过度依赖单一预测模型可能遗漏重要的调控机制。 | 对ATG13 IDR和ULK1 IDR进行丙氨酸扫描，结合交联质谱或NMR，系统性地鉴定所有可能的互作界面。 | 文中仅对预测的保守基序(DHF, PVP)进行了突变验证。 |
| 体外激酶活性测定中，ULK1C浓度(3 nM)远低于生理浓度，且使用截短的底物(ATG16L1 78-300)。 | 高浓度下可能绕过某些调控步骤，或截短底物丢失了其他调控位点。 | 体外重建的定量结果可能无法直接外推到体内。 | 在更接近生理浓度的条件下重复实验，并使用全长ATG16L1作为底物。 | Methods节: "Reactions contained 3 nM ULK1+/-... 100 nM ATG16(78-300)". |
| MD模拟仅进行了1 μs，可能不足以捕捉到所有构象变化或脂质重排。 | 更长时间的模拟可能揭示复合物的动态解离或新的稳定状态。 | 对复合物稳定性的评估可能不完整。 | 进行多副本、更长时间(>10 μs)的MD模拟，或使用增强采样技术。 | Methods节: "production runs in the NPT ensemble for 1 μs." |
| 细胞实验主要依赖过表达系统，可能掩盖了内源蛋白水平的调控。 | 过表达可能导致非生理性的互作或表型。 | 结论的生理相关性需要内源水平的验证。 | 使用CRISPR敲入技术，在内源位点引入点突变，重复关键细胞实验。 | 文中使用KO细胞回补过表达质粒。 |

## 14 学到什么
**Agent 提炼的知识候选**

1.  **概念: IDR介导的多步骤膜锚定和激酶定位**
    - **可迁移性**: 本课题(IDP/IDR × 蛋白互作 × AI/物理模拟)可直接借鉴。许多信号通路中的激酶或效应蛋白通过长IDR与膜锚定部分连接，其活性可能受类似机制调控。
    - **如何迁移**: 在研究一个含IDR的蛋白X时，可假设其IDR包含多个SLiMs，分别介导与膜受体(如WIPI)和自身催化结构域(如激酶)的互作，从而调控其空间定位和活性。可使用AlphaFold2预测IDR与候选互作蛋白的复合物结构，并用MD模拟验证。

2.  **方法: AlphaFold2 + MD模拟 + 生化重建的闭环验证策略**
    - **可迁移性**: 这是研究IDP/IDR介导的蛋白互作和功能的标准范式。
    - **如何迁移**: 对于任何IDP/IDR介导的互作，可先用AlphaFold2预测复合物结构，然后用MD模拟评估其稳定性和动态性，最后通过体外生化重建(如结合、活性测定)和细胞实验验证预测的关键残基和功能。

3.  **公式/概念: 纳米级定位的“体积缩小”效应**
    - **可迁移性**: 本文通过计算IDR结合前后KD可探索的体积变化(从~6×10^4 nm³缩小8倍)，量化了定位机制对局部浓度的贡献。这种量化思路可用于其他系统。
    - **如何迁移**: 在研究一个通过IDR连接远端功能结构域的蛋白时，可计算IDR与锚定点的结合如何限制功能结构域的构象空间，从而估算其局部浓度增加倍数，为理解其活性调控提供定量依据。

4.  **实验设计: 使用GUV和脂质体进行膜结合和激酶活性重建**
    - **可迁移性**: 这是研究膜相关蛋白互作和功能的强大工具。
    - **如何迁移**: 在研究IDP/IDR介导的膜招募时，可制备含特定脂质的GUV或脂质体，通过荧光标记观察蛋白招募，或通过添加底物和ATP重建下游反应(如磷酸化、泛素化)。

## 15 与已有知识连接
- **相似**: 与2023年发现WIPI2在BNIP3/NIX线粒体自噬中招募ULK1C的工作(参考文献27, 28)直接相关，本文将其扩展到一般自噬并揭示了更复杂的协同机制。
- **组合**: 本文发现的ULK1 IDR PVP基序与ATG13 HORMA互作，与先前发现的ULK1 EAT结构域棕榈酰化(参考文献45)共同作用，将ULK1C锚定在膜上。这展示了多种膜定位机制的协同。
- **冲突**: 本文明确反驳了早期认为ATG13 N端碱性残基簇直接结合PI3P的假说(参考文献26)，并通过更严格的实验证明其不成立。
- **可迁移领域**: 该机制可迁移到其他由PI3P信号调控的膜运输过程，如内吞体分选。WIPI蛋白的同源物(如酵母Atg18)也参与其他膜动力学过程。IDR介导的激酶定位机制可能普遍存在于受体酪氨酸激酶(RTK)信号、T细胞受体(TCR)信号等通路中。

## 16 研究想法
**Agent 生成的研究候选**

1.  **名称**: 探索IDR介导的激酶定位机制在T细胞受体(TCR)信号通路中的普适性。
    - **来源局限/观察**: 本文发现ULK1通过IDR中的PVP基序与ATG13 HORMA互作，将激酶KD定位到膜附近。TCR信号中，关键激酶如ZAP-70和Lck也通过长IDR与膜锚定蛋白(如LAT, CD4/CD8)连接。
    - **核心假设**: ZAP-70或Lck的IDR中也存在与膜近端支架蛋白(如LAT)互作的SLiMs，这些互作对于将激酶KD定位到TCR微簇附近并磷酸化底物至关重要。
    - **相对本文的增量**: 将IDR介导的激酶定位机制从自噬领域扩展到免疫信号领域，验证其作为通用调控原理的潜力。
    - **初步方法**: 1) 使用AlphaFold2预测ZAP-70/Lck的IDR与LAT等膜近端蛋白的互作。2) 通过交联质谱或NMR验证预测的互作界面。3) 在T细胞系中敲入突变，通过磷酸化流式或免疫荧光检测TCR信号强度和微簇形成。
    - **验证方式**: 突变体应导致ZAP-70/Lck的膜定位减弱、底物(如LAT, SLP-76)磷酸化降低、以及T细胞活化受损。
    - **可能的失败模式**: ZAP-70/Lck的IDR可能缺乏与LAT的直接互作，其定位主要依赖其他机制(如SH2结构域与磷酸化ITAM的结合)。AlphaFold2预测可能不准确。
    - **创新状态**: unverified。

2.  **名称**: 开发基于AlphaFold2和MD模拟的IDR SLiM预测和验证流程。
    - **来源局限/观察**: 本文手动识别了DHF和PVP基序，但IDR中可能存在更多未被发现的、功能重要的SLiMs。现有SLiM预测工具(如ELM)假阳性率高。
    - **核心假设**: 结合AlphaFold2的高精度结构预测和MD模拟的稳定性评估，可以显著提高对IDR中功能性SLiMs的预测准确性。
    - **相对本文的增量**: 提供一个系统性的、可推广的计算流程，用于发现和验证IDR中的SLiMs，而不仅限于单个案例。
    - **初步方法**: 1) 收集已知的IDR SLiM-折叠蛋白互作对作为训练/测试集。2) 开发一个流程: a) 使用AlphaFold2批量预测IDR片段与候选折叠蛋白的互作；b) 对高置信度预测进行短MD模拟(如100 ns)评估界面稳定性；c) 基于界面能和RMSD筛选候选SLiMs。3) 在已知的IDP/IDR(如p53, BRCA1)上测试流程的召回率和精确率。
    - **验证方式**: 流程预测的SLiMs应显著富集已知功能位点，并能预测出新的、可被实验验证的SLiMs。
    - **可能的失败模式**: AlphaFold2对IDR-折叠蛋白互作的预测精度可能不足以区分真实互作和假阳性。MD模拟的计算成本可能过高。
    - **创新状态**: unverified。