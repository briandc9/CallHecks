import random
class Calendar:
    def _init_(self, location):
        self.events = {}
        self.location = location
        
    def addEvent(self, event):
        self.events[(event.name, event.date)] = event
        
        
class Event:
    def _init_(self, name, genre, date, description, price):
        self.name = name
        self.genre = genre
        self.date = date
        self.description = description
        self.price = price
        self.all_artists = set()
        self.approved_artists = {}
        self.unapproved_artists = set()
        
    def register(self, artist):
        self.unapproved_artists.add(artist)
        
    def vote(self, artist):
        self.approved_artists[artist.name] += 1
        
    def unvote(self, artist):
        self.approved_artists[artist.name] -= 1
    
    def approve(self, artist):
        self.unapproved_artists.remove(artist)
        self.approved_artists[artist.name] = 0
        
    def finalizeArtist(self):
        maximum = max(self.approved_artists.items())
        inverse = [self.approved_artists.getKey() for maximum in self.approved_artists.items()]
        return inverse[random.randInt(0, inverse.length)]
    
    def 