#Reverse The Each Word Of String
stri="Hello How Are You"
s=stri.split()

for word in s:
    rev=""
    for i in range(len(word)-1,-1,-1):
        rev+=word[i]
    print(rev,end=" ")