#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
first_word, second_word, third_word, fourth_word = 'Thirty', 'Days', 'Of', 'Python'
print(f"{first_word} {second_word} {third_word} {fourth_word}")
#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
word_1, word_2, word_3 = 'Coding', 'For', 'All'
print(f"{word_1} {word_2} {word_3}")
company = 'Coding For All'
print(company.upper(), len(company))
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company[7:])
print(company.find('Coding')) #returns the index number of the asked parameter
print(company.index('Coding'))
print(company.replace('Coding', 'Python'))
print(company.split())
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", "))
#What is the character at index 0 in the string Coding For All.
print(company[0])
print(len(company) - 1)
print(company[10])
text = "Python For Everyone"
words = text.split()
acronym = words[0][0] + words[1][0] + words[2][0]
print(acronym)
words2 = company.split()
acronym2 = words2[0][0] + words2[1][0] + words2[2][0]
print(acronym2)
print(company.index('C'))
print(company.index('F'))
print(company.rfind('l'))
sentence = 'You cannot end a sentence with because because because is a conjunction'
print(sentence.find('because'))
print(sentence.rindex('because'))
print(sentence[31:54])
print(company.startswith('Coding'))
print(company.endswith('Coding'))
space_company = '   Coding For All      '
print(space_company.strip())
days = '30DaysOfPython'
dais = 'thirty_days_of_python'
print(days.isidentifier())
print(dais.isidentifier())
list_language = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(list_language))
print("I am enjoying this challenge.\nI just wonder what is next.")
print('Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki')
radius = 10
area = int(3.14 * radius ** 2)
print(f'The area of the circle with radius {radius} is {area} meters square')
