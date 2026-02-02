#create a new file
new_file = open('New_File.txt','x')
new_file.close()

#check if a file exists
import os
print("Checking if my_file exists or not....")
if os.path.exists("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("The file does not exists")

#create a new if it doesn't
my_file = open('my_file.txt','w')
my_file.write("Hi! I am Ppenguin and I am 1 yr old.")
my_file.close()

#delete file name Codingal
os.remove(r'C:\Users\Krina V\Desktop\Codingal\Web_Dev_Codingal\ACP\Module_9-Specialization_in_Python\L3-Operations_on_a_File_part_2\Codingal.txt')

#delete the folder
os.rmdir(r'C:\Users\Krina V\Desktop\Codingal\Web_Dev_Codingal\ACP\Module_9-Specialization_in_Python\L3-Operations_on_a_File_part_2\Folder')