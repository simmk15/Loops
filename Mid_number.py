num=input("Enter a number=")
product=1
for i in range(len(num)):
    for j in range(1):
        if i !=0 and i != len(num)-1:
            product=product*int(num[i])
print("Product of middle digits is=",product)