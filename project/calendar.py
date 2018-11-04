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
# Author: Brian Chin <bchin821@berkeley.edu>
"""Define Calendar object."""


class Calendar:
    """A collection of events for a particular location."""

    def __init__(self, zip_codes):
        """Initialize a calendar for some location.

        Arguments:
            zip_codes: A collection of five-digit numbers.
        """
        self.events = set()
        self.zip_codes = zip_codes

    def add(self, event):
        """Add an event to the calendar.

        Arguments:
            event: An Event object.
        """
        for other in self.events:
            if event.overlaps(other):
                raise ValueError("Performance times conflict.")
        self.events.add(event)

    def remove(self, event):
        """Remove an event from the calendar.

        Arguments:
            event: An Event object.
        """
        self.events.remove(event)

    @property
    def size(self):
        """Return number of events in the calendar."""
        return len(self.events)
