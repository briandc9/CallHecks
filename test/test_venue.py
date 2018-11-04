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
"""Test Venue object implemented in py."""
import unittest
import datetime

from project.venues import Venue
from project.consumers import Performer
from project.events import Performance


# pylint: disable=invalid-name, missing-docstring
class TestVenue(unittest.TestCase):

    def test_constructor(self):
        club = Venue("Berkeley City Club", "2315 Durant Avenue")
        self.assertTrue(club.name, "Berkeley City Club")
        self.assertTrue(club.address, "2315 Durant Avenue")

    def test_host(self):
        club = Venue("Berkeley City Club", "2315 Durant Avenue")
        rager = Performance("Nathan Trinkl's Birthday Bash",
                            datetime.datetime(18, 3, 16, 9, 55))
        self.assertTrue(rager not in club.events)
        club.host(rager)
        self.assertTrue(rager in club.events)

    def test_host_overlapping_events(self):
        club = Venue("Berkeley City Club", "2315 Durant Avenue")
        rager = Performance("Steven Huangs's Birthday Bash",
                            datetime.datetime(18, 3, 16, 9, 45))
        rave = Performance("Japanese Pop Rave",
                           rager.start_time + datetime.timedelta(minutes=10))
        club.host(rager)
        with self.assertRaises(ValueError):
            club.host(rave)

    def test_approve(self):
        club = Venue("Berkeley City Club", "2315 Durant Avenue")
        anant = Performer("Anant Sahai", 94704, "I reenact animes.")
        rager = Performance("Nathan Trinkl's Birthday Bash",
                            datetime.datetime(18, 3, 16, 9, 55))
        club.host(rager)
        anant.apply_to(rager)
        self.assertTrue(anant not in rager.approved_performers)
        club.approve(anant, rager)
        self.assertTrue(anant in rager.approved_performers)

    def test_approve_for_not_hosted_event(self):
        club = Venue("Berkeley City Club", "2315 Durant Avenue")
        anant = Performer("Anant Sahai", 94704, "I reenact animes.")
        rager = Performance("Nathan Trinkl's Birthday Bash",
                            datetime.datetime(18, 3, 16, 9, 55))
        anant.apply_to(rager)
        with self.assertRaises(ValueError):
            club.approve(anant, rager)

    def test_str(self):
        club = Venue("Berkeley City Club", "2315 Durant Avenue")
        self.assertEqual(str(club), "Berkeley City Club")

    def test_repr(self):
        club = Venue("Berkeley City Club", "2315 Durant Avenue")
        self.assertEqual(
            repr(club), "Venue('Berkeley City Club', '2315 Durant Avenue')")

    def test_eq(self):
        club1 = Venue("Berkeley City Club", "2315 Durant Avenue")
        club2 = Venue("Berkeley City Club", "2315 Durant Avenue")
        self.assertEqual(club1, club2)
        hall = Venue("Carnegie Hall", "6124 Jefferson Street")
        self.assertNotEqual(club1, hall)
