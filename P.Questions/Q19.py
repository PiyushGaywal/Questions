#Find The Second Largest in Array
arr=[10,20,30,40,50,60,70,80,90,100]
largest=0
slarge=0
for i in range(len(arr)):
    if arr[i] > largest:
        slarge=largest
        largest=arr[i]
    elif arr[i] > slarge and arr[i] < largest:
        slarge=arr[i]
print(slarge)