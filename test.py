fruits = ["apple", "mango", "banana", "cherry", "kiwi"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)


newlist = [x for x in fruits if x != "apple"]
print(newlist)
