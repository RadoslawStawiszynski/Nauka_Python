
print('PROSTY KALKULATOR')
print()

x = int(input('Podaj pierwszą liczbę: '))
f = input('Jakie działanie chcesz wykonać? \n Dostępne działania to [  +  -  *  /  ] :')
y = int(input('Podaj drugą liczbę: '))



match f:
    case f if f == '+':
        print(x, ' + ', y, ' = ', x + y)
    case f if f == '-':
        print(x, ' - ', y, ' = ', x - y)
    case f if f == '*':
        print(x, ' * ', y, ' = ', x * y)
    case f if f == '/':
        print(x, ' / ', y, ' = ', x / y)
    case _:
        print('Uwaga błąd sprawdź równanie!')



