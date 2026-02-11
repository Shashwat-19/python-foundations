#  Dictionary Methods

dict = {
    "name" : "Shashwat",
    "subjects" : {
        "phy" : 89
    }
}

print(len(dict.keys()))
print(list(dict.values()))
print(dict.items())

# get

print(dict.get("name"))

# update
dict.update({"city": "Patna"})
print(dict)