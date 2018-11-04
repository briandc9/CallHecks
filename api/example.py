from datetime import datetime

from project.users import User, Performer
from project.venues import Venue
from project.scheduling import Calendar, Performance


balaji = User("Balaji Veeramani", 53562)
brian = Performer("Brian Chin", 94704)
bryson = Performer("Bryson Bauer", 53562)

# The venue Greek Theater decides to host an event
greek_theater = Venue("Greek Theater", "2001 Gayley Rd, Berkeley, CA 94720")
# This event is on 11/3/2018 at 7:30pm
concert = Performance("Big Rager at the Greek Theater",
                       datetime(2018, 11, 3, 19, 30))
greek_theater.host(concert)

brian.apply_to(concert)
# Brian has applied to the event, but hasn't been aproved yet
greek_theater.approve(brian)
# The venue approves Brian for the event

bryson.apply_to(concert)
greek_theater.approve(bryson)
# Now there are two performers, each with zero votes

balaji.vote_for(brian)
# Brian now has more votes than Bryson

concert.close_voting()
# Now that voting's done, get the final performer
concert.performer
