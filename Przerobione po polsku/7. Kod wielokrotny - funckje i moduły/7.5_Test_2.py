print('Podaj liczbę ile pierwszych liczb całkowitych chcesz z sumować:')
N = int(input())
nsum = 0
for n in range(0,N+1):
    nsum = n + nsum
    if n == N:
        print(nsum)



print('Podaj liczbę ile pierwszych liczb całkowitych chcesz z sumować:')

N = int(input())
i = sum(range(0,N+1))
print(i)