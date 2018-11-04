# Copyright 2018 Aidan Abdulali, Brian Chin, Balaji Veeramani, Surya Vengadesan
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# Author: Balaji Veeramani <bveeramani@berkeley.edu>
"""Define Venue object."""


class Venue:
    """A place where events happen."""

    def __init__(self, name, address):
        """Construct a new venue.

        Arguments:
            name: A string representing the name of the venue.
            address: A string representing the location of the venue.
        """
        self.name = name
        self.address = address
        self.events = []

    def host(self, event):
        """Add the given event to the venue's list of events.

        Arguments:
            events: An Performance instance
        """
        for other in self.events:
            if event.overlaps(other):
                raise ValueError("Performance times conflict.")
        self.events.append(event)

    def approve(self, performer, event):
        """Approve an performer for consideration to perform at an event.

        Arguments:
            performer: A Performer instance.
            event: An Performance instance.

        Raises:
            ValueError: If venue is not hosting the event.
        """
        if event not in self.events:
            raise ValueError("Venue not hosting event.")
        event.approve(performer)

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Venue('{0}', '{1}')".format(self.name, self.address)

    def __eq__(self, other):
        if not isinstance(other, Venue):
            return False
        if self is other:
            return True
        return self.name == other.name and self.address == other.address
