#Find The Third largest in an array
arr=[10,20,30,40,50,60,70,800,900,100]
l=0
sl=0
tl=0
for i in range(len(arr)):
    if arr[i] > l:
        tl=sl
        sl=l
        l=arr[i]
    elif arr[i] > sl:
        tl=sl
        sl=arr[i]
    elif arr[i] > tl:
        tl=arr[i]
print(tl)
