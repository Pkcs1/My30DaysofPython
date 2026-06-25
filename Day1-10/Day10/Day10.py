"""LOOPS"""
#Level 1
"""#1
for i in range(11):
    print(i)
j = 0
while j != 11:
    print(j)
    j += 1
"""
"""#2
for i in range(10,0,-1):
    print(i)
j = 10
while j != -1:
    print(j)
    j -= 1
"""
"""#3
for i in range(1,8):
    print('#' * i)
"""
"""#4
i = 1
while i <= 8:
    print("# " * 8) 
    i += 1
"""
"""#5
for i in range(11):
    print(f"{i} x {i} = {i*i}")
"""
"""#6
a_list = ['Python', 'Numpy','Pandas','Django', 'Flask']
for i in a_list:
    print(i)
"""
"""#7 
for i in range(101):
    if i % 2 == 0:
        print(f"{i} is an even number")
"""
"""#8
for i in range(101):
    if i % 2 != 0:
        print(f"{i} is odd number")
"""
#Level 2
"""#1
total = 0
for i in range(101):
    total = total + i
print(f"The sum of all numbers is {total}")
"""
"""#2
sum_evem = 0
sum_odd = 0
for i in range(101):
    if i % 2 == 0:
        sum_evem = sum_evem + i
    else:
        sum_odd = sum_odd + i
print(f"The sum of all evens is {sum_evem}. And the sum of all odds is {sum_odd}.")
"""

