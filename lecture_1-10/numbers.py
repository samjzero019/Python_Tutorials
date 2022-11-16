# lets make a calculator as basic practice in free time

def print_words(filename):
  print(filename)
  count_dict={}
  file_list=[]
  with open(filename) as f:
    file_content = f.read()
    file_list = list(set(file_content.lower().split()))
    # file_list.sort()
    for item in file_list:
        count_dict[item] = file_content.count(item)  # this will cause overriting as many times as they exist 

  return count_dict


def print_top(filename):
    res = {}
    result_dict = print_words(filename)
    while(len(res)!= 20 or len(result_dict)<1):
        max_value_key = max(result_dict, key=result_dict.get)
        res[max_value_key] = result_dict[max_value_key]
        result_dict.pop(max_value_key)

    return res



print_top("./alice.txt")

def mimic_dict(filename):
  """Returns mimic dict mapping each word to list of words which follow it."""
  # +++your code here+++
  result_dict = {}
  with open(filename) as f:
    file_content = f.read()
    file_content_as_list = file_content.split()
    for item in file_content_as_list:
      temp_list =[]
      for i in range(len(file_content_as_list)-1):
        if file_content_as_list[i] == item:
          temp_list.append(file_content_as_list[i+1])
      result_dict[item] = temp_list  
  
  print(result_dict)
  return

mimic_dict("./small.txt")
