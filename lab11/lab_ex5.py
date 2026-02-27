company = {
    "employees": [
        {"name": "Dan", "position" : "Master", "salary": 500000},
        {"name": "Jack", "position" : "Bachelor", "salary": 10000},
    ]
}

company["employees"].append({"name": "Alex", "position": "Manager", "salary": 150000})
for employee in company["employees"]:
    print(employee["name"])