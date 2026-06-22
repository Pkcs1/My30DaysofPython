import math
"""Exercise 1 & 2"""

x = 3
y = 4
print(3+4)
print(3-4)
print(3*4)
print(3%4)
print(3/4)
print(3**4)
print(3//4)

print("naufal")
print("family")

print(type(['Asabeneh', 'Python', 'Finland'])) #list
print(type(4-4j)) # Complex
print(type(10)) #int
print(type(3.14)) #float
print(type("halo")) #str
print(type(True)) #bool
print(type((10.1,1,30))) #Tuple
print(type({30,2,102})) #set
print(type({
    "nama": "Naufal",
    "umur": "17",
    "favorite_subject": "Bankai"})) #Dict




"""Exercise: Level 3
Find an Euclidean distance between (2, 3) and (10, 8) """

x1,y1 = 2,3
x2,y2 = 10,8

EDistance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
print("The Euclidian distance is:", EDistance)