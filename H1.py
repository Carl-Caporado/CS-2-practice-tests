def find(items, target):
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


members = []
while True:
    name = input("Enter the name of your member: (done to stop): ")
    if name == "done":
        break
    members.append(name)

look_for = input("Look for: ")
pos = find(members, look_for)

if pos != -1:
    print(look_for, "is member number", pos + 1)
else:
    print(look_for, "is not a member")