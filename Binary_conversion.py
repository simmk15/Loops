num=int(input("Enter a decimal number="))
binary=""
while num>0:
    remainder=num%2
    binary=str(remainder)+binary
    num=num//2
if binary=="":
    binary="0"
print("The binary number is",binary)