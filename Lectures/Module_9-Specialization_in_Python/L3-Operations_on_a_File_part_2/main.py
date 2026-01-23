#write in file using with() function
file_path = r"C:\Users\Krina V\Desktop\Codingal\Web_Dev_Codingal\Lectures\Module_9-Specialization_in_Python\L3-Operations_on_a_File_part_2\Codingal.txt"

with open(file_path,'w') as file:
    file.write("Hi! I am Penguin and I am 1 yr old.")
file.close()

#split file into words
with open(file_path,'r') as file:
    data = file.readlines()
    print("Words in this file are ....")
    for line in data:
        word = line.split()
        print(word)
file.close()