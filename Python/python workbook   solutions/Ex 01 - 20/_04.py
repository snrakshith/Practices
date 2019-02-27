# -- Outcome TypeError !!

# Question:
#   Fix the last line so that it outputs the sum of 1 and 2.

''' Hint: 
#   str(1)  converts integer 1 to string "1". 
#   What would convert string "1" to integer 1?
'''

a = "1"
b = 2
print(int(a) + b)
# --- Alternative
a = "1"
a = int(a)
b = 2
print(int(a) + b)

'''Explanation
    Values in Python can be of different types. 
    In this exercise the value assigned to 'a'  was of string type (i.e. text),
    while the value of 'b'  was an integer (i.e. whole number) and 
    you cannot add strings with integers.
    Therefore we needed to convert the string to an integer using,
    `The int()`  built-in function for the addition operation to be possible.
'''
