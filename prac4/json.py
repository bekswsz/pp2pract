import json

with open("sample-data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("Interface Status")
print("DN Description Speed MTU")

for item in data["imdata"]:
    attrs = item["l1PhysIf"]["attributes"]
    dn = attrs.get("dn", "")
    descr = attrs.get("descr", "")
    speed = attrs.get("speed", "")
    mtu = attrs.get("mtu", "")
    print(dn, descr, speed, mtu)