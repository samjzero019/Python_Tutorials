
# from Side_files import my_module as mm

# print(mm.find_index(['alpha','beta', 'charlie', 'delta'], 'delta'))

# test some built-in modules like MAth , Random , dateTime, calender, os , sys 

import os, sys, math, calendar, datetime,random

print(os.getcwd()) # current working directory 
print(sys.path) # get lib paths 

print(math.pow(3,3)) # get power 
print(random.random()) # get random value 

print(datetime.date.today()) # Todays' date 
print(calendar.isleap(2020))
