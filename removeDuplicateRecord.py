''' remove the duplicate records'''
import os
BASE_DIR = os.path.abspath('.')
# print(BASE_DIR)

inputDir = os.path.join(BASE_DIR,'record.txt')
outputDir = os.path.join(BASE_DIR,'result.txt')
newList = []
with open(inputDir, 'r') as f:
    recordList = f.readlines()

s = set(recordList)
for i in s:
    print("%s has found %s" % (i,recordList.count(i)))
print(s)

with open(outputDir, 'w') as fw:
    fw.writelines(s)
print('successfully')
input()
