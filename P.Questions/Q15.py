#Find The Largest in An Array
arr=[10,20,20,40,500,70,80,90,100]
largest=arr[0]
for i in arr:
    if i >= largest:
        largest=i
print(largest)
