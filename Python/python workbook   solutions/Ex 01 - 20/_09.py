# -- Outcome Negative Slicing !!

# Question:
#    Complete the script so that it prints out a list slice containing the last three items of list letters .
#    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]


letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]

# print(letters[7:])
# print(letters[7:10])
# -----
# Alternative
print(letters[-3:])

'''Hint: 
    Since we're dealing with last items, it is wise to use negative indexing.
    [-3:]  means from item with index -3  (i.e. h ) to the very last item of the list.
    When you don't put any index to the right of the colon everything is included ,
    and upper-bound exclusivity is ignored.
'''
