# Write the programme for Perfect Nummber
num=int(input("Enter The Num:"))
Tsum=0
for i in range(1,num):
    if num % i==0:
        Tsum+=i
if Tsum == num:
    print("The Num Is Perfect")
else:
    print("The Num Is Not Perfect")