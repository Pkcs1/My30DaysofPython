dog = {}
dog["name"] = {"Appa"}
dog["Color"] = {"Black"}
dog["Breed"] = {"Golden Retriever"}
dog["legs"] = {True}
dog["Age"] = {5}
print(dog)

student = {
    "first_name" : "Zen",
    "last_name" : "Wawan",
    "gender": True,
    "Age": 18,
    "maritial status": False,
    "skills": ["Typing", "Python", "English"],
    "Country": "Indonesia",
    "Address": {
        "City": "Soul Society",
        "Complex": "Division 1"
    }
}
print(len(student))

value = student["skills"]
tipe = type(value)
print(value, tipe)
student["skills"] = {"Bankai"}


keys = student.keys()
vlues = student.values()
print(keys, vlues)
stdtpl = student.items()

del student["Age"]
del dog