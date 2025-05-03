rowSize = int(input("Enter the number of rows: "))


if rowSize % 2 == 0:
    halfDiamRow = rowSize // 2
else:
    halfDiamRow = rowSize // 2 + 1


space = halfDiamRow - 1
for i in range(1, halfDiamRow + 1):
    print(" " * space, end="") 
    num = 1
    for j in range(2 * i - 1):
        print(num, end="")
        num += 1
    print()
    space -= 1


space = 1
for i in range(1, halfDiamRow):
    print(" " * space, end="")
    num = 1
    for j in range(2 * (halfDiamRow - i) - 1):
        print(num, end="")
        num += 1
    print()
    space += 1
