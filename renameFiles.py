import os
def renameFiles():
    folder_path = "/Users/rohitmungre/Downloads/prank";
    file_list = os.listdir(folder_path)
    print(file_list)
    saved_path = os.getcwd();
    os.chdir(folder_path)

    for file_name in file_list:
        new_file_name = file_name.translate(None, "0123456789")
        os.rename(file_name, new_file_name)
renameFiles()    

