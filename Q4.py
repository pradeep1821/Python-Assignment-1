start = int(input("Enter start: "))
stop = int(input("Enter stop: "))
total = sum(i for i in range(start, stop+1) if i % 2 != 0)
print("Sum of odd numbers:", total)
