file = open("#21.1.6file", "r")
a = file.readline()
output = ""
for items in a:
    if items.isupper():
        output += items.lower()
    if items.islower():
        output += items.upper()
print(output)
file.close()