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
"""Test Venue object implemented in venues.py."""
import unittest

from project import venues


class TestVenue(unittest.TestCase):

    def testConstructor_correctName(self):
        club = venues.Venue("Berkeley City Club", "2315 Durant Avenue", 250)
        self.assertTrue("Berkeley City Club", club.name)

    def testConstructor_correctAddress(self):
        club = venues.Venue("Berkeley City Club", "2315 Durant Avenue", 250)
        self.assertTrue("2315 Durant Avenue", club.address)

    def testConstructor_correctSize(self):
        club = venues.Venue("Berkeley City Club", "2315 Durant Avenue", 250)
        self.assertTrue(250, club.size)
