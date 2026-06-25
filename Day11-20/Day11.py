import math
"""Functions"""
#Level 1
"""#1
num1 = int(input())
num2 = int(input())
def add_two_number(n, m):
    return n + m
print(add_two_number(num1, num2))
"""
"""#2
ratio = int(input("What the circle's ratio: "))
def area_of_circle(r):
    return math.pi * r ** 2
print(area_of_circle(ratio))
"""
"""#3
def add_all_num(*nums):
    for i in nums:
        if not isinstance(i, int):
            print("Return a valid integer")
            return
    total = 0
    for i in nums:
        total += i
    return total
result = add_all_num(*range(1,100))
print(result, type(result))
"""
"""#4
def convert_celcius_to_fahrenheit(c): #F = (°C x 9/5) + 32
    fahrenheit = (c * (9/5)) + 32
    print(f"{c} degrees celcius converted into fahrenheit is {fahrenheit}")
convert_celcius_to_fahrenheit(0)
"""
"""#5
def check_season(month):
    month = month.lower().strip()
    
    if month in ["september", "october", "november"]:
        return "Autumn"
    if month in ["december", "january", "february"]:
        return "Winter"
    if month in ["march", "april", "may"]:
        return "Spring"
    if month in ["june", 'july', 'august']:
        return "Summer"
    else:
        return "Please enter a valid month"
month = input("Enter a valid month: ")
print(check_season(month))
"""
"""#6
def calculate_slope(x1, y1, x2, y2):
    rise = y2 - y1
    run = x2 - x1
    return rise / run
print(calculate_slope(2,4,6,10))
"""
"""#7
def solve_quadratic_eqn(a,b,c):
    discriminant = b**2 - 4*a*c
    xp = (-b + math.sqrt(discriminant)) / 2*a
    xm = (-b - math.sqrt(discriminant)) / 2*a
    return xp, xm
print(solve_quadratic_eqn(1,5,6))
"""
"""#8
def print_list(lst):
    for i in lst:
        print(i)
print_list([1,2,3,4,5,6,7])
"""
"""#9
def reverse_list(lst):
    empty = []
    for i in range(len(lst)-1,-1,-1):
        empty.append(lst[i])
    return empty
print(reverse_list([1, 2, 3, 4, 5]))
"""
"""#10
def capitalize_list(lst):
    empty = []
    for i in lst:
        empty.append(i.capitalize())
    return empty
print(capitalize_list(["hello", "world", "zen"]))
"""
#11
