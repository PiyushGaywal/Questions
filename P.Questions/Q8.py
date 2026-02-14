# Write The Programme For Sum Of Digits of A Number
num=int(input("Enter The Number:"))
n=len(str(num))
tsum=0
for i in str(num):
    tsum+=int(i)
print(tsum)