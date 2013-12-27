'''
Created on 30.09.2012

@author: The Best Pessimist
'''

#-------------------------------------------------------------------------------
# Script used for renaming files downloaded with jdownloader 2 from youtube.
# It takes the files and moves them to a specified folder.
# Use linux style folder delimiters ('/' and not '\\')
#-------------------------------------------------------------------------

import os
import shutil
import sys


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
        print ('New path does not exist, creating...')
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

        print(songCounter, oldFilePath)
        print(newFileName)
        print(newFilePath)
        print()

        # this might throw a duplicate error. needs further testing
        shutil.copy2(oldFilePath, newFilePath)

    # for debug info
    # print 'Songs processed: ', songCounter


def main():
    # to redirect stdout
    # sys.stdout = open(os.path.join(os.environ['USERPROFILE'],
    # 'Desktop/rename log.txt'), 'w')
    path = os.path.normpath('C:/Users/CristianViorel/Desktop/PLM/xxx/1')
    newPath = os.path.normpath('C:/Users/CristianViorel/Desktop/PLM/xxx/2')

    renameThem(path, newPath)



if __name__ == '__main__':
    main()