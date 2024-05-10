import FileProcess as FileProcess
import os
import time


#Class that controls process
class FileCheck:
		
	#init
	def __init__(self):
		self.controlFlag : bool = True
		self.defaultPath : str = "/home/porti/Documents/ROOT/IT/Python/ETL/Files_Repo"
		self.defaultCheckTimeInterval : int = 300 # seconds

		self.setPath(None)
		self.setCheckTimeInterval( 5 )

	# set value for path, address of folder where are files expected to be
	def setPath( self, path : str ):
	
		if path is None:
			self.path : str = self.defaultPath
		else:
			self.path = path
			
	#set value for field checkTimeInterval in seconds	
	def setCheckTimeInterval( self, checkTimeInterval ):
	
		if checkTimeInterval is None:
			self.checkTimeInterval = self.defaultCheckTimeInterval	
		else:
			self.checkTimeInterval = checkTimeInterval


	#method that start loop that periodically check for new files
	def mainLoop( self ):
		
		self.currentFileName : str = '' 
		self.noFileCheck : int = 0
		
		print( 'loop starts' )
		
		while self.controlFlag:
			
			if self.noFileCheck == 5:				
				break
			
			#check for file in folder
			self.filesList = os.listdir( self.path )
			self.filesList.remove( 'Processed_Files' )
			
			if len(self.filesList) > 0:
				
				self.filesList.sort()
				
				try:		
					print( 'process starts')
					self.currentFileName = str( self.filesList[0] )	
					
					#init class for processing file
					self.fp = FileProcess.FileProcess( self.path, self.currentFileName )

					#start processing of files one by one
					self.fp.processFile()
					
				except Exception as e:
					print( e )
					#logovanje
				finally:
					print( "zavrsena obrada fajla: " + self.currentFileName )
				
				self.filesList.remove( self.currentFileName )
			else:
				self.noFileCheck += 1
				print("Nema fajlova za obradu. noFileCheck=" + str(self.noFileCheck) )	
				
				FileProcess.FileProcess.getBackProcessedFile
				
				
			time.sleep( self.checkTimeInterval )
		print('Obrada zavrsena. ')
