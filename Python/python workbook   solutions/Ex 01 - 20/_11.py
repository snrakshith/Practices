# -- Printing out List not manually..

list_of_number = []

for number in range(1, 21):
    list_of_number += list_of_number[number]
    # print(f'numbers are {}', number)
    print(list_of_number)

print("Done!!..")

# list_ = range(1, 21)
# print(list(list_))
