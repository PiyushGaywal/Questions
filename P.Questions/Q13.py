# Find The Longst Word In String
string="Today Is Independence Day"
longest=""
word=string.split()
for i in word:
    if len(i) > len(longest):
        longest=i
print(longest)