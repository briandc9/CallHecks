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
"""Test Artist object implemented in users.py."""
import unittest

from project import users


# pylint: disable=invalid-name, missing-docstring
class TestArtist(unittest.TestCase):

    def testConstructor_correctName(self):
        anant = users.Artist("Anant Sahai", 94704, "I like anime.")
        self.assertTrue(anant.name, "Anant Sahai")

    def testConstructor_correctZipCode(self):
        anant = users.Artist("Anant Sahai", 94704, "I like anime.")
        self.assertTrue(anant.zip_code, 94704)

    def testConstructor_correctBiography(self):
        anant = users.Artist("Anant Sahai", 94704, "I like anime.")
        self.assertTrue(anant.biography, "I like anime.")
