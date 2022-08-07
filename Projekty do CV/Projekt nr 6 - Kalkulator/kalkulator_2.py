print('SIMPLE CALCULATOR +')
print()


def num(s):
    try:
        return int(s)
    except ValueError:
        return float(s)


def check(operator, arr):
    while True:
        if operator in arr:
            return operator
        else:
            print(" That is wrong choose ")
            operator = input('What do you want to do? \n The available actions are [  +  -  *  /  ] :')
            continue


x = input('Insert first number: ')
x = num(x)

operator = input('What do you want to do? \n The available actions are [  +  -  *  /  ] :')
arr = ['+', '-', '/', '*']
operator = check(operator, arr)


y = input('Insert second number: ')
y = num(y)

match operator:
    case operator if operator == '+':
        print(x, ' + ', y, ' = ', x + y)
    case operator if operator == '-':
        print(x, ' - ', y, ' = ', x - y)
    case operator if operator == '*':
        print(x, ' * ', y, ' = ', x * y)
    case operator if operator == '/':
        print(x, ' / ', y, ' = ', x / y)
    case _:
        print('ALERT! Check the equation')


