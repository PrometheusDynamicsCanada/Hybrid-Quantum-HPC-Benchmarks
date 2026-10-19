# PROMETHEUS DYNAMICS // AMAZON BRAKET SCOPED EXPERIMENT PACKAGE
**Prepared for:** Michael Brett, Head of Go-To-Market for Quantum Technologies, AWS (`brettaws@amazon.com`)  
**Prepared by:** William Denyer, Founder, Prometheus Dynamics (`william@prometheusdynamics.ca`)  
**Date:** October 19, 2026  

---

## 1. Executive Summary & Live Hardware Corpus (`107` Completed QPU Jobs / `321` Compiled Circuits / `4.96M` Shots)

We have compiled and executed a reproducible hardware benchmark corpus across **three 156-qubit IBM Heron superconducting processors (`ibm_marrakesh`, `ibm_fez`, `ibm_kingston`)**, **NVIDIA H100 hybrid solvers (`VeloxQH100_1`)**, and the **Amazon Braket SDK (`LocalSimulator`)**:

- **107 Completed 3-Way Jobs on 156-Qubit IBM Quantum Processors (`321` Physical Compiled Circuits, `4,964,352` Completed Quantum Shots; out of `110` historical queue dispatches / `5,111,808` dispatched shots):** Head-to-head physical executions (`SABRE O3` vs. `Quantinuum TKET` vs. `Prometheus`) using **4- to 23-qubit circuits** across `Dense All-to-All ($K_N$)`, `3-Regular QAOA MaxCut`, `Quantum Fourier Transform (QFT)`, `Quantum Volume (Random SU4)`, and `Star Graph` topologies. All three compilers execute within the same hardware job to reduce exposure to calibration drift.
- **Corpus-Wide Physical Hardware Win Rate (`107` Completed 3-Way Hardware Triplets, Measured by Higher Computational-Basis Distribution Fidelity):**
  - **vs. Quantinuum `TKET`:** Achieved higher computational-basis distribution fidelity than `TKET` on **100 out of 107 live QPU benchmarks (`93.5%` win rate)**, cutting two-qubit gate counts by up to **`-54.5%`**.
  - **vs. IBM Qiskit `SABRE O3`:** Achieved higher computational-basis distribution fidelity than `SABRE O3` on **80 out of 107 live QPU benchmarks (`74.8%` win rate)**, cutting two-qubit gate counts by up to **`-34.8%`** and circuit depth by up to **`-38.8%`**. All `27 / 107` cases where `SABRE O3` outperformed Prometheus are retained in the public ledger.
- **Supporting Hybrid Quantum-HPC Benchmarks on NVIDIA H100 (`VeloxQH100_1`, `4` to `1,029` QUBO Binary Variables):** Pre-execution problem compression reducing 72-variable industrial scheduling formulations by **`94.44%` (`72` to `4` binary variables)** for direct 4-qubit gate-QPU execution (`94.04%` to `96.34%` computational-basis distribution fidelity) and solving 45-operation (`1,029`-binary-variable) schedules to the `26h` target horizon in `5.26s` on NVIDIA H100.

### Table 1A - Representative Highlights from the 107-Job (`4.96M-Shot`) 156Q Hardware Corpus

| Target Processor | Live Job ID | Workload & Scale | Circuit Depth (`SABRE` / `TKET` / **`Prometheus`**) | 2Q Gates (`SABRE` / `TKET` / **`Prometheus`**) | Computational-Basis Distribution Fidelity (`F_dist`) & HOP / XEB (`SABRE` / `TKET` -> **`Prometheus`**) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`ibm_kingston`** *(156Q)* | `dbajlrhgv2cc73e6vuj0` | **19Q Dense All-to-All ($K_{19}$)** | `358` / `501` / **`281` (`-21.5%`)** | `444` / `717` / **`358` (`-19.4%`)** | `18.98%` / `1.62%` -> **`24.26%` (`70.45%` HOP vs `63.28%` SABRE & `54.38%` TKET)** |
| **`ibm_marrakesh`** *(156Q)* | `dbajlqpgv2cc73e6vuhg` | **19Q Dense All-to-All ($K_{19}$)** | `459` / `501` / **`281` (`-38.8%`)** | `482` / `717` / **`358` (`-25.7%`)** | `6.27%` / `3.26%` -> **`12.78%` (XEB `339.8` vs `148.6` SABRE)** |
| **`ibm_fez`** *(156Q)* | `dbajlrhgv2cc73e6vuig` | **19Q Dense All-to-All ($K_{19}$)** | `414` / `501` / **`313` (`-24.4%`)** | `429` / `717` / **`390` (`-9.1%`)** | `3.57%` / `2.20%` -> **`6.54%` (XEB `208.5` vs `126.9` SABRE)** |
| **`ibm_kingston`** *(156Q)* | `dagv039hvn6c73cr72jg` | **18Q Dense All-to-All ($K_{18}$)** | `315` / `451` / **`248` (`-21.3%`)** | `387` / `632` / **`312` (`-19.4%`)** | `23.14%` / `2.08%` -> **`31.17%`** |
| **`ibm_kingston`** *(156Q)* | `daguvj8mhr3c73e5ohe0` | **17Q Dense All-to-All ($K_{17}$)** | `284` / `412` / **`221` (`-22.2%`)** | `341` / `558` / **`276` (`-19.1%`)** | `22.85%` / `2.94%` -> **`30.65%`** |
| **`ibm_fez`** *(156Q)* | `dbaign9gv2cc73e6u5sg` | **12Q QAOA MaxCut (3-Reg)** | `124` / `212` / **`115` (`-7.3%`)** | `58` / `108` / **`54` (`-6.9%`)** | `86.12%` / `88.35%` -> **`91.21%`** |
| **`ibm_marrakesh`** *(156Q)* | `dbaio50c77vs7382t5qg` | **12Q Quantum Fourier Transform** | `375` / `573` / **`329` (`-12.3%`)** | `236` / `375` / **`203` (`-14.0%`)** | `89.76%` / `79.18%` -> **`91.17%`** |
| **`ibm_marrakesh`** *(156Q)* | `dbaijj9gv2cc73e6ubmg` | **8Q Quantum Fourier Transform** | `226` / `288` / **`175` (`-22.6%`)** | `104` / `137` / **`85` (`-18.3%`)** | `98.62%` / `95.79%` -> **`99.29%`** |
| **`ibm_marrakesh`** *(156Q)* | `db9nfnfi0auc7390uvvg` | **4Q Compressed Schedule ($K_4$)** | `33` / `34` / **`27` (`-18.2%`)** | `42` / `42` / **`33` (`-21.4%`)** | `90.12%` / `91.85%` -> **`96.34%`** |

---

## 2. Amazon Braket `LocalSimulator` Verification (`validate_braket_local.py`)

We verified all seven proposed logical workloads using the official **`amazon-braket-sdk` (`LocalSimulator("default")`)** at both `shots=0` (exact probability distribution equivalence against Qiskit Statevector) and **`shots=4096`** (empirical 4,096-shot sampling execution), and archived the compiled structural benchmarks (`braket_local_validation_results.json`) across the native square-lattice topologies of **Rigetti Cepheus (`108Q`)** and **IQM Garnet (`20Q`)**:

1. **Initial Phase 1A Core Suite (`8Q` & `12Q`):** **3-Regular QAOA MaxCut** (`QAOA_MaxCut_8Q`, `QAOA_MaxCut_12Q`) and **Quantum Fourier Transform** (`QFT_8Q`, `QFT_12Q`).
2. **Optional High-Width All-to-All Extension (`17Q`, `18Q`, `19Q`):** **Dense All-to-All ($K_{17}, K_{18}, K_{19}$)** (`Dense_AllToAll_17Q`, `Dense_AllToAll_18Q`, `Dense_AllToAll_19Q`), testing deep non-local routing near the 20-qubit capacity boundary of IQM Garnet and across the multi-chip square lattice of Rigetti Cepheus.

### Table 2A - Verified Amazon Braket `LocalSimulator` & Structural Benchmark (`4,096 Shots/Circuit`)

| Target Braket QPU Topology | Algorithm & Scale | Braket `LocalSimulator` (`4,096` Shots) | Circuit Depth (`SABRE` / `TKET` / **`Prometheus`**) | 2Q Gates (`SABRE` / `TKET` / **`Prometheus`**) | Simulated Distribution Fidelity (`SABRE` / `TKET` -> **`Prometheus`**) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Rigetti Cepheus** *(108Q Grid)* | `QAOA_MaxCut_8Q` | `PASS (1.000000)` | `180` / `254` / **`156`** | `74` / `105` / **`77` (`-26.7%` vs TKET)** | `0.7900` / `0.8871` -> **`0.9253`** |
| **Rigetti Cepheus** *(108Q Grid)* | `QAOA_MaxCut_12Q` | `PASS (1.000000)` | `261` / `398` / **`248`** | `106` / `168` / **`97` (`-8.5%` vs S, `-42.3%` vs T)** | `0.4375` / `0.5001` -> **`0.6014`** |
| **Rigetti Cepheus** *(108Q Grid)* | `QFT_8Q` | `PASS (1.000000)` | `163` / `197` / **`151`** | `54` / `57` / **`53` (`-1.9%` vs S, `-7.0%` vs T)** | `0.6932` / `0.9028` -> **`0.9396`** |
| **Rigetti Cepheus** *(108Q Grid)* | `QFT_12Q` | `PASS (1.000000)` | `247` / `347` / **`261`** | `92` / `117` / **`93` (`-20.5%` vs TKET)** | `0.3393` / `0.5396` -> **`0.6176`** |
| **Rigetti Cepheus** *(108Q Grid)* | `Dense_AllToAll_17Q` *(Opt.)* | `PASS (1.000000)` | `182` / `250` / **`129` (`-29.1%`)** | `145` / `165` / **`125` (`-13.8%` vs S, `-24.2%` vs T)** | `0.0332` / `0.1536` -> **`0.2718`** |
| **Rigetti Cepheus** *(108Q Grid)* | `Dense_AllToAll_18Q` *(Opt.)* | `PASS (1.000000)` | `132` / `338` / **`113` (`-14.4%`)** | `149` / `240` / **`131` (`-12.1%` vs S, `-45.4%` vs T)** | `0.0124` / `0.0508` -> **`0.2200`** |
| **Rigetti Cepheus** *(108Q Grid)* | `Dense_AllToAll_19Q` *(Opt.)* | `PASS (1.000000)` | `167` / `258` / **`154` (`-7.8%`)** | `182` / `219` / **`169` (`-7.1%` vs S, `-22.8%` vs T)** | `0.0129` / `0.0787` -> **`0.1434`** |
| **IQM Garnet** *(20Q Crystal)* | `QAOA_MaxCut_8Q` | `PASS (1.000000)` | `190` / `239` / **`185`** | `75` / `105` / **`75` (`-28.6%` vs TKET)** | `0.8696` / `0.8153` -> **`0.9117`** |
| **IQM Garnet** *(20Q Crystal)* | `QAOA_MaxCut_12Q` | `PASS (1.000000)` | `272` / `393` / **`250`** | `105` / `132` / **`104` (`-1.0%` vs S, `-21.2%` vs T)** | `0.4825` / `0.4774` -> **`0.5800`** |
| **IQM Garnet** *(20Q Crystal)* | `QFT_8Q` | `PASS (1.000000)` | `165` / `204` / **`165`** | `55` / `57` / **`50` (`-9.1%` vs S, `-12.3%` vs T)** | `0.8467` / `0.8208` -> **`0.9290`** |
| **IQM Garnet** *(20Q Crystal)* | `QFT_12Q` | `PASS (1.000000)` | `276` / `365` / **`231` (`-16.3%`)** | `97` / `114` / **`89` (`-8.2%` vs S, `-21.9%` vs T)** | `0.4629` / `0.4096` -> **`0.5560`** |
| **IQM Garnet** *(20Q Crystal)* | `Dense_AllToAll_17Q` *(Opt.)* | `PASS (1.000000)` | `175` / `262` / **`151` (`-13.7%`)** | `135` / `204` / **`131` (`-3.0%` vs S, `-35.8%` vs T)** | `0.0500` / `0.0142` -> **`0.2012`** |
| **IQM Garnet** *(20Q Crystal)* | `Dense_AllToAll_18Q` *(Opt.)* | `PASS (1.000000)` | `184` / `263` / **`222`** | `159` / `207` / **`163` (`-21.3%` vs TKET)** | `0.0215` / `0.0081` -> **`0.1370`** |
| **IQM Garnet** *(20Q Crystal)* | `Dense_AllToAll_19Q` *(Opt.)* | `PASS (1.000000)` | `169` / `321` / **`166`** | `169` / `276` / **`169` (`-38.8%` vs TKET)** | `0.0476` / `0.0041` -> **`0.0801`** |

---

## 3. Scoped Phase 1A QPU Cost Estimate (`aws.amazon.com/braket/pricing/`)

Per official Amazon Braket on-demand QPU pricing (`$0.30 / task`, **`$0.000425 / shot` for Rigetti Cepheus**, and **`$0.00145 / shot` for IQM Garnet**; excluding ancillary AWS charges):

- **Initial Request - Phase 1A Core Suite (4 Workloads):** `QAOA MaxCut (3-Regular)` and `QFT` at `8Q` and `12Q` $\times$ `3` compilers (`SABRE O3`, `TKET`, `Prometheus`) $\times$ `3` execution windows = **`36 tasks` (`147,456 shots`) per QPU** = **`72 tasks` (`294,912 shots`) total** = **`$298.08 USD`** across Rigetti Cepheus and IQM Garnet.
- **Optional High-Width All-to-All Extension (+3 Workloads):** `17Q`, `18Q`, and `19Q` `Dense All-to-All` ($K_{17}, K_{18}, K_{19}$) $\times$ `3` compilers $\times$ `3` execution windows = **`+27 tasks` (`+110,592 shots`) per QPU** = **`+54 tasks` (`+221,184 shots`) total** = **`+$223.56 USD`** (`$521.64 USD` combined across all `126 tasks` / `516,096 shots` if the optional extension is included).

### Table 3A - Phase 1A QPU Cost Breakdown (Official On-Demand AWS Braket Pricing)

| Phase / Target QPU | Architecture | Workloads | Tasks (`Workloads x 3 Compilers x 3 Windows`) | Shots / Task | Total Shots | Task Fees (`$0.30/task`) | Shot Fees | Estimated QPU Charges (USD) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Rigetti Cepheus (Core 8Q & 12Q)** | 108Q Superconducting Square Grid | `4` (`8Q/12Q QAOA + QFT`) | `36 tasks` | `4,096` | `147,456` | `$10.80` | `$62.67` (`$0.000425/shot`) | **`$73.47`** |
| **IQM Garnet (Core 8Q & 12Q)** | 20Q Superconducting Crystal Grid | `4` (`8Q/12Q QAOA + QFT`) | `36 tasks` | `4,096` | `147,456` | `$10.80` | `$213.81` (`$0.00145/shot`) | **`$224.61`** |
| **Initial Request Total (Core 8Q & 12Q)** | **Rigetti Cepheus + IQM Garnet** | **`4 workloads`** | **`72 tasks`** | **`4,096`** | **`294,912`** | **`$21.60`** | **`$276.48`** | **`$298.08 USD`** |
| **Rigetti Cepheus (Optional 17Q-19Q $K_N$)** | 108Q Superconducting Square Grid | `3` (`17Q, 18Q, 19Q K_N`) | `27 tasks` | `4,096` | `110,592` | `$8.10` | `$47.00` (`$0.000425/shot`) | **`$55.10`** |
| **IQM Garnet (Optional 17Q-19Q $K_N$)** | 20Q Superconducting Crystal Grid | `3` (`17Q, 18Q, 19Q K_N`) | `27 tasks` | `4,096` | `110,592` | `$8.10` | `$160.36` (`$0.00145/shot`) | **`$168.46`** |
| **Optional Extension Subtotal (17Q-19Q)** | **Rigetti Cepheus + IQM Garnet** | **`3 workloads`** | **`54 tasks`** | **`4,096`** | **`221,184`** | **`$16.20`** | **`$207.36`** | **`$223.56 USD`** |
| **Combined Total (Core + Optional Ext.)** | **Rigetti Cepheus + IQM Garnet** | **`7 workloads (8Q to 19Q)`** | **`126 tasks`** | **`4,096`** | **`516,096`** | **`$37.80`** | **`$483.84`** | **`$521.64 USD`** |

*(Note: Optional Phase 2 cross-paradigm expansion to IonQ and QuEra Aquila is deferred until Phase 1A superconducting lattice benchmarks complete).*

---

## 4. Checklist Status for AWS Credit Provisioning

1. **AWS Skill Builder - Amazon Braket Knowledge Badge:** **COMPLETED & VERIFIED** - [https://www.credly.com/badges/b64dc9e8-8f3e-4996-8494-4acee97db732/public_url](https://www.credly.com/badges/b64dc9e8-8f3e-4996-8494-4acee97db732/public_url)
2. **Local Braket Simulator Validation (`validate_braket_local.py`):** **COMPLETED & VERIFIED** across all 7 workloads (`QAOA_MaxCut_8Q`, `QAOA_MaxCut_12Q`, `QFT_8Q`, `QFT_12Q`, plus the optional `Dense_AllToAll_17Q`, `Dense_AllToAll_18Q`, `Dense_AllToAll_19Q` extension) at both `shots=0` and `shots=4096` on `braket.devices.LocalSimulator("default")`, alongside archived 3-compiler structural benchmarks (`braket_local_validation_results.json`) for **Rigetti Cepheus (`108Q`)** and **IQM Garnet (`20Q`)**.
3. **Scoped QPU Cost Estimate:** **COMPLETED** (**`$298.08 USD` initial core request** for the 4-workload 8Q/12Q suite across `72 tasks` / `294,912 shots`, plus **`$223.56 USD` optional extension** for the 17Q-19Q Dense All-to-All sweep across `54 tasks` / `221,184 shots`, totaling `$521.64 USD` if both are included).
4. **AWS Account ID:** Provided directly in email correspondence.
