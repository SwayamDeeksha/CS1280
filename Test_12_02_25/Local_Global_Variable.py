x = 5
print(f"The global variable x - value is {x}")
def my_fn():
    y = 10
    print(f"The local variable y - value is {y}")
    print(f"The global variable x - value is {x} even inside the function")
    
my_fn()