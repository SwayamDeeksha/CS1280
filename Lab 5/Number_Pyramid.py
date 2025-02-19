rows = int(input("Enter the number of rows:"))

for i in range(1, rows + 1):
    print(" " * (rows - i) + " ".join(str(num) for num in range(1, i + 1)))
    
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + " ".join(str(num) for num in range(1, i + 1)))
