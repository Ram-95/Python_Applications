'''Bulk File Renaming Application'''

'''
-> Given a Directory path, Renames the contents of the Directory with the new name provided by the user.
-> Takes care of renaming the files with correct extensions.
-> User can Undo the rename operation.(Only Once)

'''

#OS Module
import os
import time

def bulk_file_rename(path):
    ''' Renames the names of the files in the given path with the given New Name with the extensions intact'''
    #List of directories in the path
    dir_tree = path.split('\\')    

    #Changing Directory to the provided path
    os.chdir(path)

    file_list = os.listdir()
    if len(file_list) == 0:
        return 'The Directory is Empty!!'

    #New Name of the file
    new_name = input('Enter the New File Name: ').strip()

    #To adjust the file numbers at the end of file name according to the no of files in a directory
    length = len(str(len(file_list)))
    j = 1
        
    #Looping over the list of files and renaming according to the files' extensions.
    for i in file_list:
        #if the current item is a directory, then No Extension is needed.
        if os.path.isdir(i):
            os.rename(i, (new_name + '_') + str(j).rjust(length, '0'))

        #if the current item is a File, then extract the extension and append it to the new file name
        elif os.path.isfile(i):
            #To store the extension of a particular file to avoid inconsistent renaming of file extensions
            extension = '.' + i.split('.')[-1]
            os.rename(i, (new_name + '_') + str(j).rjust(length, '0') + extension)

        j += 1
    
    
#************************************************************************#
    ''' Code for Undoing the Rename Operation '''
    choice = input('UNDO Renaming ? (Y/N): ')

    if choice in ('y', 'Y'):
        file_list_new = os.listdir()
        
        for i in range(len(file_list_new)):
            os.rename(file_list_new[i], file_list[i])
        
    return '***************** File Renaming Completed. *****************'
    

#Path where you want to rename the files
path = input('Enter Path: ').strip()

print(bulk_file_rename(path))


