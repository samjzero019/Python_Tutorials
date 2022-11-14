
# # but dictionaries is bound  to keys \
dic1 = {'name': 'Alpha','age':'23'}

# #poped_ele = dic1.pop(1) # its error as dictionaries has no index .. they have keys  
# poped_ele = dic1.pop('name')
# print(dic1, poped_ele )
# dic1[1]= "to check pop methods"
# print(dic1, poped_ele )
# poped_ele = dic1.pop(1)
# print(dic1, poped_ele )


# #### get keys , values or items 

# print(dic1.keys()) 

# print(dic1.values()) 

# print(dic1.items()) 



##########Conditionals  

#python has no switch .. as if ..elif ..else if pretty obvious!!! as per them 

# main thing in this is Object Identity (is) which checks if both object has same id/address

# a = 10
# b=a
# c = 30 
# print(a is b)
# print(a is c)

# another thing to note is that which stuff by defuat is taken as false 

# '''
# Flase Values:
#     Fasle
#     None
#     Zero of any numeric type
#     any empty sequence. For example: '', (), []
#     any empty mapping. FOr example: {} 

# '''

# # some testing 

# if False: 
#     print("condition was true" )
# else:
#     print("condition was false")

# if None: 
#     print("condition was true" )
# else:
#     print("condition was false")

# if 0: 
#      print("condition was true" )
# else:
#     print("condition was false")

# if 10: 
#     print("condition was true" )
# else:
#     print("condition was false")


# if '': 
#     print("condition was true" )
# else:
#     print("condition was false")

# if () and [] : 
#     print("condition was true" )
# else:
#     print("condition was false")

# if {}: 
#     print("condition was true" )
# else:
#     print("condition was false")


######################### Functions 

#important thing to note is that of *arg and **kwargs which represent tuple of arguments and dictionary of keywards arguments

def function_to_print_args_and_kwargs(*args,**kwargs):
    print(args)
    print(kwargs)


function_to_print_args_and_kwargs('alpha', 'beta', 1,2,3, name='codewards', pattern = "militry") 

names_arg = ('alpha', 'beta', 1,2,3)
key_args ={'name': 'codewards', 'pattern': "militry"}
#Can also do it 
function_to_print_args_and_kwargs(*names_arg,**key_args) 