'''
Implementation of the Tongues Problem
'''
from codejam.codejambase import CodeJamBase
from codejam.tongues.data import Translator


class Tongues(CodeJamBase):
    '''
    The main class of the solution of the Tongues Code Jam problem
    '''

    def __init__(self, input_file, output_file, test_mode=False):
        super(Tongues, self).__init__(input_file, output_file, test_mode)
        if self.test_mode:
            self.lines = []
        self.trans = Translator()

    def run(self):
        while self.lines_emitted < self.num_cases:
            translated = self.trans.get_normal(self.read_input_line())
            if self.test_mode:
                self.lines.append(translated)
            self.emit_output_line(translated)

        return 0
