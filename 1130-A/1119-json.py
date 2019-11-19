import json
from pprint import pprint as pp

with open('test.json') as fi:
    jd = json.loads(fi.read())

#pp(jd)

print(jd["Name"])
print(jd["Age"])
print(jd["Weight"])
for kid in jd["Kids"]:
    print(f"{kid['Name']} is {kid['Age']} years old")

jd["Age"] = 47

with open('test.json','w') as fi:
    fi.write(json.dumps(jd))
