"""
cd ..
cd solution_files
cd Test_Project_1
python3 provera.py
pip3 install pandas
"""
import pandas as pd
from os.path import exists
import connect as connection
from Logger import Logger

class DataBaseUtil():
	
	# init
	def __init__( self, df : DataFrame ):
		self.log = Logger()
		self.log.Log("=> DataBaseUtil-Init")
		self.df = df
        
    # lista kolona
	def getFileColumns( self ):
		self.log.Log( "getFileColumns" )
		self.columns = list( self.df.columns.values )

	# kreiraj sql za tabelu
	def createDml( self ):
		self.log.Log( "createDml" )

		self.read_csv_file()
		columns = self.columns

		sql = 'Create+table+if+not+exists+food_orders'
		sql = sql + '('

		for column in columns:
			column = column.strip()
			sql = sql +',+'+ column +'+char(100)'		

		sql = sql + ')'
		sql = sql.lower()
		sql = sql.replace('/','_').replace(' ','_').replace('+',' ').replace('(,','(')
		self.sql = sql

	# kreiraj tabelu
	def createTable( self, dml ):
		self.log.Log( 'createTable' )

		#create connection		
		dbc = connection.db_connection()
		dbc.create_connection()
		self.conn = dbc.get_connection()

		#cursor
		self.cur = self.conn.cursor() 

		#execute statement
		try:
			self.cur.execute( self.sql )

		except Exception as e:
			print( e )

		else:
			self.conn.commit()
			self.cur.close()
			self.conn.close()
	"""
	# del
	def __del__( self ):
		print( '=> __del__' )
		self.log.CloseLog
	"""
		










