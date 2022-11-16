
#BEFORE

x = 50
y = 30

print((f"Sum of {x} and {y} is: {x + y}"))
print((f"Subtract of {x} and {y} is: {x - y}"))
print((f"Sum of {x} and {y} is: {x * y}"))

#after
import logging
# you cna chnage the format of log ... for this just check doc file .. no need to remember 
logging.basicConfig(filename="./lecture11-30/Side_files/info.txt" ,level=logging.INFO)


logging.info((f"Sum of {x} and {y} is: {x + y}"))
logging.info((f"Subtract of {x} and {y} is: {x - y}"))
logging.info((f"Sum of {x} and {y} is: {x * y}"))
logging.info(("\n"))




##################Exceptions

def custom_sum(x,y):
    return x + y
    

try:
    x = input("Enter integer value of x:")
    y = input("Enter integer value of y:")
    if (type(x)== type(1) and  type(y)== type(1)):
        print(f"custom_sum of {x} and {y} is {custom_sum(x,y)}")
    else:
        raise ValueError 
except ValueError as e:
        print("Given values is not integers")

except Exception as e:
        print("Something went wrong!")

 

