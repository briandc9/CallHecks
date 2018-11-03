class Calendar():
	def _init_(self, events, location):
		self.events = events
		self.location = location
        
class Event(object):
    def _init_(self, name, genre, date, time, description, price, all_artists = {}, unapproved_artists={}, approved_artists={}):
        self.name = name
        self.genre = genre
        self.date = date
        self.time = time
        self.all_artists = all_artists
        self.approved_artists = approved_artists
    def addUnapproved(artist):
        if (artist.name in self.all_artists):
            print (artist.name + 'has already applied to this venue.')
            return
        else:
            
    def vote(artist):
        pass
    
    def approve(artist):
        pass
        
        
        