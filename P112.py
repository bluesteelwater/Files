import os 
#Operating System
import shutil
#Shifting Files from one location to another

source='C:/Users/bholm/downloads'
destination='C:/Users/bholm/OneDrive/Pictures'

files=os.listdir(source)
for i in files:
    name,ext=os.path.splitext(i)
    #Splits the name of the file like .png and downloads
    if ext == '':
        continue
    if ext in ['.txt', '.doc','docx','pdf']:
        path1 = source + '/' + i
        path2 = destination + '/' + "Document_Files"
        path3 = destination + '/' + "document_Files" + '/' + i

        if os.path.exists(path2):
            print('moving')
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print('creating folder and moving')
            shutil.move(path1,path3)