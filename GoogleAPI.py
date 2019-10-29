#!/usr/bin/python

# Script to automate downloading CSV files from GoogleDocs into the lens asset folders
# Note that google broke password authentication in April 2015, so the interface changed slightly
# to use the oauth-supporting library gspread.
#
# Expects a Google oauth key file named google_oauth_key.json, created and downloaded
# from  http://console.developers.google.com
#
# Usage example:
#   #!/usr/bin/python
#   import GoogleDocToCSV
#
#   GoogleDocToCSV.download("Spreadsheet Name", "Worksheet Title", "../Destination/Path/sheet.csv");
#

import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GSheets:
	"""
	A CSV writer which will write rows to CSV file "f",
	which is encoded in the given encoding.
	"""
	def __init__(self, keyfile):
		# Redirect output to a queue
		self.authorize(keyfile)

	def authorize(self, keyfile):
		self.keyfile = keyfile
		scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
		credentials = ServiceAccountCredentials.from_json_keyfile_name(self.keyfile, scope)
		self.google = gspread.authorize(credentials)
		print "Google APIs Authorized"

	# Just get the file-like object
	def download(self, spreadsheet_title, worksheet_title):
		print "Downloading: " + spreadsheet_title + " > " + str(worksheet_title)
		return self.google.open(spreadsheet_title).worksheet(worksheet_title)
