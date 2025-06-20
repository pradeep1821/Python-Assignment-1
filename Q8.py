a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def lcm(x, y):
    greater = max(x, y)
    while True:
        if greater % x == 0 and greater % y == 0:
            return greater
        greater += 1

print("LCM is:", lcm(a, b))
