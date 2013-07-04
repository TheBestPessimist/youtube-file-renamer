
'''
Created on 30.09.2012

@author: The Best Pessimist
'''

#-------------------------------------------------------------------------------
# script used for renaming files downloaded with jdownloader 2 from youtube.
# it takes the files and moves them to a "renamed" folder if succesfull rename
# or leaves them untouched if nothing could be done (actually no, it does not do that :P)
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
	path = os.path.normpath(u"D:\zzmusic\aaaaa\\")
	newPath = os.path.normpath("C:\Users\TheBestPessimist\Desktop\youtube\\")

	counter = 0;
	renameErrorIndex = 0        

	for dirPath, dirNames, fileNames in os.walk(path):
		filesFullPath = [os.path.join(dirPath, name) for name in fileNames]
		for oldFileName in filesFullPath:
			 
			indexToDelete = findIndexToDelete(oldFileName)                
			if indexToDelete != -1 :
				counter += 1;
				extension = (os.path.splitext(oldFileName))[1]
							
				if os.path.exists(oldFileName):
					print oldFileName
					auxFileName = oldFileName[:indexToDelete] + extension

					index = auxFileName.rfind('\\')
					newFileName = os.path.normpath(os.path.join(newPath + auxFileName[index:]))

					print counter,
					print auxFileName
					print newFileName
					print "\n" 

					try:
					#                    newPath = findNewPath(newFileName)
						if not os.path.exists(os.path.normpath(newPath)):
							print 'tibi'
							os.makedirs(os.path.dirname(newPath))
						#                        
						shutil.copy2(oldFileName, newFileName)  # this usually throws me a duplicate
#                     shutil.copy2(newFileName, newPath)
#                    print 'old file name: ' + oldFileName.encode('utf-8', 'replace')
#                    print 'renamed file: ', newFileName.encode('utf-8', 'replace')
# #                    if os.path.isfile(newFileName):
# #                        os.remove(newFileName)
					except Exception, e:
						print e
#                    if os.path.isfile(oldFileName):
#                        print 'Possible duplicate: ', oldFileName.encode('utf-8', 'replace')
#                        os.remove(oldFileName)
						renameErrorIndex = renameErrorIndex + 1
#                    print 'Error ', renameErrorIndex, '. ', oldFileName.encode('utf-8', 'replace')
#                    pass

							
	if not renameErrorIndex:
		print "Success!"
	else:
		print 'Had some errors. about ', renameErrorIndex, ' of them :('

	print counter
	  
	  
if __name__ == '__main__':
	 renameThem()
