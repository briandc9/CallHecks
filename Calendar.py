class Calendar():
	def _init_(self, events, location):
		self.events = events
		self.location = location
        
class Event(object):
    def _init_(self, name, genre, date, time, description, price, unapproved_artists={}, approved_artists={}, rejected_artists={}):
        self.name = name
        self.genre = genre
        self.date = date
        self.time = time
        self.unapproved_artists = unapproved_artists
        self.approved_artists = approved_artists
        self.rejected_artists = rejected_artists
    def addUnapproved(