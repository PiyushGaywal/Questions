#Count Even And Odd Numbers in an Array
arr=[1,2,3,4,5,6,7,8,9]
Even_count=0
Odd_count=0
for num in arr:
    if num % 2==0:
        Even_count+=1
    else:
        Odd_count+=1
print("Even Numbers:",Even_count)
print("Odd Numbers:",Odd_count)