from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
from qiskit.transpiler.preset_passmanagers import generate_preset_pass_manager
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Initialize Service
service = QiskitRuntimeService(channel="ibm_quantum_platform", token="u6aLksjE0rTgrt_xp33HMVtZvJoPEw8KnjOwz-w7XXYS")

# Create Abstract Circuit
qc = QuantumCircuit(2, 2)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

# Select Backend
backend = service.least_busy(simulator=False, operational=True)
print(f"Running on real backend: {backend.name}")

# Transpile Circuit (create Physical Circuit)
pm = generate_preset_pass_manager(optimization_level=1, backend=backend)
isa_circuit = pm.run(qc)

# Run the Circuit and extract results
counts = Sampler(backend).run([isa_circuit], shots=500).result()[0].data.c.get_counts()

# Display Results
print("\nResults with Quantum Noise:", counts)
plot_histogram(counts)
plt.show()
