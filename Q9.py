lst = [1, 2, 3, 2, 4, 1, 2, 4, 5]
freq = {}

for item in lst:
    freq[item] = freq.get(item, 0) + 1

print("Frequency count:", freq)
