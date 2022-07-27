# sprawdzanie jakiego rodzaju mamy dane i czy są int, float, tuple, complex lub inne
print(1),

A = 45
B = 3.33
C = (2, 4)
D = 2j + 3j
print("A")
print(isinstance(A, (tuple, str)))
print("B")
print(isinstance(B, (tuple, float)))
print("C")
print(isinstance(C, (tuple, int, float)))
print("D")
print(isinstance(D, complex))
