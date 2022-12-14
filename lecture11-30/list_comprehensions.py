#code by nomal looping -> list comprehensions for lists , tupes and sets.....
# zip(iteratable_1,iteratable_2 ),
#  yield---> return 
# expresion generator
# map /filter  ,
#  lamda  





def match_ends(words):
  # +++your code here+++
  count = 0
  for str in words:
    if len(str) > 1 and str[0] == str[-1]:
      count+=1   
  return count

def front_x(words):
  # +++your code here+++
  list2=[str for  str in words if str[0] == 'x']
  for str in list2:
    words.remove(str)
  words.sort()
  list2.sort()

  return list2 + (words) 


# def sort_last(tuples):
#   # +++your code here+++
#     for i in tuples[:len(tuples)-1]:
#         for index,item in enumerate(tuples[:len(tuples)-1]):
#             if item[-1] > tuples[index+1][-1] :
#                 x= tuples[index]
#                 tuples[index] = tuples[index+1]
#                 tuples[index+1] = x
#     return tuples

def get_last(itm):
    return itm[-1]

def sort_last(tuples):
    # +++your code here+++
    return sorted(tuples, key=get_last)

def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
  print('match_ends')
  test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
  test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
  test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

  print()
  print ('front_x')
  test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
  test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
  test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])
  
  print
  print ('sort_last')
  test(sort_last([(1, 3), (3, 2), (2, 1)]),
       [(2, 1), (3, 2), (1, 3)])
  test(sort_last([(2, 3), (1, 2), (3, 1)]),
       [(3, 1), (1, 2), (2, 3)])
  test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
       [(2, 2), (1, 3), (3, 4, 5), (1, 7)])



if __name__ == '__main__':
  main()










