# Dictionary 
dict = {
    "name": "Shashwat",
    "age": 21,
    "marks": [45, 55, 33]
}

print(dict["marks"])

# Nested Dictionary

student = {
    "name": "Shashwat",
    "age": 21,
    "marks": [45, 55, 33],
    "subj" : {
        "phy" : 99,
        "chem" : 98,
        "math" : 97
    }
}

print(student["subj"]["phy"])