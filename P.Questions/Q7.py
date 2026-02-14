#Reverse The Digit Of The Nummber Without Built In Method
num=int(input("Enter The Number:"))
n=str(num)
for i in range(len(n)-1,-1,-1):
    print(n[i])

