# Temperature Lookup
temps = [68.8, 70.2, 67.2, 71.8, 73.2, 75.6, 74.0]
day = input("Enter a day (sun, mon, tue, wed, thur, fri, sat): ")
days = ["sun", "mon", "tue", "wed", "thur", "fri", "sat"]
if day in days:
    print(f"The temperature on {day.upper()} is {temps[days.index(day)]}")
else:
    print("Invalid day")