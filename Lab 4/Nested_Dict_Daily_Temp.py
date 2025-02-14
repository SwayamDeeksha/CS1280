# Daily temperatures stored in a dictionary
temps = {
    "sun": 68.8,
    "mon": 70.2,
    "tue": 67.2,
    "wed": 71.8,
    "thur": 73.2,
    "fri": 75.6,
    "sat": 74.0,
}

# User input
day = input("Enter a day (sun, mon, tue, wed, thur, fri, sat): ")
print(f"The temperature on {day} is {temps.get(day, 'Invalid day')}")