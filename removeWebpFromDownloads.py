import os
from send2trash import send2trash

os.chdir('C:\\Users\\marti\\Downloads')
print("Current Working Directory: ", os.getcwd())

for folderName, subfolders, filenames in os.walk('C:\\Users\\marti\\Downloads'):
    for filename in filenames:
        if filename.endswith('.webp'):
            file_path = os.path.join(folderName, filename)
            send2trash(file_path)
            print('Remove .webp file: ' + file_path)
    print('The filenames in ' + folderName + ' are: ' + str(filenames))
    print()


