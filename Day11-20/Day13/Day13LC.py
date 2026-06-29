"""languages = 'Python'
lst = [i for i in languages]
print(lst)

number = [i for i in range(11)]
print(number)

squares = [i * i for i in range(11)]
print(squares)

numtup = [(i, i * i) for i in range (11)]
print(numtup)"""

"""even_numbers = [i for i in range(20) if i % 2 == 0]
print(even_numbers)

numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positiveven = [i for i in numbers if i > 0 and i % 2 == 0]
negativeodd = [i for i in numbers if i < 0 and i % 2 != 0]
print(positiveven)
print(negativeodd)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattend = [i for j in list_of_lists for i in j]
print(flattend)"""

area_of_circle = lambda r: 3.14 * r * r
print(area_of_circle(21))