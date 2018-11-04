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
"""Define Consumer and Performer objects."""


class Consumer:
    """A consumer who can vote on performers."""

    def __init__(self, name, zip_code):
        """Create a new consumer.

        Arguments:
            name: A string representing the full name of the consumer.
            zip_code: A five digit number.
        """
        self.name = name
        self.zip_code = zip_code
        self.vote_history = {}

    def vote_for(self, performer, event):
        """Vote for a performer for a particular event.

        Arguments:
            performer: A Performer object.
            event: An Performance object.
        """
        if event in self.vote_history:
            most_recent_vote = self.vote_history[event]
            event.downvote(most_recent_vote)
        event.upvote(performer)
        self.vote_history[event] = performer

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if not isinstance(other, Consumer):
            return False
        if self is other:
            return True
        return self.name == other.name and self.zip_code == other.zip_code

    def __repr__(self):
        return "Consumer('{0}', {1})".format(self.name, self.zip_code)

    def __hash__(self):
        return hash((self.name, self.zip_code))


class Performer(Consumer):
    "A consumer who can apply to perform at an event."

    def __init__(self, name, zip_code, biography):
        """Create a new performer.

        Arguments:
            name: A string representing the full name of the consumer.
            zip_code: A five digit number.
            biography: A string of any length.
        """
        Consumer.__init__(self, name, zip_code)
        self.biography = biography

    def apply_to(self, event):
        """Apply to perform at an event.

        Arguments:
            event: An Performance object.
        """
        event.register(self)

    def __repr__(self):
        return "Performer('{0}', {1}, '{2}')".format(self.name, self.zip_code,
                                                     self.biography)
