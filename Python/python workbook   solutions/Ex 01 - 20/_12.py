# more on ranges

my_range = range(1, 21)

number = 1

for number in my_range:
    number *= 10
    print(number, end='\t')

# Alternative 01

updated = [number * 10 for number in range(1, 21)]
print(updated, end='')

# Alternative 02

print([number * 10 for number in range(1, 21)])
