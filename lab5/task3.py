num = int(input("Enter a number: "))

sum = 0
for digit in str(num):
    sum += int(digit)

print("The sum of the digits is:", sum)