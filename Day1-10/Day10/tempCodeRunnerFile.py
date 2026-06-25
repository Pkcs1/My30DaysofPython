languages = set()
for country in countries:
    for language in country["languages"]:
        languages.add(language)
print(len(languages))