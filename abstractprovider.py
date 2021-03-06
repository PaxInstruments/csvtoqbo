#provider.py
#Hides provider-specific details for the main csvtoqbo method.

class AbstractProvider:
    #Abstract base class to be inherited by all concrete provider classes.
	__providerID = ''
	__providerName = ''

	@staticmethod
	def getDatePosted(self, row):
		raise NotImplementedError( "Method getDatePosted not implemented." )

	@staticmethod
	def getTxnType(self,row):
		raise NotImplementedError( "Method getTxnType not implemented." )

	@staticmethod
	def getToFrom(self,row):
		raise NotImplementedError( "Method getToFrom not implemented." )

	@staticmethod
	def getTxnName(self,row):
		raise NotImplementedError( "Method getTxnName not implemented." )

	@staticmethod
	def getStatus(self,row):
		raise NotImplementedError( "Method getStatus not implemented." )

	@staticmethod
	def getTxnAmount(self,row):
		raise NotImplementedError( "Method getTxnAmount not implemented." )

	@staticmethod
	def getFeeAmount(self,row):
		raise NotImplementedError( "Method getFeeAmount not implemented." )

	@staticmethod
	def getTransactionID(self,row):
		raise NotImplementedError( "Method getTransactionID not implemented." )

	@staticmethod
	def getReference(self,row):
		raise NotImplementedError( "Method getReference not implemented." )

	def getID( self ):
		raise NotImplementedError( "Method getProviderID not implemented." )

	def getName(self):
		raise NotImplementedError( "Method getName not implemented." )

