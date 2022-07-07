print(dir(["lista",'krótka',"rónorodna"]))
print('ok1')
print(dir(1))
print('ok2')
# po wywołaniu teraz tej funkcji nie będzie funkcji math
print(dir())
print("ok3")
import math
print(dir(math))
print('ok4')
# po wywołaniu teraz tej funkcji Będzie! funkcja math
print(dir())
print('ok5')
print("POP")
print()
pop = "Pop jest skrótem od nazwy Popcorn"
print(dir(pop))
print()
help(pop.upper)
# UWAGA mega przydatna funkcja, wyjaśniająca działanie funkcji
print(pop.upper())





