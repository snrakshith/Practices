# -- Sequence Slicing !!

# Question:
#   Please complete the script so that it prints out a list slice containing items
#   d , e , and f .
#   letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

letters = ["a", "b", "c", "d",
           "e", "f", "g", "h",
           "i", "j"
           ]
# -- Hint
#  For slicing a variable syntax <[start:end+1:step]>
#  Keep in mind that list slicing is upper-bound exclusive.

print(letters[3:6])
print(tuple(letters[3:6]))  # to convert into a tuple
