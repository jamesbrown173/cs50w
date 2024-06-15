people = [
    {"name": "Pete", "House": "Castle"},
    {"name": "Liz", "House": "Buckingham"},
    {"name": "Ali", "House": "Prison"},
]


people.sort(key=lambda person: person["name"])

print(people)
