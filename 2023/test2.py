s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

print(f"Set 1: {s1}\nSet 2: {s2}")

print('\nWel in set 1, niet in set 2:')
print(s1 - s2)
print(s1.difference(s2))

print('\nNiet in set 1, wel in set 2:')
print(s2 - s1)
print(s2.difference(s1))

print('\nWel in set 1, niet in set 2 OF niet in set 1, wel in set 2;'
      "\noftewel, komt maar in 1 van de 2 sets voor:")
print(s1 ^ s2)
print(s1.symmetric_difference(s2))

print("\nIn set 1 en set 2:")
print(s1 & s2)
print(s1.intersection(s2))

print("\nVoegt sets bij elkaar:")
print(s1 | s2)
print(s1.union(s2))

print("\nSet 1 volledig in set 2:")
print(s1.issubset(s2))
print(s1 <= s2)
# Kan ook:
# print(s2.issuperset(s1))
# print(s2 >= s1)

print("\nSet 1 heeft set 2 volledig in zich:")
print(s1.issuperset(s2))
print(s1 >= s2)
# Kan ook:
# print(s2.issubset(s1))
# print(s2 <= s1)
