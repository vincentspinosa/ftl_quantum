from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(2, 2) # q0 is |0>, q1 is |0>

qc.h(0) # q0 is in superposition, q1 is still |0>

# CNOT gate: entangle qubit 0 and qubit 1
# If q0 is |1>, it flips q1.
qc.cx(0, 1)

# Measure both
qc.measure([0, 1], [0, 1])
print(qc.draw())

counts = AerSimulator().run(qc, shots=500).result().get_counts()
print(f"\nResults (Should be roughly 50% '00' and 50% '11'): {counts}")
plot_histogram(counts)
plt.show()
