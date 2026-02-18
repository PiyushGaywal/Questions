# Reverse The Array
arr=[10,20,30,40,50,60,70,80,90,100]
n=len(arr)
reversed=[]
for i in range(n-1,-1,-1):
    reversed.append(arr[i])
print(reversed)