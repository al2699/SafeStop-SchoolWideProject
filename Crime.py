class Crime:

	crimeName = ""
	crimeDate = ""
	crimeType = ""

	def __init__(self, crimeName, crimeDate, crimeType):
		self.crimeName = crimeName
		self.crimeDate = crimeDate
		self.crimeType = crimeType

	#SETTERS
	def setCrimeName(self, crimeName):
		self.crimeName = crimeName

	def setCrimeDate(self, crimeDate):
		self.crimeDate = crimeDate

	def setCrimeType(self, crimeType):
		self.crimeType = crimeType

	#GETTERS
	def getCrimeName(self):
		return self.crimeName

	def getCrimeDate(self):
		return self.crimeName

	def getCrimeType(self):
		return self.crimeType