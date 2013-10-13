"""
Unittests for the codejambase module
"""

import os
import sys
import unittest
from codejam.codejambase import CodeJamBase


class TestCodeJamBase(unittest.TestCase):

    def setUp(self):
        self.input_file = open(os.path.join(os.path.dirname(__file__),
                                            'resource',
                                            'test_input_good.txt'),
                               'r')
        self.input_file_bad = open(os.path.join(os.path.dirname(__file__),
                                                'resource',
                                                'test_input_bad.txt'),
                                   'r')
        self.output_file = sys.stdout
        self.codejam_tester = CodeJamBase(self.input_file, self.output_file)
        self.codejam_tester_bad = CodeJamBase(self.input_file_bad,
                                              self.output_file)

    def test_mode(self):
        self.assertFalse(self.codejam_tester.test_mode)

    def test_solve(self):
        self.assertEquals(self.codejam_tester.solve(), 1)

    def test_bad_input(self):
        self.assertEquals(self.codejam_tester_bad.solve(), 3)

    def test_read_input(self):
        self.assertEquals(self.codejam_tester.num_cases, 0)
        self.codejam_tester.solve()
        self.assertEquals(self.codejam_tester.num_cases, 3)
        self.assertEquals(self.codejam_tester.read_input_line(), 'foo')
        self.assertEquals(self.codejam_tester.read_input_line(), 'bar')
        self.assertEquals(self.codejam_tester.read_input_line(), 'baz')
        self.assertIsNone(self.codejam_tester.read_input_line())
        self.assertIsNone(self.codejam_tester.read_input_line())
