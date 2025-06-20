num = int(input("Enter a number: "))
div_sum = sum(i for i in range(1, num) if num % i == 0)
if div_sum == num:
    print("Yes, it's a perfect number")
else:
    print("No, it's not a perfect number")
