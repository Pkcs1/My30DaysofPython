import keyword
from countries_data import countries
"""# 1
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(7))"""

"""#2
def check_item(items):
    seen = []
    for item in items:
        if item in seen:
            return False
        seen.append(item)
    return True
print(check_item([1, 2, 2, 4]))
"""
"""#3
def same_item(items):
    first_type = type(items[0])
    for i in items:
        if type(i) != first_type:
            return False
    return True
print(same_item([1,'2',3,4]))"""
"""#4
def is_valid_variable(name):
    if not name.isidentifier():
        return False
    if keyword.iskeyword(name):
        return False
    return True
print(is_valid_variable("10k"))"""
#5
"""def most_spoken_languages():
    most = {}
    for key in countries:
        for value in key['languages']:
            if value not in most:
                most[value] = 1
            else:
                most[value] += 1
    sorted_most = sorted(most.items(),reverse=True, key=lambda item: item[1])
    print(f"Top 10: {sorted_most[:10]}")
    print(f"Top 20: {sorted_most[:20]}")
most_spoken_languages()"""

def most_populated_countries():
    sorted_countries = sorted(countries, reverse=True, key=lambda item: item['population'])
    print("Top 10")
    for country in sorted_countries[:10]:
        print(country['name'], country['population'])
    print("Top 20")
    for country in sorted_countries[:20]:
        print(country['name'], country['population'])

most_populated_countries()
