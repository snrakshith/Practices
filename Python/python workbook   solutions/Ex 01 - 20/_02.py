# -- Naming Rules !!

# Question:
#   What's wrong with the following script?

"""
  a =  1
 _a  = 2
 _a2 = 3
  2a = 4
"""
# variable assignment of 2a = 4 is invalid


""" 
Answer: 
Line 4 throws a SyntaxError because variables cannot start with a number. 

Explanation: 
Variable names must start with a letter or an underscore. 
Everything else will throw a SyntaxError.

"""
