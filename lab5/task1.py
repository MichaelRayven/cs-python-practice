days = int(input("Enter days: "))
hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
seconds = int(input("Enter seconds: "))

total = seconds
total += minutes * 60
total += hours * 60 * 60
total += days * 24 * 60 * 60
print("Total:", total, "seconds")