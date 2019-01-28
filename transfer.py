#根据list 生成一个csv的format。
' a test module '
import os
BASE_DIR = os.path.abspath('.')

inputpath = os.path.join('list.txt')
outputpath = os.path.join('reformat.txt')

# reformat_mems = 4
def reformat_fun():
    reformat_list = []
    with open(inputpath,'r') as f:
        lists = f.readlines()
    for i,l in enumerate(lists):
        if i == (len(lists)-1):
            reformat_list.append(l.strip('\n').strip())
        else:
            reformat_list.append(l.strip('\n').strip()+',')
    # print(reformat_list)
    # print(len(l))
    memInLine = 70//(len(l)+1)
    # print(memInLine)
    return reformat_list,memInLine

reformat_list, members = reformat_fun()
page = 0
with open(outputpath,'w') as f:
    # f.writeline(reformat_list)
    # print(reformat_list[0:99999])
    for i in range((len(reformat_list)//members+1)):
        f.writelines(reformat_list[page:page + members])
        f.writelines('\n')
        # print(reformat_list[page:page + members])
        page = page + members
    


# reformat_list, 
# with open(outputpath,'w') as f:
#     f.writelines(reformat_list)
# print('successfully')
# input()
