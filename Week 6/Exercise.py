from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_bloch_multivector
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, plot_state_city
import matplotlib.pyplot as plt

#Exercise 1

#qc = QuantumCircuit(1,1)
#qc.h(0)
#qc.x(0)
#qc.measure_all()
#print(qc)
#simulator = AerSimulator()
#job = simulator.run(qc, shots=100)
#result = job.result()
#print(qc)
#plot_histogram(result.get_counts(qc))
#plt.show()

#Exercise 2
#qc2 = QuantumCircuit(2,2)
#qc2.h(0)
#qc2.cx(0,1)
#qc2.measure_all()
#simulator = AerSimulator()
#job = simulator.run(qc2, shots=100)
#result = job.result()
#print(qc2)
#plot_histogram(result.get_counts(qc2))
#plt.show()

#Exercise 3
#qc3 = QuantumCircuit(1)
#qc3.x(0)
#qc3.y(0)
#qc3.z(0)
#qc3.h(0)
print(Statevector.from_instruction(qc3))
plot_bloch_multivector(state=Statevector.from_instruction(qc3))
plt.show()