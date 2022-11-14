"""
    This file will contains all the practice code for the strings! && some string methods/functions
"""

# leta take a string and assigning it to pre- name as it is prone to change!

str = "Strom Cloud Gathers, Darkness prowels, Revenge is Coming, Best Served Cold! `(0-0)`"

""" You might be thinking that damn it good but str is lengthy .... 
        yes yes i know that as well but you see that 
        single and double quotes string defining does not support
         multi line format so .......
                how to solve this ... 
                    well this is easy....  
                    all you need to do is either concate them by smaller anonymous string 
                    or .. you can use multi line comment format     as shown 
                    
                    # and i am not liking that this VSCode  is not able to distinct it as multi line comment
                    # well yes i can customize that but its hassale to do so!! so i will pretent i never saw this
                    
                    """
str_multiline_format_1 = (  # and you might be wondering ... why this braces.... welll..it cant be helped as ... python is indent sensitive .. and its going to indent error if not placed braces!
    "Strom Cloud Gathers,"
    + "Darkness prowels,"
    + "Revenge is Coming,"
    + "Best Served Cold! "
    + " hahahhaha`(0-0)`"
)


str_multiline_format_2 = """Strom Cloud Gathers,
     Darkness prowels, 
     Revenge is Coming,  
     Best Served Cold! 
      hahahhaha`(0-0)`"""



###===========>>>>>>>>><<<<<<>>>>>><<<<><><><><><><><><<><><<
# make it go lower and higher in Case
print(str_multiline_format_2)
print(str_multiline_format_2.lower())
print(str_multiline_format_2.upper())
print(str_multiline_format_2.title()) # make it sentense case!

#-------====----===----==----- Find index

print("first occurance index of o is: ",str.find('o'))

#--- find count of occurance

print("Count of occurance of o: " , str.count('o'))

# try f strings and formating ..inshort string interpolation
fname = "Sam"
lname = "J"
print("My FIrst name is " + fname + "And my last name is " + lname) # it requires manual spacing w.r.t concate sign!
print("My FIrst name is " , fname , "And my last name is " , lname) # it gives auto spacing w.r.t each comma
print("My FIrst name is {} And my last name is {}".format(fname,lname)) # it requies to add place holders  to each place and later on call format function with required params ... it is sort of improved/custom form of C string interpolation format
print("My FIrst name is %s  And my last name is %s" %(fname ,lname)) # C lang --- string interpolation format
print(f"My FIrst name is {fname} And my last name is {lname}") # new format of string interpolation ... just add f before string do normal interpolation.... web type interpolation with custom indicator


#General!

print(dir(str)) # will give all the methods and function avaliable for this varibale 
# help over class will give details of all the function and help over class function can give specific details on given function!
help(str.lower)
help(str.rfind)

#<<<<<<<<<<<<<<<<<<<<<<<<<<<END STRINGS
