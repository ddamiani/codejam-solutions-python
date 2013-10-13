"""
The base input/output handling class for codejam problems
"""


class CodeJamBase(object):
    """
    The base class for all codejam solutions
    """

    def __init__(self, input_file, output_file, test_mode=False, line_case=1):
        self.input_file = input_file
        self.output_file = output_file
        self.test_mode = test_mode
        self.line_case = line_case
        self.num_cases = 0
        self.lines_consumed = 0
        self.lines_emitted = 0

    def solve(self):
        """
        The function to call to kick off the solving of the problem
        """
        try:
            self.num_cases = int(self.input_file.readline())
        except ValueError:
            print 'The input file is malformed: No number of cases specified'
            return 3
        return self.run()

    def run(self):
        """
        Runs the actual implementation of the problem solving. This is meant to
        be overridden in the inheriting class
        """
        self.output_file.write("Number of cases: %d\n" % self.num_cases)
        self.output_file.write("No problem implemented\n")
        return 1

    def read_input_line(self):
        """
        Reads of a line of input from the test input source.

        It prints an error if more input lines have been read than expected
        based on the config
        """
        if self.line_case > 0 and self.lines_consumed > self.num_cases * \
           self.line_case:
            print 'All intended input lines (%d) have already been consumed!' \
                  % self.num_cases * self.line_case

        current_line = self.input_file.readline()
        if current_line:
            self.lines_consumed += 1
            return current_line.rstrip()

    def emit_output_line(self, output_line):
        """
        Emits a single line of output in the appropriate format.
        """
        self.output_file.write('Case #%d: %s\n' %
                               (self.lines_emitted + 1, output_line))
        self.lines_emitted += 1
