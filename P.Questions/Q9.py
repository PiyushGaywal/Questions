# Write The Programme for Find the largest in Number
num=58749
largest=1
for digit in str(num):
    if int(digit)>largest:
        largest=int(digit)
print(largest)