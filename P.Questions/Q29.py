#find the first reapeting char
word="Programming"
for i in word:
    if word.count(i) > 1:
        print(i)
        break