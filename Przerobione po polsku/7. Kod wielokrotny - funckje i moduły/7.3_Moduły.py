import time
import sys

print(time.asctime())

# print(sys.stdin.readline())

def podaj_wiek(wiek):
    if wiek >= 32 or wiek >= 33 or wiek >= 34:
        print('Ile to jest 13+12+123+132+321+231+213+231?  '
              'Dlamnie to za dużo liczenia')
        wynik = 13 + 12 + 123 + 132 + 321 + 231 + 213 + 231
        print('Python:', wynik)
    else:
        print('Że co?')
        
print()

podaj_wiek(12)
podaj_wiek(32)

def podaj_wiek2():
    print('Ile masz lat?')
    wiek = int(sys.stdin.readline())
    if wiek >= 16:
        print('Ile to jest 13+12+123+132+321+231+213+231?  '
              'Dlamnie to za dużo liczenia')
        wynik = 13 + 12 + 123 + 132 + 321 + 231 + 213 + 231
        print('Python:', wynik)
    else:
        print('Że co?')

podaj_wiek2()