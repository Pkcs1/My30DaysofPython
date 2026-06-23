"""
Dictionaries
{}
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
len = checks the number of pairs
"""
#Example dict
myself = {
    "nama": "Naufal",
    "umur": "18",
    "job": "Mahasiswa",
    "languages": ["English", "Indonesia", "Python"],
    "enjoymusic": True,
    "Address": {
        "Country": "Ireland",
        "College": "Dublin City College"
    }
}
print(f"{myself['nama']}\n{myself['languages'][0]}\n{myself['Address']}")
print(myself["enjoymusic"])
print(myself.get('LikesSomeone'))

#Adding something to a dict
myself['Foods'] = 'Fries' 
#or
myself['languages'].append("JS") #Adds only to a key that already exists
print(myself)

#modifying an item
myself['nama'] = 'Naufal Rama'

#Checking key in a dict
print('umur' in myself)
print('LikesSomeone' in myself)

#Removing key or value pairs
# .pop() Removes the item with the designated key
# .popitem() Removes the last item
# del removes the selected key
# .clear

#dct.items() changes a dictionary into a list of tuples
#.copy to copy the dictionary
#.keys to get the dictionary keys
#.values to get the dictionary values


