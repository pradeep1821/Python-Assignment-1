text = input("Enter a string: ")
letters = sum(c.isalpha() for c in text)
digits = sum(c.isdigit() for c in text)
print("Alphabets:", letters, "& Numbers:", digits)
