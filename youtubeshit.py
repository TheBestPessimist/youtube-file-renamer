'''
Created on 30.09.2012

@author: The Best Pessimist
'''

#-------------------------------------------------------------------------------
# script used for renaming files downloaded with jdownloader 2 from youtube.
# it takes the files and moves them to a specified folder.
# use linux style folder delimiters ('/' and not '\\')
#-------------------------------------------------------------------------

import os
import shutil
import sys
# to force using utf8
reload(sys)
sys.setdefaultencoding("utf-8")


def findNewFileName(oldFileName):
    indexToDelete = oldFileName.rfind('(108')
    if indexToDelete == -1:
        indexToDelete = oldFileName.rfind('(720')
    if indexToDelete == -1:
        indexToDelete = oldFileName.rfind('(480')
    if indexToDelete == -1:
        indexToDelete = oldFileName.rfind('(360')
    if indexToDelete == -1:
        indexToDelete = oldFileName.rfind('(240')
    if indexToDelete == -1:
        indexToDelete = oldFileName.rfind('-[www')  # not used anymore

    # if found a new name to edit
    extension = (os.path.splitext(oldFileName))[1]
    newFileName = oldFileName[:indexToDelete] + extension
    return newFileName


def renameThem(path, newPath):
    
    if not os.path.exists(newPath):
        print 'New path does not exist, creating...'
        os.makedirs(newPath)

    songCounter = 0
    filesFullPath = []

    for dirPath, dirNames, fileNames in os.walk(path):
        filesFullPath += [os.path.join(dirPath, name) for name in fileNames]

    for oldFilePath in filesFullPath:
        songCounter += 1
        oldFileName = os.path.basename(oldFilePath)
        newFileName = findNewFileName(oldFileName)
        newFilePath = os.path.join(newPath, newFileName)

        print songCounter, oldFilePath
        print newFileName
        print newFilePath
        print

        # this might throw a duplicate error. needs further testing
        shutil.copy2(oldFilePath, newFilePath)

    # for debug info
    # print 'Songs processed: ', songCounter


if __name__ == '__main__':
    # redirect stdout
    # sys.stdout = open(os.path.join(os.environ['USERPROFILE'],
    # 'Desktop/rename log.txt'), 'w')
    path = os.path.normpath(u"E:/zzmusic/aac 112/xxx/")
    newPath = os.path.normpath(u"C:/youtube/")

    renameThem(path, newPath)
