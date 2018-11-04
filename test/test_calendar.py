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
"""Test Calendar object implemented in scheduling.py."""
import unittest
import datetime

from project import scheduling


# pylint: disable=invalid-name, missing-docstring
class TestCalendar(unittest.TestCase):

    def test_constructor(self):
        calendar = scheduling.Calendar({94701, 94702, 94703, 94704})
        self.assertTrue(calendar.zip_codes, {94701, 94702, 94703, 94704})

    def test_add(self):
        calendar = scheduling.Calendar({94701, 94702, 94703, 94704})
        rager = scheduling.Event("Nathan Trinkl's Birthday Bash",
                                 datetime.datetime(18, 3, 16, 9, 55))
        self.assertEqual(calendar.size, 0)
        calendar.add(rager)
        self.assertEqual(calendar.size, 1)

    def test_add_overlapping_events(self):
        calendar = scheduling.Calendar({94701, 94702, 94703, 94704})
        rager = scheduling.Event("Nathan Trinkl's Birthday Bash",
                                 datetime.datetime(18, 3, 16, 9, 55))
        rave = scheduling.Event(
            "EDM Banger Rave", rager.start_time + datetime.timedelta(minutes=5))
        calendar.add(rager)
        with self.assertRaises(ValueError):
            calendar.add(rave)

    def test_remove(self):
        calendar = scheduling.Calendar({94701, 94702, 94703, 94704})
        rager = scheduling.Event("Nathan Trinkl's Birthday Bash",
                                 datetime.datetime(18, 3, 16, 9, 55))
        self.assertEqual(calendar.size, 0)
        calendar.add(rager)
        self.assertEqual(calendar.size, 1)
        calendar.remove(rager)
        self.assertEqual(calendar.size, 0)

    def test_size(self):
        calendar = scheduling.Calendar({94701, 94702, 94703, 94704})
        rager = scheduling.Event("Nathan Trinkl's Birthday Bash",
                                 datetime.datetime(18, 3, 16, 9, 55))
        self.assertEqual(calendar.size, 0)
        calendar.add(rager)
