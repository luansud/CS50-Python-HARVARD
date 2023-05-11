frase = input("Input: ")
frase1 = frase
for i in frase1:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" or i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
         frase = frase.replace(i,"")

print(frase)

