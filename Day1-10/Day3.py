import math
"""
age = int(input("Age: "))
height = float(input("Height: "))
complex = 1 + 1j

#Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = int(input("Enter base: "))
height = int(input("Enter height: "))
area = 0.5 * base * height
print("The area of this triangle is: ", area)
#Write a script that prompts the user to enter side a, side b, and side c of the triangle. 
#Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a = int(input("Side A: "))
side_b = int(input("Side B: "))
side_c = int(input("Side C: "))
perimiter = side_a + side_b + side_c
print("The perimiter for this triangle is: ", perimiter)
# Get length and width of a rectangle using prompt. 
# Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("Length: "))
width = int(input("Width"))
area2 = length * width
perimiter2 = 2 * (length + width)
#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
r = int(input("Insert radius digit: "))
area_circ = 3.14 * (r ** 2)
c = 2 * 3.14 * r

#Calculate the slope, x-intercept and y-intercept of y = 2x -2
m = 2
b = -2

slope = m
y_intercept = b
x_intercept = -b / m

print(f"Slope of y = 2x-2: {slope}")
print(f"y intercept of y = 2x-2: {y_intercept} ")
print(f"x intercept of y = 2x-2: {x_intercept}")


#Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10

slope_m = (y2-y1)/(x2-x1)
euclid = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

if slope_m > m:
    print("slope task 9 lebih besar")
elif slope_m < m:
    print("slope task 8 lebih besar")
else:
    print("slope nya sama")

#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
x_val = -3
y_equ = x_val**2 + 6*x_val + 9
print(y_equ)
#Find the length of 'python' and 'dragon' and make a falsy comparison statement.
len("Dragon") != len("Python")
#Use and operator to check if 'on' is found in both 'python' and 'dragon'
py = "python"
gon = "dragon"
if  "on" in py and "on" in gon:
    print("True")
#or
print("on" in py and "on" in gon)
#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("jargon" in "I hope this course is not full of jargon")
#There is no 'on' in both dragon and python
print(not "on" in py and not "on" in gon)
#Find the length of the text python and convert the value to float and convert it to string
panjang_py = len(py)
panjang_py = float(panjang_py)
panjang_py = str(panjang_py)
#or
str(float(len(py)))
#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
number = int(input("Masukkan angka: "))
print(number % 2 == 0)
#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7 // 3 == int(2.7))
#Check if type of '10' is equal to type of 10
print(type("10") == type(10))
#Check if int('9.8') is equal to 10
print(int('9.8') == 10)

hours = int(input("How many hours you work? "))
ratephour = int(input("How much is your Rate/Hour: "))
print(f"Your pay is: {hours} * {ratephour}")

years = int(input("How many years have you lived: "))
print(f"you have lived for {years * 31536000}")
"""
for i in range(1, 6):
    print(i, 1, i**1, i**2, i**3)