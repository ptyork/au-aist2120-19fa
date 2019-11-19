import json

with open('test.json') as fi:
    test_dict = json.loads(fi.read())

print(test_dict["Name"])
print(test_dict["Age"])
print(test_dict['Weight'])
for kid in test_dict["Kids"]:
    print(f"{kid['Name']} is {kid['Age']} years old")

test_dict["Age"] = 47

with open("test.json","w") as fi:
    fi.write(json.dumps(test_dict))

