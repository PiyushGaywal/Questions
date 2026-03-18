#Find The Intersection in Two Arrays
arr=[3,4,5,8,9,11]
arr1=[1,2,4,6,9,13]
intersection=[]

for i in arr:
    for j in arr1:
        if i==j and i not in intersection:
            intersection.append(i)
print(intersection)