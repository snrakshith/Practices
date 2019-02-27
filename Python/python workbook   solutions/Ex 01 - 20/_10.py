# -- Outcome  Sequence Item Picking !!

# Question:
#    Complete the script so that it prints out a,
#    list slice containing letters a, c, e, g, and i.
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
'''Hint: 
        Again, this is done using slicing syntax,
        but you should add a second colon here and a number after that.
'''
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[0::2])
# Alternative
print(letters[::2])

'''Explaination:
    The complete syntax of list slicing is [start:end:step] .
    When you don't pass a step, Python assumes the,
        step is 1. [:]  itself means get everything from start to end. 
        So, [::2]  means get everything from start to end at a step of two.
'''
