#####################################################################
#																	#
#	File: csvtoqbo.py												#
#	Developer: Justin Leto											#
#																	#
#	csvtoqbo-test.py is the file for unit testing the				#
#   csvtoqbo.py utility.											#
#																	#
#	Usage: python csvtoqbo.py										#
#																	#
#####################################################################

import os
import unittest
import qbo
import qboconst
import amazonpayments
import cStringIO
from datetime import date

class csvtoqboTest(unittest.TestCase):

	#  Initialize qbo object and ensure constant values pulled in from file
	def testInit(self):
		myQbo = qbo.qbo()
		self.assertEquals(myQbo.getHEADER(), qboconst.HEADER)
		self.assertEquals(myQbo.getFOOTER(), qboconst.FOOTER)
		self.assertEquals(myQbo.getDATE_START(), qboconst.DATE_START)
		self.assertEquals(myQbo.getDATE_END(), qboconst.DATE_END)
		self.assertEquals(myQbo.getBANKTRANLIST_START(), qboconst.BANKTRANLIST_START)
		self.assertEquals(myQbo.getBANKTRANLIST_END(), qboconst.BANKTRANLIST_END)
		self.assertEquals(myQbo.getTRANSACTION_START(), qboconst.TRANSACTION_START)
		self.assertEquals(myQbo.getTRANSACTION_END(), qboconst.TRANSACTION_END)

	#	Add a valid transaction through the qbo.addTransaction() method with fee
	def testAddTransaction(self):
		myQbo = None
		myQbo = qbo.qbo()

		status = 'Completed'
		date_posted = str(date.today().strftime('%m/%d/%Y'))
		memo = 'AddTransactionTest'
		txn_type = 'Payment'
		to_from_flag = 'From'
		txn_amount = '1.00'
		txn_fee = '0.05'
		name = 'TestBuy'
		transaction_id = '12345'
		reference = '67890'

		self.assertEquals(myQbo.addTransaction(status, date_posted, txn_type, to_from_flag, txn_amount, txn_fee, transaction_id, reference, name, myQbo.getCount()), True)
		self.assertEquals(myQbo.getCount(), 2)

	#	Compare size of built document against file size known at development time
	def testBuild(self):
		myQbo = None
		myQbo = qbo.qbo()

		status = 'Completed'
		date_posted = str(date.today().strftime('%m/%d/%Y'))
		memo = 'AddTransactionTest'
		txn_type = 'Payment'
		to_from_flag = 'From'
		txn_amount = '1.00'
		txn_fee = '0.05'
		name = 'TestBuy'
		transaction_id = '12345'
		reference = '67890'

		self.assertEquals(myQbo.addTransaction(status, date_posted, txn_type, to_from_flag, txn_amount, txn_fee, transaction_id, reference, name, myQbo.getCount()), True)
		self.assertEquals(len(myQbo.getDocument()), 1840)

	#	Writing document of known size to file
	def testWrite(self):
		myQbo = None
		myQbo = qbo.qbo()
	
		status = 'Completed'
		date_posted = str(date.today().strftime('%m/%d/%Y'))
		memo = 'AddTransactionTest'
		txn_type = 'Payment'
		to_from_flag = 'From'
		txn_amount = '1.00'
		txn_fee = '0.05'
		name = 'TestBuy'
		transaction_id = '12345'
		reference = '67890'

		self.assertEquals(myQbo.addTransaction(status, date_posted, txn_type, to_from_flag, txn_amount, txn_fee, transaction_id, reference, name, myQbo.getCount()), True)
		self.assertEquals(myQbo.Write('./csvtoqbo-test.qbo'), True)
		statinfo = os.stat('./csvtoqbo-test.qbo')
		self.assertEquals(statinfo.st_size, 2284)

	#	Provider ID is set correctly on intialization
	def testProviderID(self):
		myProvider = amazonpayments.amazonpayments()
		self.assertEquals(myProvider.getID(), 'amazon')
		self.assertEquals(myProvider.getName(), 'Amazon Payments')
		
	#	QBO class get functions for transaction method
	def testProviderGetters(self):
		myProvider = amazonpayments.amazonpayments()
		myDict = {'Status' : 'Completed',
						'Date' : 'May 8, 2013',
						'Type' : 'Payment',
						'To/From' : 'From',
						'Amount' : '1.00',
						'Fees' : '0.05',
						'Transaction ID' : '12345',
						'Reference' : '67890',
						'Name' : 'TestBuy'}
		self.assertEquals(myProvider.getStatus(myProvider,myDict), 'Completed')
		self.assertEquals(myProvider.getDatePosted(myProvider,myDict), 'May 8, 2013')
		self.assertEquals(myProvider.getTxnType(myProvider, myDict), 'Payment')
		self.assertEquals(myProvider.getToFrom(myProvider, myDict), 'From')
		self.assertEquals(myProvider.getTxnAmount(myProvider, myDict), '1.00')
		self.assertEquals(myProvider.getFeeAmount(myProvider, myDict), '0.05')
		self.assertEquals(myProvider.getTransactionID(myProvider, myDict), '12345')
		self.assertEquals(myProvider.getReference(myProvider, myDict), '67890')
		self.assertEquals(myProvider.getTxnName(myProvider, myDict), 'TestBuy')

	#	Test against command line with sample amazon test csv file
	def testCommandLineSampleCSVFile(self):

		name = 'Amazon-CSV-Test'
		csvname = name + '.csv'
		logname = name + '.log'
		try:
			with open(logname): 
				os.remove(logname)
		except IOError:
		   pass

		os.system('python csvtoqbo.py -amazon %s' % csvname)
		assert os.path.exists(logname)
		
		with open(logname) as f:
			content = f.readlines()
			if not "written successfully" in content[len(content)-1]:
				print(content)
				self.assertEquals(True, False)
				
# main method for running unit tests
if __name__ == '__main__':
    unittest.main()
