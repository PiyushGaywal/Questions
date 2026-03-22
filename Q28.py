#Find First Non Repeating character
word="Programming"

for ch in word:
    if word.count(ch) ==1:
        print(ch)
        break