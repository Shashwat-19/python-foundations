import json

person = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "hasChildren": False,
    "titles": ["Mr.", "Dr."]
}

personJSON = json.dump(person, open("person.json", "a"), indent=4, separators=(',', ':'))
