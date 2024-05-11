import psycopg2
from Config import load_config

class db_connection:
	
	def connect( self, config ):
		#Connect to the PostgreSQL database server
		try:
			self.conn= psycopg2.connect( **config )

		except (psycopg2.DatabaseError, Exception) as error:
			print(error)
		else:
			print('Connected to the PostgreSQL server.')
						
	def create_connection( self ):
		try:
			config = load_config()
			self.connect( config )

		except Exception as e:
			print( e )

	def get_connection( self ):
		return self.conn

if __name__ == '__main__':
	dbc = db_connection()
	dbc.create_connection()

