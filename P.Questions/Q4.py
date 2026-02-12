# Write The Programme For Finding the HCF Of Two Nums
a=int(input("Enter The Num1:"))
b=int(input("Enter The Num2:"))
hcf=1

for i in range(2,max(a,b)):
    if a % i==0 and b% i==0:
        hcf=i
print(hcf)