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
"""Test Performer object implemented in users.py."""
import unittest
import datetime

from project import users
from project import scheduling


# pylint: disable=missing-docstring
class TestPerformer(unittest.TestCase):

    def test_constructor(self):
        anant = users.Performer("Anant Sahai", 94704, "I reenact anime.")
        self.assertEqual(anant.name, "Anant Sahai")
        self.assertEqual(anant.zip_code, 94704)
        self.assertEqual(anant.biography, "I reenact anime.")

    def test_apply_to(self):
        anant = users.Performer("Anant Sahai", 94704, "I reenact anime.")
        rager = scheduling.Event("Nathan Trinkl's Birthday Bash",
                                 datetime.datetime(18, 3, 16, 9, 55))
        self.assertTrue(anant not in rager.unapproved_performers)
        anant.apply_to(rager)
        self.assertTrue(anant in rager.unapproved_performers)

    def test_repr(self):
        anant = users.Performer("Anant Sahai", 94704, "I reenact anime.")
        self.assertEqual(
            repr(anant), "Performer('Anant Sahai', 94704, 'I reenact anime.')")
