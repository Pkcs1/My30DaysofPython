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
myself['languages'].append("JS")
print(myself)
