# Remove Duplicate Char From String
stri="Hello How Are You"
s=stri.lower()
unique=[]
for char in s:
    if char  not in unique:
        unique.append(char)
print("".join(unique))