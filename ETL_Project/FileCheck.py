import FileProcess as fp
import os
import time
from Logger import Logger

#Class that controls process
class FileCheck:
		
	#init
	def __init__(self):
		self.controlFlag : bool = True
		self.path : str = None

		self.scriptDir = os.path.dirname( __file__ )
		self.defaultPath : str          = "Files_Repo/"
		self.defaultPathProcessed : str = "Files_Repo/Processed_Files/"

		self.defaultCheckTimeInterval : int = 300 # seconds

		self.setPath( None )
		self.setCheckTimeInterval( 2 )

		self.log = Logger()		

	# set value for path, address of folder where are files expected to be
	def setPath( self, path : str ):
	    	
		if path is None:
			self.path = os.path.join( self.scriptDir, self.defaultPath )
		else:
			self.path = path
			
		print( 'self.path =>' + self.path )
		print( 'self.scriptDir =>' + self.scriptDir ) 
		
	#set value for field checkTimeInterval in seconds	
	def setCheckTimeInterval( self, checkTimeInterval ):
	
		if checkTimeInterval is None:
			self.checkTimeInterval = self.defaultCheckTimeInterval	
		else:
			self.checkTimeInterval = checkTimeInterval

	# method that start loop that periodically check for new files
	def mainLoop( self ):
		
		self.currentFileName : str = '' 
		self.noFileCheck : int = 0
		
		while self.controlFlag:
			
			if self.noFileCheck == 3:				
				break
			
			#check for file in folder
			self.filesList = os.listdir( self.path )
			self.filesList.remove( 'Processed_Files' )

			for fileName in self.filesList: #if len(self.filesList) > 0:
				try:		
					self.log.Log( 'start:' + fileName )	

					#init class for processing file
					self.fp = fp.FileProcess( self.path, fileName )

					#processing of one file
					self.fp.processFile()
					
					self.moveProcessedFile( self.path, fileName )

				except Exception as e:
					print( e )
				finally:
					print( "zavrsena obrada fajla: " + self.currentFileName )
			else:
				self.noFileCheck += 1
				print("Nema fajlova za obradu. noFileCheck=" + str(self.noFileCheck) )	
				
				time.sleep( self.checkTimeInterval )
				
		print('Obrada zavrsena. ')
		
		#self.getBackProcessedFiles( self.filesList )

 	# Vracanje fajlova u procsuiranje 		
	def getBackProcessedFiles( self, filesList : list ):
		self.log.Log( 'FileCheck - getBackProcessedFile' )	

		for fileName in self.filesList:
			try:
				Path( self.defaultPathProcessed + fileName ).rename( self.path + fileName )
				self.log.Log( 'Fajl je vracen:' + fileName )
			except Exception as e:
				print( e )

		print("Svi fajlovi vraceni")	

	#Premestanje procesuiranigh fajlova		
	def moveProcessedFile( self, path, pathProcessed, fileName ):
		self.log.Log( 'moveProcessedFile' )	
		try:
			Path( path ).rename( pathProcessed + fileName )
			self.log.Log( 'Fajl je prenet' )
		except Exception as e:
			self.log.Log( str(e) )

