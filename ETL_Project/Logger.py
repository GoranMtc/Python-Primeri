import os
from datetime import datetime

class Logger:
	
	_logfile = None
	_printLog : int= 1
	
	# singleton
	def __new__(cls, *args, **kwargs):
		if not hasattr(cls, 'instance'):
			cls.instance = super( Logger, cls).__new__(cls)
		return cls.instance
	
	# init
	def __init__( self ):
		print( '=> Logger init 2' )
		today = datetime.today()
		formatted_date = today.strftime("%Y%m%d_%H%M%S") # Format the date as YYYY MM DD
		self._logfile = open( 'log_'+formatted_date+'.txt', 'a')
	
	# Log text into file
	def Log( self, text : str ):	
		if self._printLog == 1:
			print( '=> Log='+ text )
		
		self._logfile.write( '\n' + text + '\n' )

	#Close Log file
	def CloseLog():
		if self._printLog == 1:
			print( '=> CloseLog' )
		self._logfile.close()


if __name__ == "__main__":
	
	log = Logger()
	log.Log('123')
	print( 'id=' + str(id(log)) )
	log.CloseLog

	log1 = Logger()
	print( 'id=' + str(id(log1)) )	
	log1.Log('456')
	log1.CloseLog	


