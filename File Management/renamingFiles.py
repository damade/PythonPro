import os
import shutil

fileList = []
newFileList = []
for filename in os.listdir(r'C:\Users\HP\Downloads\SocialMedia\Website-24-48-96px'):
    fileList.append(filename)
print(fileList)

for itemList in fileList:
    itemList = itemList.replace("-", "_")
    itemList = itemList.replace("8", "")
    newFileList.append(itemList)
print(newFileList)

currentFile = []
for file in fileList:
    file = r'C:\Users\HP\Downloads\SocialMedia\Website-24-48-96px\\' + file
    currentFile.append(file)

newFile = []
for file in newFileList:
    file = r'C:\Users\HP\Downloads\SocialMedia\Website-24-48-96px\\' + file
    newFile.append(file)

for i in range(0, len(currentFile)):
    shutil.move(currentFile[i], newFile[i])
