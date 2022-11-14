print("importing my_module ")

def find_index(to_search,target):
    for index,item in enumerate(to_search):
        if item == target:
            return index
    return -1
