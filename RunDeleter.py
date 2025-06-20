import os
from DirsDeleter import DirsDeleter

print("__________________Delete Non-Empty Directory__________________\n")
Quit = 1
while(Quit != 'X'):
   
   path = str(input("Enter the full path of the directory:"))

   if '/' or '\\' in path : 
       if '\\' in path :
               path = path.replace('\\','/') 
       print('\n\n/!\\ All files and directories in "{}" will be deleted.'.format(path))
       confirm = input("Are you sure [Y/N]:").upper()
       if confirm == 'Y' :
           try :
               print("\nStarting deletion of directory: {}\n".format(path))
               DirsDeleter(path)
           except Exception as errorFond :
                print("Error: ",errorFond)
                input()
       else :
           print('\nDeletion of directory "{}" canceled\n'.format(path))
   else :
       print("\nInvalid Path!")

   PathMyRep = 'C:/Users/merouane/Documents/Python/MyWork - Python/Delete Repertoire'
   RepNotImport = os.path.join(PathMyRep,'__pycache__')      

   if os.path.exists(RepNotImport): 
          DirsDeleter(RepNotImport)    
   print("\n(1) Delete New Directory\n(X) Quit ")
   Quit = input().upper()

