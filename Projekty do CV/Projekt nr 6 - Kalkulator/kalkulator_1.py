print('PROSTY KALKULATOR')
print()

x = int(input('Podaj pierwszÄ… liczbÄ™: '))
f = input('Jakie dziaĹ‚anie chcesz wykonaÄ‡? \n DostÄ™pne dziaĹ‚ania to [  +  -  *  /  ] :')
y = int(input('Podaj drugÄ… liczbÄ™: '))



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
        print('Uwaga bĹ‚Ä…d sprawdĹş rĂłwnanie!')

x = rebase
