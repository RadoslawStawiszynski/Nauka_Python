# Cwiczenie nr 1

for x in range(0, 20):
    print('Hello word %s' % x)
    if x >= 9:
        break
print()
print()

# Cwiczenie nr 2

w1 = 1
while w1 < 35:
    print('%s' % w1)
    w1 = w1 + 2
print()
print()

# Cwiczenie nr 3

sk = ['jabłko', 'pomarańcza', 'winogrona', 'pożeczka', 'jagody']

for x in range(0, 5):
    print('%s %s' % (x+1, sk[x]))
print()
print()

# Cwiczenie nr 4

waga_z = 90
waga_k = waga_z * 0.165
for w in range(1, 16):
    waga_k = waga_k + 1
    print('Po roku %s waga na ksiezycu wynosi = %s ' % (w, waga_k))
