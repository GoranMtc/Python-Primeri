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

class file_reader():
	
	# init
	def __init__(self, path_to_file):
		print( '=> file_reader init' )
		self.path_to_file = path_to_file
		print( '=>' + self.path_to_file )
		self.log = Logger()
		self.log.Log( "=> file_reader Init" )

	# procitaj fajl
	def read_csv_file(self):
		#print( '=> read_csv_file' )
		self.log.Log( "=> read_csv_file" )

		self.file_exists = exists( self.path_to_file )

		if ( self.file_exists ):
			self.df = pd.read_csv( self.path_to_file )
			#print( '=> postoji fajl' )
			self.log.Log( "=> postoji fajl" ) 
		else:
			#print( '=> ne postoji fajl' )
			self.log.Log( "=> ne postoji fajl" )
        
        # lista kolona
	def get_file_columns(self):
		self.log.Log( "=> get_file_columns" )
		self.columns = list( self.df.columns.values )

	# kreiraj sql za tabelu
	def create_dml(self):
		self.log.Log( "=> create_dml" )

		self.read_csv_file()
		self.get_file_columns()

		sql = 'Create+table+if+not+exists+food_orders'
		sql = sql + '('

		for column in self.columns:
			column = column.strip()
			sql = sql +',+'+ column +'+char(100)'		

		sql = sql + ')'
		sql = sql.lower()
		sql = sql.replace('/','_').replace(' ','_').replace('+',' ').replace('(,','(')
		self.sql = sql  #print( self.sql )
		
	#kreiraj tabelu
	def create_table(self):
		self.log.Log( '=> create_table' )
		
		dbc = connection.db_connection()
		dbc.create_connection()
		self.conn = dbc.get_connection()
		
		self.cur = self.conn.cursor() 

		try:
			self.cur.execute( self.sql )

		except Exception as e:
			print( e )
		else:
			self.conn.commit()
			self.cur.close()
			self.conn.close()

	def __del__(self):
		print( '=> __del__' )
		self.log.CloseLog
		










