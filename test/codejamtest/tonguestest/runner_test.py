'''
Unittests for the Tongues problem runner
'''

import os
import sys
import unittest
from codejam.tongues.runner import Tongues


class TestTongues(unittest.TestCase):

    def setUp(self):
        self.input_file = open(os.path.join(os.path.dirname(__file__),
                                            'resource',
                                            'test_input.txt'),
                               'r')
        self.output_file = sys.stdout
        self.result_filename = os.path.join(os.path.dirname(__file__),
                                            'resource',
                                            'test_result.txt')
        self.problem = Tongues(self.input_file, self.output_file, True)

    def test_problem(self):
        self.assertEquals(self.problem.solve(), 0)
        with open(self.result_filename, 'r') as result_test:
            for entry in self.problem.lines:
                self.assertEquals(entry, result_test.readline().rstrip())
