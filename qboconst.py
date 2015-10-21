#####################################################################
#																	#
#	File: qboconst.py												#
#	Developer: Justin Leto											#
#																	#
#	qboconst.py holds const values for QBO file format				#
#																	#
#	Usage: Called from qbo.py										#
#																	#
#####################################################################

from datetime import date, time

INTUBID = "62160" # Bank list https://ofx-prod-filist.intuit.com/qb2600/data/fidir.txt
BANK_ID = "999999999" # Bank routing number
ACCOUNT_ID = "999999999999" # Account number
ACCOUNT_TYPE = "CHECKING" # CHECKING of SAVINGS

DATE_TODAY = "" + date.today().strftime('%Y%m%d%H%M%S') + ".000[-5]"

HEADER = ("OFXHEADER:100\n"
		"DATA:OFXSGML\n"
		"VERSION:102\n"
		"SECURITY:NONE\n"
		"ENCODING:USASCII\n"
		"CHARSET:1252\n"
		"COMPRESSION:NONE\n"
		"OLDFILEUID:NONE\n"
		"NEWFILEUID:NONE\n\n"		  
		"<OFX>\n"
		"	<SIGNONMSGSRSV1>\n"
		"		<SONRS>\n"
		"			<STATUS>\n"
		"				<CODE>0\n"
		"				<SEVERITY>INFO\n"
		"				<MESSAGE>OK\n"
		"			</STATUS>\n"
		"			<DTSERVER>" + DATE_TODAY + "\n"
		"			<LANGUAGE>ENG\n"
		"			<INTU.BID>" + INTUBID + "\n"
		"		</SONRS>\n"
		"	</SIGNONMSGSRSV1>\n"
		"	<BANKMSGSRSV1>\n"
		"		<STMTTRNRS>\n"
		"			<TRNUID>" + DATE_TODAY + "\n"
		"			<STATUS>\n"
		"				<CODE>0\n"
		"				<SEVERITY>INFO\n"
		"				<MESSAGE>OK\n"
		"			</STATUS>\n"
		"			<STMTRS>\n"
		"				<CURDEF>USD\n"
		"				<BANKACCTFROM>\n"
		"					<BANKID>" + BANK_ID + "\n"
		"					<ACCTID>" + ACCOUNT_ID + "\n"
		"					<ACCTTYPE>" + ACCOUNT_TYPE + "\n"
		"				</BANKACCTFROM>")

BANKTRANLIST_START = "				<BANKTRANLIST>"
DATE_START = "					<DTSTART>" +  DATE_TODAY + ""
DATE_END = "					<DTEND>" +  DATE_TODAY + ""
TRANSACTION_START = "					<STMTTRN>"
BANKTRANLIST_END = "				</BANKTRANLIST>"

TRANSACTION_END = "					</STMTTRN>"

FOOTER = ("				<LEDGERBAL>\n"
		"					<BALAMT>0.00\n"
		"					<DTASOF>" + DATE_TODAY + "\n"
		"				</LEDGERBAL>\n"
		"				<AVAILBAL>\n"
		"					<BALAMT>0.00\n"
		"					<DTASOF>" +  DATE_TODAY + "\n"
		"				</AVAILBAL>\n"
		"			</STMTRS>\n"
		"		</STMTTRNRS>\n"
		"	</BANKMSGSRSV1>\n"
		"</OFX>\n")



