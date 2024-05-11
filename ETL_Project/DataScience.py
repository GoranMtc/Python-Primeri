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
		
		#obradi kolone kojima fale podaci
		#dopuni kolone kojima fale podace
		#interpolacija podataka
		#da se zapise koji su slogovi uklonjeni
		#da se kreira index kolona
		#da se prikazu grafici
		#da se upise u neku tabelu koji su fajlovi bili procesuirani, koliko je to trajalo
		#da se u postgresu uradi procedura koja prenosi inkrementalno podatke u drugu semu
		#da se u proceduri uloguju potencijalne greske
		#da se uradi rekurzivni upit ... za nesto
		#da se kroz fajl proslede imena user-a i privilegija za user-e i dinamicki izvrti
		#da se uradi automatsko razmotavanje baze
		#da se u toku obrade prikazuje vrteci znak [ / -- | \ -- ...]
        	#da posalje mail kada se obrada zavrsi
		
		
	#	
		
	
