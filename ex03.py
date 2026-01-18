from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator

def deutsch_jozsa_algorithm(oracle, n):
    dj_circuit = QuantumCircuit(n + 1, n)

    # Prepare ancilla |1>
    dj_circuit.x(n)

    # Hadamards
    for qubit in range(n + 1):
        dj_circuit.h(qubit)

    # Convert oracle to a Gate
    oracle_gate = oracle.to_gate(label="Oracle")
    dj_circuit.append(oracle_gate, range(n + 1))

    # Hadamards on input qubits
    for qubit in range(n):
        dj_circuit.h(qubit)

    dj_circuit.measure(range(n), range(n))
    return dj_circuit


# Oracle
n = 3
balanced_oracle = QuantumCircuit(n + 1)
for i in range(n):
    balanced_oracle.cx(i, n)

# Build and run
circuit = deutsch_jozsa_algorithm(balanced_oracle, n)

sim = AerSimulator()
tqc = transpile(circuit, sim)
result = sim.run(tqc, shots=500).result()

print(circuit.draw())
print(result.get_counts())
