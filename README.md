# Prometheus Dynamics - Hybrid Quantum-HPC & Multi-QPU Benchmark Corpus

[![Platform](https://img.shields.io/badge/Platform-Prometheus%20Dynamics-4F46E5)](https://prometheusdynamics.ca)
[![AWS Braket QPUs](https://img.shields.io/badge/AWS%20Braket%20QPUs-14%20ProgramSet%20Tasks%20%7C%20126.0K%20Shots-FF9900)](./aws_braket_qpu_14_jobs_ledger.json)
[![IBM Quantum](https://img.shields.io/badge/IBM%20Heron%20156Q-107%20Completed%20Jobs%20%7C%204.96M%20Shots-054ADA)](./ibm_heron_156q_verified_benchmarks.json)
[![Hybrid HPC](https://img.shields.io/badge/NVIDIA%20H100%20%28VeloxQ%29-42%20Configs%20%7C%204%E2%86%921%2C029%20Binary%20Vars-00D1B2)](./veloxq_h100_hybrid_benchmarks.json)
[![AWS Braket Badge](https://img.shields.io/badge/AWS%20Braket-Verified%20Badge-FF9900)](https://www.credly.com/badges/b64dc9e8-8f3e-4996-8494-4acee97db732/public_url)

Official empirical hardware and hybrid-solver benchmark corpus for **Prometheus Dynamics** ([`https://prometheusdynamics.ca`](https://prometheusdynamics.ca)), documenting **121 completed 3-way physical quantum hardware benchmark jobs (`363` compiled circuits, `5,090,304` completed hardware shots)** across **six physical quantum processors** spanning **Amazon Braket (`Rigetti Cepheus-1-108Q`, `IQM Garnet` 20Q, `IQM Emerald` 54Q)** and **IBM Quantum (`ibm_marrakesh`, `ibm_fez`, `ibm_kingston` 156Q Heron)**, alongside **VeloxQ NVIDIA H100 physics-inspired QUBO solvers (`VeloxQH100_1`)** and the **Amazon Braket SDK (`LocalSimulator`)**.

> **Intellectual Property & Reproducibility Boundary:** To protect proprietary compilation and problem-compression IP, internal routing source code, internal scoring weights, QUBO Hamiltonian penalty coefficients, and routed physical OpenQASM trajectories are withheld from this repository. Instead, this repository provides **complete machine-readable benchmark ledgers (including verifiable Amazon Braket Task ARNs and IBM Quantum Job IDs), full scheduling instance specifications, returned schedules, exact MILP lower-bound certificates, and standalone Python verification scripts** (`verify_corpus_and_schedules.py` and `validate_braket_local.py`).

---

## 1. Corpus Overview & Reconciled Execution Accounting

| Benchmark Pillar | Hardware / Environment | Reconciled Scale & Scope | Key Empirical Outcome |
| :--- | :--- | :--- | :--- |
| **Amazon Braket Live QPU Corpus** | **Rigetti `Cepheus-1-108Q`** (`108Q`), **IQM `Garnet`** (`20Q`), **IQM `Emerald`** (`54Q`) | **14 Completed 3-Way `ProgramSet` Tasks** (**`42` verbatim compiled circuits, `125,952` completed physical shots**) across `Dense All-to-All`, `QFT`, and `QAOA MaxCut` ([`aws_braket_qpu_14_jobs_ledger.json`](./aws_braket_qpu_14_jobs_ledger.json)) | **100% (`14 / 14`) simultaneous reduction in circuit depth and 2Q `CZ` gates**; **`+379.42%` (`4.79x`) distribution fidelity & `9.03x` XEB vs. `SABRE O3` (`+887.34%` / `9.87x` vs. `TKET`) on Rigetti `Cepheus-1-108Q` (`9Q Dense All-to-All`)**; **`+116.13%` (`2.16x`) fidelity on `Cepheus-1-108Q` (`6Q Dense All-to-All`)**; **`+14.92%` fidelity (`-52.6%` TVD) on IQM `Emerald` (`6Q QFT`)**; **`+9.39%` fidelity (`+43.1%` XEB) on IQM `Garnet` (`9Q Dense All-to-All`)** |
| **156Q Gate-QPU Compilation Corpus** | **`ibm_marrakesh`**, **`ibm_fez`**, **`ibm_kingston`** *(156Q IBM Heron)* | **107 Completed 3-Way Jobs** (**`321` compiled physical circuits, `4,964,352` completed physical shots**) across **18 qubit scales (`4Q`-`23Q`)** *(out of `110` total dispatches / `5,111,808` dispatched shots; `3` unrecovered queue dispatches documented)* | Beat **Quantinuum `TKET` on `100 / 107` (`93.5%`)** and **IBM `SABRE O3` on `80 / 107` (`74.8%`)** completed hardware triplets; up to **`-54.5%`** 2Q gate reduction vs. `TKET` and **`-34.8%`** vs. `SABRE O3` |
| **19Q Dense All-to-All ($K_{19}$) Survival** | **`ibm_marrakesh`**, **`ibm_fez`**, **`ibm_kingston`** *(156Q IBM Heron)* | **19-Qubit Dense All-to-All ($K_{19}$)** (`171` logical all-to-all pairs, `16,384 shots/compiler`) | Achieved **`24.26%`** (`ibm_kingston`), **`12.78%`** (`ibm_marrakesh`), and **`6.54%`** (`ibm_fez`) computational-basis distribution fidelity vs. `18.98%`, `6.27%`, and `3.57%` for `SABRE O3`; achieved **`70.45%` heavy-output probability (`HOP`)** on `ibm_kingston` (exceeding the `2/3` heavy-output reference threshold, vs. `63.28%` `SABRE O3` and `54.38%` `TKET`) |
| **Hybrid Quantum-HPC QUBO Compression** | **VeloxQ NVIDIA H100 (`VeloxQH100_1`)** + **156Q IBM Heron** | **42 Distinct Benchmark Configurations** (**`150` multi-seed H100 solver executions**) scaling from **`4` to `1,029` QUBO binary variables** | **`94.44%` variable compression (`72` $\to$ `4` binary variables, `0.0%` optimality gap)** mapped to **4 physical qubits** on IBM Heron (`94.04%-96.34%` distribution fidelity); **`10.0x`-`11.3x` (`3x3`)** and **`26.1x`-`34.0x` (`4x3`)** ground-state sampling boost on H100; **`1,029` binary variables (`15x3` schedule)** solved to the **`26h`** target horizon (`0.0%` horizon gap; `25h` unrestricted pure-$C_{\max}$ MILP lower bound) in **`5.26s`** |
| **Multi-Architecture Braket Verification** | **Amazon Braket SDK (`LocalSimulator`)** - **Rigetti Cepheus (108Q)** & **IQM Garnet (20Q)** | **7 Logical Workloads Verified at `4,096` Shots on `LocalSimulator` + 14 Archived 3-Compiler Structural Benchmarks** (`8Q` & `12Q` `QAOA MaxCut` + `QFT`, and optional `17Q`, `18Q`, `19Q` `Dense All-to-All` $\times$ `SABRE O3`, `TKET`, `Prometheus`) | Won **14 out of 14** structural benchmarks across Rigetti Cepheus and IQM Garnet (`validate_braket_local.py` verifies Qiskit-to-Braket logical equivalence and 4,096-shot execution across all 7 workloads and prints the 14-row benchmark table) |

### Quick-Start Independent Verification
Run both verification suites locally to audit the 107-job IBM Heron corpus, the 14-job live Amazon Braket QPU corpus, the 45-operation schedule feasibility, and Qiskit-to-Braket logical circuit equivalence:
```bash
python verify_corpus_and_schedules.py
python validate_braket_local.py
```

---

## 2. Metric Definitions & Methodological Boundaries

To ensure unambiguous interpretation across hardware and hybrid-solver benchmarks, all reported metrics follow strict definitions:

1. **Classical Computational-Basis Distribution Fidelity (`fidelity`):**
   - Throughout [`ibm_heron_156q_verified_benchmarks.json`](./ibm_heron_156q_verified_benchmarks.json) and [`aws_braket_qpu_14_jobs_ledger.json`](./aws_braket_qpu_14_jobs_ledger.json), `fidelity` denotes the **classical computational-basis distribution overlap** between the noiseless ideal measurement probability distribution $P_{\text{ideal}}(x)$ and the empirical hardware bitstring frequency distribution $P_{\text{meas}}(x)$ over computational-basis states $x \in \{0,1\}^n$.
   - This metric directly measures computational-basis output distribution preservation from shot histograms without requiring $4^n$ full quantum state tomography. It is reported alongside **Total Variation Distance** $\text{TVD} = \frac{1}{2}\sum_x |P_{\text{ideal}}(x) - P_{\text{meas}}(x)|$ and **Linear Cross-Entropy Benchmarking** $\text{XEB} = 2^n \sum_x P_{\text{ideal}}(x) P_{\text{meas}}(x) - 1$.
2. **Heavy-Output Probability (`HOP`) vs. Formal Quantum Volume (`QV`):**
   - On the 19-qubit dense all-to-all ($K_{19}$) benchmark on `ibm_kingston` (`dbajlrhgv2cc73e6vuj0`), Prometheus achieved a **Heavy-Output Probability (`HOP`) of `70.45%`** (exceeding the `2/3` / `66.67%` heavy-output reference threshold, compared to `63.28%` for `SABRE O3` and `54.38%` for `TKET`).
   - **Methodological Boundary:** Crossing `2/3` heavy-output probability on this deterministic $K_{19}$ workload establishes heavy-output survival on that specific 19-qubit dense circuit; it is **not** a formal Quantum Volume (`QV`) certification, which under Qiskit's protocol requires a random $\text{SU}(4)$ model-circuit ensemble evaluated across $\ge 100$ independent random trials with a $2\sigma$ confidence bound.
3. **Physical Qubits (`Q`) vs. QUBO Binary Variables:**
   - **Physical Qubits (`4Q` to `23Q` on `156Q` IBM Heron processors; `4Q` to `17Q` on live Amazon Braket QPUs)** refer exclusively to gate-model quantum circuits.
   - **QUBO Binary Variables (`4` to `1,029` binary decision variables)** refer to combinatorial Ising/QUBO formulations executed on the **VeloxQ NVIDIA H100 GPU solver (`VeloxQH100_1`)**. Only the compressed `4-variable` Tier-5 schedule formulation (and `8Q`/`9Q` small instances) are mapped directly to physical gate-model qubits (`4Q` on `ibm_marrakesh`, `ibm_kingston`, and `ibm_fez`).
4. **Corpus Accounting (`121` Completed 3-Way Hardware Jobs Across IBM Quantum & Amazon Braket) & Unfavorable Cases:**
   - [`aws_braket_qpu_14_jobs_ledger.json`](./aws_braket_qpu_14_jobs_ledger.json) contains **14 distinct completed 3-way `ProgramSet` hardware benchmark tasks** (`42` verbatim compiled circuits, `125,952` completed physical shots) across **Rigetti `Cepheus-1-108Q`**, **IQM `Garnet` (`20Q`)**, and **IQM `Emerald` (`54Q`)**.
   - [`ibm_heron_156q_verified_benchmarks.json`](./ibm_heron_156q_verified_benchmarks.json) contains **107 distinct completed 3-way hardware benchmark jobs** (`321` compiled physical circuits, `4,964,352` completed physical shots). Three earlier `8Q Dense All-to-All` queue dispatches (`db3v85svf2bc73ctral0`, `db3v85svf2bc73ctrakg`, `db3v85imb58s7388ed7g`, totaling `9` circuits and `147,456` dispatched shots) remained in `PENDING_IN_QUEUE` on an expired account session and are listed separately under `unrecovered_queue_dispatches` (`4,964,352 + 147,456 = 5,111,808` total dispatched shots across `110` dispatches).
   - **Retained Unfavorable Results:** All 121 completed hardware jobs (`107` IBM Heron + `14` AWS Braket) are retained without cherry-picking, including all `27 / 107` IBM Heron cases and `2 / 11` in-coherence AWS Braket cases where `SABRE O3` outperformed Prometheus. Retaining mixed outcomes demonstrates why workload- and calibration-specific multi-compiler arbitration is essential in production.

---

## 3. Live Multi-Cloud QPU Benchmarks (`SABRE O3` vs. `Quantinuum TKET` vs. `Prometheus`)

### 3A. Live Amazon Braket QPU Benchmarks (`Rigetti Cepheus-1-108Q`, `IQM Garnet` 20Q, `IQM Emerald` 54Q)

All 14 completed 3-way Amazon Braket `ProgramSet` tasks (`42` verbatim physical circuits, `125,952` physical shots) are recorded with full Task ARNs in [`aws_braket_qpu_14_jobs_ledger.json`](./aws_braket_qpu_14_jobs_ledger.json):

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

### 3B. Live 156-Qubit IBM Heron Benchmarks (`ibm_marrakesh`, `ibm_fez`, `ibm_kingston`)

All 107 completed 3-way hardware benchmark triplets (`321` physical circuits, `4,964,352` physical shots) are recorded in [`ibm_heron_156q_verified_benchmarks.json`](./ibm_heron_156q_verified_benchmarks.json). Representative highlights (`16,384 shots/compiler`):

| Target Processor | Live Job ID | Workload & Scale | Circuit Depth (`SABRE` / `TKET` / **`Prometheus`**) | 2Q Gates (`SABRE` / `TKET` / **`Prometheus`**) | Distribution Fidelity (`F_dist`) & HOP / XEB (`SABRE` / `TKET` $\to$ **`Prometheus`**) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`ibm_marrakesh`** *(156Q)* | `dbajlqpgv2cc73e6vuhg` | **19Q Dense All-to-All ($K_{19}$)** | `459` / `501` / **`281` (`-38.8%`)** | `482` / `717` / **`358` (`-25.7%` vs SABRE, `-50.1%` vs TKET)** | `6.27%` / `3.26%` $\to$ **`12.78%` (XEB `339.8` vs `148.6` SABRE)** |
| **`ibm_fez`** *(156Q)* | `dbajlrhgv2cc73e6vuig` | **19Q Dense All-to-All ($K_{19}$)** | `414` / `501` / **`313` (`-24.4%`)** | `429` / `717` / **`390` (`-9.1%` vs SABRE, `-45.6%` vs TKET)** | `3.57%` / `2.20%` $\to$ **`6.54%` (XEB `208.5` vs `126.9` SABRE)** |
| **`ibm_kingston`** *(156Q)* | `dbajlrhgv2cc73e6vuj0` | **19Q Dense All-to-All ($K_{19}$)** | `358` / `501` / **`281` (`-21.5%`)** | `444` / `717` / **`358` (`-19.4%` vs SABRE, `-50.1%` vs TKET)** | `18.98%` / `1.62%` $\to$ **`24.26%` (`70.45%` HOP vs `63.28%` SABRE & `54.38%` TKET)** |
| **`ibm_fez`** *(156Q)* | `dbaign9gv2cc73e6u5sg` | **12Q QAOA MaxCut (3-Reg)** | `124` / `212` / **`115` (`-7.3%`)** | `58` / `108` / **`54` (`-6.9%` vs SABRE, `-50.0%` vs TKET)** | `86.12%` / `88.35%` $\to$ **`91.21%` (`+5.91%` vs SABRE)** |
| **`ibm_marrakesh`** *(156Q)* | `dbaehak24mrc73859340` | **12Q QAOA MaxCut (3-Reg)** | `118` / `212` / **`170`** | `66` / `108` / **`57` (`-13.6%` vs SABRE, `-47.2%` vs TKET)** | `83.88%` / `83.18%` $\to$ **`90.67%` (`+8.10%` vs SABRE)** |
| **`ibm_marrakesh`** *(156Q)* | `dbaignc24mrc7385fgbg` | **12Q QAOA MaxCut (3-Reg)** | `106` / `212` / **`106`** | `54` / `108` / **`51` (`-5.6%` vs SABRE, `-52.8%` vs TKET)** | `89.83%` / `83.52%` $\to$ **`90.67%` (`+0.94%` vs SABRE, `+8.57%` vs TKET)** |
| **`ibm_kingston`** *(156Q)* | `dbaign8c77vs7382smbg` | **12Q QAOA MaxCut (3-Reg)** | `110` / `212` / **`165`** | `63` / `108` / **`54` (`-14.3%` vs SABRE, `-50.0%` vs TKET)** | `89.14%` / `85.52%` $\to$ **`90.02%` (`+1.00%` vs SABRE, `+5.27%` vs TKET)** |
| **`ibm_marrakesh`** *(156Q)* | `dbaio50c77vs7382t5qg` | **12Q Quantum Fourier Transform** | `375` / `573` / **`329` (`-12.3%`)** | `236` / `375` / **`203` (`-14.0%` vs SABRE, `-45.9%` vs TKET)** | `89.76%` / `79.18%` $\to$ **`91.17%` (`+1.57%` vs SABRE, `+15.14%` vs TKET)** |
| **`ibm_kingston`** *(156Q)* | `dbaio4vi0auc73923sk0` | **12Q Quantum Fourier Transform** | `394` / `573` / **`288` (`-26.9%`)** | `245` / `375` / **`205` (`-16.3%` vs SABRE, `-45.3%` vs TKET)** | `85.73%` / `74.50%` $\to$ **`84.99%` (`+14.08%` vs TKET; `3,882/4,096` states)** |
| **`ibm_marrakesh`** *(156Q)* | `dbaijj9gv2cc73e6ubmg` | **8Q Quantum Fourier Transform** | `226` / `288` / **`175` (`-22.6%`)** | `104` / `137` / **`85` (`-18.3%` vs SABRE, `-38.0%` vs TKET)** | `98.62%` / `95.79%` $\to$ **`99.29%` (`+0.67%` vs SABRE, `-26.4%` TVD error)** |
| **`ibm_kingston`** *(156Q)* | `dbaijj9gv2cc73e6ubn0` | **8Q Quantum Fourier Transform** | `186` / `288` / **`207`** | `91` / `137` / **`85` (`-6.6%` vs SABRE, `-38.0%` vs TKET)** | `97.83%` / `90.95%` $\to$ **`98.42%` (`+0.61%` vs SABRE, `+8.21%` vs TKET)** |
| **`ibm_marrakesh`** *(156Q)* | `db9nfnfi0auc7390uvvg` | **4Q Compressed Schedule ($K_4$)** | `33` / `34` / **`27` (`-18.2%`)** | `42` / `42` / **`33` (`-21.4%`)** | `90.12%` / `91.85%` $\to$ **`96.34%` (`+6.90%` vs SABRE)** |
| **`ibm_kingston`** *(156Q)* | `db9nflpgv2cc73e5q9l0` | **4Q Compressed Schedule ($K_4$)** | `33` / `34` / **`27` (`-18.2%`)** | `42` / `42` / **`33` (`-21.4%`)** | `88.94%` / `91.02%` $\to$ **`95.00%` (`+6.81%` vs SABRE)** |
| **`ibm_fez`** *(156Q)* | `db9nfmvi0auc7390uvug` | **4Q Compressed Schedule ($K_4$)** | `33` / `34` / **`27` (`-18.2%`)** | `42` / `42` / **`33` (`-21.4%`)** | `86.40%` / `89.68%` $\to$ **`94.04%` (`+8.84%` vs SABRE)** |

---

## 4. Hybrid Quantum-HPC Benchmarks on NVIDIA H100 (`VeloxQH100_1` - `4` to `1,029` QUBO Binary Variables)

[`veloxq_h100_hybrid_benchmarks.json`](./veloxq_h100_hybrid_benchmarks.json) documents all **42 distinct hybrid scheduling configurations** (including **150 multi-seed H100 executions** across 15 QUBO scaling models at 10 seeds $\times$ 4,096 reads/seed, 6 compression tiers, 5 operational constraint models, fleet dispatch, and cross-algorithm comparisons).

### 4A. 15-Point Multi-Seed Scaling Curve on VeloxQ NVIDIA H100 (`VeloxQH100_1`)

| Model & Formulation | QUBO Binary Variables | Seeds $\times$ Reads | Target Horizon (`H`) & Pure-$C_{\max}$ MILP LB | VeloxQ H100 Mean Makespan (`Horizon Gap`) | Ground-State Hits (`/ 4,096`) | Mean H100 Runtime |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `3x3 Tier-5 Compressed Basis` *(also run on 4Q IBM Heron)* | **`4` vars** *(vs. `72` naive)* | `10 x 4,096` | `8h` (`LB = 8h`) | **`8.0h` (`0.0%`)** | `1,644 / 4,096` (`40.14%`) | `0.138s` |
| `2x2 Tier-1 Reduced` | **`8` vars** *(vs. `16` naive)* | `10 x 4,096` | `4h` (`LB = 4h`) | **`4.0h` (`0.0%`)** | `4,096 / 4,096` (`100.0%`) | `0.143s` |
| `3x3 Tier-4 Compact` | **`9` vars** *(vs. `72` naive)* | `10 x 4,096` | `8h` (`LB = 8h`) | **`8.0h` (`0.0%`)** | `1,410 / 4,096` (`34.42%`) | `0.140s` |
| `2x2 Naive Time-Indexed` | **`16` vars** | `10 x 4,096` | `4h` (`LB = 4h`) | **`4.0h` (`0.0%`)** | `4,064 / 4,096` (`99.22%`) | `0.141s` |
| `3x3 Tier-3 Compact Slack` | **`21` vars** *(vs. `72` naive)* | `10 x 4,096` | `8h` (`LB = 8h`) | **`8.0h` (`0.0%`)** | `4,096 / 4,096` (`100.0%`) | `0.002s` |
| `3x3 Tier-2 Reduced` | **`28` vars** *(vs. `72` naive)* | `10 x 4,096` | `8h` (`LB = 8h`) | **`8.0h` (`0.0%`)** | `830 / 4,096` (`20.26%`) | `0.152s` |
| `3x3 Tier-1 Reduced` *(10.0x-11.3x hit boost vs. 72-var)* | **`39` vars** *(vs. `72` naive)* | `10 x 4,096` | `8h` (`LB = 8h`) | **`8.0h` (`0.0%`)** | `807 / 4,096` (`19.70%`) | `0.159s` |
| `4x3 Tier-1 Reduced` *(26.1x-34.0x hit boost vs. 108-var)* | **`63` vars** *(vs. `108` naive)* | `10 x 4,096` | `9h` (`LB = 9h`) | **`9.0h` (`0.0%`)** | `653 / 4,096` (`15.94%`) | `0.174s` |
| `3x3 Naive Time-Indexed` | **`72` vars** | `10 x 4,096` | `8h` (`LB = 8h`) | **`8.0h` (`0.0%`)** | `81 / 4,096` (`1.98%`) | `0.189s` |
| `4x3 Naive Time-Indexed` | **`108` vars** | `10 x 4,096` | `9h` (`LB = 9h`) | **`9.0h` (`0.0%`)** | `25 / 4,096` (`0.61%`) | `0.226s` |
| `6x3 Tier-1 Reduced` | **`135` vars** *(vs. `198` naive)* | `10 x 4,096` | `11h` (`LB = 11h`) | **`11.0h` (`0.0%`)** | `54 / 4,096` (`1.32%`) | `0.255s` |
| `8x3 Tier-1 Reduced` | **`255` vars** *(vs. `336` naive)* | `10 x 4,096` | `14h` (`LB = 14h`) | **`14.0h` (`0.0%`)** | `1 / 4,096` (`0.02%`) | `0.446s` |
| `10x3 Tier-1 Reduced` | **`414` vars** *(vs. `510` naive)* | `10 x 4,096` | `17h` (`LB = 17h`) | **`17.0h` (`0.0%`)** | `1 / 4,096` (`0.02%`) | `1.531s` |
| `12x3 Tier-1 Reduced` | **`570` vars** *(vs. `684` naive)* | `10 x 4,096` | `19h` (`LB = 19h`) | **`19.0h` (`0.0%`)** | `1 / 4,096` (`0.02%`) | `2.300s` |
| `15x3 Tier-1 Reduced Plant Schedule` | **`1,029` vars** *(vs. `1,170` naive)* | `10 x 4,096` | `H = 26h` (`Pure-Cmax LB = 25h`) | **`26.0h` (`0.0%` vs `H=26h`)** | `1 / 4,096` (`0.02%`) | `5.257s` |

### 4B. `1,029-Variable` (`15x3`) Schedule & Feasibility Certificate
In [`veloxq_h100_hybrid_benchmarks.json`](./veloxq_h100_hybrid_benchmarks.json) (`plant_scale_15x3_1029var_verification_artifact`), we provide:
- The complete `15-job x 3-machine` (`45-operation`) job-duration table (`Z1`-`Z15` across Lathe `T`, Milling `F`, and Welding `S`, with total machine loads $T = 22\text{h}$, $F = 21\text{h}$, $S = 19\text{h}$),
- The **analytical one-machine head-plus-tail lower bound** ($\sum_j d_{j,T} + \min_j(d_{j,F} + d_{j,S}) = 24\text{h}$) and the **unrestricted pure-$C_{\max}$ HiGHS MILP lower-bound reference schedule** (`25h`), and
- All **45 scheduled start/end intervals (`veloxq_h100_optimal_schedule_45_ops`)** returned by `VeloxQH100_1` for the `H = 26h` horizon formulation (`makespan = 26h`, `0.0%` horizon violation), independently verified for zero machine overlap and strict technological precedence by `python verify_corpus_and_schedules.py`.

---

## 5. Amazon Braket Verification (`validate_braket_local.py`)

Running `python validate_braket_local.py` executes two transparent steps:
- **Stage 1 (Logical Qiskit-to-Braket Equivalence & 4,096-Shot Execution Check):** Independently builds all 7 proposed Phase 1A logical workloads (`QAOA_MaxCut_8Q`, `QAOA_MaxCut_12Q`, `QFT_8Q`, `QFT_12Q`, `Dense_AllToAll_17Q`, `Dense_AllToAll_18Q`, `Dense_AllToAll_19Q`), translates each Qiskit circuit into an Amazon Braket `Circuit`, runs each on Qiskit Statevector and the official Amazon Braket `LocalSimulator("default")` at both `shots=0` (exact probability vector) and `shots=4096` (empirical 4,096-shot sampling), and verifies `1.000000` computational-basis distribution equivalence (`7/7 PASS`).
- **Stage 2 (Archived Structural Benchmark Table Loader):** Loads and displays the saved structural compilation comparison metrics (`depth`, `2Q gates`, `simulated_fidelity`) from [`braket_local_validation_results.json`](./braket_local_validation_results.json) across all 14 device-workload pairs for **Rigetti Cepheus** (`108Q`) and **IQM Garnet** (`20Q`). *(Note: To protect compiler IP and physical execution trajectories per `PUBLIC_DISCLOSURE.md`, routed physical OpenQASM circuits and internal scoring weights are withheld from the public repository; running `validate_braket_local.py` verifies logical circuit translation equivalence and 4,096-shot `LocalSimulator` execution and displays the archived structural comparison table below.)*

| Target Braket QPU Topology | Algorithm & Scale | Stage 1 `LocalSimulator` (`4,096` Shots) | Archived Depth (`S`/`T`/**`P`**) | Archived 2Q Gates (`S`/`T`/**`P`**) | Archived Simulated Fidelity (`SABRE` / `TKET` -> **`Prometheus`**) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Rigetti Cepheus** *(108Q Grid)* | `QAOA_MaxCut_8Q` | `PASS` (`1.000000`) | `180` / `254` / **`156`** | `74` / `105` / **`77` (`-26.7%` vs T)** | `0.7900` / `0.8871` -> **`0.9253`** |
| **Rigetti Cepheus** *(108Q Grid)* | `QAOA_MaxCut_12Q` | `PASS` (`1.000000`) | `261` / `398` / **`248`** | `106` / `168` / **`97` (`-8.5%` vs S, `-42.3%` vs T)** | `0.4375` / `0.5001` -> **`0.6014`** |
| **Rigetti Cepheus** *(108Q Grid)* | `QFT_8Q` | `PASS` (`1.000000`) | `163` / `197` / **`151`** | `54` / `57` / **`53` (`-1.9%` vs S, `-7.0%` vs T)** | `0.6932` / `0.9028` -> **`0.9396`** |
| **Rigetti Cepheus** *(108Q Grid)* | `QFT_12Q` | `PASS` (`1.000000`) | `247` / `347` / **`261`** | `92` / `117` / **`93` (`-20.5%` vs T)** | `0.3393` / `0.5396` -> **`0.6176`** |
| **Rigetti Cepheus** *(108Q Grid)* | `Dense_AllToAll_17Q` | `PASS` (`1.000000`) | `182` / `250` / **`129`** | `145` / `165` / **`125` (`-13.8%` vs S, `-24.2%` vs T)** | `0.0332` / `0.1536` -> **`0.2718`** |
| **Rigetti Cepheus** *(108Q Grid)* | `Dense_AllToAll_18Q` | `PASS` (`1.000000`) | `132` / `338` / **`113`** | `149` / `240` / **`131` (`-12.1%` vs S, `-45.4%` vs T)** | `0.0124` / `0.0508` -> **`0.2200`** |
| **Rigetti Cepheus** *(108Q Grid)* | `Dense_AllToAll_19Q` | `PASS` (`1.000000`) | `167` / `258` / **`154`** | `182` / `219` / **`169` (`-7.1%` vs S, `-22.8%` vs T)** | `0.0129` / `0.0787` -> **`0.1434`** |
| **IQM Garnet** *(20Q Crystal)* | `QAOA_MaxCut_8Q` | `PASS` (`1.000000`) | `190` / `239` / **`185`** | `75` / `105` / **`75` (`-28.6%` vs T)** | `0.8696` / `0.8153` -> **`0.9117`** |
| **IQM Garnet** *(20Q Crystal)* | `QAOA_MaxCut_12Q` | `PASS` (`1.000000`) | `272` / `393` / **`250`** | `105` / `132` / **`104` (`-1.0%` vs S, `-21.2%` vs T)** | `0.4825` / `0.4774` -> **`0.5800`** |
| **IQM Garnet** *(20Q Crystal)* | `QFT_8Q` | `PASS` (`1.000000`) | `165` / `204` / **`165`** | `55` / `57` / **`50` (`-9.1%` vs S, `-12.3%` vs T)** | `0.8467` / `0.8208` -> **`0.9290`** |
| **IQM Garnet** *(20Q Crystal)* | `QFT_12Q` | `PASS` (`1.000000`) | `276` / `365` / **`231`** | `97` / `114` / **`89` (`-8.2%` vs S, `-21.9%` vs T)** | `0.4629` / `0.4096` -> **`0.5560`** |
| **IQM Garnet** *(20Q Crystal)* | `Dense_AllToAll_17Q` | `PASS` (`1.000000`) | `175` / `262` / **`151`** | `135` / `204` / **`131` (`-3.0%` vs S, `-35.8%` vs T)** | `0.0500` / `0.0142` -> **`0.2012`** |
| **IQM Garnet** *(20Q Crystal)* | `Dense_AllToAll_18Q` | `PASS` (`1.000000`) | `184` / `263` / **`222`** | `159` / `207` / **`163` (`-21.3%` vs T)** | `0.0215` / `0.0081` -> **`0.1370`** |
| **IQM Garnet** *(20Q Crystal)* | `Dense_AllToAll_19Q` | `PASS` (`1.000000`) | `169` / `321` / **`166`** | `169` / `276` / **`169` (`-38.8%` vs T)** | `0.0476` / `0.0041` -> **`0.0801`** |

---

## 6. Repository Files & Prometheus Dynamics Public Portfolio Index

### Files in This Repository
- [`aws_braket_qpu_14_jobs_ledger.json`](./aws_braket_qpu_14_jobs_ledger.json) - Live 14-task (`42-circuit`, `125,952-shot`) Amazon Braket `ProgramSet` hardware benchmark ledger across **Rigetti `Cepheus-1-108Q`**, **IQM `Garnet` (`20Q`)**, and **IQM `Emerald` (`54Q`)** with verifiable Task ARNs.
- [`ibm_heron_156q_verified_benchmarks.json`](./ibm_heron_156q_verified_benchmarks.json) - Reconciled 107-job (`321-circuit`, `4,964,352-shot`) physical 156Q IBM Heron benchmark ledger (`4Q`-`23Q`) + 3 documented unrecovered queue dispatches (`110` total dispatches).
- [`veloxq_h100_hybrid_benchmarks.json`](./veloxq_h100_hybrid_benchmarks.json) - Complete 15-point multi-seed VeloxQ NVIDIA H100 (`VeloxQH100_1`) scaling dataset (`4`-`1,029` QUBO binary variables), 6 compression tiers, 5 operational constraint models, and the 45-operation `1,029-variable` schedule (`26h`) + HiGHS MILP lower-bound certificate.
- [`verify_corpus_and_schedules.py`](./verify_corpus_and_schedules.py) - Standalone audit script verifying the 107-job IBM Heron corpus, the 14-job live Amazon Braket QPU corpus, and the 45-operation `1,029-variable` schedule feasibility.
- [`braket_local_validation_results.json`](./braket_local_validation_results.json) & [`validate_braket_local.py`](./validate_braket_local.py) - Archived structural compilation comparison metrics and Amazon Braket `LocalSimulator` logical-equivalence verifier.
- [`AWS_BRAKET_SCOPED_PROPOSAL.md`](./AWS_BRAKET_SCOPED_PROPOSAL.md) - Scoped Phase 1 Amazon Braket QPU experiment specification, live Braket QPU results, and cost breakdown.

### Related Public Repositories (`PrometheusDynamicsCanada`)
| Repository | Primary Focus |
| :--- | :--- |
| **[`Hybrid-Quantum-HPC-Benchmarks`](https://github.com/PrometheusDynamicsCanada/Hybrid-Quantum-HPC-Benchmarks)** *(This Repo)* | Master multi-cloud QPU (`121` completed 3-way jobs across AWS Braket & IBM Heron) and hybrid NVIDIA H100 (`4`-`1,029` QUBO binary variables) benchmark corpus and verification scripts. |
| **[`qpu-selection-execution-quality`](https://github.com/PrometheusDynamicsCanada/qpu-selection-execution-quality)** | Cryptographically hashed (`SHA-256`) raw hardware execution packages, bitstring archives, and multi-QPU target-selection telemetry. |
| **[`prometheus-quantum-telemetry`](https://github.com/PrometheusDynamicsCanada/prometheus-quantum-telemetry)** | Distributional concentration (`TVD`, `JSD`, `Hellinger`), randomized-instance robustness (`4Q`-`20Q`), and scaling inflection-surface studies with verification scripts. |
| **[`prometheus-execution-intelligence`](https://github.com/PrometheusDynamicsCanada/prometheus-execution-intelligence)** | Architectural overview of the Prometheus compilation, hardware-risk arbitration, and hybrid execution-selection stack. |

---

**Contact:**  
William Denyer - Founder, Prometheus Dynamics  
`william@prometheusdynamics.ca` | [`https://prometheusdynamics.ca`](https://prometheusdynamics.ca)

