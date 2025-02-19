# Get user input
num = int(input("Enter a number:"))

# Print Multiplication table
print(f"The Multiplication Table of {num}")
for i in range(1, 11):
    print(num*i)
    # Loop 1 to 10
    print(f"{num} X {i} = {num * i}")
