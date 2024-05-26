codes = ["._", "_...","_._.","_..",".",".._.","__.","....","..",".__","_._","._..","__","_.","___"]

text = input("enter the word ")

morse_str = ""

for i in text:
    morse_str = morse_str + codes[ord(i)-97] + " "

print(morse_str)
