# PROMETHEUS DYNAMICS // AMAZON BRAKET SCOPED EXPERIMENT PACKAGE
**Prepared for:** Michael Brett, Head of Go-To-Market for Quantum Technologies, AWS (`brettaws@amazon.com`)  
**Prepared by:** William Denyer, Founder, Prometheus Dynamics (`william@prometheusdynamics.ca`)  
**Date:** October 19, 2026  

---

## 1. Executive Summary & Multi-Cloud Live QPU Corpus (`121` Completed 3-Way Hardware Jobs / `363` Compiled Circuits / `5.09M` Shots)

We have compiled and executed a reproducible multi-cloud hardware benchmark corpus across **six physical quantum processors** spanning **Amazon Braket (`Rigetti Cepheus-1-108Q`, `IQM Garnet` 20Q, `IQM Emerald` 54Q)** and **IBM Quantum (`ibm_marrakesh`, `ibm_fez`, `ibm_kingston` 156Q Heron)**, alongside **NVIDIA H100 hybrid solvers (`VeloxQH100_1`)** and the **Amazon Braket SDK (`LocalSimulator`)**:

- **14 Completed 3-Way `ProgramSet` Tasks on Live Amazon Braket QPUs (`42` Verbatim Compiled Circuits, `125,952` Completed Quantum Shots, [`aws_braket_qpu_14_jobs_ledger.json`](./aws_braket_qpu_14_jobs_ledger.json)):** Executed directly on **Rigetti `Cepheus-1-108Q` (`108Q` / `107` active qubits, `us-west-1`)**, **IQM `Garnet` (`20Q`, `eu-north-1`)**, and **IQM `Emerald` (`54Q`, `eu-north-1`)** using OpenQASM 3.0 `#pragma braket verbatim` `ProgramSet` bundles so `Qiskit SABRE O3`, `Quantinuum TKET`, and `Prometheus` execute inside the exact same Amazon Braket QuantumTask:
  - **100% Structural Reduction Rate (`14 / 14` Live Braket Tasks):** Simultaneous reduction in both compiled circuit depth and two-qubit `CZ` gate count across every job (`up to -54.0% depth` and `-32.5% 2Q gates` vs. `SABRE O3`; `up to -51.9% depth` and `-37.8% 2Q gates` vs. `TKET`).
  - **Physical Hardware Observable Gains (`4Q` to `10Q` In-Coherence Regime):** Achieved higher computational-basis distribution fidelity than `SABRE O3` on **`9 / 11` (`81.8%`)** in-coherence benchmarks (`8 / 8` / `100%` on `Dense All-to-All`, `QFT`, and `10Q QAOA`), highlighted by **`+379.42%` (`4.79x`) distribution fidelity and `9.03x` XEB on Rigetti `Cepheus-1-108Q` (`9Q Dense All-to-All`)**, **`+116.13%` (`2.16x`) distribution fidelity and `11.37x` XEB on Rigetti `Cepheus-1-108Q` (`6Q Dense All-to-All`)**, **`+14.92%` distribution fidelity and `-52.6%` TVD reduction on IQM `Emerald` (`6Q QFT`)**, and **`+9.39%` distribution fidelity and `+43.1%` XEB on IQM `Garnet` (`9Q Dense All-to-All`)**. All 14 Task ARNs (including shallow 4Q/7Q QAOA ties and 17Q coherence-horizon probes) are published in [`aws_braket_qpu_14_jobs_ledger.json`](./aws_braket_qpu_14_jobs_ledger.json).
- **107 Completed 3-Way Jobs on 156-Qubit IBM Quantum Processors (`321` Physical Compiled Circuits, `4,964,352` Completed Quantum Shots, [`ibm_heron_156q_verified_benchmarks.json`](./ibm_heron_156q_verified_benchmarks.json)):** Head-to-head physical executions (`SABRE O3` vs. `Quantinuum TKET` vs. `Prometheus`) using **4- to 23-qubit circuits** (`out of 110 historical queue dispatches / 5,111,808 dispatched shots`). Achieved higher computational-basis distribution fidelity than **Quantinuum `TKET` on `100 / 107` (`93.5%`)** and **IBM `SABRE O3` on `80 / 107` (`74.8%`)** completed hardware triplets (`all 27 cases where SABRE O3 outperformed Prometheus are retained in the public ledger`).
- **Supporting Hybrid Quantum-HPC Benchmarks on NVIDIA H100 (`VeloxQH100_1`, `4` to `1,029` QUBO Binary Variables):** Pre-execution problem compression reducing 72-variable industrial scheduling formulations by **`94.44%` (`72` to `4` binary variables)** for direct 4-qubit gate-QPU execution (`94.04%` to `96.34%` computational-basis distribution fidelity) and solving 45-operation (`1,029`-binary-variable) schedules to the `26h` target horizon in `5.26s` on NVIDIA H100.

### Table 1A - Live Amazon Braket QPU Benchmark Ledger (`Rigetti Cepheus-1-108Q`, `IQM Garnet`, `IQM Emerald`)

All 14 live Amazon Braket `ProgramSet` executions (`42` verbatim circuits, `125,952` shots) are archived in [`aws_braket_qpu_14_jobs_ledger.json`](./aws_braket_qpu_14_jobs_ledger.json):

| Amazon Braket QPU | Workload & Width | Shots / Circuit | Depth (`S / T /` **`P`**) | 2Q `CZ` (`S / T /` **`P`**) | Distribution Fidelity (`SABRE / TKET ->` **`Prometheus`**) | TVD (`SABRE / TKET ->` **`Prometheus`**) | Verifiable Amazon Braket Task ARN |
| :--- | :--- | :-: | :-: | :-: | :--- | :--- | :--- |
| **Rigetti `Cepheus-1-108Q`** | **Dense All-to-All (`9Q`)** | `1,024` | `137 / 131 /` **`63`** (`-54.0%`) | `80 / 83 /` **`54`** (`-32.5%`) | `0.0435 / 0.0211 ->` **`0.2088` (`+379.42%` vs S, `+887.34%` vs T; XEB `14.92` vs `1.65`)** | `0.9329 / 0.9515 ->` **`0.7966`** | `arn:aws:braket:us-west-1:893688540163:quantum-task/2df64966-8b30-4e19-a859-25efc2f2b136` |
| **Rigetti `Cepheus-1-108Q`** | **Dense All-to-All (`6Q`)** | `4,096` | `63 / 82 /` **`40`** (`-36.5%`) | `31 / 33 /` **`23`** (`-25.8%`) | `0.0880 / 0.0955 ->` **`0.1903` (`+116.13%` vs S, `+99.23%` vs T; XEB `2.29` vs `0.20`)** | `0.9000 / 0.9034 ->` **`0.8195`** | `arn:aws:braket:us-west-1:893688540163:quantum-task/02427b15-5597-4721-95e1-b3d2547aafb8` |
| **IQM `Emerald` (`54Q`)** | **Dense All-to-All (`6Q`)** | `4,096` | `57 / 56 /` **`41`** (`-28.1%`) | `28 / 33 /` **`23`** (`-17.9%`) | `0.7322 / 0.5931 ->` **`0.7853` (`+7.25%` vs S, `+32.39%` vs T; XEB `15.71` vs `13.67`)** | `0.3266 / 0.4296 ->` **`0.2785`** | `arn:aws:braket:eu-north-1:893688540163:quantum-task/b5317346-c659-4c3e-bd10-0c84df2e74d5` |
| **IQM `Emerald` (`54Q`)** | **QFT (`6Q`)** | `4,096` | `88 / 89 /` **`64`** (`-27.3%`) | `44 / 48 /` **`38`** (`-13.6%`) | `0.8355 / 0.9648 ->` **`0.9602` (`+14.92%` vs S)** | `0.3425 / 0.1575 ->` **`0.1624` (`-52.6%` vs S)** | `arn:aws:braket:eu-north-1:893688540163:quantum-task/68dbffa0-f842-48c4-bdf5-c95d5a69036b` |
| **IQM `Garnet` (`20Q`)** | **Dense All-to-All (`9Q`)** | `1,024` | `130 / 129 /` **`103`** (`-20.8%`) | `79 / 87 /` **`70`** (`-11.4%`) | `0.5513 / 0.6211 ->` **`0.6031` (`+9.39%` vs S; XEB `5.71` vs `3.99`; HOP `0.7764` #1)** | `0.5341 / 0.4738 ->` **`0.4790`** | `arn:aws:braket:eu-north-1:893688540163:quantum-task/8a04e33b-e945-4ec7-b7da-2801a644f610` |
| **Rigetti `Cepheus-1-108Q`** | **QAOA MaxCut (`10Q`)** | `4,096` | `66 / 91 /` **`47`** (`-28.8%`) | `30 / 45 /` **`28`** (`-6.7%`) | `0.7783 / 0.8268 ->` **`0.8364` (`+7.46%` vs S, `+1.16%` vs T; 3-Way Winner)** | `0.3413 / 0.2979 ->` **`0.2783`** | `arn:aws:braket:us-west-1:893688540163:quantum-task/6c662e9c-d64e-41b9-b7a2-bb10477e073f` |
| **Rigetti `Cepheus-1-108Q`** | **QFT (`8Q`)** | `4,096` | `181 / 261 /` **`129`** (`-28.7%`) | `82 / 95 /` **`70`** (`-14.6%`) | `0.9329 / 0.9528 ->` **`0.9664` (`+3.58%` vs S, `+1.43%` vs T; 3-Way Winner)** | `0.2039 / 0.1721 ->` **`0.1467` (`-28.1%` vs S)** | `arn:aws:braket:us-west-1:893688540163:quantum-task/eeee4e59-68e5-4ad0-b1fb-8b71dbd6638b` |
| **IQM `Garnet` (`20Q`)** | **Dense All-to-All (`4Q`)** | `4,096` | `25 / 26 /` **`22`** (`-12.0%`) | `12 / 12 /` **`8`** (`-33.3%`) | `0.9612 / 0.9430 ->` **`0.9685` (`+0.76%` vs S, `+2.70%` vs T; 3-Way Winner)** | `0.0769 / 0.1653 ->` **`0.0676`** | `arn:aws:braket:eu-north-1:893688540163:quantum-task/8875ef13-5943-4401-9c79-b2abb37e91f8` |
| **IQM `Garnet` (`20Q`)** | **QFT (`4Q`)** | `4,096` | `50 / 48 /` **`37`** (`-26.0%`) | `18 / 21 /` **`14`** (`-22.2%`) | `0.9791 / 0.9953 ->` **`0.9836` (`+0.46%` vs S)** | `0.1338 / 0.0527 ->` **`0.1030` (`-23.0%` vs S)** | `arn:aws:braket:eu-north-1:893688540163:quantum-task/904c6e83-0279-417f-a91c-080316c73ef0` |
| **IQM `Garnet` (`20Q`)** | **QAOA MaxCut (`4Q`)** | `4,096` | `21 / 23 /` **`19`** (`-9.5%`) | `9 / 9 /` **`7`** (`-22.2%`) | `0.9967 / 0.9959 -> 0.9944` (`-0.23%` vs S; shallow 4Q tie at `>99.4%`) | `0.0461 / 0.0520 -> 0.0574` | `arn:aws:braket:eu-north-1:893688540163:quantum-task/7e3ad9a8-6038-4e5e-bf89-0b86bc425fe5` |
| **IQM `Emerald` (`54Q`)** | **QAOA MaxCut (`7Q`)** | `4,096` | `36 / 47 /` **`34`** (`-5.6%`) | `19 / 22 /` **`17`** (`-10.5%`) | `0.9719 / 0.9802 -> 0.9585` (`-1.38%` vs S) | `0.1316 / 0.1123 -> 0.1621` | `arn:aws:braket:eu-north-1:893688540163:quantum-task/89cebd67-b2a4-460c-80a8-41e47b2a3d01` |
| **Rigetti `Cepheus-1-108Q`** | **Dense All-to-All (`9Q` Pre-Patch)** | `1,024` | `125 / 131 /` **`87`** (`-30.4%`) | `76 / 83 /` **`69`** (`-9.2%`) | `0.2704 / 0.2233 -> 0.2362` (`+5.74%` vs T; **`HOP: 0.6260` #1 vs `0.5791` S & `0.5332` T**) | `0.7389 / 0.7717 -> 0.7710` | `arn:aws:braket:us-west-1:893688540163:quantum-task/f337ec8e-9348-4414-8a8d-10f2ed333d07` |
| **IQM `Garnet` (`20Q`)** | **Dense All-to-All (`17Q` Probe)** | `1,024` | `299 / 447 /` **`278`** (`-7.0%`) | `310 / 425 /` **`301`** (`-2.9%`) | `0.0005 / 0.0000 -> 0.0003` (`+679.38%` vs T; beyond chip $T_2$ horizon) | `0.9900 / 0.9984 -> 0.9926` | `arn:aws:braket:eu-north-1:893688540163:quantum-task/fe63dc72-97dc-4041-b8f4-f1f80a5ba92e` |
| **Rigetti `Cepheus-1-108Q`** | **Dense All-to-All (`17Q` Probe)** | `1,024` | `382 / 508 /` **`120`** (`-68.6%`) | `331 / 432 /` **`204`** (`-38.4%`) | `0.0003 / 0.0001 -> 0.0002` (`+122.32%` vs T; **`HOP: 0.5244` #1**; beyond chip $T_2$ horizon) | `0.9925 / 0.9968 -> 0.9956` | `arn:aws:braket:us-west-1:893688540163:quantum-task/58b458c9-a1b7-4303-8345-ddc33b3d2254` |

### Table 1B - Representative Highlights from the 107-Job (`4.96M-Shot`) 156Q IBM Heron Corpus

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

## 4. Checklist Status & Live Cloud UI Access

1. **AWS Skill Builder - Amazon Braket Knowledge Badge:** **COMPLETED & VERIFIED** - [https://www.credly.com/badges/b64dc9e8-8f3e-4996-8494-4acee97db732/public_url](https://www.credly.com/badges/b64dc9e8-8f3e-4996-8494-4acee97db732/public_url)
2. **Local Braket Simulator & Live Braket QPU Validation:** **COMPLETED & VERIFIED** across all 7 workloads on `braket.devices.LocalSimulator("default")` (`validate_braket_local.py`) **plus 14 live 3-way `ProgramSet` hardware executions (`42` compiled circuits, `125,952` shots)** on **Rigetti `Cepheus-1-108Q`**, **IQM `Garnet` (`20Q`)**, and **IQM `Emerald` (`54Q`)** archived in [`aws_braket_qpu_14_jobs_ledger.json`](./aws_braket_qpu_14_jobs_ledger.json).
3. **Scoped QPU Cost Estimate:** **COMPLETED** (**`$298.08 USD` initial core request** for the 4-workload 8Q/12Q multi-window replication suite, plus **`$223.56 USD` optional extension** totaling `$521.64 USD`).
4. **AWS Account ID:** `893688540163`
5. **Interactive Cloud UI Evaluation (`https://prometheusdynamics.ca/QuantumCompiler/`):** Available during supervised live evaluation sessions for AWS Braket technical reviewers to dispatch custom OpenQASM 2.0/3.0 workloads directly to live Amazon Braket QPUs and inspect 3-way compilation (`SABRE O3` vs. `TKET` vs. `Prometheus`) in real time.

