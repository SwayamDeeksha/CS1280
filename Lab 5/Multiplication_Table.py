num = int(input("Enter a number:"))

print(f"The Multiplication Table of {num}")
for i in range(1, 11):
    print(f"{num} X {i} = {num * i}")