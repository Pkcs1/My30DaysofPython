import random
import string
#1
def random_user_id():
    empty = ""
    x = string.hexdigits
    for i in range(10):
        empty += random.choice(x)
    return empty
print(random_user_id())

#2
def user_id_gen_by_user():
    num_chars = int(input("How many characters would you want in the ID: "))
    num_id = int(input("How many ID do you need?: "))
    x = string.hexdigits
    for i in range(num_id):
        empty = ""
        for j in range(num_chars):
            empty += random.choice(x)    
        print(empty)
user_id_gen_by_user()
#3
def rgb_color_gen():
    r, g, b = [random.randint(0, 255) for _ in range(3)]
    print(f"{r},{g},{b}")
rgb_color_gen()

#level 2
def generate_colors(color_type, num):
    result = []
    for i in range(num):
        if color_type == 'hexa':
            hx = "#"
            hexdgts = string.hexdigits
            for j in range(6):    
                hx += random.choice(hexdgts)
            result.append(hx)
        elif color_type == 'rgb':
            r,g,b = [random.randint(0,255) for _ in range(3)]
            color = r,g,b
            result.append(color)
    return result
print(generate_colors('hexa', 1))
print(generate_colors('rgb', 2))
#level 3
#1
def shuffle_list(lst):
    random.shuffle(lst)
    return lst
lst = [
    "apple", "banana", "mango", "grape", "watermelon",
    "pizza", "burger", "sushi", "ramen", "tacos",
    "cat", "dog", "elephant", "tiger", "penguin",
    "python", "javascript", "rust", "golang", "typescript",
    "jakarta", "tokyo", "paris", "london", "sydney",
    "red", "blue", "green", "purple", "yellow",
    "guitar", "piano", "drums", "violin", "saxophone",
    "football", "basketball", "tennis", "badminton", "swimming",
    "iron man", "batman", "superman", "spiderman", "thor",
    "minecraft", "valorant", "chess", "poker", "monopoly",
    "einstein", "newton", "tesla", "darwin", "curie",
    "sun", "moon", "mars", "jupiter", "saturn",
    "ocean", "mountain", "desert", "forest", "volcano",
    "coffee", "tea", "juice", "milk", "soda",
    "laptop", "keyboard", "monitor", "mouse", "headphones",
    "shirt", "jeans", "hoodie", "sneakers", "jacket",
    "lion", "shark", "eagle", "wolf", "gorilla",
    "gold", "silver", "bronze", "platinum" ]
print(shuffle_list(lst))

#2
def unique_list():
    return random.sample(range(10), 7)
print(unique_list())