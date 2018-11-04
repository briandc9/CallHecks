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
"""Define Event objects."""
import datetime


class Event:
    """An event of some kind."""

    def __init__(self, name, start_time, duration=180):
        """Create a new event.

        Arguments:
            name: A string representing the name of the event.
            genre: A string representing the genre of the event.
            start_time: A datetime object representing start time.
            duration: A number representing the duration of the event in minutes.
        """
        self.name = name
        self.start_time = start_time
        self.duration = duration

    @property
    def end_time(self):
        """Return the time at which the event ends.

        Returns:
            A datetime object.
        """
        return self.start_time + datetime.timedelta(minutes=self.duration)

    def __eq__(self, other):
        if not isinstance(other, Performance):
            return False
        if self is other:
            return True
        return self.name == other.name and self.start_time == other.start_time

    def __hash__(self):
        return hash(self.start_time)

    def overlaps(self, event):
        """Return true if this event overlaps with the given event.

        Arguments:
            event: An Event object.
        """
        starts_after_event_starts = self.start_time > event.start_time
        starts_before_event_ends = self.start_time < event.end_time
        ends_after_event_starts = self.end_time > event.start_time
        ends_before_event_ends = self.end_time < event.end_time
        start_overlaps = starts_after_event_starts and starts_before_event_ends
        end_overlaps = ends_after_event_starts and ends_before_event_ends
        return start_overlaps or end_overlaps


class Performance(Event):
    """An event where consumers can vote on the performer."""

    def __init__(self, name, start_time, duration=180, **metadata):
        """Create a new performance event.

        Arguments:
            name: A string representing the name of the event.
            genre: A string representing the genre of the event.
            start_time: A datetime object representing start time.
            duration: A number representing the duration of the event in minutes.
            metadata: A dictionary of supplementary information.
        """
        Event.__init__(self, name, start_time, duration, **metadata)
        self.votes = {}
        self.approved_performers = set()
        self.unapproved_performers = set()
        self.is_accepting_votes = True

    def num_votes(self, performer):
        """Return the number of votes for an performer."""
        return self.votes.get(performer, 0)

    def register(self, performer):
        """Add performer to collection of performers-to-be-aproved.

        Arguments:
            performer: An Performer object.
        """
        self.unapproved_performers.add(performer)

    def upvote(self, performer):
        """Increment the number of votes for an performer.

        Arguments:
            performer: An Performer object.

        Raises:
            ValueError: If performer has not been aproved yet.
        """
        if not self.is_accepting_votes:
            raise ValueError("Event is no longer accepting votes.")
        if performer not in self.approved_performers:
            raise ValueError("Performer has not been aproved yet.")
        self.votes[performer] += 1

    def downvote(self, performer):
        """Decrement the number of votes for an performer.

        Arguments:
            performer: An Performer object.

        Raises:
            ValueError: If the performer has never been voted for.
        """
        if not self.is_accepting_votes:
            raise ValueError("Event is no longer accepting votes.")
        if self.num_votes(performer) == 0:
            raise ValueError("Performer already has zero votes.")
        self.votes[performer] -= 1

    def approve(self, performer):
        """Move performer to set of approved performers.

        approve initializes the number of votes for the performer to zero.

        Arguments:
            performer: An Performer object.

        Raises:
            ValueError: If the performer did not register for this event.
            ValueError: If the performer has already been approved.
        """
        if performer not in self.unapproved_performers:
            raise ValueError("Performer has not registered for this event.")
        if performer in self.approved_performers:
            raise ValueError("Performer has already been approved.")
        self.unapproved_performers.remove(performer)
        self.approved_performers.add(performer)
        self.votes[performer] = 0

    def close_voting(self):
        """Prevent event from accepting more votes."""
        self.is_accepting_votes = False

    @property
    def performer(self):
        """Return the performer with the most votes.

        Returns:
            An Performer instance.
        """
        return max(self.votes, key=lambda performer: self.votes[performer])
