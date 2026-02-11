#Write the Programme for Armstrong Number
num=int(input("Enter The Num:"))
n=len(str(num))
Tsum=0
for digit in str(num):
    Tsum+= int(digit)**n
if Tsum == num:
    print("The Num Is Armstrong")
else:
    print("The Num Is Not Armstrong")
