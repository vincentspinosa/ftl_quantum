from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Quantum Circuit with 1 qubit and 1 classical bit
qc = QuantumCircuit(1, 1)

# Apply Hadamard gate to put the qubit in superposition
# State becomes: 1/sqrt(2) * (|0> + |1>) which gives 50% chance of measuring 0 or 1
qc.h(0)

# Maps state of qubit at index 0 to classical bit at index 0 of the QuantumCircuit
qc.measure(0, 0)
print(f"Circuit Visual: {qc.draw()}")

counts = AerSimulator().run(qc, shots=500).result().get_counts()
print(f"\nMeasurement results (500 shots): {counts}")
plot_histogram(counts)
plt.show()
