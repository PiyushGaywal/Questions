#Find sum of even digits in a number
num=123456789
tsum=0
for i in str(num):
    if int(i) % 2 ==0:
        tsum+=int(i)
print(tsum)
        