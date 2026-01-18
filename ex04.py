from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import numpy as np
import matplotlib.pyplot as plt

# Inversion about the mean
def diffuser(nqubits):
    qc = QuantumCircuit(nqubits)

    for qubit in range(nqubits):
        qc.h(qubit)
        qc.x(qubit)

    qc.h(nqubits - 1)
    qc.mcx(list(range(nqubits - 1)), nqubits - 1)
    qc.h(nqubits - 1)

    for qubit in range(nqubits):
        qc.x(qubit)
        qc.h(qubit)

    return qc


# Grover setup
n = 3
grover_circuit = QuantumCircuit(n)

# Superposition
grover_circuit.h(range(n))

# Oracle (marks |101>)
oracle = QuantumCircuit(n)
oracle.x(1)
oracle.h(2)
oracle.mcx([0, 1], 2)
oracle.h(2)
oracle.x(1)

# Convert oracle & diffuser to Gates
oracle_gate = oracle.to_gate(label="Oracle")
diffuser_gate = diffuser(n).to_gate(label="Diffuser")

# Grover iterations
iterations = int(np.floor(np.pi / 4 * np.sqrt(2 ** n)))
print(f"Optimal iterations: {iterations}")

for _ in range(iterations):
    grover_circuit.append(oracle_gate, range(n))
    grover_circuit.append(diffuser_gate, range(n))

grover_circuit.measure_all()

print(f"\nFinal Grover Circuit: {grover_circuit.draw()}")

sim = AerSimulator()
tqc = transpile(grover_circuit, sim)
result = sim.run(tqc, shots=500).result()
counts = result.get_counts()

print("\nFinal Counts:", counts)
plot_histogram(counts)
plt.show()
