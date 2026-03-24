#Rotate Arry by K Position
arr=[1,2,3,4,5,6,7,8,9,10]
k=1
n=len(arr)
k=k%n
arr=arr[-k:]+arr[:-k]
print(arr)