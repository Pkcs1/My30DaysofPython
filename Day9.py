#level 1
"""age = int(input("Enter your age: "))
if age >= 18:
    print("you are old enough to drive")
else:
    print(f"You need {18 - age} more years to drive")

your_age = int(input("Your age: "))
my_age = int(input("My age: "))
difference = abs(your_age - my_age)
if your_age > my_age and difference == 1:
    print(f"You are a year older than me")
elif my_age > your_age and difference == 1:
    print("Im a year older than you")
elif your_age > my_age:
    print(f"You are {difference} years older than me")
elif your_age < my_age:
    print(f'Im {difference} years older than you')
else:
    print(f"We are both the same age")


number_a = int(input("Input number a: "))
number_b = int(input("Input number b: "))
if number_a > number_b:
    print(f"{number_a} is greater than {number_b}")
elif number_b > number_a:
    print(f"{number_a} is less than {number_b}")
else:
    print(f"{number_a} is equal to {number_b}")

score = abs(int(input("Enter your score: "))) #Not optimized. Should have a condition if it receive other than an int.
if score >= 90:
    print("Grade A")
elif score >= 80 and score <= 89:
    print("Grade B")
elif score >= 70 and score <= 79:
    print("Grade C")
elif score >= 60 and score <= 69:
    print("Grade D")
else:
    print("Grade F")

#Not really optimized
season = input("Whats the month? ")
if season.lower() == 'september' or season.lower() == 'october' or season.lower() == 'november':
    print("Autumn")
elif season.lower() == 'december' or season.lower() == 'january' or season.lower() == 'february':
    print("Winter")
elif season.lower() == 'march' or season.lower() == 'april' or season.lower() == 'may':
    print("Spring")
elif season.lower() == 'june' or season.lower() == 'july' or season.lower() == 'august':
    print("Summer")
else:
    print("Please enter a valid month")

fruits = ['banana', 'orange', 'mango', 'lemon']
check_fruit = input("What would you like to add? ").strip()
if check_fruit not in fruits:
    fruits.append(check_fruit)
    print(fruits)
else:
    print("That fruit already exist in the list")
"""
person = {
    'first_name': 'Naufal',
    'last_name': 'Zen',
    'age': 18,
    'country': 'Finland',
    'is_married': True,
    'skills': ['English', 'Math', 'Physics', 'Python', 'Davinci', 'Java', 'React', 'Node', 'MongoDB'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    skills_list = person['skills']
    set_skill = set(skills_list)
    
    # middle skill
    mid = len(skills_list) // 2
    print(f"Middle skill found: {skills_list[mid]}")
    
    # check specific skill
    if 'Python' in skills_list:
        print("Has Python skill: True")
        
    # def skills
    front_end_skills = {'Java', 'React'}
    back_end_skills = {'Node', 'Python', 'MongoDB'}
    full_stack_skills = {'React', 'Node', 'MongoDB'}
    
    # dev title
    if full_stack_skills.issubset(set_skill):
        print("Role assessment: This guy is a Fullstack developer.")
    elif back_end_skills.issubset(set_skill):
        print("Role assessment: This guy is a Backend developer.")
    elif front_end_skills.issubset(set_skill):
        print("Role assessment: This guy is a Frontend developer.")
    else:
        print("Role assessment: Skills do not match a specific developer role.")

if person['is_married'] and person['country'] == 'Finland':
    print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is married")
#Asabeneh Yetayeh lives in Finland. He is married.


