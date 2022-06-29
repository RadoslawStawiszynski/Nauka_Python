# ładne tabelki

from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
x.add_row(["Adelaide", 1295, 1158259, 600.5])
x.add_row(["Brisbane", 5905, 1857594, 1146.4])
x.add_row(["Darwin", 112, 120900, 1714.7])
x.add_row(["Hobart", 1357, 205556, 619.5])
x.add_row(["Sydney", 2058, 4336374, 1214.8])
x.add_row(["Melbourne", 1566, 3806092, 646.9])
x.add_row(["Perth", 5386, 1554769, 869.4])

print(x)

x.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
x.add_rows(
    [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
)

print(x)

q = PrettyTable()
q.add_column("City name_2",
             ["Adelaide", "Brisbane", "Darwin", "Hobart", "Sydney", "Melbourne", "Perth"])
q.add_column("Area_2", [1295, 5905, 112, 1357, 2058, 1566, 5386])
q.add_column("Population_2", [1158259, 1857594, 120900, 205556, 4336374, 3806092,
                              1554769])
q.add_column("Annual Rainfall_2", [600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9,
                                   869.4])

print(q)
print(type(q))
print(q.get_string())
print(type(q.get_string()))

# To pass options changing the look of the table, use the get_string() method documented below:
#       print(x.get_string())
#    Stringing
#
#    If you don't want to actually print your table in ASCII form but just get a string containing
#    what would be printed if you use print(x), you can use the get_string method:
#       mystring = x.get_string()
#    This string is guaranteed to look exactly the same as what would be printed by doing print(x).
#    You can now do all the usual things you can do with a string,
#    like write your table to a file or insert it into a GUI.


print(q.get_string(fields=["City name_2", "Population_2"]))
print(q.get_string(start=0, end=4))
print('Zadanie wyrównania 1')
q.align = "r"
print(q)
print('Zadanie wyrównania 2')
q.align["City name_2"] = "c"
print(q)
print('Zadanie sortowania 1')
print(q.get_string(sortby="Population_2"))
print('Zadanie sortowania 2')
q.sortby = "City name_2"
q.reversesort = True
print(q)

print('MSWORD_FRIENDLY')
from prettytable import MSWORD_FRIENDLY
q.set_style(MSWORD_FRIENDLY)
print(q)

print('PLAIN_COLUMNS')
from prettytable import PLAIN_COLUMNS
q.set_style(PLAIN_COLUMNS)
print(q)

print('MARKDOWN')
from prettytable import MARKDOWN
q.set_style(MARKDOWN)
print(q)

print('ORGMODE')
from prettytable import ORGMODE
q.set_style(ORGMODE)
print(q)


print('SINGLE_BORDER')
from prettytable import SINGLE_BORDER
q.set_style(SINGLE_BORDER)
print(q)

print('DOUBLE_BORDER')
from prettytable import DOUBLE_BORDER
q.set_style(DOUBLE_BORDER)
print(q)

print('DEFAULT')
from prettytable import DEFAULT
q.set_style(DEFAULT)
print(q)