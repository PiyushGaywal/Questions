#Move all Zeros to The End
arr=[1,2,0,3,0,4,0,5]
n=len(arr)
j=0
for i in range(n):
    if arr[i] !=0:
        arr[j]=arr[i]
        j+=1
while j < n:
    arr[j]=0
    j+=1
print(arr)