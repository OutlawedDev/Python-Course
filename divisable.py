print("Enter a Number (numerator): ")
num = int(input())
print("Enter a Number (Denominator): ")
numb = int(input())

if num%numb == 0:
    print("/n +str(num)+ is divisable by +str(numb)")
else:
    print("/n +str(num)+ is not divisable by +str(numb)")