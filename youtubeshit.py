
'''
Created on 30.09.2012

@author: The Best Pessimist
'''

#-------------------------------------------------------------------------------
# script used for renaming files downloaded with jdownloader 2 from youtube.
# it takes the files and moves them to a "renamed" folder if succesfull rename
# or leaves them untouched if nothing could be done (actually no, it does not
# do that just yet :P)
#-------------------------------------------------------------------------------

import os
import shutil
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# redirect stdout
# sys.stdout = open(os.path.normpath('C:\Users\CristianViorel\Desktop\output.txt'), 'w')


def findIndexToDelete(oldFileName):
	indexToDelete = oldFileName.rfind('(108')
	if indexToDelete == -1 :
		indexToDelete = oldFileName.rfind('(720')
	if indexToDelete == -1 :
		indexToDelete = oldFileName.rfind('(480')
	if indexToDelete == -1:
		indexToDelete = oldFileName.rfind('(360')
	if indexToDelete == -1 :
		indexToDelete = oldFileName.rfind('(240')            
	if indexToDelete == -1 :
		indexToDelete = oldFileName.rfind('-[www')
	return indexToDelete


def renameThem():
	# path = os.path.normpath("D:\Users\TheBestPessimist\Desktop\music\\")
	path = os.path.normpath(u"D:/zzmusic/a/")
	newPath = os.path.normpath(u"C:/Users/TheBestPessimist/Desktop/youtube/")

	songCounter = 0;
	renameErrorIndex = 0        
	filesFullPath = []

	for dirPath, dirNames, fileNames in os.walk(path):
		filesFullPath += [os.path.join(dirPath, name) for name in fileNames]
		
	for oldFilePath in filesFullPath:
		# print songCounter, oldFilePath

		oldFileName = os.path.basename(oldFilePath)
		indexToDelete = findIndexToDelete(oldFileName)                
		
		# if found a new name to edit
		if indexToDelete != -1:
			songCounter += 1;
			extension = (os.path.splitext(oldFileName))[1]
			auxFileName = oldFileName[:indexToDelete] + extension
			newFilePath = os.path.join(newPath, auxFileName)

			print songCounter, oldFilePath
			print auxFileName
			print newFilePath
			print "\n" 
			'''
			try:
			#                    newPath = findNewPath(newFilePath)
				if not os.path.exists(os.path.normpath(newPath)):
					print 'tibi'
					os.makedirs(os.path.dirname(newPath))
				#                        
				shutil.copy2(oldFilePath, newFilePath)  # this usually throws me a duplicate
#                     shutil.copy2(newFilePath, newPath)
#                    print 'old file name: ' + oldFilePath.encode('utf-8', 'replace')
#                    print 'renamed file: ', newFilePath.encode('utf-8', 'replace')
# #                    if os.path.isfile(newFilePath):
# #                        os.remove(newFilePath)
			except Exception, e:
				print e
#                    if os.path.isfile(oldFilePath):
#                        print 'Possible duplicate: ', oldFilePath.encode('utf-8', 'replace')
#                        os.remove(oldFilePath)
				renameErrorIndex = renameErrorIndex + 1
#                    print 'Error ', renameErrorIndex, '. ', oldFilePath.encode('utf-8', 'replace')
#                    pass

			'''
	if not renameErrorIndex:
		print "Success!"
	else:
		print 'Had some errors. about ', renameErrorIndex, ' of them :('

	print 'Songs processed: ', songCounter
	  
	  
if __name__ == '__main__':
	 renameThem()
