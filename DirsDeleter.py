import os

def DirsDeleter(PathReprt):

  def RepEmpty(PATH):
     if len(os.listdir(PATH)) == 0 :
         isEmpty = True 
     else : 
         isEmpty = False
     return isEmpty
  
  if '\\' in PathReprt :
      PathReprt = PathReprt.replace('\\','/') 
  # new point 
  os.chdir(PathReprt)
  while(os.path.exists(PathReprt)):
    if RepEmpty(os.getcwd()):
       print('Directory {} is empty '.format(os.getcwd()))
       DirDel = os.getcwd()
       # new point 
       os.chdir(os.path.dirname(os.getcwd()))
       os.removedirs(DirDel)
       if not os.path.exists(DirDel):
           print('_______________________')
           print('\nDirectory deleted successfully')
           print('-----------------------')
           DirDel = 0 
    elif not RepEmpty(os.getcwd()):
       print('Directory {} is not empty '.format(os.getcwd()))
       for element in os.listdir(os.getcwd()) : 
          if os.path.isfile(element):
             print('File detected: ', element)
             os.remove(element)
             if not os.path.exists(element):
                print('File deleted successfully')
          if os.path.isdir(element):
             print('Folder detected: ', element)
             # new point 
             os.chdir(os.path.join(os.getcwd(), element))
             break  
  RepNotImport = os.path.join(os.getcwd(), '__pycache__')      
  if os.path.exists(RepNotImport):
       DirsDeleter(RepNotImport)
