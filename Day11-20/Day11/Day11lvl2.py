"""#1
def evens_and_odds(n):
    if not isinstance(n, int):
        print("Enter an int")
        return None    
    if n < 0:
        print("Please enter a positive number")
        return None

    ev = []
    od = []
    for i in range(n + 1):
        if i % 2 == 0:
            ev.append(i)
        else:
            od.append(i)
    return sum(ev), sum(od)
print(evens_and_odds(10))"""
"""#2
def factorial(n):
    if not isinstance(n,int):
        print("Please enter a whole number")
        return None
    total = 1
    for i in range(1, n+1):
        total = total * i
    return total
print(factorial(100))"""
"""#3
def is_empty(lst):
    if not lst:
        return "No Data"
    else:
        return "Theres Data"
print(is_empty([]))"""
"""#4
def greet(name=None):
    if name is None:
        print(f"Hello, Guest!")
    else:
        print(f"Hello, {name}!")
greet("Ichigo")"""
"""#5
def show_args(**args):
    for k, v in args.items():
        print(k, "=", v)
show_args(name="Zen", age=18, food="Fries")"""