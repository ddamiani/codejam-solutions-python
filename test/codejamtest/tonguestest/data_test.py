"""
Unittests for the data module
"""

import unittest
import codejam.tongues.data


class TestTranslator(unittest.TestCase):

    def setUp(self):
        self.trans = codejam.tongues.data.Translator()

    def test_get_normal(self):
        translated = self.trans.get_normal(codejam.tongues.data.MUTATED_LETTERS)
        self.assertEquals(translated, codejam.tongues.data.NORMAL_LETTERS)

    def test_get_mutated(self):
        translated = self.trans.get_mutated(codejam.tongues.data.NORMAL_LETTERS)
        self.assertEquals(translated, codejam.tongues.data.MUTATED_LETTERS)

