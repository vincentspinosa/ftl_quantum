# Qiskit Quantum Algorithms & Hardware Integration

This repository contains a series of five Python exercises designed to demonstrate the fundamental principles of quantum computing, ranging from basic gate operations to complex algorithmic implementations and real-world hardware execution.

### `ex00.py` - Superposition and the Hadamard Gate
An introduction to quantum states using a single qubit and classical bit.
* **Core Concept:** Utilizing the **Hadamard (H) gate** to transform a qubit from the $|0\rangle$ state to a superposition state: $\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$.
* **Output:** A circuit visual and a histogram showing an approximately 50/50 distribution between 0 and 1.


### `ex01.py` - Quantum Entanglement (Bell State)
Demonstrates the creation of a **Bell State** using two qubits.
* **Core Concept:** Applying an H-gate to the first qubit followed by a **Controlled-NOT (CX)** gate to entangle them.
* **Output:** Results showing that qubits are perfectly correlated (measuring `00` or `11`).


### `ex02.py` - Real Hardware & IBM Runtime
Transfers quantum logic from a simulator to a **physical quantum processor**.
* **Core Concept:** Connects to `ibm_quantum_platform` using `QiskitRuntimeService`. 
* **Key Features:** Uses `generate_preset_pass_manager` for circuit transpilation and `SamplerV2` to execute on the least busy operational backend.
* **Result:** Demonstrates "Quantum Noise" where physical hardware may produce small counts of erroneous states (e.g., `01` or `10`).

### `ex03.py` - Deutsch-Jozsa Algorithm
A demonstration of quantum speedup for determining function properties.
* **Problem:** Identifying if an oracle function is **constant** or **balanced**.
* **Implementation:** Uses a 3-qubit input with an ancilla qubit in the $|1\rangle$ state. The oracle is constructed using CX gates to create a balanced state.
* **Outcome:** The algorithm correctly identifies the balanced oracle in a single query.


### `ex04.py` - Grover's Search Algorithm
Implements a search through an unstructured database for the specific state $|101\rangle$.
* **Oracle:** Marks the target state $|101\rangle$ using X gates and a multi-controlled X (MCX) gate.
* **Diffuser:** Implements "Inversion about the Mean" to amplify the probability of the target state.
* **Optimal Iterations:** Calculates the required steps using $iterations = \lfloor \frac{\pi}{4}\sqrt{2^n} \rfloor$.
