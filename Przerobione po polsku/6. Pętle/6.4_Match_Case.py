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
    return (n ** 2)


def calc(n: float):
    return (n ** 3)


n = 9.5
is_int = isinstance(n, int)

match is_int:
    case True:
        print("Square is:", calc(n))
    case False:
        print("Cube is:", calc(n))
