# PROMETHEUS DYNAMICS // AMAZON BRAKET SCOPED EXPERIMENT PACKAGE
**Prepared for:** Michael Brett, Head of Go-To-Market for Quantum Technologies, AWS (`brettaws@amazon.com`)  
**Prepared by:** William Denyer, Founder, Prometheus Dynamics (`william@prometheusdynamics.ca`)  
**Date:** October 19, 2026  

---

## 1. Executive Summary & Multi-Cloud Live QPU Corpus (`119` Completed 3-Way Hardware Jobs / `357` Compiled Circuits / `5.08M` Shots)

We have compiled and executed a reproducible multi-cloud hardware benchmark corpus across **six physical quantum processors** spanning **Amazon Braket (`Rigetti Cepheus-1-108Q`, `IQM Garnet` 20Q, `IQM Emerald` 54Q)** and **IBM Quantum (`ibm_marrakesh`, `ibm_fez`, `ibm_kingston` 156Q Heron)**, alongside **NVIDIA H100 hybrid solvers (`VeloxQH100_1`)** and verified cross-paradigm compilation for **Trapped-Ion (`AQT IBEX Q1` 12Q, `IonQ Forte 1` 36Q)** and **Neutral-Atom (`QuEra Aquila` 256Q)** on the **Amazon Braket SDK (`LocalSimulator`)**:

- **12 Completed 3-Way `ProgramSet` Performance Benchmark Tasks on Live Amazon Braket QPUs (`36` Verbatim Compiled Circuits, `119,808` Completed Quantum Shots, [`aws_braket_qpu_12_jobs_ledger.json`](./aws_braket_qpu_12_jobs_ledger.json)):** Executed directly on **Rigetti `Cepheus-1-108Q` (`108Q` / `107` active qubits, `us-west-1`)**, **IQM `Garnet` (`20Q`, `eu-north-1`)**, and **IQM `Emerald` (`54Q`, `eu-north-1`)** using OpenQASM 3.0 `#pragma braket verbatim` circuits submitted together in one Amazon Braket `ProgramSet` task per benchmark to reduce timing differences between comparisons (`Qiskit SABRE O3`, `Quantinuum TKET`, and `Prometheus`):
  - **100% Structural Reduction Rate (`12 / 12` Live Braket Benchmark Tasks):** Lower compiled circuit depth and lower two-qubit `CZ` gate count than both `SABRE O3` and `TKET` in every recorded comparison (`up to -54.0% depth` and `-33.3% 2Q gates` vs. `SABRE O3`; `up to -51.9% depth` and `-37.8% 2Q gates` vs. `TKET`).
  - **Physical Hardware Observable Outcomes (`9 / 12` Fidelity Wins vs. `SABRE O3`, `75.0%`):** Achieved higher computational-basis distribution fidelity than `SABRE O3` on **`9 / 12` (`75.0%`)** performance benchmark tasks (`3 / 3` on `QFT`, `5 / 6` on `Dense All-to-All`, and `1 / 3` on `QAOA MaxCut`), highlighted by **`+379.42%` (`4.79x`) distribution fidelity and `9.03x` XEB on Rigetti `Cepheus-1-108Q` (`9Q Dense All-to-All`)**, **`+116.13%` (`2.16x`) distribution fidelity and `11.37x` XEB on Rigetti `Cepheus-1-108Q` (`6Q Dense All-to-All`)**, **`+14.92%` distribution fidelity and `-52.6%` TVD reduction on IQM `Emerald` (`6Q QFT`)**, and **`+9.39%` distribution fidelity and `+43.1%` XEB on IQM `Garnet` (`9Q Dense All-to-All`)**. All 12 performance benchmark Task ARNs (including the 3 unfavorable outcomes on shallow 4Q/7Q QAOA and one 9Q Rigetti run) are published in [`aws_braket_qpu_12_jobs_ledger.json`](./aws_braket_qpu_12_jobs_ledger.json). *(Two initial `17Q` connectivity smoke tests executed during endpoint setup - `fe63dc72-97dc-4041-b8f4-f1f80a5ba92e` and `58b458c9-a1b7-4303-8345-ddc33b3d2254` - are noted separately in `README.md` for account traceability.)*
- **107 Completed 3-Way Jobs on 156-Qubit IBM Quantum Processors (`321` Physical Compiled Circuits, `4,964,352` Completed Quantum Shots, [`ibm_heron_156q_verified_benchmarks.json`](./ibm_heron_156q_verified_benchmarks.json)):** Head-to-head physical executions (`SABRE O3` vs. `Quantinuum TKET` vs. `Prometheus`) using **4- to 23-qubit circuits** (`out of 110 historical queue dispatches / 5,111,808 dispatched shots`). Achieved higher computational-basis distribution fidelity than **Quantinuum `TKET` on `100 / 107` (`93.5%`)** and **IBM `SABRE O3` on `80 / 107` (`74.8%`)** completed hardware triplets (`all 27 cases where SABRE O3 outperformed Prometheus are retained in the public ledger`).
- **Supporting Hybrid Quantum-HPC Benchmarks on NVIDIA H100 (`VeloxQH100_1`, `4` to `1,029` QUBO Binary Variables):** Pre-execution problem compression reducing 72-variable industrial scheduling formulations by **`94.44%` (`72` to `4` binary variables)** for direct 4-qubit gate-QPU execution (`94.04%` to `96.34%` computational-basis distribution fidelity) and solving 45-operation (`1,029`-binary-variable) schedules to the `26h` target horizon in `5.26s` on NVIDIA H100.

### Table 1A - Live Amazon Braket QPU Benchmark Ledger (`Rigetti Cepheus-1-108Q`, `IQM Garnet`, `IQM Emerald`)

All 12 live Amazon Braket `ProgramSet` executions (`36` verbatim circuits, `119,808` shots) are archived with AWS Task ARNs for traceability in [`aws_braket_qpu_12_jobs_ledger.json`](./aws_braket_qpu_12_jobs_ledger.json):

| Amazon Braket QPU | Workload & Width | Shots / Circuit | Depth (`S / T /` **`P`**) | 2Q `CZ` (`S / T /` **`P`**) | Distribution Fidelity (`SABRE / TKET ->` **`Prometheus`**) | TVD (`SABRE / TKET ->` **`Prometheus`**) | Amazon Braket Task ARN |
| :--- | :--- | :-: | :-: | :-: | :--- | :--- | :--- |
| **Rigetti `Cepheus-1-108Q`** | **Dense All-to-All (`9Q`)** | `1,024` | `137 / 131 /` **`63`** (`-54.0%`) | `80 / 83 /` **`54`** (`-32.5%`) | `0.0435 / 0.0211 ->` **`0.2088` (`+379.42%` vs S, `+887.34%` vs T; XEB `14.92` vs `1.65`)** | `0.9329 / 0.9515 ->` **`0.7966`** | `arn:aws:braket:us-west-1:893688540163:quantum-task/2df64966-8b30-4e19-a859-25efc2f2b136` |
| **Rigetti `Cepheus-1-108Q`** | **Dense All-to-All (`6Q`)** | `4,096` | `63 / 82 /` **`40`** (`-36.5%`) | `31 / 33 /` **`23`** (`-25.8%`) | `0.0880 / 0.0955 ->` **`0.1903` (`+116.13%` vs S, `+99.23%` vs T; XEB `2.29` vs `0.20`)** | `0.9000 / 0.9034 ->` **`0.8195`** | `arn:aws:braket:us-west-1:893688540163:quantum-task/02427b15-5597-4721-95e1-b3d2547aafb8` |
| **IQM `Emerald` (`54Q`)** | **Dense All-to-All (`6Q`)** | `4,096` | `57 / 56 /` **`41`** (`-28.1%`) | `28 / 33 /` **`23`** (`-17.9%`) | `0.7322 / 0.5931 ->` **`0.7853` (`+7.25%` vs S, `+32.39%` vs T; XEB `15.71` vs `13.67`)** | `0.3266 / 0.4296 ->` **`0.2785`** | `arn:aws:braket:eu-north-1:893688540163:quantum-task/b5317346-c659-4c3e-bd10-0c84df2e74d5` |
| **IQM `Emerald` (`54Q`)** | **QFT (`6Q`)** | `4,096` | `88 / 89 /` **`64`** (`-27.3%`) | `44 / 48 /` **`38`** (`-13.6%`) | `0.8355 / 0.9648 ->` **`0.9602` (`+14.92%` vs S)** | `0.3425 / 0.1575 ->` **`0.1624` (`-52.6%` vs S)** | `arn:aws:braket:eu-north-1:893688540163:quantum-task/68dbffa0-f842-48c4-bdf5-c95d5a69036b` |
| **IQM `Garnet` (`20Q`)** | **Dense All-to-All (`9Q`)** | `1,024` | `130 / 129 /` **`103`** (`-20.8%`) | `79 / 87 /` **`70`** (`-11.4%`) | `0.5513 / 0.6211 ->` **`0.6031` (`+9.39%` vs S; XEB `5.71` vs `3.99`; HOP `0.7764` #1)** | `0.5341 / 0.4738 ->` **`0.4790`** | `arn:aws:braket:eu-north-1:893688540163:quantum-task/8a04e33b-e945-4ec7-b7da-2801a644f610` |
| **Rigetti `Cepheus-1-108Q`** | **QAOA MaxCut (`10Q`, 3-Reg)** | `4,096` | `66 / 91 /` **`47`** (`-28.8%`) | `30 / 45 /` **`28`** (`-6.7%`) | `0.7783 / 0.8268 ->` **`0.8364` (`+7.46%` vs S, `+1.16%` vs T; 3-Way Winner)** | `0.3413 / 0.2979 ->` **`0.2783`** | `arn:aws:braket:us-west-1:893688540163:quantum-task/6c662e9c-d64e-41b9-b7a2-bb10477e073f` |
| **Rigetti `Cepheus-1-108Q`** | **QFT (`8Q`)** | `4,096` | `181 / 261 /` **`129`** (`-28.7%`) | `82 / 95 /` **`70`** (`-14.6%`) | `0.9329 / 0.9528 ->` **`0.9664` (`+3.58%` vs S, `+1.43%` vs T; 3-Way Winner)** | `0.2039 / 0.1721 ->` **`0.1467` (`-28.1%` vs S)** | `arn:aws:braket:us-west-1:893688540163:quantum-task/eeee4e59-68e5-4ad0-b1fb-8b71dbd6638b` |
| **IQM `Garnet` (`20Q`)** | **Dense All-to-All (`4Q`)** | `4,096` | `25 / 26 /` **`22`** (`-12.0%`) | `12 / 12 /` **`8`** (`-33.3%`) | `0.9612 / 0.9430 ->` **`0.9685` (`+0.76%` vs S, `+2.70%` vs T; 3-Way Winner)** | `0.0769 / 0.1653 ->` **`0.0676`** | `arn:aws:braket:eu-north-1:893688540163:quantum-task/8875ef13-5943-4401-9c79-b2abb37e91f8` |
| **IQM `Garnet` (`20Q`)** | **QFT (`4Q`)** | `4,096` | `50 / 48 /` **`37`** (`-26.0%`) | `18 / 21 /` **`14`** (`-22.2%`) | `0.9791 / 0.9953 ->` **`0.9836` (`+0.46%` vs S)** | `0.1338 / 0.0527 ->` **`0.1030` (`-23.0%` vs S)** | `arn:aws:braket:eu-north-1:893688540163:quantum-task/904c6e83-0279-417f-a91c-080316c73ef0` |
| **IQM `Garnet` (`20Q`)** | **QAOA MaxCut (`4Q`, 3-Reg)** | `4,096` | `21 / 23 /` **`19`** (`-9.5%`) | `9 / 9 /` **`7`** (`-22.2%`) | `0.9967 / 0.9959 -> 0.9944` (`-0.23%` vs S; shallow 4Q tie at `>99.4%`) | `0.0461 / 0.0520 -> 0.0574` | `arn:aws:braket:eu-north-1:893688540163:quantum-task/7e3ad9a8-6038-4e5e-bf89-0b86bc425fe5` |
| **IQM `Emerald` (`54Q`)** | **QAOA MaxCut (`7Q`, Bounded-Deg)** | `4,096` | `36 / 47 /` **`34`** (`-5.6%`) | `19 / 22 /` **`17`** (`-10.5%`) | `0.9719 / 0.9802 -> 0.9585` (`-1.38%` vs S) | `0.1316 / 0.1123 -> 0.1621` | `arn:aws:braket:eu-north-1:893688540163:quantum-task/89cebd67-b2a4-460c-80a8-41e47b2a3d01` |
| **Rigetti `Cepheus-1-108Q`** | **Dense All-to-All (`9Q` Run 1)** | `1,024` | `125 / 131 /` **`87`** (`-30.4%`) | `76 / 83 /` **`69`** (`-9.2%`) | `0.2704 / 0.2233 -> 0.2362` (`+5.74%` vs T; **`HOP: 0.6260` #1 vs `0.5791` S & `0.5332` T**) | `0.7389 / 0.7717 -> 0.7710` | `arn:aws:braket:us-west-1:893688540163:quantum-task/f337ec8e-9348-4414-8a8d-10f2ed333d07` |

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

## 2. Amazon Braket `LocalSimulator` & Cross-Paradigm Compilation Verification (`validate_braket_local.py`)

We verified all proposed logical workloads using the official **`amazon-braket-sdk` (`LocalSimulator("default")`)** at both `shots=0` (exact probability distribution equivalence against Qiskit Statevector) and **`shots=4096`** (empirical 4,096-shot sampling execution), and archived the compiled structural benchmarks across **Superconducting (`Rigetti Cepheus-1-108Q`, `IQM Garnet` 20Q, `IQM Emerald` 54Q)**, **Trapped-Ion (`AQT IBEX Q1` 12Q, `IonQ Forte 1` 36Q)**, and **Neutral-Atom (`QuEra Aquila` 256Q)**:

### Table 2A - Verified Superconducting `LocalSimulator` & Structural Benchmark (`4,096 Shots/Circuit`)

| Target Braket QPU Topology | Algorithm & Scale | Braket `LocalSimulator` (`4,096` Shots) | Circuit Depth (`SABRE` / `TKET` / **`Prometheus`**) | 2Q Gates (`SABRE` / `TKET` / **`Prometheus`**) | Simulated Distribution Fidelity (`SABRE` / `TKET` -> **`Prometheus`**) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Rigetti Cepheus** *(108Q Grid)* | `QAOA_MaxCut_8Q` | `PASS (1.000000)` | `180` / `254` / **`156`** | `74` / `105` / **`77` (`-26.7%` vs TKET)** | `0.7900` / `0.8871` -> **`0.9253`** |
| **Rigetti Cepheus** *(108Q Grid)* | `QAOA_MaxCut_12Q` | `PASS (1.000000)` | `261` / `398` / **`248`** | `106` / `168` / **`97` (`-8.5%` vs S, `-42.3%` vs T)** | `0.4375` / `0.5001` -> **`0.6014`** |
| **Rigetti Cepheus** *(108Q Grid)* | `QFT_8Q` | `PASS (1.000000)` | `163` / `197` / **`151`** | `54` / `57` / **`53` (`-1.9%` vs S, `-7.0%` vs T)** | `0.6932` / `0.9028` -> **`0.9396`** |
| **Rigetti Cepheus** *(108Q Grid)* | `QFT_12Q` | `PASS (1.000000)` | `247` / `347` / **`261`** | `92` / `117` / **`93` (`-20.5%` vs TKET)** | `0.3393` / `0.5396` -> **`0.6176`** |
| **Rigetti Cepheus** *(108Q Grid)* | `Dense_AllToAll_17Q` *(Opt.)* | `PASS (1.000000)` | `182` / `250` / **`129` (`-29.1%`)** | `145` / `165` / **`125` (`-13.8%` vs S, `-24.2%` vs T)** | `0.0332` / `0.1536` -> **`0.2718`** |
| **Rigetti Cepheus** *(108Q Grid)* | `Dense_AllToAll_18Q` *(Opt.)* | `PASS (1.000000)` | `132` / `338` / **`113` (`-14.4%`)** | `149` / `240` / **`131` (`-12.1%` vs S, `-45.4%` vs T)** | `0.0124` / `0.0508` -> **`0.2200`** |
| **Rigetti Cepheus** *(108Q Grid)* | `Dense_AllToAll_19Q` *(Opt.)* | `PASS (1.000000)` | `167` / `258` / **`154` (`-7.8%`)** | `169` / `219` / **`169` (`-7.1%` vs S, `-22.8%` vs T)** | `0.0129` / `0.0787` -> **`0.1434`** |
| **IQM Garnet** *(20Q Crystal)* | `QAOA_MaxCut_8Q` | `PASS (1.000000)` | `190` / `239` / **`185`** | `75` / `105` / **`75` (`-28.6%` vs TKET)** | `0.8696` / `0.8153` -> **`0.9117`** |
| **IQM Garnet** *(20Q Crystal)* | `QAOA_MaxCut_12Q` | `PASS (1.000000)` | `272` / `393` / **`250`** | `105` / `132` / **`104` (`-1.0%` vs S, `-21.2%` vs T)** | `0.4825` / `0.4774` -> **`0.5800`** |
| **IQM Garnet** *(20Q Crystal)* | `QFT_8Q` | `PASS (1.000000)` | `165` / `204` / **`165`** | `55` / `57` / **`50` (`-9.1%` vs S, `-12.3%` vs T)** | `0.8467` / `0.8208` -> **`0.9290`** |
| **IQM Garnet** *(20Q Crystal)* | `QFT_12Q` | `PASS (1.000000)` | `276` / `365` / **`231` (`-16.3%`)** | `97` / `114` / **`89` (`-8.2%` vs S, `-21.9%` vs T)** | `0.4629` / `0.4096` -> **`0.5560`** |
| **IQM Garnet** *(20Q Crystal)* | `Dense_AllToAll_17Q` *(Opt.)* | `PASS (1.000000)` | `175` / `262` / **`151` (`-13.7%`)** | `135` / `204` / **`131` (`-3.0%` vs S, `-35.8%` vs T)** | `0.0500` / `0.0142` -> **`0.2012`** |
| **IQM Garnet** *(20Q Crystal)* | `Dense_AllToAll_18Q` *(Opt.)* | `PASS (1.000000)` | `184` / `263` / **`222`** | `159` / `207` / **`163` (`-21.3%` vs TKET)** | `0.0215` / `0.0081` -> **`0.1370`** |
| **IQM Garnet** *(20Q Crystal)* | `Dense_AllToAll_19Q` *(Opt.)* | `PASS (1.000000)` | `169` / `321` / **`166`** | `169` / `276` / **`169` (`-38.8%` vs TKET)** | `0.0476` / `0.0041` -> **`0.0801`** |

### Table 2B - Verified Trapped-Ion All-to-All Compilation Benchmark (`AQT IBEX Q1` 12Q & `IonQ Forte 1` 36Q)

On all-to-all trapped-ion processors, standard `SABRE O3` and `Quantinuum TKET` (via `qiskit-braket-provider`) translate logical two-qubit gates into native trapped-ion basis gates (`rxx` on AQT, `rzz` on IonQ) without first fusing consecutive SU(4) blocks into continuous-angle interactions. Prometheus's **Two-Stage Continuous-Angle Ion-Trap KAK Synthesis + Per-Ion Telemetry Layout** achieves substantial reductions in both entangling MS/`rzz` gates and single-qubit laser pulses while preserving exact `1.00000000` unitary equivalence:

| Target Trapped-Ion QPU | Native Basis | Workload | Compiled Depth (`SABRE` / `TKET` / **`Prometheus`**) | Native 2Q Gates (`SABRE` / `TKET` / **`Prometheus`**) | Native 1Q Pulses (`SABRE` / `TKET` / **`Prometheus`**) | Exact Ideal Fidelity |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **AQT `IBEX Q1` (`12Q`, `eu-north-1`)** | `['rxx', 'r', 'rz']` | `QFT_6Q` | `38` / `62` / **`27` (`-28.9%` vs S, `-56.5%` vs T)** | `24` / `39` / **`15` `rxx` (`-37.5%` vs S, `-61.5%` vs T)** | `97` / `132` / **`52` `r` (`-46.4%` vs S)** | `PASS (1.00000000)` |
| **IonQ `Forte 1` (`36Q`, `us-east-1`)** | `['rzz', 'gpi', 'gpi2']` | `QFT_6Q` | `226` / `223` / **`56` (`-75.2%` vs S, `-74.9%` vs T)** | `39` / `39` / **`15` `rzz` (`-61.5%` vs S & T)** | `591` / `561` / **`123` `gpi/gpi2` (`-79.2%` vs S)** | `PASS (1.00000000)` |

---

## 3. Scoped Multi-Window Cross-Paradigm Cost Estimate (`aws.amazon.com/braket/pricing/`)

To evaluate execution quality across all five quantum hardware vendors accessible through Amazon Braket (**Rigetti, IQM, AQT, IonQ, and QuEra**), the scoped credit plan is structured into three modular phases using `ProgramSet` batching on all gate-model QPUs (`$0.30 / task` per 3-compiler `ProgramSet`, reducing per-task fees by `3x`):

1. **Phase 1 - Superconducting Lattice Multi-Window Replication (`Rigetti Cepheus-1-108Q` & `IQM Garnet` 20Q):**
   - **Phase 1A Core Suite (`8Q` & `12Q` `QAOA MaxCut` + `QFT`, `3` windows, `4,096` shots/circuit):** `24 ProgramSet` tasks (`72` circuits, `294,912` shots) = **`$283.68 USD`** (`$298.08 USD` if separate tasks).
   - **Phase 1B Optional High-Width All-to-All Extension (`17Q, 18Q, 19Q` Dense $K_N$, `3` windows, `4,096` shots/circuit):** `+18 ProgramSet` tasks (`+54` circuits, `+221,184` shots) = **`+$212.76 USD`** (`$496.44 USD` combined superconducting).
2. **Phase 2 - Trapped-Ion All-to-All Continuous-Angle KAK Suite (`AQT IBEX Q1` 12Q & `IonQ Forte 1` 36Q):**
   - **AQT `IBEX Q1` (`12Q`, `eu-north-1`, `$0.30/task` + `$0.0235/shot`):** `4` workloads (`6Q` & `10Q` `QFT` + `Dense All-to-All`) $\times$ `3` windows = **`12 ProgramSet` tasks (`36` circuits)** at `250` shots/circuit (`750` shots/task, `9,000` shots total) = **`$215.10 USD`** (`$222.30 USD` if separate tasks).
   - **IonQ `Forte 1` (`36Q`, `us-east-1`, `$0.30/task` + `$0.0800/shot`):** `4` workloads (`8Q` & `12Q` `QAOA MaxCut` + `QFT`) $\times$ `3` windows = **`12 ProgramSet` tasks (`36` circuits)** at `100` shots/circuit (`300` shots/task, `3,600` shots total) = **`$291.60 USD`** (`$298.80 USD` if separate tasks).
   - **Phase 2 Trapped-Ion Subtotal (`AQT IBEX Q1` + `IonQ Forte 1`):** **`$506.70 USD`** (`24 ProgramSet` tasks, `72` circuits, `12,600` shots).
3. **Phase 3 - Neutral-Atom 2D Rydberg Blockade AHS Suite (`QuEra Aquila` 256Q):**
   - **QuEra `Aquila` (`256Q` Neutral-Atom AHS, `us-east-1`, `$0.30/task` + `$0.0100/shot`):** `4` unit-disk Maximum Independent Set (MIS) register scales (`16`, `36`, `64`, and `100` Rubidium-87 atoms) $\times$ `3` windows = **`12 AHS tasks`** at `500` shots/task (`6,000` shots total) = **`$63.60 USD`**.

### Table 3A - Complete Cross-Paradigm QPU Cost Breakdown Across All 5 AWS Braket Hardware Vendors

| Phase / Target QPU | Architecture & Region | Workloads (`3` Windows Each) | Batched Tasks (`Programs`) | Shots / Circuit (`Total Shots`) | Per-Shot Rate (`+ $0.30/task`) | `ProgramSet` / AHS Total (USD) | Separate-Task Total (USD) |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: | :---: |
| **Phase 1A: Rigetti `Cepheus-1-108Q`** | 108Q Superconducting (`us-west-1`) | `4` (`8Q/12Q QAOA + QFT`) | `12 ProgramSets` (`36 circuits`) | `4,096` (`147,456`) | `$0.000425 / shot` | **`$66.27`** | `$73.47` |
| **Phase 1A: IQM `Garnet`** | 20Q Superconducting (`eu-north-1`) | `4` (`8Q/12Q QAOA + QFT`) | `12 ProgramSets` (`36 circuits`) | `4,096` (`147,456`) | `$0.001450 / shot` | **`$217.41`** | `$224.61` |
| **Phase 1A Core Superconducting Subtotal** | **Rigetti + IQM (Core 8Q/12Q)** | **`4 workloads`** | **`24 ProgramSets` (`72 circuits`)** | **`294,912` shots** | | **`$283.68 USD`** | **`$298.08 USD`** |
| **Phase 1B: Rigetti `Cepheus-1` (Opt. 17Q-19Q)** | 108Q Superconducting (`us-west-1`) | `3` (`17Q, 18Q, 19Q K_N`) | `9 ProgramSets` (`27 circuits`) | `4,096` (`110,592`) | `$0.000425 / shot` | **`$49.70`** | `$55.10` |
| **Phase 1B: IQM `Garnet` (Opt. 17Q-19Q)** | 20Q Superconducting (`eu-north-1`) | `3` (`17Q, 18Q, 19Q K_N`) | `9 ProgramSets` (`27 circuits`) | `4,096` (`110,592`) | `$0.001450 / shot` | **`$163.06`** | `$168.46` |
| **Phase 1B Superconducting Ext. Subtotal** | **Rigetti + IQM (17Q-19Q $K_N$)** | **`3 workloads`** | **`18 ProgramSets` (`54 circuits`)** | **`221,184` shots** | | **`$212.76 USD`** | **`$223.56 USD`** |
| **Phase 2: AQT `IBEX Q1`** | 12Q Trapped-Ion (`eu-north-1`) | `4` (`6Q/10Q QFT + K_N`) | `12 ProgramSets` (`36 circuits`) | `250` (`9,000`) | `$0.023500 / shot` | **`$215.10`** | `$222.30` |
| **Phase 2: IonQ `Forte 1`** | 36Q Trapped-Ion (`us-east-1`) | `4` (`8Q/12Q QAOA + QFT`) | `12 ProgramSets` (`36 circuits`) | `100` (`3,600`) | `$0.080000 / shot` | **`$291.60`** | `$298.80` |
| **Phase 2 Trapped-Ion Subtotal** | **AQT `IBEX Q1` + IonQ `Forte 1`** | **`4 workloads / QPU`** | **`24 ProgramSets` (`72 circuits`)** | **`12,600` shots** | | **`$506.70 USD`** | **`$521.10 USD`** |
| **Phase 3: QuEra `Aquila` (Neutral-Atom)** | 256Q Rydberg AHS (`us-east-1`) | `4` (`16, 36, 64, 100 Atom MIS`) | `12 AHS Tasks` (`12 schedules`) | `500` (`6,000`) | `$0.010000 / shot` | **`$63.60 USD`** | **`$63.60 USD`** |
| **Core Cross-Paradigm Total (1A + 2 + 3)** | **All 5 Vendors (Core 6Q-12Q + AHS)** | **Superconducting + Ion + Atom** | **`60 Tasks` (`156 programs`)** | **`313,512` shots** | | **`$853.98 USD`** | **`$882.78 USD`** |
| **Full Cross-Paradigm Total (1A + 1B + 2 + 3)** | **All 5 Vendors (Full 6Q-100Q Suite)** | **All Phases Combined** | **`78 Tasks` (`210 programs`)** | **`534,696` shots** | | **`$1,066.74 USD`** | **`$1,106.34 USD`** |

---

## 4. Checklist Status & Live Cloud UI Access

1. **AWS Skill Builder - Amazon Braket Knowledge Badge:** **COMPLETED & VERIFIED** - [https://www.credly.com/badges/b64dc9e8-8f3e-4996-8494-4acee97db732/public_url](https://www.credly.com/badges/b64dc9e8-8f3e-4996-8494-4acee97db732/public_url)
2. **Local Braket Simulator & Live Braket QPU Validation:** **COMPLETED & VERIFIED** across all proposed workloads on `braket.devices.LocalSimulator("default")` (`validate_braket_local.py`), verified continuous-angle KAK compilation for **AQT `IBEX Q1`** and **IonQ `Forte 1`** plus Rydberg AHS compilation for **QuEra `Aquila`**, and **12 live 3-way `ProgramSet` hardware executions (`36` compiled circuits, `119,808` shots)** on **Rigetti `Cepheus-1-108Q`**, **IQM `Garnet` (`20Q`)**, and **IQM `Emerald` (`54Q`)** archived with AWS Task ARNs for traceability in [`aws_braket_qpu_12_jobs_ledger.json`](./aws_braket_qpu_12_jobs_ledger.json).
3. **Scoped Cross-Paradigm QPU Cost Estimate:** **COMPLETED** across all 5 AWS Braket hardware vendors (**`$283.68 USD`** for Phase 1A Superconducting Core, **`+$212.76 USD`** for Phase 1B 17Q-19Q Superconducting Extension, **`+$506.70 USD`** for Phase 2 Trapped-Ion `AQT IBEX Q1` + `IonQ Forte 1`, and **`+$63.60 USD`** for Phase 3 Neutral-Atom `QuEra Aquila` 256Q = **`$853.98 USD` Core Cross-Paradigm** or **`$1,066.74 USD` Full Suite**).
4. **AWS Account ID:** `893688540163`
5. **Interactive Cloud UI Evaluation (`https://prometheusdynamics.ca/QuantumCompiler/`):** Supports all 7 AWS Braket QPUs (`Rigetti Cepheus-1-108Q`, `IQM Garnet`, `IQM Emerald`, `AQT IBEX Q1`, `IonQ Forte 1`, `IonQ Forte Enterprise 1`, and `QuEra Aquila`) and 15 circuit families, available during supervised live evaluation sessions for AWS Braket technical reviewers.
