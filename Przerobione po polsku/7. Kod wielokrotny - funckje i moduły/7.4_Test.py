import sys


# CWICZENIE NR 1

print("CWICZENIE NR 1")

def waga_na_ksiezycu(waga_z, wsp_wzr_1):
    waga_k = waga_z * 0.165
    for w in range(1, 16):
        waga_k = waga_k + wsp_wzr_1
        print('Po roku %s waga na ksiezycu wynosi = %s ' % (w, waga_k))


waga_na_ksiezycu(30, 0.25)


# CWICZENIE NR 2

print("CWICZENIE NR 2")


def waga_na_ksiezycu_2(waga_z, wsp_wzr_2, lata):
    waga_k = waga_z * 0.165
    lata1 = lata + 1
    for w in range(1, lata1):
        waga_k = waga_k + wsp_wzr_2
        print('Po roku %s waga na ksiezycu wynosi = %s ' % (w, waga_k))


waga_na_ksiezycu_2(90, 0.25, 5)


# CWICZENIE NR 3

print("CWICZENIE NR 3")


def waga_na_ksiezycu_3():
    print("Proszę podaj swoją aktualną wagę na planecie Ziemia:")
    waga_z1 = int(sys.stdin.readline())
    print("Proszę podaj, o ile Twoja waga rośnie każdego roku:")
    wsp_wzr_3 = int(sys.stdin.readline())
    print("Proszę podaj liczbę, przez ile będzie rosła waga:")
    lata2 = int(sys.stdin.readline())
    waga_k = waga_z1 * 0.165
    lata3 = lata2 + 1
    for w in range(1, lata3):
        waga_k = waga_k + wsp_wzr_3
        print('Po roku %s waga na ksiezycu wynosi = %s ' % (w, waga_k))


waga_na_ksiezycu_3()
