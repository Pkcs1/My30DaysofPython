"""#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
negative = [i for i in numbers if i <= 0]
print(negative)"""
"""#2
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattend = [i for k in list_of_lists for i in k]
print(flattend)"""

"""#3
num = list(range(6))
for i in range(11):
    row = [i ** num for num in range(6)]
    print([i] + row)"""

"""#4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattend = [i for k in countries for i in k]
result = [[i.upper(), i[:3].upper(), k.upper()] for i, k in flattend]
print(result)"""

"""#5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
setup = [i for k in countries for i in k]
diction = [{'countries': i.upper(), 'city': k.upper()} for i, k in setup]
print(diction)"""

"""#6
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concat = [i for k in names for i in k]
gabung = [' '.join(i) for i in concat]
print(gabung)"""

"""#7
slope = lambda x1,y1,x2,y2: (y2 - y1) / (x2 - x1)
print(slope(3,4,6,5))
yinter = lambda y,slope,x: y - slope*x
print(yinter(4, slope(3,4,6,5), 3))"""