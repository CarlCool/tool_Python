# -*- coding: utf-8 -*-
' a test module '
import os
BASE_DIR = os.path.abspath('.')
# print(BASE_DIR)

inputDir = os.path.join(BASE_DIR,'datasetlist.txt')
outputDir = os.path.join(BASE_DIR,'result.txt')
newList = []
with open(inputDir, 'r') as f:
    fileList = f.readlines()

for fl in fileList:
    newList.append("GET " + "'" + fl.strip('\n') + "'" + " " + fl.strip('\n')+ ".txt"+"\n")
# print(newList)

with open(outputDir, 'w') as fw:
    fw.writelines(newList)
print('successfully')
input()
