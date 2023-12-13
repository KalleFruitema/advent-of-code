a = "0.1"
b = "1"
c = "fcba03"
d = "III"
e = "৴৵৶৷৸৹"
f = "൦൧൨൩൪൫൬൭൮൯"
print(a.isdigit(), a.isdecimal(), a.isnumeric())
print(b.isdigit(), b.isdecimal(), b.isnumeric())
print(c.isdigit(), c.isdecimal(), c.isnumeric())
print(d.isdigit(), d.isdecimal(), d.isnumeric())
print(e.isdigit(), e.isdecimal(), e.isnumeric())
print(f.isdigit(), f.isdecimal(), f.isnumeric())

from re import split

print([1, 1, 3]*5)