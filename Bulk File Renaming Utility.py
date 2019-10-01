'''Bulk File Renaming Application'''

'''
-> Given a Directory path, Renames the files with the new name provided by the
user.
-> Takes care of renaming the files with correct extensions.
-> User can Undo the rename operation.(Only Once)
-> Ignores the Directories - Will not rename the Directories.
'''

#OS Module
import os

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

    #List of directories names
    dir_list = [x for x in file_list if os.path.isdir(x) == True]
    
    
    #List of Files names
    file_list = [x for x in file_list if os.path.isfile(x) == True]

    
    
    
    #Looping over the list of files and renaming according to the files' extensions.
    for i in file_list:
        #To store the extension of a particular file to avoid inconsistent renaming of file extensions
        extension = '.' + i.split('.')[-1]
        os.rename(i, (new_name + '_') + str(j).rjust(length, '0') + extension)
        j += 1

    print('File Renaming Completed Successfully.')

#************************************************************************#
    ''' Code for Undoing the Rename Operation '''
    choice = input('UNDO Renaming ? (Y/N): ')

    if choice in ('y', 'Y'):
        file_list_new = os.listdir()
        file_list_new = [x for x in file_list_new if os.path.isfile(x) == True]
        
        for i in range(len(file_list_new)):
            os.rename(file_list_new[i], file_list[i])


    return '*********** File Renaming Completed.******************'

#Path wheere you want to rename the files
path = input('Enter Path: ').strip()

print(bulk_file_rename(path))

'''
Rename all the contents of the directory no matter what it is..
use os.path.isfile and os.path.isdir
'''

