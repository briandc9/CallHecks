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
"""Test Performance object implemented in py."""
import unittest
import datetime

from project.consumers import Performer
from project.events import Performance


# pylint: disable=invalid-name, missing-docstring
class TestPerformance(unittest.TestCase):

    def test_constructor(self):
        rager = Performance("Nathan Trinkl's Birthday Bash",
                            datetime.datetime(18, 3, 16, 9, 55))
        self.assertEqual(rager.name, "Nathan Trinkl's Birthday Bash")
        self.assertEqual(rager.start_time, datetime.datetime(18, 3, 16, 9, 55))
        self.assertEqual(rager.duration, 180)

    def test_register(self):
        rager = Performance("Nathan Trinkl's Birthday Bash",
                            datetime.datetime(18, 3, 16, 9, 55))
        anant = Performer("Anant Sahai", 94704, "I reenact animes.")
        self.assertTrue(anant not in rager.unapproved_performers)
        rager.register(anant)
        self.assertTrue(anant in rager.unapproved_performers)

    def test_vote_increments_num_votes(self):
        rager = Performance("Nathan Trinkl's Birthday Bash",
                            datetime.datetime(18, 3, 16, 9, 55))
        anant = Performer("Anant Sahai", 94704, "I reenact animes.")
        anant.apply_to(rager)
        rager.approve(anant)
        self.assertEqual(rager.num_votes(anant), 0)
        rager.upvote(anant)
        self.assertEqual(rager.num_votes(anant), 1)

    def test_vote_unapproved_performer_raises_exception(self):
        rager = Performance("Nathan Trinkl's Birthday Bash",
                            datetime.datetime(18, 3, 16, 9, 55))
        anant = Performer("Anant Sahai", 94704, "I reenact animes.")
        anant.apply_to(rager)
        with self.assertRaises(ValueError):
            rager.upvote(anant)

    def test_downvote_decrements_num_votes(self):
        rager = Performance("Nathan Trinkl's Birthday Bash",
                            datetime.datetime(18, 3, 16, 9, 55))
        anant = Performer("Anant Sahai", 94704, "I reenact animes.")
        anant.apply_to(rager)
        rager.approve(anant)
        self.assertEqual(rager.num_votes(anant), 0)
        rager.upvote(anant)
        self.assertEqual(rager.num_votes(anant), 1)
        rager.downvote(anant)
        self.assertEqual(rager.num_votes(anant), 0)

    def test_downvote_below_zero_raises_exception(self):
        rager = Performance("Nathan Trinkl's Birthday Bash",
                            datetime.datetime(18, 3, 16, 9, 55))
        anant = Performer("Anant Sahai", 94704, "I reenact animes.")
        rager.register(anant)
        with self.assertRaises(ValueError):
            rager.downvote(anant)

    def test_approve_moves_performer(self):
        rager = Performance("Nathan Trinkl's Birthday Bash",
                            datetime.datetime(18, 3, 16, 9, 55))
        anant = Performer("Anant Sahai", 94704, "I reenact animes.")
        self.assertEqual(len(rager.unapproved_performers), 0)
        anant.apply_to(rager)
        self.assertEqual(len(rager.unapproved_performers), 1)
        self.assertEqual(len(rager.approved_performers), 0)
        rager.approve(anant)
        self.assertEqual(len(rager.unapproved_performers), 0)
        self.assertEqual(len(rager.approved_performers), 1)

    def test_performer(self):
        rager = Performance("Nathan Trinkl's Birthday Bash",
                            datetime.datetime(18, 3, 16, 9, 55))
        performer1 = Performer("Anant Sahai", 94704, "I reenact animes.")
        performer2 = Performer("Anant Sabai", 94704, "I reenact fiestas.")
        performer3 = Performer("Anant Sagai", 94704, "I reenact movies.")
        for performer in [performer1, performer2, performer3]:
            performer.apply_to(rager)
            rager.approve(performer)
        rager.upvote(performer2)
        self.assertEqual(rager.performer, performer2)

    def test_end_time(self):
        party = Performance("Balaji's Birthday Siesta",
                            datetime.datetime(18, 5, 14, 6, 15), 30)
        self.assertEqual(party.end_time, datetime.datetime(18, 5, 14, 6, 45))

    def test_eq(self):
        rager1 = Performance("Nathan Trinkl's Birthday Bash",
                             datetime.datetime(18, 3, 16, 9, 55))
        rager2 = Performance("Nathan Trinkl's Birthday Bash",
                             datetime.datetime(18, 3, 16, 9, 55))
        self.assertEqual(rager1, rager2)

    def test_num_votes(self):
        rager = Performance("Nathan Trinkl's Birthday Bash",
                            datetime.datetime(18, 3, 16, 9, 55))
        anant = Performer("Anant Sahai", 94704, "I reenact animes.")
        anant.apply_to(rager)
        rager.approve(anant)
        rager.upvote(anant)
        self.assertEqual(rager.num_votes(anant), 1)

    def test_overlaps(self):
        rager = Performance("Nathan Trinkl's Birthday Bash",
                            datetime.datetime(18, 3, 16, 9, 55))
        rave = Performance("EDM Banger Rave",
                           rager.start_time + datetime.timedelta(minutes=5))
        self.assertTrue(rager.overlaps(rave))

    def test_close_voting(self):
        rager = Performance("Nathan Trinkl's Birthday Bash",
                            datetime.datetime(18, 3, 16, 9, 55))
        self.assertTrue(rager.is_accepting_votes)
        rager.close_voting()
        self.assertFalse(rager.is_accepting_votes)
