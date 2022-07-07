# funkcja FLOAT służy do przekształcania liczby całkowitej na liczbę dziesiętną (zmiennoprzecinkową)
# funkcja INT służy do przekształcania liczby dziesiętnej na liczbę całkowitą

num1 = 10
num2 = 10.01
num3 = "10"
num4 = "10.01"

print(float(num1))
print(float(num2))
print(float(num3))
print(float(num4))

print(int(num1))
print(int(num2))
print(int(num3))
# print(int(num4)) ----- ta funkcja generuje błąd

print(dir(int))


print("Przykład")

twoj_wiek = input("Ile masz lat?")

wiek_f = float(twoj_wiek)
wiek_i = int(twoj_wiek)

if wiek_i >= 18 or wiek_f >= 18:
    print("Jesteś stary tzn. pełnoletni")
else:
    print("Jesteś młody")
    print("1i. Do pełnoletności masz jeszcze %s lat" % (18 - wiek_i))
    print(f"2f. Do pełnoletności masz jeszcze {18 - wiek_f} lat")

