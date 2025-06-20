def digit_sum(n):
    while n >= 10:
        n = sum(int(i) for i in str(n))
    return n

num = int(input("Enter a number: "))
print("Final Output:", digit_sum(num))
