# Find The Duplicate Characters In String
string="Hello"
duplicate=[]
for i in string:
    if i.isalpha():
        if string.count(i)>1 and i not in duplicate:
            duplicate.append(i)
print(duplicate)