# Prometheus Dynamics - Hybrid Quantum-HPC & Multi-QPU Benchmark Corpus

[![Platform](https://img.shields.io/badge/Platform-Prometheus%20Dynamics-4F46E5)](https://prometheusdynamics.ca)
[![AWS Braket QPUs](https://img.shields.io/badge/AWS%20Braket%20QPUs-12%20ProgramSet%20Tasks%20%7C%20119.8K%20Shots-FF9900)](./aws_braket_qpu_12_jobs_ledger.json)
[![IBM Quantum](https://img.shields.io/badge/IBM%20Heron%20156Q-107%20Completed%20Jobs%20%7C%204.96M%20Shots-054ADA)](./ibm_heron_156q_verified_benchmarks.json)
[![Hybrid HPC](https://img.shields.io/badge/NVIDIA%20H100%20%28VeloxQ%29-42%20Configs%20%7C%204%E2%86%921%2C029%20Binary%20Vars-00D1B2)](./veloxq_h100_hybrid_benchmarks.json)
[![AWS Braket Badge](https://img.shields.io/badge/AWS%20Braket-Verified%20Badge-FF9900)](https://www.credly.com/badges/b64dc9e8-8f3e-4996-8494-4acee97db732/public_url)

Official empirical hardware and hybrid-solver benchmark corpus for **Prometheus Dynamics** ([`https://prometheusdynamics.ca`](https://prometheusdynamics.ca)), documenting **119 completed 3-way physical quantum hardware benchmark jobs (`357` compiled circuits, `5,084,160` completed hardware shots)** across **six physical quantum processors** spanning **Amazon Braket (`Rigetti Cepheus-1-108Q`, `IQM Garnet` 20Q, `IQM Emerald` 54Q)** and **IBM Quantum (`ibm_marrakesh`, `ibm_fez`, `ibm_kingston` 156Q Heron)**, alongside **VeloxQ NVIDIA H100 physics-inspired QUBO solvers (`VeloxQH100_1`)** and the **Amazon Braket SDK (`LocalSimulator`)**.

> **Verification & Traceability:** All datasets include Amazon Braket Task ARNs, IBM Quantum Job IDs, pre-execution SHA-256 commitments, scheduling instance specifications, exact MILP lower-bound certificates, and standalone Python verification scripts (`verify_corpus_and_schedules.py`, `validate_braket_local.py`, and `validation_suite_144_executions/score_counts.py`).

---

## 1. Corpus Overview & Reconciled Execution Accounting

| Benchmark Pillar | Hardware / Environment | Reconciled Scale & Scope | Key Empirical Outcome |
| :--- | :--- | :--- | :--- |
| **Amazon Braket Live QPU Corpus** | **Rigetti `Cepheus-1-108Q`** (`108Q`), **IQM `Garnet`** (`20Q`), **IQM `Emerald`** (`54Q`) | **12 Completed 3-Way `ProgramSet` Tasks** (**`36` verbatim compiled circuits, `119,808` completed physical shots**) across `4Q`-`10Q` `Dense All-to-All`, `QFT`, and `QAOA MaxCut` ([`aws_braket_qpu_12_jobs_ledger.json`](./aws_braket_qpu_12_jobs_ledger.json)) | **100% (`12 / 12`) lower circuit depth and 2Q `CZ` gate count vs. both `SABRE O3` and `TKET`**; **`9 / 12` (`75.0%`) physical fidelity wins vs. `SABRE O3` (`3 / 3` on `QFT`, `5 / 6` on `Dense All-to-All`, `1 / 3` on `QAOA MaxCut`)**, led by **`+379.42%` (`4.79x`) fidelity vs. `SABRE O3` (`+887.34%` / `9.87x` vs. `TKET`) on Rigetti `Cepheus-1-108Q` (`9Q Dense All-to-All`)**, **`+116.13%` (`2.16x`) fidelity on `Cepheus-1-108Q` (`6Q Dense All-to-All`)**, **`+14.92%` fidelity (`-52.6%` TVD) on IQM `Emerald` (`6Q QFT`)**, and **`+9.39%` fidelity (`+43.1%` XEB) on IQM `Garnet` (`9Q Dense All-to-All`)** |
| **Pre-Committed 144-Execution Validation Suite** | **`ibm_marrakesh`**, **`ibm_fez`**, **`ibm_kingston`** *(156Q IBM Heron)* | **4 Packed `SamplerV2` Batch Jobs (`144` physical circuit runs, `147,456` shots, `48.0s` QPU usage)** across 6 families (`dense`, `bipartite`, `star`, `ising`, `qaoa`, `qft_phase` at `6Q, 9Q, 12Q`) with frozen pre-execution SHA-256 policy & backend commitments ([`validation_suite_144_executions/`](./validation_suite_144_executions/)) | **Beat `SABRE O3` on `16 / 18` (`88.9%`) and `TKET` on `15 / 18` (`83.3%`)** primary task metrics on `ibm_marrakesh` (`2 x 1,024` shots), winning **`6 / 6` (`100%`) of all `12Q` instances** and **`3 / 3` (`100%`) of `QAOA MaxCut` instances**; pre-committed multi-QPU dispatch (`C:ibm_kingston`) beat single-backend `SABRE O3` on **`6 / 6` (`100%`)** vs. `ibm_marrakesh` (`Fixed A`) & `ibm_fez` (`Fixed B`), and **`5 / 6` (`83.3%`)** vs. `ibm_kingston` (`Fixed C`) |
| **156Q Gate-QPU Compilation Corpus** | **`ibm_marrakesh`**, **`ibm_fez`**, **`ibm_kingston`** *(156Q IBM Heron)* | **107 Completed 3-Way Jobs** (**`321` compiled physical circuits, `4,964,352` completed physical shots**) across **18 qubit scales (`4Q`-`23Q`)** *(out of `110` total dispatches / `5,111,808` dispatched shots; `3` unrecovered queue dispatches documented)* | Beat **Quantinuum `TKET` on `100 / 107` (`93.5%`)** and **IBM `SABRE O3` on `80 / 107` (`74.8%`)** completed hardware triplets; up to **`-54.5%`** 2Q gate reduction vs. `TKET` and **`-34.8%`** vs. `SABRE O3` |
| **19Q Dense All-to-All ($K_{19}$) Survival** | **`ibm_marrakesh`**, **`ibm_fez`**, **`ibm_kingston`** *(156Q IBM Heron)* | **19-Qubit Dense All-to-All ($K_{19}$)** (`171` logical all-to-all pairs, `16,384 shots/compiler`) | Achieved **`24.26%`** (`ibm_kingston`), **`12.78%`** (`ibm_marrakesh`), and **`6.54%`** (`ibm_fez`) computational-basis distribution fidelity vs. `18.98%`, `6.27%`, and `3.57%` for `SABRE O3`; achieved **`70.45%` heavy-output probability (`HOP`)** on `ibm_kingston` (exceeding the `2/3` heavy-output reference threshold, vs. `63.28%` `SABRE O3` and `54.38%` `TKET`) |
| **Hybrid Quantum-HPC QUBO Compression** | **VeloxQ NVIDIA H100 (`VeloxQH100_1`)** + **156Q IBM Heron** | **42 Distinct Benchmark Configurations** (**`150` multi-seed H100 solver executions**) scaling from **`4` to `1,029` QUBO binary variables** | **`94.44%` variable compression (`72` $\to$ `4` binary variables, `0.0%` optimality gap)** mapped to **4 physical qubits** on IBM Heron (`94.04%-96.34%` distribution fidelity); **`10.0x`-`11.3x` (`3x3`)** and **`26.1x`-`34.0x` (`4x3`)** ground-state sampling boost on H100; **`1,029` binary variables (`15x3` schedule)** solved to the **`26h`** target horizon (`0.0%` horizon gap; `25h` unrestricted pure-$C_{\max}$ MILP lower bound) in **`5.26s`** |
| **Multi-Architecture Braket Verification** | **Amazon Braket SDK (`LocalSimulator`)** - **Rigetti Cepheus (108Q)** & **IQM Garnet (20Q)** | **7 Logical Workloads Verified at `4,096` Shots on `LocalSimulator` + 14 Archived 3-Compiler Structural Benchmarks** (`8Q` & `12Q` `QAOA MaxCut` + `QFT`, and optional `17Q`, `18Q`, `19Q` `Dense All-to-All` $\times$ `SABRE O3`, `TKET`, `Prometheus`) | **`7 / 7` (`100%`) logical equivalence (`1.000000`) on `LocalSimulator` (`4,096` shots)**; **`14 / 14` (`100%`) higher modeled execution fidelity (`simulated_fidelity` ↑) vs. both `SABRE O3` and `TKET`**; **`14 / 14` (`100%`) lower depth (↓) & 2Q gates (↓) vs. `TKET`**, and **`12 / 14` (`85.7%`) lower-or-equal depth & 2Q gates vs. `SABRE O3`** (with higher 2Q/depth on `Cepheus 12Q QFT` and `Garnet 18Q Dense`) |

### Quick-Start Independent Verification
Run both verification suites locally to audit the 107-job IBM Heron corpus, the 12-job live Amazon Braket QPU corpus, the 45-operation schedule feasibility, and Qiskit-to-Braket logical circuit equivalence:
```bash
python verify_corpus_and_schedules.py
python validate_braket_local.py
```

---

## 2. Metric Definitions & Methodological Boundaries

To ensure unambiguous interpretation across hardware and hybrid-solver benchmarks, all reported metrics follow strict definitions:

1. **Classical Computational-Basis Distribution Fidelity (`Bhattacharyya Overlap` $F_B$ ↑ vs. `Squared Hellinger Fidelity` $F_H = F_B^2$ ↑):**
   - Throughout [`ibm_heron_156q_verified_benchmarks.json`](./ibm_heron_156q_verified_benchmarks.json) and [`aws_braket_qpu_12_jobs_ledger.json`](./aws_braket_qpu_12_jobs_ledger.json), `fidelity` denotes the **Bhattacharyya distribution overlap** $F_B = \sum_{x \in \{0,1\}^n} \sqrt{P_{\text{ideal}}(x)\, P_{\text{meas}}(x)}$ (↑ higher is better) between the noiseless ideal Z-basis probability distribution $P_{\text{ideal}}(x)$ and the measured hardware bitstring distribution $P_{\text{meas}}(x)$. In [`validation_suite_144_executions/`](./validation_suite_144_executions/), `squared_hellinger_fidelity` denotes $F_H = F_B^2 = \left(\sum_x \sqrt{P_{\text{ideal}}(x)\, P_{\text{meas}}(x)}\right)^2$ (↑ higher is better).
   - This metric directly measures computational-basis output distribution preservation from shot histograms without requiring $4^n$ full quantum state tomography. It is reported alongside **Total Variation Distance** $\text{TVD} = \frac{1}{2}\sum_x |P_{\text{ideal}}(x) - P_{\text{meas}}(x)|$ and **Linear Cross-Entropy Benchmarking** $\text{XEB} = 2^n \sum_x P_{\text{ideal}}(x) P_{\text{meas}}(x) - 1$.
2. **Heavy-Output Probability (`HOP`) vs. Formal Quantum Volume (`QV`):**
   - On the 19-qubit dense all-to-all ($K_{19}$) benchmark on `ibm_kingston` (`dbajlrhgv2cc73e6vuj0`), Prometheus achieved a **Heavy-Output Probability (`HOP`) of `70.45%`** (exceeding the `2/3` / `66.67%` heavy-output reference threshold, compared to `63.28%` for `SABRE O3` and `54.38%` for `TKET`).
   - **Methodological Boundary:** Crossing `2/3` heavy-output probability on this deterministic $K_{19}$ workload establishes heavy-output survival on that specific 19-qubit dense circuit; it is **not** a formal Quantum Volume (`QV`) certification, which under Qiskit's protocol requires a random $\text{SU}(4)$ model-circuit ensemble evaluated across $\ge 100$ independent random trials with a $2\sigma$ confidence bound.
3. **Physical Qubits (`Q`) vs. QUBO Binary Variables:**
   - **Physical Qubits (`4Q` to `23Q` on `156Q` IBM Heron processors; `4Q` to `10Q` on live Amazon Braket QPUs)** refer exclusively to gate-model quantum circuits.
   - **QUBO Binary Variables (`4` to `1,029` binary decision variables)** refer to combinatorial Ising/QUBO formulations executed on the **VeloxQ NVIDIA H100 GPU solver (`VeloxQH100_1`)**. Only the compressed `4-variable` Tier-5 schedule formulation (and `8Q`/`9Q` small instances) are mapped directly to physical gate-model qubits (`4Q` on `ibm_marrakesh`, `ibm_kingston`, and `ibm_fez`).
4. **Corpus Accounting (`119` Completed 3-Way Hardware Benchmark Jobs Across IBM Quantum & Amazon Braket) & Unfavorable Cases:**
   - [`validation_suite_144_executions/`](./validation_suite_144_executions/) - Pre-committed 144-execution (`147,456-shot`, `48.0s` QPU time) multi-QPU validation suite across `ibm_marrakesh`, `ibm_fez`, and `ibm_kingston` (`4` packed `SamplerV2` jobs), including 18 logical OpenQASM 2.0 circuits, exact reference distributions, frozen pre-execution SHA-256 commitments (`commitments_hardware.json`), raw canonical counts (`results_hardware.json`), offline scorer (`score_counts.py`), and 3 scoreboards (`scoreboard_report_hardware.md`).
- [`aws_braket_qpu_12_jobs_ledger.json`](./aws_braket_qpu_12_jobs_ledger.json) contains **all 12 completed 3-way `ProgramSet` performance benchmark tasks** (`36` verbatim compiled circuits, `119,808` completed physical shots) across `4Q-10Q` workloads on **Rigetti `Cepheus-1-108Q`**, **IQM `Garnet` (`20Q`)**, and **IQM `Emerald` (`54Q`)**, with Amazon Braket Task ARNs for traceability. *(Two initial `17Q` pipeline connectivity smoke tests executed during endpoint setup - `arn:aws:braket:eu-north-1:893688540163:quantum-task/fe63dc72-97dc-4041-b8f4-f1f80a5ba92e` and `arn:aws:braket:us-west-1:893688540163:quantum-task/58b458c9-a1b7-4303-8345-ddc33b3d2254`, `6` circuits / `6,144` shots - are recorded here for account traceability and excluded from the `4Q-10Q` performance benchmark statistics.)*
   - [`ibm_heron_156q_verified_benchmarks.json`](./ibm_heron_156q_verified_benchmarks.json) contains **107 distinct completed 3-way hardware benchmark jobs** (`321` compiled physical circuits, `4,964,352` completed physical shots). Three earlier `8Q Dense All-to-All` queue dispatches (`db3v85svf2bc73ctral0`, `db3v85svf2bc73ctrakg`, `db3v85imb58s7388ed7g`, totaling `9` circuits and `147,456` dispatched shots) remained in `PENDING_IN_QUEUE` on an expired account session and are listed separately under `unrecovered_queue_dispatches` (`4,964,352 + 147,456 = 5,111,808` total dispatched shots across `110` dispatches).
   - **Retained Unfavorable Results:** All 119 completed performance benchmark jobs (`107` IBM Heron + `12` AWS Braket) are retained without cherry-picking, including all `27 / 107` IBM Heron cases and `3 / 12` AWS Braket cases where `SABRE O3` achieved higher computational-basis distribution fidelity. Retaining mixed outcomes demonstrates why workload- and calibration-specific multi-compiler arbitration is essential in production.

---

## 3. Live Multi-Cloud QPU Benchmarks (`SABRE O3` vs. `Quantinuum TKET` vs. `Prometheus`)

### 3A. Live Amazon Braket QPU Benchmarks (`Rigetti Cepheus-1-108Q`, `IQM Garnet` 20Q, `IQM Emerald` 54Q)

All 12 completed 3-way Amazon Braket `ProgramSet` tasks (`36` verbatim physical circuits, `119,808` physical shots) are recorded with AWS Task ARNs for traceability in [`aws_braket_qpu_12_jobs_ledger.json`](./aws_braket_qpu_12_jobs_ledger.json):

| Amazon Braket QPU | Workload & Width | Shots / Circuit | Depth (`S / T /` **`P`** ↓) | 2Q `CZ` (`S / T /` **`P`** ↓) | Distribution Fidelity $F_B$ (`SABRE / TKET ->` **`Prometheus`** ↑) | TVD (`SABRE / TKET ->` **`Prometheus`** ↓) | Amazon Braket Task ARN |
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

### 3B. Live 156-Qubit IBM Heron Benchmarks (`ibm_marrakesh`, `ibm_fez`, `ibm_kingston`)

All 107 completed 3-way hardware benchmark triplets (`321` physical circuits, `4,964,352` physical shots) are recorded in [`ibm_heron_156q_verified_benchmarks.json`](./ibm_heron_156q_verified_benchmarks.json). Representative highlights (`16,384 shots/compiler`):

| Target Processor | Live Job ID | Workload & Scale | Circuit Depth (`SABRE` / `TKET` / **`Prometheus`** ↓) | 2Q Gates (`SABRE` / `TKET` / **`Prometheus`** ↓) | Distribution Fidelity $F_B$ (↑) & HOP / XEB (`SABRE` / `TKET` $\to$ **`Prometheus`** ↑) |
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

### 3C. Pre-Committed 144-Execution Multi-QPU Validation Suite (`ibm_marrakesh`, `ibm_fez`, `ibm_kingston` - Oct 27, 2026)

[`validation_suite_144_executions/`](./validation_suite_144_executions/) contains a self-contained, offline-verifiable 144-execution validation suite across 6 circuit families (`dense`, `bipartite`, `star`, `ising`, `qaoa`, `qft_phase`) at `6Q`, `9Q`, and `12Q` (`18` logical OpenQASM 2.0 workloads in [`validation_suite_144_executions/generated/`](./validation_suite_144_executions/generated/)). All circuit SHA-256 commitments and multi-QPU target-dispatch decisions were frozen prior to hardware execution in [`commitments_hardware.json`](./validation_suite_144_executions/commitments_hardware.json).

| Batch Slot | Target Processor | IBM Quantum Job ID | Circuits Executed | Shots / Circuit | Total Shots | Official QPU Usage |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **Slot A (Block 1)** | **`ibm_marrakesh`** *(156Q)* | `dbghgkdrd2mc73cuo0jg` | `54` (`18 x 3`) | `1,024` | `55,296` | `17.0s` |
| **Slot A (Block 2)** | **`ibm_marrakesh`** *(156Q)* | `dbghgroiudkc73e4gvig` | `54` (`18 x 3`) | `1,024` | `55,296` | `17.0s` |
| **Slot B (9Q Broadcast)** | **`ibm_fez`** *(156Q)* | `dbghh7ljm0ks73egl000` | `18` (`6 x 3`) | `1,024` | `18,432` | `7.0s` |
| **Slot C (9Q Broadcast)** | **`ibm_kingston`** *(156Q)* | `dbgjtecdgr2s73crlre0` | `18` (`6 x 3`) | `1,024` | `18,432` | `7.0s` |
| **Total** | **3 Heron r2 QPUs** | **4 Packed `SamplerV2` Jobs** | **`144` Executions** | **`1,024`** | **`147,456` Shots** | **`48.0s`** |

- **Scoreboard 1 (3-Way Hardware Performance on Primary Backend A, `2 x 1,024` Shots):** Prometheus beat `SABRE O3` on **`16 / 18` (`88.9%`)** instances and beat `TKET` on **`15 / 18` (`83.3%`)** instances on each family's pre-specified primary task metric, winning **`6 / 6` (`100%`) of all `12Q` instances** and **`3 / 3` (`100%`) of `QAOA MaxCut` instances** (`qaoa_6q`, `qaoa_9q`, `qaoa_12q`), with a **`4.21x` (`0.0762` vs. `0.0181` SABRE / `0.0005` TKET)** target-state recovery advantage on `qft_phase_12q_s260528`.
- **Scoreboard 2 (Multi-QPU Broadcast & Pre-Committed Dispatch across `ibm_marrakesh`, `ibm_fez`, `ibm_kingston`):** Pre-committed `P-Dispatch` selected `C:ibm_kingston` prior to execution and beat fixed single-backend `SABRE O3` on **`6 / 6` (`100%`)** of the `9Q` broadcast cohort across `ibm_marrakesh` (`Fixed A`) and `ibm_fez` (`Fixed B`), and on `5 / 6` (`83.3%`) vs. `SABRE O3` on `ibm_kingston` (`Fixed C`).
- Full tables and offline scorer: [`validation_suite_144_executions/scoreboard_report_hardware.md`](./validation_suite_144_executions/scoreboard_report_hardware.md) and `python validation_suite_144_executions/score_counts.py validation_suite_144_executions/results_hardware.json`.

---

## 4. Hybrid Quantum-HPC Benchmarks on NVIDIA H100 (`VeloxQH100_1` - `4` to `1,029` QUBO Binary Variables)

[`veloxq_h100_hybrid_benchmarks.json`](./veloxq_h100_hybrid_benchmarks.json) documents all **42 distinct hybrid scheduling configurations** (including **150 multi-seed H100 executions** across 15 QUBO scaling models at 10 seeds $\times$ 4,096 reads/seed, 6 compression tiers, 5 operational constraint models, fleet dispatch, and cross-algorithm comparisons).

### 4A. 15-Point Multi-Seed Scaling Curve on VeloxQ NVIDIA H100 (`VeloxQH100_1`)

| Model & Formulation | QUBO Binary Variables (↓) | Seeds $\times$ Reads | Target Horizon (`H`) & Pure-$C_{\max}$ MILP LB | VeloxQ H100 Mean Makespan (`Horizon Gap` ↓) | Ground-State Hits (`/ 4,096` ↑) | Mean H100 Runtime (↓) |
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

| Target Braket QPU Topology | Algorithm & Scale | Stage 1 `LocalSimulator` (`4,096` Shots) | Archived Depth (`S` / `T` / `P` ↓) | Archived 2Q Gates (`S` / `T` / `P` ↓) | Archived Modeled Fidelity (`SABRE` / `TKET` -> **`Prometheus`** ↑) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Rigetti Cepheus** *(108Q Grid)* | `QAOA_MaxCut_8Q` | `PASS` (`1.000000`) | `180` / `254` / **`156`** | `74` / `105` / **`77` (`-26.7%` vs T)** | `0.7900` / `0.8871` -> **`0.9253`** |
| **Rigetti Cepheus** *(108Q Grid)* | `QAOA_MaxCut_12Q` | `PASS` (`1.000000`) | `261` / `398` / **`248`** | `106` / `168` / **`97` (`-8.5%` vs S, `-42.3%` vs T)** | `0.4375` / `0.5001` -> **`0.6014`** |
| **Rigetti Cepheus** *(108Q Grid)* | `QFT_8Q` | `PASS` (`1.000000`) | `163` / `197` / **`151`** | `54` / `57` / **`53` (`-1.9%` vs S, `-7.0%` vs T)** | `0.6932` / `0.9028` -> **`0.9396`** |
| **Rigetti Cepheus** *(108Q Grid)* | `QFT_12Q` | `PASS` (`1.000000`) | **`247`** / `347` / `261` | **`92`** / `117` / `93` (`-20.5%` vs T) | `0.3393` / `0.5396` -> **`0.6176`** |
| **Rigetti Cepheus** *(108Q Grid)* | `Dense_AllToAll_17Q` | `PASS` (`1.000000`) | `182` / `250` / **`129`** | `145` / `165` / **`125` (`-13.8%` vs S, `-24.2%` vs T)** | `0.0332` / `0.1536` -> **`0.2718`** |
| **Rigetti Cepheus** *(108Q Grid)* | `Dense_AllToAll_18Q` | `PASS` (`1.000000`) | `132` / `338` / **`113`** | `149` / `240` / **`131` (`-12.1%` vs S, `-45.4%` vs T)** | `0.0124` / `0.0508` -> **`0.2200`** |
| **Rigetti Cepheus** *(108Q Grid)* | `Dense_AllToAll_19Q` | `PASS` (`1.000000`) | `167` / `258` / **`154`** | `182` / `219` / **`169` (`-7.1%` vs S, `-22.8%` vs T)** | `0.0129` / `0.0787` -> **`0.1434`** |
| **IQM Garnet** *(20Q Crystal)* | `QAOA_MaxCut_8Q` | `PASS` (`1.000000`) | `190` / `239` / **`185`** | **`75`** / `105` / **`75` (`-28.6%` vs T)** | `0.8696` / `0.8153` -> **`0.9117`** |
| **IQM Garnet** *(20Q Crystal)* | `QAOA_MaxCut_12Q` | `PASS` (`1.000000`) | `272` / `393` / **`250`** | `105` / `132` / **`104` (`-1.0%` vs S, `-21.2%` vs T)** | `0.4825` / `0.4774` -> **`0.5800`** |
| **IQM Garnet** *(20Q Crystal)* | `QFT_8Q` | `PASS` (`1.000000`) | **`165`** / `204` / **`165`** | `55` / `57` / **`50` (`-9.1%` vs S, `-12.3%` vs T)** | `0.8467` / `0.8208` -> **`0.9290`** |
| **IQM Garnet** *(20Q Crystal)* | `QFT_12Q` | `PASS` (`1.000000`) | `276` / `365` / **`231`** | `97` / `114` / **`89` (`-8.2%` vs S, `-21.9%` vs T)** | `0.4629` / `0.4096` -> **`0.5560`** |
| **IQM Garnet** *(20Q Crystal)* | `Dense_AllToAll_17Q` | `PASS` (`1.000000`) | `175` / `262` / **`151`** | `135` / `204` / **`131` (`-3.0%` vs S, `-35.8%` vs T)** | `0.0500` / `0.0142` -> **`0.2012`** |
| **IQM Garnet** *(20Q Crystal)* | `Dense_AllToAll_18Q` | `PASS` (`1.000000`) | **`184`** / `263` / `222` | **`159`** / `207` / `163` (`-21.3%` vs T) | `0.0215` / `0.0081` -> **`0.1370`** |
| **IQM Garnet** *(20Q Crystal)* | `Dense_AllToAll_19Q` | `PASS` (`1.000000`) | `169` / `321` / **`166`** | **`169`** / `276` / **`169` (`-38.8%` vs T)** | `0.0476` / `0.0041` -> **`0.0801`** |

### 5B. Trapped-Ion (`AQT IBEX Q1` & `IonQ Forte 1`) & Neutral-Atom (`QuEra Aquila`) Cross-Paradigm Compilation & Scoped Budget

In addition to superconducting square/crystal lattices (`Rigetti Cepheus-1-108Q`, `IQM Garnet`, `IQM Emerald`), Prometheus natively compiles for **All-to-All Trapped-Ion QPUs (`AQT IBEX Q1` 12Q using `rxx/r/rz` and `IonQ Forte 1` 36Q using `rzz/gpi/gpi2`)** and **256-Qubit Neutral-Atom Rydberg AHS (`QuEra Aquila`)**:

| Target Trapped-Ion QPU | Native Basis | Workload | Compiled Depth (`SABRE` / `TKET` / **`Prometheus`**) | Native 2Q Gates (`SABRE` / `TKET` / **`Prometheus`**) | Native 1Q Pulses (`SABRE` / `TKET` / **`Prometheus`**) | Exact Ideal Fidelity |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **AQT `IBEX Q1` (`12Q`, `eu-north-1`)** | `['rxx', 'r', 'rz']` | `QFT_6Q` | `38` / `62` / **`27` (`-28.9%` vs S, `-56.5%` vs T)** | `24` / `39` / **`15` `rxx` (`-37.5%` vs S, `-61.5%` vs T)** | `97` / `132` / **`52` `r` (`-46.4%` vs S)** | `PASS (1.00000000)` |
| **IonQ `Forte 1` (`36Q`, `us-east-1`)** | `['rzz', 'gpi', 'gpi2']` | `QFT_6Q` | `226` / `223` / **`56` (`-75.2%` vs S, `-74.9%` vs T)** | `39` / `39` / **`15` `rzz` (`-61.5%` vs S & T)** | `591` / `561` / **`123` `gpi/gpi2` (`-79.2%` vs S)** | `PASS (1.00000000)` |

Full modular cross-paradigm budget in [`AWS_BRAKET_SCOPED_PROPOSAL.md`](./AWS_BRAKET_SCOPED_PROPOSAL.md):
- **Phase 1A Superconducting Core (`Rigetti Cepheus-1-108Q` + `IQM Garnet` 20Q, `24 ProgramSet` tasks / `294,912` shots):** **`$283.68 USD`** (`+$212.76 USD` for Phase 1B `17Q-19Q` extension = **`$496.44 USD`**).
- **Phase 2 Trapped-Ion All-to-All (`AQT IBEX Q1` 12Q `$215.10` + `IonQ Forte 1` 36Q `$291.60`, `24 ProgramSet` tasks / `12,600` shots):** **`+$506.70 USD`**.
- **Phase 3 Neutral-Atom Rydberg AHS (`QuEra Aquila` 256Q, `12 AHS` tasks / `6,000` shots):** **`+$63.60 USD`**.
- **Combined 5-Vendor Cross-Paradigm Total (`Rigetti` + `IQM` + `AQT` + `IonQ` + `QuEra`):** **`$853.98 USD` Core Cross-Paradigm** (`$1,066.74 USD` including Phase 1B `17Q-19Q` extension).

---

## 6. Repository Files & Prometheus Dynamics Public Portfolio Index

### Files in This Repository
- [`aws_braket_qpu_12_jobs_ledger.json`](./aws_braket_qpu_12_jobs_ledger.json) - Live 12-task (`36-circuit`, `119,808-shot`) Amazon Braket `ProgramSet` hardware benchmark ledger across **Rigetti `Cepheus-1-108Q`**, **IQM `Garnet` (`20Q`)**, and **IQM `Emerald` (`54Q`)** with AWS Task ARNs for traceability.
- [`ibm_heron_156q_verified_benchmarks.json`](./ibm_heron_156q_verified_benchmarks.json) - Reconciled 107-job (`321-circuit`, `4,964,352-shot`) physical 156Q IBM Heron benchmark ledger (`4Q`-`23Q`) + 3 documented unrecovered queue dispatches (`110` total dispatches).
- [`veloxq_h100_hybrid_benchmarks.json`](./veloxq_h100_hybrid_benchmarks.json) - Complete 15-point multi-seed VeloxQ NVIDIA H100 (`VeloxQH100_1`) scaling dataset (`4`-`1,029` QUBO binary variables), 6 compression tiers, 5 operational constraint models, and the 45-operation `1,029-variable` schedule (`26h`) + HiGHS MILP lower-bound certificate.
- [`verify_corpus_and_schedules.py`](./verify_corpus_and_schedules.py) - Standalone audit script verifying the 107-job IBM Heron corpus, the 12-job live Amazon Braket QPU corpus, and the 45-operation `1,029-variable` schedule feasibility.
- [`braket_local_validation_results.json`](./braket_local_validation_results.json) & [`validate_braket_local.py`](./validate_braket_local.py) - Archived structural compilation comparison metrics and Amazon Braket `LocalSimulator` logical-equivalence verifier.
- [`AWS_BRAKET_SCOPED_PROPOSAL.md`](./AWS_BRAKET_SCOPED_PROPOSAL.md) - Scoped Phase 1 Amazon Braket QPU experiment specification, live Braket QPU results, and cost breakdown.

## Prometheus Dynamics Public Repository Portfolio

| Repository | Scope & Empirical Dataset | Primary Verification Artifacts |
| :--- | :--- | :--- |
| **[`Hybrid-Quantum-HPC-Benchmarks`](https://github.com/PrometheusDynamicsCanada/Hybrid-Quantum-HPC-Benchmarks)** | **Multi-Cloud QPU & Hybrid GPU Corpus:** `12` live Amazon Braket `ProgramSet` tasks (`Rigetti Cepheus-1-108Q`, `IQM Garnet` 20Q, `IQM Emerald` 54Q), `107` IBM Heron 3-way jobs (`4Q`-`23Q`), `144`-execution pre-committed validation suite (`48.0s` QPU time), and `150` NVIDIA H100 (`VeloxQH100_1`) QUBO runs (`4` to `1,029` variables). | [`aws_braket_qpu_12_jobs_ledger.json`](https://github.com/PrometheusDynamicsCanada/Hybrid-Quantum-HPC-Benchmarks/blob/main/aws_braket_qpu_12_jobs_ledger.json), [`ibm_heron_156q_verified_benchmarks.json`](https://github.com/PrometheusDynamicsCanada/Hybrid-Quantum-HPC-Benchmarks/blob/main/ibm_heron_156q_verified_benchmarks.json), [`validation_suite_144_executions/`](https://github.com/PrometheusDynamicsCanada/Hybrid-Quantum-HPC-Benchmarks/tree/main/validation_suite_144_executions), `verify_corpus_and_schedules.py` |
| **[`IBM-Heron-156Q-Benchmarks`](https://github.com/PrometheusDynamicsCanada/IBM-Heron-156Q-Benchmarks)** | **156Q Heron r2 Scaling & Pre-Committed Suite:** `10` packed `SamplerV2` batch jobs (`441` physical circuits, `755,712` shots) across `ibm_fez`, `ibm_marrakesh`, and `ibm_kingston` covering `3Q`-`13Q` odd/even parity scaling, a `15-algorithm` matrix at `9Q`, and the `144-execution` pre-committed validation suite. | [`data/heron_156q_99tournaments_297circuits.csv`](https://github.com/PrometheusDynamicsCanada/IBM-Heron-156Q-Benchmarks/blob/main/data/heron_156q_99tournaments_297circuits.csv), [`validation_suite_144_executions/`](https://github.com/PrometheusDynamicsCanada/IBM-Heron-156Q-Benchmarks/tree/main/validation_suite_144_executions), `scripts/verify_ledger.py` |
| **[`qpu-selection-execution-quality`](https://github.com/PrometheusDynamicsCanada/qpu-selection-execution-quality)** | **Cryptographic Provenance & Cross-QPU Arbitration:** Archived IBM Quantum job ZIP bundles and `SHA-256` manifests (`16Q`-`23Q` dense all-to-all across `ibm_fez`, `ibm_kingston`, and `ibm_marrakesh`). | [`EVIDENCE_INDEX.md`](https://github.com/PrometheusDynamicsCanada/qpu-selection-execution-quality/blob/main/EVIDENCE_INDEX.md), [`REPOSITORY_SHA256SUMS.txt`](https://github.com/PrometheusDynamicsCanada/qpu-selection-execution-quality/blob/main/REPOSITORY_SHA256SUMS.txt), `Fez_Marrakesh_Kingston/3_verify_and_view.py` |
| **[`prometheus-quantum-telemetry`](https://github.com/PrometheusDynamicsCanada/prometheus-quantum-telemetry)** | **Mechanistic Operating Envelope (`01`-`05`):** Distributional concentration (`100k` shots/circuit), `40` randomized matched pairs, `3Q`-`10Q` scaling boundaries, `13Q` ground-state avoidance, and a `540`-PUB (`1.11M`-shot) 3-QPU sweep. | [`IBM_JOB_EVIDENCE_INDEX.csv`](https://github.com/PrometheusDynamicsCanada/prometheus-quantum-telemetry/blob/main/IBM_JOB_EVIDENCE_INDEX.csv), [`MASTER_RESULTS.csv`](https://github.com/PrometheusDynamicsCanada/prometheus-quantum-telemetry/blob/main/MASTER_RESULTS.csv), `verify_sha256_evidence.py` |
| **[`prometheus-execution-intelligence`](https://github.com/PrometheusDynamicsCanada/prometheus-execution-intelligence)** | **System Architecture & Execution-Selection Overview:** Multi-compiler candidate evaluation (`SABRE O3`, `TKET`, `Prometheus`), multi-QPU dispatch workflow, and Studio interface walkthrough. | [`ARCHITECTURE.md`](https://github.com/PrometheusDynamicsCanada/prometheus-execution-intelligence/blob/main/ARCHITECTURE.md), [`SCREENSHOT_GALLERY.md`](https://github.com/PrometheusDynamicsCanada/prometheus-execution-intelligence/blob/main/SCREENSHOT_GALLERY.md) |
| **[`Hyperion-fusion-telemetry`](https://github.com/PrometheusDynamicsCanada/Hyperion-fusion-telemetry)** | **Multi-Tokamak Disruption Forecasting Telemetry:** `4,121` supervised holdout discharges (`ASIPP EAST`, `GA DIII-D`, `MIT Alcator C-Mod`) with binary confusion matrices & 95% Wilson CIs, plus a `12,693`-shot `UKAEA MAST` archive audit (`2,017` disruptions). | [`data/holdout/cross_reactor_summary.csv`](https://github.com/PrometheusDynamicsCanada/Hyperion-fusion-telemetry/blob/main/data/holdout/cross_reactor_summary.csv), [`scripts/verify_classification_metrics.py`](https://github.com/PrometheusDynamicsCanada/Hyperion-fusion-telemetry/blob/main/scripts/verify_classification_metrics.py) |

---

**Contact:**  
William Denyer - Founder, Prometheus Dynamics  
`william@prometheusdynamics.ca` | [`https://prometheusdynamics.ca`](https://prometheusdynamics.ca)

