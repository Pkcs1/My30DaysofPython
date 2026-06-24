#More optimized 2.2
season = input("Whats the month? ").lower().strip()

match season:
    case 'september' | 'october' | 'november':
        print("Autumn")
    case 'december' | 'january' | 'february':
        print("Winter")
    case 'march' | 'april' | 'may':
        print("Spring")
    case 'june' | 'july' | 'august':
        print("Summer")
    case _: # The underscore acts as the 'else' fallback
        print("Please enter a valid month")

#or
"""season = input("Whats the month? ").lower().strip() # .strip() removes accidental spaces

if season in ['september', 'october', 'november']:
    print("Autumn")
elif season in ['december', 'january', 'february']:
    print("Winter")
elif season in ['march', 'april', 'may']:
    print("Spring")
elif season in ['june', 'july', 'august']:
    print("Summer")
else:
    print("Please enter a valid month")
"""

#Optimized 2.3
fruits = ['banana', 'orange', 'mango', 'lemon']

check_fruit = input("What would you like to add? ").strip()

# 1. Check if the input is actually a valid word (no numbers or symbols)
if not check_fruit.isalpha():
    print("Error: Please enter a valid fruit name using letters only.")

else:
    # 2. Create a temporary lowercase list just for a fair comparison
    # ['banana', 'orange', 'mango', 'lemon']
    lowercase_fruits = [fruit.lower() for fruit in fruits]
    
    # 3. Compare lowercase input to lowercase list
    if check_fruit.lower() not in lowercase_fruits:
        fruits.append(check_fruit)
        print("Updated list:", fruits)
    else:
        print("That fruit already exists in the list.")