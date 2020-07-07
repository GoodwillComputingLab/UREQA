# The following circuit conversions can be used to predict the error rates of gates and approximate circuit success probability
# All Qiskit standard gates can be represented in terms of 'h', rx', 'ry', 'rz', 'ch', 'crx', 'cry', and 'crx'
# For example, if s gate is applied to qubit a, predict the error rate of applying the 'rz' operation of qubit a
# If swap gate is applied to link a-b, then predict the error rate (1 - success rate) of applying the 'crx' operation to link a-b and cube the success rate to get the overall success rate of the swap operation

#### Single-qubit gates

# Identity gate
id = []

# Rotations of 180 degrees
x = ['rx']
y = ['ry']
x = ['rz']

# Rotations of arbitrary angles
rx = ['rx']
ry = ['ry']
rz = ['rz']

# Clifford gates
s = ['rz']
sdg = ['rz']

# C3 gates
t = ['rz']
tdg = ['rz']

# Hadamard gate
h = ['h']

##### Double-qubit gates

# Controlled 180 degrees rotations
cx = ['crx']
cy = ['cry']
cz = ['crz']

# Controlled Hadamard gate
ch = ['ch']

# Controlled rotations
crx = ['crx']
cry = ['cry']
crz = ['crz']

# Swap two qubits a-b
swap = ['crx', 'crx', 'crx']

##### Triple-qubit gates

# Toffoli applied to qubits a, b, c
ccx = {'a': ['rz'],
	   'b': ['rz', 'rz'],
	   'c': ['h', 'h', 'rz', 'rz', 'rz', 'rz'],
	   'a-b': ['crx', 'crx'],
	   'a-c': ['crx', 'crx'],
	   'b-c': ['crx', 'crx']
	   }

# cswap applied to qubits a, b, c
cswap = {'a': ['rz'],
		 'b': ['rz', 'rz'],
		 'c': ['h', 'h', 'rz', 'rz', 'rz', 'rz'],
		 'a-b': ['crx', 'crx'],
		 'a-c': ['crx', 'crx'],
		 'b-c': ['crx', 'crx', 'crx', 'crx']
		 }
