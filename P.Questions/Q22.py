#Find Missing Number In Array
arr=[10,20,40,50,60,70,80,90,100]
expected_sum=0
actual_sum=0
for i in range(10,101,10):
    expected_sum+=i
for i in arr:
    actual_sum+=i
print("Missing Number:",expected_sum-actual_sum)
