from pathlib import Path		
from Logger import Logger
import pandas as pd
from DataScience import DataScience as ds


#class for processing of one file
class FileProcess:
	
	#init
	def __init__( self, path : str, fileName : str ):
		self.log = Logger()
		self.log.Log( ' processFile - init ' )
		self.fileName : str = fileName
		self.path : str = path
		self.fullPath :str = self.path + '/' + self.fileName
		self.df = pd.DataFrame()

	#
	def processFile( self ):
		self.log.Log( ' processFile - processFile ' )
		self.readFile()

		self.ds = ds()
		self.ds.processDataFrame( self.df )
		

	# Method to process csv file
	def readFile( self ) -> pd.DataFrame:
		self.log.Log( 'processFile - readFile' )

		self.df = pd.DataFrame()
	
		if self.fileName.find('.csv') >= 0:
			self.df = pd.read_csv( self.fullPath )		
			pass

		elif self.fileName.find('.xls') >= 0:
			self.df = pd.read_excel( self.fullPath )		
			pass

		else:
			#nepoznat format
			self.log.Log( 'nepoznat format fajla' )
			pass  

		return self.df		

