'''File Handling Practice'''

# # old method in which we have to manually close the file!
# f = open('./lecture11-30/Side_files/file.txt','r') # default mode reading 
# # print(dir(f))
# # print(">>>>>>>>>>>>>>>>>>")
# # file_content = f.read()

# # print(type(file_content))

# test = f.read()
# print(test)
# print(test.count('to'))
# # as files is not open with contxt manager Thus have to close manually 
# f.close()


# with open('./lecture11-30/Side_files/file.txt','r+') as f:
#     print(f.read().count('to'))


# # lets write !

# with open('./lecture11-30/Side_files/file_1.txt','w') as wf: # will create and override if file exists 
#     wf.write("""I am writing this string in the fome of comment as 
#                     this is easy mutiline format to  
#                     write to file  edited    
#                         """)
# # in order to not overrite file .. use a  mode to append text at the end of file .. or you can move seeker with your will!

# with open('./lecture11-30/Side_files/file_2.txt','r+') as f: # will create and override if file exists 
#     f.write("""I am writing this string in the form of comment as 
#                     this is easy mutiline format to  
#                     write to file  edited    
#                         """)
#     f.seek(102) # move pointer to location 102th letter
#     print("pointer location: ", f.tell())
#     f.write(" this line was added through seek function which moves seek pointer in background")
#     print(f.read())


## read image file as binary and copy it ..

with open('./lecture11-30/Side_files/OIP.jpg','rb') as rf: # will create and override if file exists 
    with open('./lecture11-30/Side_files/OIP_copy_2.jpg','wb') as wf:
        with open('./lecture11-30/Side_files/OIP_2.txt','wb') as tf:
            # for line in rf:
            #     wf.write(line) # this will give a copy of read file
            #     tf.write(line) # this will give gibrish as it will not be readable 
            size_to_read = 1024 # if want more control
            file_content = rf.read(size_to_read)
            while (len(file_content))> 0:
                wf.write(file_content) # this will give a copy of read file
                tf.write(file_content) # this will give gibrish as it will not be readable 
                file_content = rf.read(size_to_read)



