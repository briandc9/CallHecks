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
"""Test User object implemented in users.py."""
import unittest
import datetime

from project import users
from project import scheduling


# pylint: disable=invalid-name, missing-docstring
class TestUser(unittest.TestCase):

    def test_constructor(self):
        john = users.User("John DeNero", 94704)
        self.assertEqual(john.name, "John DeNero")
        self.assertEqual(john.zip_code, 94704)

    def test_vote_increments_num_votes(self):
        john = users.User("John DeNero", 94704)
        anant = users.Performer("Anant Sahai", 94704, "I reenact anime.")
        rager = scheduling.Event("Nathan Trinkl's Birthday Bash",
                                 datetime.datetime(18, 3, 16, 9, 55))
        anant.apply_to(rager)
        rager.approve(anant)
        self.assertEqual(rager.num_votes(anant), 0)
        john.vote_for(anant, rager)
        self.assertEqual(rager.num_votes(anant), 1)

    def test_vote_works_correctly_when_vote_changes(self):
        john = users.User("John DeNero", 94704)
        anant = users.Performer("Anant Sahai", 94704, "I reenact anime.")
        rager = scheduling.Event("Nathan Trinkl's Birthday Bash",
                                 datetime.datetime(18, 3, 16, 9, 55))
        anant.apply_to(rager)
        rager.approve(anant)
        john.vote_for(anant, rager)
        self.assertEqual(rager.num_votes(anant), 1)
        paul = users.Performer("Paul Hilfinger", 94704, "I sing opera.")
        paul.apply_to(rager)
        rager.approve(paul)
        john.vote_for(paul, rager)
        self.assertEqual(rager.num_votes(anant), 0)
        self.assertEqual(rager.num_votes(paul), 1)

    def test_vote_works_with_multiple_events(self):
        john = users.User("John DeNero", 94704)
        anant = users.Performer("Anant Sahai", 94704, "I reenact anime.")
        paul = users.Performer("Paul Hilfinger", 94704, "I sing opera.")
        rager = scheduling.Event("Nathan Trinkl's Birthday Bash",
                                 datetime.datetime(18, 3, 16, 9, 55))
        concert = scheduling.Event("Yanni Live at the Taj Mahal",
                                   datetime.datetime(14, 7, 24, 6, 30))
        anant.apply_to(rager)
        paul.apply_to(concert)
        rager.approve(anant)
        concert.approve(paul)
        john.vote_for(anant, rager)
        john.vote_for(paul, concert)
        self.assertEqual(rager.num_votes(anant), 1)
        self.assertEqual(concert.num_votes(paul), 1)

    def test_str(self):
        john = users.User("John DeNero", 94704)
        self.assertEqual(str(john), "John DeNero")

    def test_eq(self):
        john1 = users.User("John DeNero", 94704)
        john2 = users.User("John DeNero", 94704)
        self.assertEqual(john1, john2)
        anant = users.Performer("Anant Sahai", 94704, "I reenact anime.")
        self.assertNotEqual(john1, anant)

    def test_repr(self):
        john = users.User("John DeNero", 94704)
        self.assertEqual(repr(john), "User('John DeNero', 94704)")
