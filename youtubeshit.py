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
        newFileName = find_new_file_name_v2(oldFileName)
        newFilePath = os.path.join(newPath, newFileName)

        # this throws so many errors... fml and unicode... :-(
        # print(songCounter, oldFilePath)
        # print(newFileName)
        # print(newFilePath)
        # print()

        # this might throw a duplicate error. needs further testing
        shutil.copy2(oldFilePath, newFilePath)


def find_new_file_name_v2(oldFileName):
    oldFileName = remove_OFM(oldFileName)
    indexToDelete = oldFileName.rfind('(')

    # if found a new name to edit
    extension = (os.path.splitext(oldFileName))[1]
    newFileName = oldFileName[:indexToDelete] + extension
    return newFileName


def remove_OFM(oldFileName):
    """Remove the "(Official music video)" shit from the name"""

    newFileName = oldFileName
    poz1 = oldFileName.lower().find('(offi')
    poz2 = oldFileName.lower().find('video)', poz1) + len('video)')
    if poz1 > 0 and poz2 > 0:
        newFileName = oldFileName[:poz1] + oldFileName[poz2:]
        print(poz1, poz2)
    return newFileName


def main():
    # to redirect stdout
    # sys.stdout = open(os.path.join(os.environ['USERPROFILE'],
    # 'Desktop/rename log.txt'), 'w+')
    # path = os.path.normpath('C:/Users/CristianViorel/Desktop/PLM/xxx/1')
    path = os.path.normpath("E:/xxx/new - Copy")
    newPath = os.path.normpath('C:/xxx/')

    renameThem(path, newPath)



if __name__ == '__main__':
    main()