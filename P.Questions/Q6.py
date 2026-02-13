#Write the programme for finding the lcm of two numbers
a=int(input("Enter The Num:"))
b=int(input("Enter The Num:"))
high=a*b
lcm=1
for i in range(2,high+1):
    if i % a==0 and i % b==0:
        lcm=i
        break
print(lcm)
