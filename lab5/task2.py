N = int(input("Enter a number (N): "))
K = int(input("Enter a number (K): "))

print("The last K digits on N are:", N % (pow(10, K)))