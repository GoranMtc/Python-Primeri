from pathlib import Path		


#class for processing of one file
class FileProcess:
	
	def __init__( self , path : str, fileName : str ):
 		#logovanje inicijalizacije fajla
		self.fileName : str = fileName
		self.path : str = path		
			
	def processFile( self ):
		#logovanje da je pocela obrada fajla		
		print( ' processFile - Start ' )
		
		if self.fileName.find('.csv') >= 0:

			self.processFile_csv()	
			pass

		elif self.fileName.find('.xls') >= 0:

			self.processFile_xls()	
			pass

		else:
			#nepoznat format
			#log
			pass  

		self.moveProcessedFile()

	# Method to process csv file
	def processFile_csv( self ):
		print( 'processFile_csv' )
		pass
	
	#Method to process xls file
	def processFile_xls( self ):
		print( 'processFile_xls' )	
		pass

	def moveProcessedFile( self ):
		print( 'moveProcessedFile' )	
		self.processedFilePath : str = "/home/porti/Documents/ROOT/IT/Python/ETL/Files_Repo/Processed_Files"
		try:
			Path( self.path + '/' + self.fileName ).rename( self.processedFilePath + '/' +self.fileName )
			print( 'Fajl je prenet' )
		except Exception as e:
			print( e )
