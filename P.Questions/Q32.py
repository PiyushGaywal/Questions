#Count Uppercase and lowercase
word="Hello How Are You"
upper=0
lower=0
for ch in word:
    if ch >= "A" and ch <= "Z":
        upper+=1
    elif ch >= "a" and ch <="z":
        lower+=1
print(upper)
print(lower)

