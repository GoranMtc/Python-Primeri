import pandas as pd
from Logger import Logger

class DataScience():

	# 
	def __init__( self  ):
		self.log = Logger()
		self.log.Log('DataScience - Init')
		pass		

	# 
	def processDataFrame( self, df : pd.DataFrame ):
		self.log.Log('DataScience - processDataFrame')
		
		#get columns of data frame
		self.dfColumns = list( df.columns.values )
				
		print( self.dfColumns )
		
		self.dfColumnTypes = dict( df.dtypes )

		print( self.dfColumnTypes )
		
	#	
		
	
