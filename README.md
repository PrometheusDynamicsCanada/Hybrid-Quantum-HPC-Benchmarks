# Prometheus Dynamics: Hybrid Quantum-HPC & Multi-QPU Benchmark Corpus

[![Platform](https://img.shields.io/badge/Platform-Prometheus%20Dynamics-4F46E5)](https://prometheusdynamics.ca)
[![AWS Braket QPUs](https://img.shields.io/badge/AWS%20Braket%20QPUs-12%20ProgramSet%20Tasks%20%7C%20119.8K%20Shots-FF9900)](./aws_braket_qpu_12_jobs_ledger.json)
[![IBM Quantum](https://img.shields.io/badge/IBM%20Heron%20156Q-107%20Completed%20Jobs%20%7C%204.96M%20Shots-054ADA)](./ibm_heron_156q_verified_benchmarks.json)
[![Hybrid HPC](https://img.shields.io/badge/NVIDIA%20H100%20%28VeloxQ%29-42%20Configs%20%7C%204%E2%86%921%2C029%20Binary%20Vars-00D1B2)](./veloxq_h100_hybrid_benchmarks.json)
[![AWS Braket Badge](https://img.shields.io/badge/AWS%20Braket-Verified%20Badge-FF9900)](https://www.credly.com/badges/b64dc9e8-8f3e-4996-8494-4acee97db732/public_url)

Official empirical hardware and hybrid-solver benchmark corpus for **Prometheus Dynamics** ([https://prometheusdynamics.ca](https://prometheusdynamics.ca)), documenting **119 completed 3-way physical quantum hardware benchmark jobs (357 compiled circuits, 5,084,160 completed hardware shots)** across six physical quantum processors spanning **Amazon Braket** (Rigetti Cepheus-1-108Q, IQM Garnet 20Q, IQM Emerald 54Q) and **IBM Quantum** (`ibm_marrakesh`, `ibm_fez`, `ibm_kingston` 156Q Heron), alongside **VeloxQ NVIDIA H100** physics-inspired QUBO solvers (`VeloxQH100_1`) and the **Amazon Braket SDK** (`LocalSimulator`).

---

## 1. Executive Summary & Principal Comparative Corpus Table

### Key Takeaways

- **Amazon Braket Live QPU Corpus (12 ProgramSet Tasks, 36 Circuits, 119,808 Shots):** Prometheus achieved **100% (12/12)** lower circuit depth and 2Q CZ gate count vs. both **SABRE O3** and **TKET**, and **9/12 (75.0%)** physical fidelity wins vs. **SABRE O3**, highlighted by **+379.42% (4.79x)** fidelity on Rigetti Cepheus-1-108Q 9Q Dense All-to-All and **+14.92%** fidelity (-52.6% TVD) on IQM Emerald 6Q QFT.
- **156Q IBM Heron Compilation Corpus (107 Completed 3-Way Jobs, 321 Circuits, 4,964,352 Shots across 4Q-23Q):** Prometheus beat **Quantinuum TKET** on **100/107 (93.5%)** and **Qiskit SABRE O3** on **80/107 (74.8%)** completed hardware triplets, including **24.26%** distribution overlap F_B and **70.45% HOP** on 19-qubit Dense All-to-All (K_19) on `ibm_kingston` (`dbajlrhgv2cc73e6vuj0`).
- **Pre-Committed 144-Execution Multi-QPU Validation Suite (4 Batch Jobs, 144 Circuits, 147,456 Shots):** Beat **SABRE O3** on **16/18 (88.9%)** and **TKET** on **15/18 (83.3%)** primary task metrics on `ibm_marrakesh`, winning **6/6 (100.0%)** at 12Q, while pre-committed dispatch (`C:ibm_kingston`) beat single-backend **SABRE O3** on **6/6 (100.0%)** vs. `ibm_marrakesh` and `ibm_fez`.
- **Hybrid Quantum-HPC QUBO Compression (VeloxQ NVIDIA H100, 150 Multi-Seed Runs across 4 to 1,029 Variables):** Compressed a 72-variable 3x3 schedule by **94.44% (72 to 4 binary variables, 0.0% optimality gap)** for 4-qubit execution on IBM Heron (94.04%-96.34% F_B), boosted H100 ground-state sampling by **10.0x-34.0x**, and solved the **1,029-variable (15x3, 45-operation)** plant schedule to the **26h** target horizon in **5.26s**.

> [!NOTE]
> **Metric & Methodological Conventions:**
> - **Classical Distribution Overlap (F_B, ↑ higher is better) vs. Squared Hellinger Fidelity (F_H = F_B², ↑ higher is better):** In [`ibm_heron_156q_verified_benchmarks.json`](./ibm_heron_156q_verified_benchmarks.json) and [`aws_braket_qpu_12_jobs_ledger.json`](./aws_braket_qpu_12_jobs_ledger.json), `fidelity` denotes F_B = Σ_x √(P_ideal(x) · P_meas(x)). In [`validation_suite_144_executions/`](./validation_suite_144_executions/), `squared_hellinger_fidelity` denotes F_H = F_B².
> - **Total Variation Distance (TVD, ↓ lower is better):** 0.5 · Σ_x |P_ideal(x) - P_meas(x)|. **Linear XEB (↑):** 2ⁿ · Σ_x P_ideal(x) · P_meas(x) - 1.
> - **19Q K_19 Heavy-Output Probability (HOP):** Achieving 70.45% HOP (> 2/3) on deterministic K_19 establishes heavy-output survival on that circuit; it is distinct from formal Quantum Volume (QV) certification.
> - **Complete Retention:** All 119 completed 3-way QPU jobs (107 IBM Heron + 12 AWS Braket) are retained without cherry-picking, including all 27/107 IBM Heron and 3/12 AWS Braket cases where **SABRE O3** achieved higher F_B.

### Table 1: Corpus Overview & Reconciled Execution Accounting

| Benchmark Pillar | Hardware / Environment | Reconciled Scale & Scope | Key Empirical Outcome |
| :--- | :--- | :--- | :--- |
| **Amazon Braket Live QPU Corpus** | Rigetti `Cepheus-1-108Q` (108Q), IQM `Garnet` (20Q), IQM `Emerald` (54Q) | **12 Completed 3-Way `ProgramSet` Tasks** (36 circuits, 119,808 shots) across 4Q-10Q Dense All-to-All, QFT, and QAOA MaxCut ([`aws_braket_qpu_12_jobs_ledger.json`](./aws_braket_qpu_12_jobs_ledger.json)) | **12/12 (100.0%)** lower depth & 2Q CZ gates vs. SABRE O3 & TKET; **9/12 (75.0%)** F_B wins vs. SABRE O3, led by **+379.42% (4.79x)** on Cepheus 9Q Dense, **+116.13% (2.16x)** on Cepheus 6Q Dense, **+14.92%** (-52.6% TVD) on Emerald 6Q QFT, and **+9.39%** (+43.1% XEB) on Garnet 9Q Dense |
| **Pre-Committed 144-Execution Suite** | `ibm_marrakesh`, `ibm_fez`, `ibm_kingston` (156Q Heron) | **4 Packed `SamplerV2` Jobs** (144 circuits, 147,456 shots, 48.0s QPU usage) across 6 families at 6Q, 9Q, 12Q ([`validation_suite_144_executions/`](./validation_suite_144_executions/)) | **16/18 (88.9%)** wins vs. SABRE O3 and **15/18 (83.3%)** vs. TKET on `ibm_marrakesh`; **6/6 (100.0%)** wins at 12Q; pre-committed dispatch (`C:ibm_kingston`) won **6/6 (100.0%)** vs. Fixed A/B and **5/6 (83.3%)** vs. Fixed C |
| **156Q Gate-QPU Compilation Corpus** | `ibm_marrakesh`, `ibm_fez`, `ibm_kingston` (156Q Heron) | **107 Completed 3-Way Jobs** (321 circuits, 4,964,352 completed shots) across 18 qubit scales (4Q-23Q) *(plus 3 documented unrecovered queue dispatches)* | Beat **TKET on 100/107 (93.5%)** and **SABRE O3 on 80/107 (74.8%)** completed hardware triplets; up to **-54.5%** 2Q gate reduction vs. TKET and **-34.8%** vs. SABRE O3 |
| **19Q Dense All-to-All (K_19) Survival** | `ibm_marrakesh`, `ibm_fez`, `ibm_kingston` (156Q Heron) | **19-Qubit Dense All-to-All (K_19)** (171 logical all-to-all pairs, 16,384 shots/compiler) | Achieved **24.26%** (`ibm_kingston`), **12.78%** (`ibm_marrakesh`), and **6.54%** (`ibm_fez`) F_B vs. 18.98%, 6.27%, and 3.57% for SABRE O3; **70.45% HOP** on `ibm_kingston` (vs. 63.28% SABRE O3 and 54.38% TKET) |
| **Hybrid Quantum-HPC QUBO Compression** | VeloxQ NVIDIA H100 (`VeloxQH100_1`) + 156Q IBM Heron | **42 Benchmark Configurations** (150 multi-seed H100 runs) scaling from 4 to 1,029 QUBO binary variables ([`veloxq_h100_hybrid_benchmarks.json`](./veloxq_h100_hybrid_benchmarks.json)) | **94.44% variable compression** (72 to 4 binary variables, 0.0% gap) executed on 4Q IBM Heron (94.04%-96.34% F_B); **10.0x-34.0x** H100 ground-state hit boost; **1,029-variable (15x3)** schedule solved to **26h** horizon (0.0% horizon gap; 25h pure-C_max MILP LB) in **5.26s** |
| **Multi-Architecture Braket Verification** | Amazon Braket SDK (`LocalSimulator`): Rigetti Cepheus (108Q) & IQM Garnet (20Q) | **7 Logical Workloads Verified at 4,096 Shots + 14 Archived 3-Compiler Structural Benchmarks** (8Q-19Q × SABRE O3, TKET, Prometheus) | **7/7 (100.0%)** logical equivalence (1.000000) on `LocalSimulator`; **14/14 (100.0%)** higher modeled execution fidelity vs. SABRE O3 & TKET; **14/14 (100.0%)** lower depth & 2Q gates vs. TKET (**12/14** vs. SABRE O3) |

### Quick-Start Independent Verification

```bash
python verify_corpus_and_schedules.py
python validate_braket_local.py
python validation_suite_144_executions/score_counts.py validation_suite_144_executions/results_hardware.json
```

---

## 2. Live Multi-Cloud QPU Benchmarks (SABRE O3 vs. Quantinuum TKET vs. Prometheus)

### 2A. Live Amazon Braket QPU Benchmarks (12 ProgramSet Tasks, 36 Circuits, 119,808 Shots)

All 12 completed 3-way Amazon Braket `ProgramSet` tasks are recorded in [`aws_braket_qpu_12_jobs_ledger.json`](./aws_braket_qpu_12_jobs_ledger.json). *(Two initial 17Q pipeline connectivity smoke tests - `arn:aws:braket:eu-north-1:893688540163:quantum-task/fe63dc72-97dc-4041-b8f4-f1f80a5ba92e` and `arn:aws:braket:us-west-1:893688540163:quantum-task/58b458c9-a1b7-4303-8345-ddc33b3d2254`, 6 circuits / 6,144 shots - are documented in the ledger for account traceability and excluded from the 4Q-10Q performance statistics.)*

| Amazon Braket QPU | Workload & Width | Shots / Circ | Depth (S / T / **P** ↓) | 2Q CZ (S / T / **P** ↓) | Distribution Fidelity F_B (SABRE / TKET → **Prometheus** ↑) | TVD (S / T / **P** ↓) | Amazon Braket Task ARN |
| :--- | :--- | :---: | :---: | :---: | :--- | :---: | :--- |
| **Rigetti Cepheus-1-108Q** | Dense All-to-All (9Q) | 1,024 | 137 / 131 / **63** (-54.0%) | 80 / 83 / **54** (-32.5%) | 0.0435 / 0.0211 → **0.2088** (**+379.42%** vs S, **+887.34%** vs T; XEB **14.92** vs 1.65) | 0.9329 / 0.9515 / **0.7966** | `arn:aws:braket:us-west-1:893688540163:quantum-task/2df64966-8b30-4e19-a859-25efc2f2b136` |
| **Rigetti Cepheus-1-108Q** | Dense All-to-All (6Q) | 4,096 | 63 / 82 / **40** (-36.5%) | 31 / 33 / **23** (-25.8%) | 0.0880 / 0.0955 → **0.1903** (**+116.13%** vs S, **+99.23%** vs T; XEB **2.29** vs 0.20) | 0.9000 / 0.9034 / **0.8195** | `arn:aws:braket:us-west-1:893688540163:quantum-task/02427b15-5597-4721-95e1-b3d2547aafb8` |
| **IQM Emerald (54Q)** | Dense All-to-All (6Q) | 4,096 | 57 / 56 / **41** (-28.1%) | 28 / 33 / **23** (-17.9%) | 0.7322 / 0.5931 → **0.7853** (**+7.25%** vs S, **+32.39%** vs T; XEB **15.71** vs 13.67) | 0.3266 / 0.4296 / **0.2785** | `arn:aws:braket:eu-north-1:893688540163:quantum-task/b5317346-c659-4c3e-bd10-0c84df2e74d5` |
| **IQM Emerald (54Q)** | QFT (6Q) | 4,096 | 88 / 89 / **64** (-27.3%) | 44 / 48 / **38** (-13.6%) | 0.8355 / **0.9648** → 0.9602 (**+14.92%** vs S) | 0.3425 / **0.1575** / 0.1624 (-52.6% vs S) | `arn:aws:braket:eu-north-1:893688540163:quantum-task/68dbffa0-f842-48c4-bdf5-c95d5a69036b` |
| **IQM Garnet (20Q)** | Dense All-to-All (9Q) | 1,024 | 130 / 129 / **103** (-20.8%) | 79 / 87 / **70** (-11.4%) | 0.5513 / **0.6211** → 0.6031 (**+9.39%** vs S; XEB **5.71** vs 3.99; HOP **0.7764** #1) | 0.5341 / **0.4738** / 0.4790 | `arn:aws:braket:eu-north-1:893688540163:quantum-task/8a04e33b-e945-4ec7-b7da-2801a644f610` |
| **Rigetti Cepheus-1-108Q** | QAOA MaxCut (10Q, 3-Reg) | 4,096 | 66 / 91 / **47** (-28.8%) | 30 / 45 / **28** (-6.7%) | 0.7783 / 0.8268 → **0.8364** (**+7.46%** vs S, **+1.16%** vs T; 3-Way Winner) | 0.3413 / 0.2979 / **0.2783** | `arn:aws:braket:us-west-1:893688540163:quantum-task/6c662e9c-d64e-41b9-b7a2-bb10477e073f` |
| **Rigetti Cepheus-1-108Q** | QFT (8Q) | 4,096 | 181 / 261 / **129** (-28.7%) | 82 / 95 / **70** (-14.6%) | 0.9329 / 0.9528 → **0.9664** (**+3.58%** vs S, **+1.43%** vs T; 3-Way Winner) | 0.2039 / 0.1721 / **0.1467** (-28.1% vs S) | `arn:aws:braket:us-west-1:893688540163:quantum-task/eeee4e59-68e5-4ad0-b1fb-8b71dbd6638b` |
| **IQM Garnet (20Q)** | Dense All-to-All (4Q) | 4,096 | 25 / 26 / **22** (-12.0%) | 12 / 12 / **8** (-33.3%) | 0.9612 / 0.9430 → **0.9685** (**+0.76%** vs S, **+2.70%** vs T; 3-Way Winner) | 0.0769 / 0.1653 / **0.0676** | `arn:aws:braket:eu-north-1:893688540163:quantum-task/8875ef13-5943-4401-9c79-b2abb37e91f8` |
| **IQM Garnet (20Q)** | QFT (4Q) | 4,096 | 50 / 48 / **37** (-26.0%) | 18 / 21 / **14** (-22.2%) | 0.9791 / **0.9953** → 0.9836 (**+0.46%** vs S) | 0.1338 / **0.0527** / 0.1030 (-23.0% vs S) | `arn:aws:braket:eu-north-1:893688540163:quantum-task/904c6e83-0279-417f-a91c-080316c73ef0` |
| **IQM Garnet (20Q)** | QAOA MaxCut (4Q, 3-Reg) | 4,096 | 21 / 23 / **19** (-9.5%) | 9 / 9 / **7** (-22.2%) | **0.9967** / 0.9959 → 0.9944 (-0.23% vs S; shallow 4Q tie at >99.4%) | **0.0461** / 0.0520 / 0.0574 | `arn:aws:braket:eu-north-1:893688540163:quantum-task/7e3ad9a8-6038-4e5e-bf89-0b86bc425fe5` |
| **IQM Emerald (54Q)** | QAOA MaxCut (7Q, Bounded-Deg) | 4,096 | 36 / 47 / **34** (-5.6%) | 19 / 22 / **17** (-10.5%) | 0.9719 / **0.9802** → 0.9585 (-1.38% vs S) | 0.1316 / **0.1123** / 0.1621 | `arn:aws:braket:eu-north-1:893688540163:quantum-task/89cebd67-b2a4-460c-80a8-41e47b2a3d01` |
| **Rigetti Cepheus-1-108Q** | Dense All-to-All (9Q Run 1) | 1,024 | 125 / 131 / **87** (-30.4%) | 76 / 83 / **69** (-9.2%) | **0.2704** / 0.2233 → 0.2362 (+5.74% vs T; **HOP: 0.6260 #1** vs 0.5791 S & 0.5332 T) | **0.7389** / 0.7717 / 0.7710 | `arn:aws:braket:us-west-1:893688540163:quantum-task/f337ec8e-9348-4414-8a8d-10f2ed333d07` |

### 2B. Live 156-Qubit IBM Heron Benchmarks (`ibm_marrakesh`, `ibm_fez`, `ibm_kingston`)

All 107 completed 3-way hardware benchmark triplets (321 physical circuits, 4,964,352 physical shots) are recorded in [`ibm_heron_156q_verified_benchmarks.json`](./ibm_heron_156q_verified_benchmarks.json) *(with 3 unrecovered queue dispatches `db3v85svf2bc73ctral0`, `db3v85svf2bc73ctrakg`, `db3v85imb58s7388ed7g` listed separately under `unrecovered_queue_dispatches`)*. Representative highlights (16,384 shots/compiler):

| Target Processor | Live Job ID | Workload & Scale | Circuit Depth (SABRE / TKET / **Prometheus** ↓) | 2Q Gates (SABRE / TKET / **Prometheus** ↓) | Distribution Fidelity F_B (↑) & HOP / XEB (SABRE / TKET → **Prometheus** ↑) |
| :--- | :--- | :--- | :---: | :---: | :--- |
| `ibm_marrakesh` (156Q) | `dbajlqpgv2cc73e6vuhg` | 19Q Dense All-to-All (K_19) | 459 / 501 / **281** (-38.8%) | 482 / 717 / **358** (-25.7% vs S, -50.1% vs T) | 6.27% / 3.26% → **12.78%** (XEB **339.8** vs 148.6 SABRE) |
| `ibm_fez` (156Q) | `dbajlrhgv2cc73e6vuig` | 19Q Dense All-to-All (K_19) | 414 / 501 / **313** (-24.4%) | 429 / 717 / **390** (-9.1% vs S, -45.6% vs T) | 3.57% / 2.20% → **6.54%** (XEB **208.5** vs 126.9 SABRE) |
| `ibm_kingston` (156Q) | `dbajlrhgv2cc73e6vuj0` | 19Q Dense All-to-All (K_19) | 358 / 501 / **281** (-21.5%) | 444 / 717 / **358** (-19.4% vs S, -50.1% vs T) | 18.98% / 1.62% → **24.26%** (**70.45% HOP** vs 63.28% SABRE & 54.38% TKET) |
| `ibm_fez` (156Q) | `dbaign9gv2cc73e6u5sg` | 12Q QAOA MaxCut (3-Reg) | 124 / 212 / **115** (-7.3%) | 58 / 108 / **54** (-6.9% vs S, -50.0% vs T) | 86.12% / 88.35% → **91.21%** (**+5.91%** vs SABRE) |
| `ibm_marrakesh` (156Q) | `dbaehak24mrc73859340` | 12Q QAOA MaxCut (3-Reg) | **118** / 212 / 170 | 66 / 108 / **57** (-13.6% vs S, -47.2% vs T) | 83.88% / 83.18% → **90.67%** (**+8.10%** vs SABRE) |
| `ibm_marrakesh` (156Q) | `dbaignc24mrc7385fgbg` | 12Q QAOA MaxCut (3-Reg) | **106** / 212 / **106** | 54 / 108 / **51** (-5.6% vs S, -52.8% vs T) | 89.83% / 83.52% → **90.67%** (**+0.94%** vs SABRE, **+8.57%** vs TKET) |
| `ibm_kingston` (156Q) | `dbaign8c77vs7382smbg` | 12Q QAOA MaxCut (3-Reg) | **110** / 212 / 165 | 63 / 108 / **54** (-14.3% vs S, -50.0% vs T) | 89.14% / 85.52% → **90.02%** (**+1.00%** vs SABRE, **+5.27%** vs TKET) |
| `ibm_marrakesh` (156Q) | `dbaio50c77vs7382t5qg` | 12Q Quantum Fourier Transform | 375 / 573 / **329** (-12.3%) | 236 / 375 / **203** (-14.0% vs S, -45.9% vs T) | 89.76% / 79.18% → **91.17%** (**+1.57%** vs SABRE, **+15.14%** vs TKET) |
| `ibm_kingston` (156Q) | `dbaio4vi0auc73923sk0` | 12Q Quantum Fourier Transform | 394 / 573 / **288** (-26.9%) | 245 / 375 / **205** (-16.3% vs S, -45.3% vs T) | **85.73%** / 74.50% → 84.99% (**+14.08%** vs TKET; 3,882/4,096 states) |
| `ibm_marrakesh` (156Q) | `dbaijj9gv2cc73e6ubmg` | 8Q Quantum Fourier Transform | 226 / 288 / **175** (-22.6%) | 104 / 137 / **85** (-18.3% vs S, -38.0% vs T) | 98.62% / 95.79% → **99.29%** (**+0.67%** vs SABRE, -26.4% TVD error) |
| `ibm_kingston` (156Q) | `dbaijj9gv2cc73e6ubn0` | 8Q Quantum Fourier Transform | **186** / 288 / 207 | 91 / 137 / **85** (-6.6% vs S, -38.0% vs T) | 97.83% / 90.95% → **98.42%** (**+0.61%** vs SABRE, **+8.21%** vs TKET) |
| `ibm_marrakesh` (156Q) | `db9nfnfi0auc7390uvvg` | 4Q Compressed Schedule (K_4) | 33 / 34 / **27** (-18.2%) | 42 / 42 / **33** (-21.4%) | 90.12% / 91.85% → **96.34%** (**+6.90%** vs SABRE) |
| `ibm_kingston` (156Q) | `db9nflpgv2cc73e5q9l0` | 4Q Compressed Schedule (K_4) | 33 / 34 / **27** (-18.2%) | 42 / 42 / **33** (-21.4%) | 88.94% / 91.02% → **95.00%** (**+6.81%** vs SABRE) |
| `ibm_fez` (156Q) | `db9nfmvi0auc7390uvug` | 4Q Compressed Schedule (K_4) | 33 / 34 / **27** (-18.2%) | 42 / 42 / **33** (-21.4%) | 86.40% / 89.68% → **94.04%** (**+8.84%** vs SABRE) |

### 2C. Pre-Committed 144-Execution Multi-QPU Validation Suite (`validation_suite_144_executions/`)

| Batch Slot | Target Processor | IBM Quantum Job ID | Circuits Executed | Shots / Circuit | Total Shots | Official QPU Usage |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **Slot A (Block 1)** | `ibm_marrakesh` (156Q) | `dbghgkdrd2mc73cuo0jg` | 54 (18 × 3) | 1,024 | 55,296 | 17.0s |
| **Slot A (Block 2)** | `ibm_marrakesh` (156Q) | `dbghgroiudkc73e4gvig` | 54 (18 × 3) | 1,024 | 55,296 | 17.0s |
| **Slot B (9Q Broadcast)** | `ibm_fez` (156Q) | `dbghh7ljm0ks73egl000` | 18 (6 × 3) | 1,024 | 18,432 | 7.0s |
| **Slot C (9Q Broadcast)** | `ibm_kingston` (156Q) | `dbgjtecdgr2s73crlre0` | 18 (6 × 3) | 1,024 | 18,432 | 7.0s |
| **Total** | **3 Heron r2 QPUs** | **4 Packed `SamplerV2` Jobs** | **144 Executions** | **1,024** | **147,456 Shots** | **48.0s** |

- **Scoreboard 1 (3-Way Hardware Performance on `ibm_marrakesh`, 2 × 1,024 Shots):** Prometheus beat **SABRE O3** on **16/18 (88.9%)** instances and **TKET** on **15/18 (83.3%)** instances on each family's pre-specified primary task metric, winning **6/6 (100.0%)** of all 12Q instances and **3/3 (100.0%)** of QAOA MaxCut instances, with a **4.21x** (0.0762 vs. 0.0181 SABRE / 0.0005 TKET) target-state recovery advantage on `qft_phase_12q_s260528`.
- **Scoreboard 2 (Multi-QPU Broadcast & Pre-Committed Dispatch):** Pre-committed P-Dispatch selected `C:ibm_kingston` prior to execution and beat fixed single-backend **SABRE O3** on **6/6 (100.0%)** across `ibm_marrakesh` and `ibm_fez`, and **5/6 (83.3%)** vs. `ibm_kingston`.

---

## 3. Hybrid Quantum-HPC Benchmarks on NVIDIA H100 (`VeloxQH100_1`: 4 to 1,029 QUBO Binary Variables)

[`veloxq_h100_hybrid_benchmarks.json`](./veloxq_h100_hybrid_benchmarks.json) documents all **42 distinct hybrid scheduling configurations** (150 multi-seed H100 executions across 15 QUBO scaling models at 10 seeds × 4,096 reads/seed, 6 compression tiers, 5 operational constraint models, fleet dispatch, and cross-algorithm comparisons).

| Model & Formulation | QUBO Binary Variables (↓) | Seeds × Reads | Target Horizon (H) & Pure-C_max MILP LB | VeloxQ H100 Mean Makespan *(mean)* (Horizon Gap ↓) | Ground-State Hits (/ 4,096 ↑) | Mean H100 Runtime *(mean)* (↓) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `3x3 Tier-5 Compressed Basis` *(also run on 4Q IBM Heron)* | **4 vars** *(vs. 72 naive)* | 10 × 4,096 | 8h (LB = 8h) | **8.0h (0.0%)** | 1,644 / 4,096 (40.14%) | 0.138s |
| `2x2 Tier-1 Reduced` | **8 vars** *(vs. 16 naive)* | 10 × 4,096 | 4h (LB = 4h) | **4.0h (0.0%)** | 4,096 / 4,096 (100.0%) | 0.143s |
| `3x3 Tier-4 Compact` | **9 vars** *(vs. 72 naive)* | 10 × 4,096 | 8h (LB = 8h) | **8.0h (0.0%)** | 1,410 / 4,096 (34.42%) | 0.140s |
| `2x2 Naive Time-Indexed` | **16 vars** | 10 × 4,096 | 4h (LB = 4h) | **4.0h (0.0%)** | 4,064 / 4,096 (99.22%) | 0.141s |
| `3x3 Tier-3 Compact Slack` | **21 vars** *(vs. 72 naive)* | 10 × 4,096 | 8h (LB = 8h) | **8.0h (0.0%)** | 4,096 / 4,096 (100.0%) | **0.002s** |
| `3x3 Tier-2 Reduced` | **28 vars** *(vs. 72 naive)* | 10 × 4,096 | 8h (LB = 8h) | **8.0h (0.0%)** | 830 / 4,096 (20.26%) | 0.152s |
| `3x3 Tier-1 Reduced` *(10.0x-11.3x hit boost vs. 72-var)* | **39 vars** *(vs. 72 naive)* | 10 × 4,096 | 8h (LB = 8h) | **8.0h (0.0%)** | 807 / 4,096 (19.70%) | 0.159s |
| `4x3 Tier-1 Reduced` *(26.1x-34.0x hit boost vs. 108-var)* | **63 vars** *(vs. 108 naive)* | 10 × 4,096 | 9h (LB = 9h) | **9.0h (0.0%)** | 653 / 4,096 (15.94%) | 0.174s |
| `3x3 Naive Time-Indexed` | **72 vars** | 10 × 4,096 | 8h (LB = 8h) | **8.0h (0.0%)** | 81 / 4,096 (1.98%) | 0.189s |
| `4x3 Naive Time-Indexed` | **108 vars** | 10 × 4,096 | 9h (LB = 9h) | **9.0h (0.0%)** | 25 / 4,096 (0.61%) | 0.226s |
| `6x3 Tier-1 Reduced` | **135 vars** *(vs. 198 naive)* | 10 × 4,096 | 11h (LB = 11h) | **11.0h (0.0%)** | 54 / 4,096 (1.32%) | 0.255s |
| `8x3 Tier-1 Reduced` | **255 vars** *(vs. 336 naive)* | 10 × 4,096 | 14h (LB = 14h) | **14.0h (0.0%)** | 1 / 4,096 (0.02%) | 0.446s |
| `10x3 Tier-1 Reduced` | **414 vars** *(vs. 510 naive)* | 10 × 4,096 | 17h (LB = 17h) | **17.0h (0.0%)** | 1 / 4,096 (0.02%) | 1.531s |
| `12x3 Tier-1 Reduced` | **570 vars** *(vs. 684 naive)* | 10 × 4,096 | 19h (LB = 19h) | **19.0h (0.0%)** | 1 / 4,096 (0.02%) | 2.300s |
| `15x3 Tier-1 Reduced Plant Schedule` | **1,029 vars** *(vs. 1,170 naive)* | 10 × 4,096 | H = 26h (Pure-C_max LB = 25h) | **26.0h (0.0% vs H=26h)** | 1 / 4,096 (0.02%) | 5.257s |

- **1,029-Variable (15x3, 45-Operation) Feasibility Certificate:** [`veloxq_h100_hybrid_benchmarks.json`](./veloxq_h100_hybrid_benchmarks.json) (`plant_scale_15x3_1029var_verification_artifact`) provides the 15-job × 3-machine duration table (T = 22h, F = 21h, S = 19h), the analytical 24h head-plus-tail lower bound, the 25h unrestricted HiGHS MILP reference schedule, and all 45 scheduled start/end intervals (`veloxq_h100_optimal_schedule_45_ops`) verified for zero machine overlap and strict precedence by `python verify_corpus_and_schedules.py`.

---

## 4. Amazon Braket Local Verification & Cross-Paradigm Compilation

<details>
<summary><strong>Stage 1 & 2: Amazon Braket LocalSimulator Equivalence & 14 Archived Structural Benchmarks (<code>validate_braket_local.py</code>)</strong></summary>

Running `python validate_braket_local.py` verifies 7 logical workloads at 4,096 shots on Amazon Braket `LocalSimulator("default")` (`1.000000` distribution equivalence, 7/7 PASS) and displays the 14 archived 3-compiler structural benchmarks from [`braket_local_validation_results.json`](./braket_local_validation_results.json):

| Target Braket QPU Topology | Algorithm & Scale | Stage 1 `LocalSimulator` (4,096 Shots) | Archived Depth (S / T / P ↓) | Archived 2Q Gates (S / T / P ↓) | Archived Modeled Fidelity (SABRE / TKET → **Prometheus** ↑) |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **Rigetti Cepheus (108Q Grid)** | `QAOA_MaxCut_8Q` | PASS (1.000000) | 180 / 254 / **156** | **74** / 105 / 77 (-26.7% vs T) | 0.7900 / 0.8871 → **0.9253** |
| **Rigetti Cepheus (108Q Grid)** | `QAOA_MaxCut_12Q` | PASS (1.000000) | 261 / 398 / **248** | 106 / 168 / **97** (-8.5% vs S, -42.3% vs T) | 0.4375 / 0.5001 → **0.6014** |
| **Rigetti Cepheus (108Q Grid)** | `QFT_8Q` | PASS (1.000000) | 163 / 197 / **151** | 54 / 57 / **53** (-1.9% vs S, -7.0% vs T) | 0.6932 / 0.9028 → **0.9396** |
| **Rigetti Cepheus (108Q Grid)** | `QFT_12Q` | PASS (1.000000) | **247** / 347 / 261 | **92** / 117 / 93 (-20.5% vs T) | 0.3393 / 0.5396 → **0.6176** |
| **Rigetti Cepheus (108Q Grid)** | `Dense_AllToAll_17Q` | PASS (1.000000) | 182 / 250 / **129** | 145 / 165 / **125** (-13.8% vs S, -24.2% vs T) | 0.0332 / 0.1536 → **0.2718** |
| **Rigetti Cepheus (108Q Grid)** | `Dense_AllToAll_18Q` | PASS (1.000000) | 132 / 338 / **113** | 149 / 240 / **131** (-12.1% vs S, -45.4% vs T) | 0.0124 / 0.0508 → **0.2200** |
| **Rigetti Cepheus (108Q Grid)** | `Dense_AllToAll_19Q` | PASS (1.000000) | 167 / 258 / **154** | 182 / 219 / **169** (-7.1% vs S, -22.8% vs T) | 0.0129 / 0.0787 → **0.1434** |
| **IQM Garnet (20Q Crystal)** | `QAOA_MaxCut_8Q` | PASS (1.000000) | 190 / 239 / **185** | **75** / 105 / **75** (-28.6% vs T) | 0.8696 / 0.8153 → **0.9117** |
| **IQM Garnet (20Q Crystal)** | `QAOA_MaxCut_12Q` | PASS (1.000000) | 272 / 393 / **250** | 105 / 132 / **104** (-1.0% vs S, -21.2% vs T) | 0.4825 / 0.4774 → **0.5800** |
| **IQM Garnet (20Q Crystal)** | `QFT_8Q` | PASS (1.000000) | **165** / 204 / **165** | 55 / 57 / **50** (-9.1% vs S, -12.3% vs T) | 0.8467 / 0.8208 → **0.9290** |
| **IQM Garnet (20Q Crystal)** | `QFT_12Q` | PASS (1.000000) | 276 / 365 / **231** | 97 / 114 / **89** (-8.2% vs S, -21.9% vs T) | 0.4629 / 0.4096 → **0.5560** |
| **IQM Garnet (20Q Crystal)** | `Dense_AllToAll_17Q` | PASS (1.000000) | 175 / 262 / **151** | 135 / 204 / **131** (-3.0% vs S, -35.8% vs T) | 0.0500 / 0.0142 → **0.2012** |
| **IQM Garnet (20Q Crystal)** | `Dense_AllToAll_18Q` | PASS (1.000000) | **184** / 263 / 222 | **159** / 207 / 163 (-21.3% vs T) | 0.0215 / 0.0081 → **0.1370** |
| **IQM Garnet (20Q Crystal)** | `Dense_AllToAll_19Q` | PASS (1.000000) | 169 / 321 / **166** | **169** / 276 / **169** (-38.8% vs T) | 0.0476 / 0.0041 → **0.0801** |

</details>

### Trapped-Ion (AQT IBEX Q1 & IonQ Forte 1) Native Basis Compilation

| Target Trapped-Ion QPU | Native Basis | Workload | Compiled Depth (SABRE / TKET / **Prometheus** ↓) | Native 2Q Gates (SABRE / TKET / **Prometheus** ↓) | Native 1Q Pulses (SABRE / TKET / **Prometheus** ↓) | Exact Ideal Fidelity (↑) |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: |
| **AQT IBEX Q1 (12Q, `eu-north-1`)** | `['rxx', 'r', 'rz']` | `QFT_6Q` | 38 / 62 / **27** (-28.9% vs S, -56.5% vs T) | 24 / 39 / **15 `rxx`** (-37.5% vs S, -61.5% vs T) | 97 / 132 / **52 `r`** (-46.4% vs S) | **PASS (1.00000000)** |
| **IonQ Forte 1 (36Q, `us-east-1`)** | `['rzz', 'gpi', 'gpi2']` | `QFT_6Q` | 226 / 223 / **56** (-75.2% vs S, -74.9% vs T) | 39 / 39 / **15 `rzz`** (-61.5% vs S & T) | 591 / 561 / **123 `gpi/gpi2`** (-79.2% vs S) | **PASS (1.00000000)** |

See [`AWS_BRAKET_SCOPED_PROPOSAL.md`](./AWS_BRAKET_SCOPED_PROPOSAL.md) for the modular 5-vendor cross-paradigm specification (283.68 USD Phase 1A superconducting core, +212.76 USD Phase 1B 17Q-19Q extension, +506.70 USD Phase 2 trapped-ion, +63.60 USD Phase 3 neutral-atom Rydberg AHS = 853.98 USD Core / 1,066.74 USD with Phase 1B).

---

## 5. Repository Files & Prometheus Dynamics Public Portfolio Index

- [`aws_braket_qpu_12_jobs_ledger.json`](./aws_braket_qpu_12_jobs_ledger.json) - Live 12-task (36-circuit, 119,808-shot) Amazon Braket `ProgramSet` hardware benchmark ledger with AWS Task ARNs.
- [`ibm_heron_156q_verified_benchmarks.json`](./ibm_heron_156q_verified_benchmarks.json) - Reconciled 107-job (321-circuit, 4,964,352-shot) physical 156Q IBM Heron benchmark ledger (4Q-23Q) + 3 documented unrecovered queue dispatches.
- [`veloxq_h100_hybrid_benchmarks.json`](./veloxq_h100_hybrid_benchmarks.json) - Complete 15-point multi-seed VeloxQ NVIDIA H100 (`VeloxQH100_1`) scaling dataset (4-1,029 QUBO binary variables) and 45-operation 1,029-variable schedule certificate.
- [`verify_corpus_and_schedules.py`](./verify_corpus_and_schedules.py) & [`validate_braket_local.py`](./validate_braket_local.py) - Standalone audit scripts verifying all ledgers, schedules, and Braket `LocalSimulator` equivalence.

### Prometheus Dynamics Public Repository Portfolio (9 repositories | 248 benchmark jobs | 5,110 physical circuits/PUBs | 13,264,640 physical shots)

**Portfolio Totals:** 9 Verified Repositories | 248 Completed Benchmark Jobs/Tasks (167 IBM Heron Jobs, 22 AWS Braket Tasks, 59 IQM Resonance Jobs) | 5,110 Physical Circuits/PUBs | 13,264,640 Physical Measurement Shots

Counts refer to completed public benchmark executions, excluding simulations, classical GPU runs, unrecovered queue dispatches, and two setup smoke tests. Shared datasets are counted once (`IBM-Heron-156Q-Benchmarks` includes the 4-job 144-circuit pre-committed suite, and `Hybrid-Quantum-HPC-Benchmarks` includes all 33 archived job ZIPs from `qpu-selection-execution-quality`).

| Repository | Scope & Empirical Dataset | Primary Verification Artifacts |
| :--- | :--- | :--- |
| **[`IQM-Resonance-Spatial-Multiplexing`](https://github.com/PrometheusDynamicsCanada/IQM-Resonance-Spatial-Multiplexing)** | **IQM Emerald (54Q) Dense-Circuit Optimization & Spatial Multiplexing:** 59 scored hardware jobs (1,479 physical circuits/PUBs, 1,935 workload evaluations, 1,135,616 physical shots): 19-job Dense-Circuit Optimization, Odd/Even Parity, & Matched-Placement Campaign (739 circuits, 756,736 shots, **+3.73%** vs. SABRE K8, **+7.57%** vs. Pure TKET K8, **16/16** matched-placement wins) + 40-job Spatial Multiplexing & Prospective Scheduler Campaign (740 PUBs, 1,196 evaluations, **3.30x** 4-Way throughput). | [`data/dense_campaign_stages2_3_4_results.json`](https://github.com/PrometheusDynamicsCanada/IQM-Resonance-Spatial-Multiplexing/blob/main/data/dense_campaign_stages2_3_4_results.json), [`data/stage2_emerald_replication_results.json`](https://github.com/PrometheusDynamicsCanada/IQM-Resonance-Spatial-Multiplexing/blob/main/data/stage2_emerald_replication_results.json), [`scripts/verify_iqm_resonance_ledger.py`](https://github.com/PrometheusDynamicsCanada/IQM-Resonance-Spatial-Multiplexing/blob/main/scripts/verify_iqm_resonance_ledger.py) |
| **[`Quantum-Execution-Manager-Spatial-Multiplexing`](https://github.com/PrometheusDynamicsCanada/Quantum-Execution-Manager-Spatial-Multiplexing)** | **IBM Heron 8-Way Spatial Multiplexing & Multi-Compiler Meta-Selection:** 19 completed hardware jobs (586 physical PUBs, 1,140 workload evaluations, 655,360 physical shots) across `ibm_fez`, `ibm_marrakesh`, and `ibm_kingston` (**2.85x** qualifying workloads per billed second, **-57.1%** billed time, and SABRE/TKET/Prometheus interoperability). | [`data/campaign3_compiler_interoperability_results.json`](https://github.com/PrometheusDynamicsCanada/Quantum-Execution-Manager-Spatial-Multiplexing/blob/main/data/campaign3_compiler_interoperability_results.json), [`scripts/verify_spatial_multiplexing_campaigns.py`](https://github.com/PrometheusDynamicsCanada/Quantum-Execution-Manager-Spatial-Multiplexing/blob/main/scripts/verify_spatial_multiplexing_campaigns.py) |
| **[`IBM-Heron-Extended-Validation-1023-Circuits`](https://github.com/PrometheusDynamicsCanada/IBM-Heron-Extended-Validation-1023-Circuits)** | **4-Pillar Extended IBM Heron r2 Validation (1,023 Circuits):** 17 batch jobs (1,023 physical circuits, 1,047,552 physical shots) across `ibm_marrakesh`, `ibm_fez`, and `ibm_kingston` (**+3.27%** mean F_B vs. SABRE O3 in Pillar 1A, **+6.67%** F_H with QPU dispatch, and 8Q-101Q Clifford mirror scaling). | [`ALL_1023_CIRCUITS_RESULTS.csv`](https://github.com/PrometheusDynamicsCanada/IBM-Heron-Extended-Validation-1023-Circuits/blob/main/ALL_1023_CIRCUITS_RESULTS.csv), [`scripts/verify_campaign.py`](https://github.com/PrometheusDynamicsCanada/IBM-Heron-Extended-Validation-1023-Circuits/blob/main/scripts/verify_campaign.py) |
| **[`AWS-Braket-Multi-Window-Validation`](https://github.com/PrometheusDynamicsCanada/AWS-Braket-Multi-Window-Validation)** | **Rigetti Cepheus-1-108Q 3-Window Replication & Cross-Provider Comparison:** 10 AWS Braket `ProgramSet` tasks (450 physical circuits, 460,800 physical shots) across 3 calibration windows (**+3.91%** vs. SABRE O3, p_Holm = 0.0112; **+9.03%** vs. TKET, p_Holm = 0.000641). | [`data/ALL_450_BRAKET_CIRCUITS_RESULTS.csv`](https://github.com/PrometheusDynamicsCanada/AWS-Braket-Multi-Window-Validation/blob/main/data/ALL_450_BRAKET_CIRCUITS_RESULTS.csv), [`scripts/verify_braket_campaign.py`](https://github.com/PrometheusDynamicsCanada/AWS-Braket-Multi-Window-Validation/blob/main/scripts/verify_braket_campaign.py) |
| **[`IBM-Heron-156Q-Benchmarks`](https://github.com/PrometheusDynamicsCanada/IBM-Heron-156Q-Benchmarks)** | **156Q Heron r2 Scaling & Pre-Committed Suite:** 10 packed `SamplerV2` batch jobs (441 physical circuits, 755,712 shots) across `ibm_fez`, `ibm_marrakesh`, and `ibm_kingston` covering 3Q-13Q odd/even parity scaling, a 15-algorithm matrix at 9Q (297 circuits), and the 144-execution pre-committed validation suite (4 jobs). | [`data/heron_156q_99tournaments_297circuits.csv`](https://github.com/PrometheusDynamicsCanada/IBM-Heron-156Q-Benchmarks/blob/main/data/heron_156q_99tournaments_297circuits.csv), [`validation_suite_144_executions/`](https://github.com/PrometheusDynamicsCanada/IBM-Heron-156Q-Benchmarks/tree/main/validation_suite_144_executions), `scripts/verify_ledger.py` |
| **[`Hybrid-Quantum-HPC-Benchmarks`](https://github.com/PrometheusDynamicsCanada/Hybrid-Quantum-HPC-Benchmarks)** | **Multi-Cloud QPU & Hybrid GPU Corpus:** 119 unique 3-way QPU jobs/tasks (357 physical circuits, 5,084,160 shots: 107 IBM Heron jobs / 321 circuits / 4,964,352 shots + 12 AWS Braket `ProgramSet` tasks / 36 circuits / 119,808 shots), plus the shared 144-execution pre-committed suite and 150 NVIDIA H100 (`VeloxQH100_1`) QUBO runs (4 to 1,029 variables). | [`aws_braket_qpu_12_jobs_ledger.json`](https://github.com/PrometheusDynamicsCanada/Hybrid-Quantum-HPC-Benchmarks/blob/main/aws_braket_qpu_12_jobs_ledger.json), [`ibm_heron_156q_verified_benchmarks.json`](https://github.com/PrometheusDynamicsCanada/Hybrid-Quantum-HPC-Benchmarks/blob/main/ibm_heron_156q_verified_benchmarks.json), [`validation_suite_144_executions/`](https://github.com/PrometheusDynamicsCanada/Hybrid-Quantum-HPC-Benchmarks/tree/main/validation_suite_144_executions), `verify_corpus_and_schedules.py` |
| **[`qpu-selection-execution-quality`](https://github.com/PrometheusDynamicsCanada/qpu-selection-execution-quality)** | **Cryptographic Provenance & Cross-QPU Arbitration:** 33 archived IBM Quantum job ZIP bundles (99 physical circuits, 1,622,016 shots across 16Q-23Q in `Fez/`, `Kingston/`, `Marrakesh/`, and 20Q-22Q broadcast runs in `Fez_Marrakesh_Kingston/`, already counted in the 107-job historical IBM corpus) plus the shared 4-job 144-circuit pre-committed suite. | [`EVIDENCE_INDEX.md`](https://github.com/PrometheusDynamicsCanada/qpu-selection-execution-quality/blob/main/EVIDENCE_INDEX.md), [`REPOSITORY_SHA256SUMS.txt`](https://github.com/PrometheusDynamicsCanada/qpu-selection-execution-quality/blob/main/REPOSITORY_SHA256SUMS.txt), `Fez_Marrakesh_Kingston/3_verify_and_view.py` |
| **[`prometheus-quantum-telemetry`](https://github.com/PrometheusDynamicsCanada/prometheus-quantum-telemetry)** | **Mechanistic Operating Envelope (01-05):** 14 IBM Heron jobs (774 physical PUBs, 4,125,440 physical shots across all 14 archived `job-*-result.json` measurement arrays; 417 normalized circuit rows in `MASTER_RESULTS.csv` for Experiments 01-03) covering distributional concentration (100k shots/circuit), 40 randomized matched pairs, 3Q-10Q scaling boundaries, 13Q ground-state avoidance, and a 540-PUB (1,105,920-shot) 3-QPU mechanistic sweep. | [`IBM_JOB_EVIDENCE_INDEX.csv`](https://github.com/PrometheusDynamicsCanada/prometheus-quantum-telemetry/blob/main/IBM_JOB_EVIDENCE_INDEX.csv), [`MASTER_RESULTS.csv`](https://github.com/PrometheusDynamicsCanada/prometheus-quantum-telemetry/blob/main/MASTER_RESULTS.csv), `verify_sha256_evidence.py` |
| **[`prometheus-execution-intelligence`](https://github.com/PrometheusDynamicsCanada/prometheus-execution-intelligence)** | **System Architecture & Consolidated Multi-Cloud Index:** Multi-compiler candidate evaluation (SABRE O3, TKET, Prometheus), multi-QPU dispatch workflow, and 18-screenshot Studio visual gallery indexing the 248 completed benchmark jobs/tasks across 6 QPUs. | [`ARCHITECTURE.md`](https://github.com/PrometheusDynamicsCanada/prometheus-execution-intelligence/blob/main/ARCHITECTURE.md), [`SCREENSHOT_GALLERY.md`](https://github.com/PrometheusDynamicsCanada/prometheus-execution-intelligence/blob/main/SCREENSHOT_GALLERY.md) |

---

**Contact:**  
William Denyer - Founder, Prometheus Dynamics  
`william@prometheusdynamics.ca` | [https://prometheusdynamics.ca](https://prometheusdynamics.ca)
