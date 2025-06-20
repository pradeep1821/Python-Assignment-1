"""1.Write a program in Python to perform the following
operation:
If a number is divisible by 3 it should print “SKILLBREW”
as a string
If a number is divisible by 5 it should print “BRUDITE” as a
string
If a number is divisible by both 3 and 5 it should print
“BRUDITE - NIRVANA” as a string.
"""
a=int(input("enter a number:"))

print(a,"here is the number")
print(f"here is the number{a}")

if (a % 3==0 and a % 5==0):
    print("BRUDITE NIRVANA")
elif a%3==0:
    print("SKILLBREW")
elif a%5==0:
    print("BRUDITE")
