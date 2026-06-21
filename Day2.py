#Day 2: 30 Days of python programming
first_name = input("Whats your first name: ")
last_name = input("Whats your last name: ")
full_name = first_name + last_name
country = input("Your country: ")
city = "Dublin"
age = int(input("Your age: "))
year = 2008
is_married = False
is_true = True
is_light_on = True
food, drink, sport = "fries", "milk", "swimming"


#untuk mengecek type of data
#make a dictionary
variables = {
    "first_name": first_name,
    "last_name": last_name,
    "full_name": full_name,
    "country": country,
    "city": city,
    "age": age,
    "year": year,
    "is_married": is_married,
    "is_true": is_true,
    "is_light_on": is_light_on,
    "food": food,
    "drink": drink,
    "sport": sport
}

#Periksa tipe data semua variabel sekaligus
for name, value in variables.items():
    print(f"{name}: {type(value)}")

jml_pertama = len(first_name)
print(f"Terdapat, {jml_pertama} huruf pada nama anda")

if len(first_name) == len(last_name):
    print("Panjang nama sama")
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_two - num_one
product = num_two * num_one
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

radius_input = input("Enter the circles radius: ")
radius = int(radius_input)
area_of_cirlce = 3.14 * (radius ** 2)
circum_of_circle = 2 * 3.14 * radius

print("the circumfrence of the circle is: ", circum_of_circle)
print("the area of the circle is: ", area_of_cirlce)
