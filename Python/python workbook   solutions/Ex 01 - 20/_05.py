# -- Sequence Indexing !!

# Question:
#    Complete the script so that it prints out the second item of the list.
'''Hint:
    List indexing starts from 0.
'''
letters = ["a", "b", "c", "d",
           "e", "f", "g", "h",
           "i",  # comment can be provided!!
           "j"
           ]

expected_op = letters[1]
print(expected_op)
# - Alternative
print(letters[1])

'''Explanation: 
Every item of a list is referenced to an index number starting from zero and increasing by one.
Such a `hidden index system` is used to access list items. 
Therefore,we accessed item b using an index of 1.
'''
