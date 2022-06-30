# The syntax looks something like this:

# match variable_name:
#            case ‘pattern1’ : //statement1
#            case ‘pattern2’ : //statement2
#           …
#            case ‘pattern n’ : //statement n

print("Przykład nr 1")
print("A")

quit_flag = False
match quit_flag:
    case True:
        print("Quitting")
        exit()
    case False:
        print("System is on")

print("B")
quit_flag = False
match quit_flag:
    case True:
        print("Quitting")
        exit()
    case False:
        print("System is on")

print()
print("Przykład nr 2")
# Sprawdzić co oznacza Function Overloading


def calc(n: int):
    return n ** 2


def calc2(n: float):
    return n ** 3


n = 2
is_int = isinstance(n, int)

match is_int:
    case True:
        print("Square is:", calc(n))
    case False:
        print("Cube is:", calc2(n))

print()
print("Przykład nr 3")

quit_flag = 4

match quit_flag:
    case True:
        print("Quitting")
        exit()
    case False:
        print("System is on")
    case _:
        print("Boolean Value was not passed")


print()
print("Przykład nr 4")

sample = True

match sample:
    case (True | False):
        print("It is a boolean value")
    case _:
        print("Not a boolean value")


print()
print("Przykład nr 5")

list1 = ['a', 'b', 'c', 'd']

match list1:
    case ['e', 'f']:
        print("e,f present")
    case ['a', 'b', 'c', 'd']:
        print("a,b,c,d present")



print()
print("Przykład nr 6")


class switch:
    on = 1
    off = 0


status = 0

match status:
    case switch.on:
        print('Switch is on')
    case switch.off:
        print('Switch is off')



print()
print("Przykład nr 7")

n = 0
match n:
    case n if n < 0:
        print("Number is negative")
    case n if n == 0:
        print("Number is zero")
    case n if n > 0:
        print("Number is positive")


print()
print("Przykład nr 8")

