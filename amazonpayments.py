#concrete provider class for handling amazon payments csv

from abstractprovider import AbstractProvider

class amazonpayments(AbstractProvider):

	__providerID = ''
	__providerName = ''

	def __init__(self):
			self.__providerID = 'amazon'
			self.__providerName = 'Amazon Payments'

	@staticmethod
	def getDatePosted(self, row):
		return row.get('Date')

	@staticmethod
	def getTxnType(self,row):
		return row.get('Type')

	@staticmethod
	def getToFrom(self,row):
		return row.get('To/From')

	@staticmethod
	def getTxnName(self,row):
		return row.get('Name')

	@staticmethod
	def getStatus(self,row):
		return row.get('Status')

	@staticmethod
	def getTxnAmount(self,row):
		return row.get('Amount')

	@staticmethod
	def getFeeAmount(self,row):
		return row.get('Fees')

	@staticmethod
	def getTransactionID(self,row):
		return row.get('Transaction ID')

	@staticmethod
	def getReference(self,row):
		return row.get('Reference')

	def getID(self):
		return self.__providerID

	def getName(self):		
		return self.__providerName

