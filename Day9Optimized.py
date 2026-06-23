#More optimized 1.1
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