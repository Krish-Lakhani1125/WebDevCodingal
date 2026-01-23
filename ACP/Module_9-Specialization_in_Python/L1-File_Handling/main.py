file_path = r"C:\Users\Krina V\Desktop\Codingal\Web_Dev_Codingal\ACP\Module_9-Specialization_in_Python\L1-File_Handling\Codingal.txt"
with open(file_path, "r") as f:
    print("File in Read Mode -")
    print(f.read())
    f.close()
with open(file_path, "w") as f:
    #write in the file
    f.write(" File in write mode ....")
    f.write("I Also Enjoy Science!")
    f.close()
with open(file_path, "a") as f:
    #open the file in append mode
    #append in the file
    f.write("/n File in append mode....")
    f.write("I Like English Too!")
    f.close()