import FileCheck as FileCheck
from Logger import Logger
			
# class for starting process		
class Main:
		
	def __init__( self  ):
		self.log = Logger()
		self.log.Log('Main - Init')
		pass		
		
	def main( self ):
		fc = FileCheck.FileCheck()
		fc.mainLoop()
		pass
	
main = Main()	
main.main()


