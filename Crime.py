class Crime:

	crimeName = ""
	crimeDate = ""
	crimeType = ""
	crimeLocation = ""

	def __init__(self, crimeName, crimeDate, crimeType, crimeLocation):
		self.crimeName = crimeName
		self.crimeDate = crimeDate
		self.crimeType = crimeType
		self.crimeLocation = crimeLocation

	#SETTERS
	def setCrimeName(self, crimeName):
		self.crimeName = crimeName

	def setCrimeDate(self, crimeDate):
		self.crimeDate = crimeDate

	def setCrimeType(self, crimeType):
		self.crimeType = crimeType

	def setCrimeLocation(self, crimeLocation):
		self.crimeLocation = crimeLocation

	#GETTERS
	def getCrimeName(self):
		return self.crimeName

	def getCrimeDate(self):
		return self.crimeName

	def getCrimeType(self):
		return self.crimeType

	def getCrimeLocation(self):
		return self.crimeLocation