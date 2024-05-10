from pathlib import Path		
from Logger  import Logger
import pandas as pd

#class for processing of one file
class FileProcess:
	
	
	def __init__( self , path : str, fileName : str ):
 		#logovanje inicijalizacije fajla
		self.fileName : str = fileName
		self.path : str = path		
		self.fullPath :str = self.path + '/' + self.fileName
		self.log = Logger()
			
	def processFile( self ):
		#logovanje da je pocela obrada fajla		
		self.log.Log( ' processFile - Start ' )
		self.readFile()

		self.moveProcessedFile()		

	# Method to process csv file
	def readFile( self ) -> pd.DataFrame:
		self.log.Log( 'processFile_csv' )

	
		if self.fileName.find('.csv') >= 0:
			#self.df = pd.DataFrame()
			self.df = pd.read_csv( self.fullPath )		
			pass

		elif self.fileName.find('.xls') >= 0:
			self.df = pd.DataFrame()
			self.df = pd.read_excel( self.fullPath )		
			pass

		else:
			#nepoznat format
			#log
			pass  
		
	def moveProcessedFile( self ):
		self.log.Log( 'moveProcessedFile' )	
		self.processedFilePath : str = "/home/porti/Documents/ROOT/IT/Python/ETL/Files_Repo/Processed_Files"
		try:
			Path( self.fullPath ).rename( self.processedFilePath + '/' +self.fileName )
			#log.Log( 'Fajl je prenet' )
		except Exception as e:
			self.log.Log( e )

	@staticmethod
	def getBackProcessedFile():
		self.log.Log( 'getBackProcessedFile' )	
		self.processedFilePath : str = "/home/porti/Documents/ROOT/IT/Python/ETL/Files_Repo/Processed_Files"
		try:
			Path( "/home/porti/Documents/ROOT/IT/Python/ETL/Files_Repo/Processed_Files/File_1.csv" ).rename( "/home/porti/Documents/ROOT/IT/Python/ETL/Files_Repo/File_1.csv" )
			
			Path( "/home/porti/Documents/ROOT/IT/Python/ETL/Files_Repo/Processed_Files/File_2.xls" ).rename( "/home/porti/Documents/ROOT/IT/Python/ETL/Files_Repo/File_2.xls" )

			
			self.log.Log( 'Fajl je vracen' )
		except Exception as e:
			self.log.Log( e )


