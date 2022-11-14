# # do check CURD for rach type and slicing methods 

# # lets take a list First 

# my_custom_list  = [1,2,3,'23','dont ask me',chr(65)]

# print("my custom list", my_custom_list)
# print("my custom list printed in reverse", my_custom_list[-1])
# print("my custom list printing with jumps", my_custom_list[::2])

# my_custom_list.append('newly added') 
# print(">>>>>>>",my_custom_list) # append only addes at the last of list!
# #my_custom_list.append('newly added ', "beleive me") # append only takes one one argumnet (can add only one value/item)

# # for multiple value addition .. it extension not append/insert but that should be list as well!

# my_custom_list.extend(["alpha ", "is ", "added", "by" , "multiple", "parts" ,"thorugh" ,"extend"])


# print(my_custom_list.append('newly added again')) # this will give none! reason ... well most of directly modifing function return none in python!

# print(">>>>>>><<<<<<<<<<",my_custom_list)

# ## remove element from list

# # remove will remove given value and pop will remove given indexed value or by default last one
# # my_custom_list.remove(2)
# poped= my_custom_list.pop(2)
# print(my_custom_list, "poped", poped)


# ########################## Sorting 

# # my_custom_list.sort() # will change the list itself and sort it !
# # print(">>>>>>><<<<<<<<<<",my_custom_list)
# # my_custom_list.sort(reverse=True)

# # above is giving error as list is not homo generic! 
# my_list =[1,2,36,8,9,4]
# sorted_list = sorted(my_list) # this will not change the list but return the sorted list
# print(sorted_list, " give list:", my_list)

# my_list.sort() # will change the list itself

# print(my_list)
# my_list.sort(reverse=True) # will change th list itself 

# print(my_list)

# ################## finding index adn checking preseneceof element in list 

# print("Index of value 8 is " ,my_list.index(8))
# # using in to check presence and get bool value
# print(8 in my_list)
# print(8 not in my_list)
# print(8 is not '8')


# # 

# for item in my_list:
#     print(f"Index of value {item} is " ,my_list.index(item))
# ## or we can use emurator to directly get index in loop
# print('\n')

# for index,item in enumerate(my_list):
#     print(f"Index of value {item} is " ,index)

# # converting list into comma or something seperated string 
# lst = ['i', 'am' ,'joining',' str list ','into str']
# list_into_str =  ','.join(lst)

# print("Comma Sepeaeted String made from list made of striong literals/words  ", list_into_str)

# BE CAREFULL AS PYTHON PASSING IS BY REFRENCE TYPE@@@@@@@@@@@@@@@@@@@@

# list1 = [1,4,6,8]
# list2 = list1
# print('list 1', list1, 'list2', list2)

# list1[0] = 2
# print('list 1', list1, 'list2', list2)


# list1 = [1,4,6,8]
# list3 = list1
# list2 = list1.copy() # can also use list1[:] # slicing method
# print('list 1', list1, 'list2', list2)

# list1[0] = 2
# print('list 1', list1, 'list2', list2, 'list3', list3)
# print('list 1', id(list1), 'list2', id(list2), 'list3', id(list3))



# list1 = [1,4,6,8]
# list3 = []
# list3 = list1
# list2 = list1.copy() # can also use list1[:] # slicing method
# print('list 1', list1, 'list2', list2)

# list1[0] = 2
# print('list 1', list1, 'list2', list2, 'list3', list3)
# print('list 1', id(list1), 'list2', id(list2), 'list3', id(list3))


# ###################### Tuples 

# i_am_tuple = ('alpha','beta',23,43)
# print(i_am_tuple)
# #i_am_tuple[0] = 55 # error as tuples can be changed later on # they are immutables 
# print(i_am_tuple.index(23))




# t1 = (1,4,6,8)
# t3 = t1 # always shallow copy  they are immutable and could only be given values at the time of assignment!
# t2 = deepcopy(t1) 
# #del(t3) #..tuples are 

# print('list 1', t1, 'list2', t2, 'list3', t3)
# print('list 1', id(t1), 'list2', id(t2), 'list3', id(t3))

############ !!!!!!important to consider ..... let make immutable to behave half immutable 

# from copy import deepcopy
# # some strangeness of false nested nature to invalid a part of immutablity

# tup = (1, 2, [])
# put = deepcopy(tup) # a deep copy 
# #tup.append("hello ") # its an error as object level is still immutable 
# put[2].append('hello')
# put[2].append('hello1')
# print(tup) # (1, 2, ['hello'])
# print (put) # (1, 2, [])
# print("tup ", id(tup), 'put', id(put))


# SETs 
# --unordered  --unique element bearer , -- empty sets are defined by class 
# empty_set = set()

# s2 = {1,2,3,4,5, 'charlie','beta'} # thus only string values is not following order
# s3 = {'Alpha', 'Charlie', 'Beta'}

# print('s2',s2, 's3',s3)
# print((dir(set)))


# s4 = {1,2,3,4,5, 'charlie','beta'}
# #print(s4[2]) # sets do not hvae subscript then i think they cant be sliced ... lets check 
# #print(s4[2:]) no slicing in sets .. you cant modify already present element in sets 
# s4.add('can add/remove')
# s4.add(10)
# print(s4)
# s4.pop() # pop in sets .. has no overloaded functions ... thus poping with index is not avaliable in sets 
# print(s4) # AND pop in sets pop out element RANDOM  value 
# s4.remove(5) # remove given value !
# print(s4)
# s4.update(('alpha', 0, 6,4,7,8,9)) # can add multiple values but in the form od iterables 

# print(">>>>>>>>>>>>>>>>>>>>",s4)


##////////////////////////////// Just testing 

# list = ['alpha', 'beta','charlie']
# #ele =  list.pop('alpha) # its error in lists 
# ele =  list.pop(2)
# list.remove('alpha')
# print(list, ele)


# # but dictionaries is bound  to keys \
# dic1 = {'name': 'Alpha','age':'23'}

# #poped_ele = dic1.pop(1) # its error as dictionaries has no index .. they have keys  
# poped_ele = dic1.pop('name')
# print(dic1, poped_ele )
# dic1[1]= "to check pop methods"
# print(dic1, poped_ele )
# poped_ele = dic1.pop(1)
# print(dic1, poped_ele )


# l = [0,1,2,3,4,5]
# for i,item in enumerate(l):
#     print('index', i, 'item', item, 'indexed value',l[-i-1])
