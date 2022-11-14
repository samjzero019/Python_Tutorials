# """Python Follows the LEGB principles"""

# """ LEGB = Local Enclosing Global Builtin """
# # let try normal behaviour then lets try different situations


# x = "I am Global X"


# def outer():
#     # global x  # this will allow us to make change  to global varibale in local scope
#     x = "i am X from outer Function"

#     def inner():
#         nonlocal x # this will also allow us to make changes to enclosing (sub-global) variables in repsective local scope 
#         x = "I am X fromm inner fucntion!"
#         print(x)

#     inner()
#     print(x)
# outer()
# print(x)

# # Results
# # when  line 14 is commented then  line 15 will print x of line 10 as for inner function.. value of x in ourter function will act as global value and
# #   incase line 10  is also commented then value of line 7 will be printed for print function on line 11 and line 15
# # and so on


