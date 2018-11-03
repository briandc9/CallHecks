import random


class Calendar:
    def _init_(self, location):
        self.events = {}
        self.location = location

    def add_event(self, event):
        self.events[(event.name, event.date)] = event

    def delete_event(self, event):
        self.events.pop((event.name, event.date))
        
        


class Event:
    def _init_(self, name, genre, date, description, price, timeslot):
        self.name = name
        self.genre = genre
        self.date = date
        self.description = description
        self.price = price
        self.timeslot = timeslot
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

    def finalize_artist(self):
        inverse = [self.approved_artists.getKey() for max(self.approved_artists.items()) in self.approved_artists.items()]
        return inverse[random.randInt(0, inverse.length)]

    def __eq__(self, other):
        if type(other) is not Event:
            return False
        return self.name == other.name and self.date == other.date
    
    def isOverlap(self, event):
        matchday = datetime.event.date.today()
        for key in self.events:
            priordate = datetime.self.events[key].date.today()
            if (priordate.equals(matchday)):
                mminutes = matchday*60 + matchday.minute
                pminutes = priordate.hour*60 + priordate.minute
                if (pminutes < mminutes and (pminutes + timeslot > mminutes)):
                    return False
                if (mminutes < pminutes and (mminutes + timeslot > pminutes)):
                    return False
        return True
                    
                    
                    
                    
                    
                    
                    
                    
                    
            