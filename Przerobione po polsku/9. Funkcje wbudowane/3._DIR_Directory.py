print(dir(["lista",'krótka',"rónorodna"]))
print()
print(dir(1))
print()
# po wywłanmiu teraz tej funkcji nie będzie funkcji math
print(dir())
print()
import math
print(dir(math))
print()
# po wywłanmiu teraz tej funkcji Będzie! funkcja math
print(dir())
print()
print("POP")
print()
pop = "Pop jest skrótem od nazwy Popcorn"
print(dir(pop))
print()
help(pop.upper)
# UWAGA mega przydatna funkcja, wyjaśniająca działanie funkcji
print(pop.upper())





