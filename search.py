# 批量search

import os
# import tkFileDialog
    
def readFilename(file_dir):
    for root, dirs, files in os.walk(file_dir): 
        return files,dirs,root

# pathlists = []
def getPath(rootPath,pathlists):
    files,dirs,root = readFilename(rootPath)
    # print(files)
    if(files != [] or dirs != []):
        if (files != []):
            for f in files:
                path = os.path.join(root,f)
                pathlists.append(path)
        if (dirs != []):
            for d in dirs:
                getPath(os.path.join(root,d),pathlists)

    return pathlists
# path = getPath(os.path.join('.'))
# print(path)


# print(readFilename("."))

def searchInFile(path,suffixes,arg):
    if path.endswith(suffixes):
        try:
            with open(path,encoding='UTF-8') as fh:
                for line in fh:
                    if arg in line:
                        print(os.path.realpath(path))
                        fh.close
                        return True
                # print('not found')
                fh.close
                return False     
        except Exception as e:
            print(os.path.realpath(path),e)
                # print('error',path,'/n')

if __name__ == "__main__":
    pathlists = []
    file_dir = 'C:\\from old pc\\SametimeTranscripts\\shsongli@cn.ibm.com'     #文件路径
    arg = 'COPY'       #要查找的字符
    suffixes = 'html'   #后缀名
    pathlist = getPath(file_dir,pathlists)
    for p in pathlist:
        # print(p)
        searchInFile(p,suffixes,arg)
    os.system("pause")

   

# searchInFile('./ttt1.txt','2017')
