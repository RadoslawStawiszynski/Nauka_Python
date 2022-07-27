print("Podaj wagę w kilogramach:")
weight = float(input())

print("Podaj wzrost w metrach:")
height = float(input())

x = weight / (height ** 2)

if x < 18.5:
    print("Underweight")
elif 18.5 <= x < 25:
    print("Normal")
elif 25 <= x < 30:
    print("Overweight")
elif x >= 30:
    print("Obesity")
else:
    print("Uwaga błąd !")

print("waga: " + str(weight))
print(type(weight))
print("wzrost: " + str(height))
print(type(weight))
print("BMI: " + str(x))

# weight / height ** 2
