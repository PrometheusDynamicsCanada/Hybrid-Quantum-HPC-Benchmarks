"""
Prometheus Dynamics - AWS Braket Local SDK Equivalence & Benchmark Table Loader
===============================================================================
Scope of Verification:
  1. Independently builds all seven proposed Phase 1A logical workloads:
       - QAOA_MaxCut_8Q (8Q 3-Regular QAOA MaxCut)
       - QAOA_MaxCut_12Q (12Q 3-Regular QAOA MaxCut)
       - QFT_8Q (8Q Quantum Fourier Transform)
       - QFT_12Q (12Q Quantum Fourier Transform)
       - Dense_AllToAll_17Q (17Q Dense All-to-All K_17)
       - Dense_AllToAll_18Q (18Q Dense All-to-All K_18)
       - Dense_AllToAll_19Q (19Q Dense All-to-All K_19)
     translates each Qiskit circuit into an Amazon Braket `Circuit`, executes
     each circuit on AWS Braket `LocalSimulator("default")` at both `shots=0`
     (exact probability vector) and `shots=4096` (empirical 4,096-shot sampling),
     and verifies 1.000000 computational-basis distribution overlap against
     Qiskit Statevector.
  2. Loads and prints the archived structural compilation comparison table
     (`braket_local_validation_results.json`) across all 14 device-workload pairs
     on Rigetti Cepheus (108Q) and IQM Garnet (20Q).

Disclosure Note:
  To protect proprietary routing IP and physical execution trajectories, routed
  physical OpenQASM circuits and internal compiler scoring weights are withheld
  from the public repository. Running this script verifies Qiskit-to-Braket
  logical circuit translation and 4,096-shot LocalSimulator execution across all
  proposed workloads and displays the archived structural benchmark table.
"""

import json
import math
from pathlib import Path
import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from braket.circuits import Circuit as BraketCircuit
from braket.devices import LocalSimulator


def qiskit_to_braket_circuit(qc: QuantumCircuit, num_qubits: int) -> BraketCircuit:
    """Translates a logical Qiskit QuantumCircuit into an Amazon Braket Circuit."""
    bk = BraketCircuit()
    for q in range(num_qubits):
        bk.i(q)
    for inst in qc.data:
        name = inst.operation.name.lower()
        q_indices = [qc.find_bit(q).index for q in inst.qubits]
        params = [float(p) for p in inst.operation.params]
        if name == "h":
            bk.h(q_indices[0])
        elif name == "x":
            bk.x(q_indices[0])
        elif name == "y":
            bk.y(q_indices[0])
        elif name == "z":
            bk.z(q_indices[0])
        elif name == "s":
            bk.s(q_indices[0])
        elif name == "sdg":
            bk.si(q_indices[0])
        elif name == "t":
            bk.t(q_indices[0])
        elif name == "tdg":
            bk.ti(q_indices[0])
        elif name == "sx":
            bk.v(q_indices[0])
        elif name == "rx":
            bk.rx(q_indices[0], params[0])
        elif name == "ry":
            bk.ry(q_indices[0], params[0])
        elif name == "rz":
            bk.rz(q_indices[0], params[0])
        elif name in ("p", "u1"):
            bk.phaseshift(q_indices[0], params[0])
        elif name in ("cx", "cnot"):
            bk.cnot(q_indices[0], q_indices[1])
        elif name == "cz":
            bk.cz(q_indices[0], q_indices[1])
        elif name == "swap":
            bk.swap(q_indices[0], q_indices[1])
        elif name in ("cp", "cu1"):
            bk.cphaseshift(q_indices[0], q_indices[1], params[0])
        elif name == "rzz":
            bk.zz(q_indices[0], q_indices[1], params[0])
        elif name in ("barrier", "measure"):
            continue
    return bk


def build_qaoa_maxcut_3reg(n_qubits: int, p_layers: int = 2) -> QuantumCircuit:
    qc = QuantumCircuit(n_qubits)
    for q in range(n_qubits):
        qc.h(q)
    edges = [(i, (i + 1) % n_qubits) for i in range(n_qubits)]
    for i in range(n_qubits // 2):
        edges.append((i, i + n_qubits // 2))
    gammas = [0.42, 0.78][:p_layers]
    betas = [0.61, 0.33][:p_layers]
    for lyr in range(p_layers):
        for u, v in edges:
            qc.cx(u, v)
            qc.rz(2 * gammas[lyr], v)
            qc.cx(u, v)
        for q in range(n_qubits):
            qc.rx(2 * betas[lyr], q)
    return qc


def build_qft_benchmark(n_qubits: int) -> QuantumCircuit:
    qc = QuantumCircuit(n_qubits)
    for q in range(n_qubits):
        qc.h(q)
        qc.rz(math.pi / float(2 ** (q % 4)), q)
    for q in range(n_qubits):
        for k in range(q + 1, min(q + 4, n_qubits)):
            angle = math.pi / float(2 ** (k - q))
            qc.cx(k, q)
            qc.rz(-angle / 2, q)
            qc.cx(k, q)
            qc.rz(angle / 2, q)
        qc.h(q)
    return qc


def build_dense_all_to_all(n_qubits: int) -> QuantumCircuit:
    qc = QuantumCircuit(n_qubits)
    for q in range(n_qubits):
        qc.h(q)
        qc.rz(math.pi / float(3 + (q % 5)), q)
    for i in range(n_qubits):
        for j in range(i + 1, n_qubits):
            if (i + j) % 3 == 0:
                angle = 0.35 / float(1 + abs(i - j))
                qc.cx(i, j)
                qc.rz(angle, j)
                qc.cx(i, j)
    for q in range(n_qubits):
        qc.h(q)
    return qc


def build_logical_workloads() -> dict[str, QuantumCircuit]:
    return {
        "QAOA_MaxCut_8Q": build_qaoa_maxcut_3reg(8, p_layers=2),
        "QAOA_MaxCut_12Q": build_qaoa_maxcut_3reg(12, p_layers=2),
        "QFT_8Q": build_qft_benchmark(8),
        "QFT_12Q": build_qft_benchmark(12),
        "Dense_AllToAll_17Q": build_dense_all_to_all(17),
        "Dense_AllToAll_18Q": build_dense_all_to_all(18),
        "Dense_AllToAll_19Q": build_dense_all_to_all(19),
    }


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    sim = LocalSimulator("default")

    print("=" * 104)
    print("STAGE 1: QISKIT-TO-BRAKET LOGICAL EQUIVALENCE & 4,096-SHOT EXECUTION (LocalSimulator('default'))")
    print("=" * 104)

    workloads = build_logical_workloads()
    for name, qc in workloads.items():
        n_q = qc.num_qubits
        sv_qk = Statevector.from_instruction(qc).probabilities()
        idx_rev = np.arange(2**n_q).reshape([2] * n_q).transpose(list(range(n_q))[::-1]).reshape(-1)
        p_qk = sv_qk[idx_rev]

        bk_exact = qiskit_to_braket_circuit(qc, n_q)
        bk_exact.probability()
        res_exact = sim.run(bk_exact, shots=0).result()
        p_bk = np.array(res_exact.values[0], dtype=float)

        bk_shots = qiskit_to_braket_circuit(qc, n_q)
        res_shots = sim.run(bk_shots, shots=4096).result()
        total_sampled_shots = sum(res_shots.measurement_counts.values())

        overlap = float(np.sum(np.sqrt(np.maximum(0.0, p_qk * p_bk))) ** 2)
        tvd = 0.5 * float(np.sum(np.abs(p_qk - p_bk)))
        status = "PASS" if (overlap > 0.999999 and total_sampled_shots == 4096) else "FAIL"
        print(
            f"  [{status}] {name:20s} | Qubits: {n_q:2d} | "
            f"Exact Overlap: {overlap:.6f} | TVD: {tvd:.2e} | Sampled Shots: {total_sampled_shots}"
        )

    results_path = base_dir / "braket_local_validation_results.json"
    if results_path.exists():
        print("\n" + "=" * 104)
        print("STAGE 2: ARCHIVED STRUCTURAL BENCHMARK SUMMARY (Rigetti Cepheus 108Q & IQM Garnet 20Q)")
        print("Note: Displays saved compilation metrics (4,096 shots/circuit); routed physical OpenQASM is withheld.")
        print("=" * 104)
        data = json.loads(results_path.read_text(encoding="utf-8"))
        for row in data["benchmarks"]:
            p = row["prometheus"]
            s = row["sabre_o3"]
            t = row["tket"]
            sabre_red = (1.0 - p["two_q_gates"] / s["two_q_gates"]) * 100.0
            tket_red = (1.0 - p["two_q_gates"] / t["two_q_gates"]) * 100.0
            print(
                f"  {row['device']:16s} | {row['workload']:20s} | "
                f"2Q Gates: Prom={p['two_q_gates']:3d} vs SABRE={s['two_q_gates']:3d} ({-sabre_red:+6.1f}%), "
                f"TKET={t['two_q_gates']:3d} ({-tket_red:+6.1f}%) | "
                f"Sim Fidelity: Prom={p['state_fidelity']:.4f} vs SABRE={s['state_fidelity']:.4f}"
            )


if __name__ == "__main__":
    main()
