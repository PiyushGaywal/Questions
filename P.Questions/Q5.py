#Write The Python Programme for counting vowels in word
vowels='aeiou'
word="Hello Word"
stri=word.lower()
vcount=0
for char in stri:
    if char in vowels:
        vcount+=1
print(vcount)