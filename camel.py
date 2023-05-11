camelcase = input("Type the variable name: ")

letter = ""
for i in camelcase:
    if i == i.upper():
        letter = i
        camelcase = camelcase.replace(letter,("_"+letter))

print(camelcase.lower())