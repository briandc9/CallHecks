class Calendar():
	def _init_(self, events, location):
		self.events = events
		self.location = location
        
class Event(object):
    def _init_(self, name, genre, date, time, description, price):
        self.name = name
        self.genre = genre
        self.date = date
        self.time = time
        self.all_artists = set()
        self.approved_artists = {}
        self.unapproved_artists = set()
        
    def vote(self, artist):
        self.approved_artists[artist.name] += 1
    
    def approve(self, artist):
        self.unapproved_artists.remove(artist)
        self.approved_artists[artist.name] = 0
    
    