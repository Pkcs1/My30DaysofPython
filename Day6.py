"""empty_tuple = ()
tuple(), count(), index(), + [join two or more to create a new tuple]
changing a tuple means to turn it into a list
"""
#Exercise 1
empty_tuple = ()

sisters = ("orihime", "Nel", "Yoruichi")
brothers = ("Zangetsu", "Urahara", "Ichigo")
siblings  = sisters + brothers
print(siblings)
print(len(siblings))
temp_siblings = list(siblings)
temp_siblings.append("Byakuya")
temp_siblings.append("Hisagi")

family = tuple(temp_siblings)
print(family)

#Exercise 2
siblings = family[:6]
parents = family[6:]
print(siblings)
print(parents)

fruit = ("Apple", "Banana", "Mango", "Orange")
Veggies = ("Carrot", "Cucumber", "Tomato")
aniproducts = ("Milk", "Eggs")
food_stuff_tp = fruit + Veggies + aniproducts
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
mid = len(food_stuff_lt) // 2
print(food_stuff_lt[mid])
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])
del food_stuff_tp

    # Check if an item is in a tuple exercise
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)