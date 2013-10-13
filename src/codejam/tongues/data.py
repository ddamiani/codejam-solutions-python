'''
Module containing the translation data
'''


NORMAL_LETTERS = '''
our language is impossible to understand
there are twenty six factorial possibilities
so it is okay if you want to just give up
zq
'''


MUTATED_LETTERS = '''
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
qz
'''


class Translator(object):
    '''
    Class for performing translations
    '''

    def __init__(self):
        self.normal_dict = None
        self.mutated_dict = None

    def _load(self):
        '''
        Loads an initializes the dictionaries
        '''

        self.normal_dict = {}
        self.mutated_dict = {}

        for norm, mut in zip(NORMAL_LETTERS, MUTATED_LETTERS):
            self.normal_dict[norm] = mut
            self.mutated_dict[mut] = norm

    @classmethod
    def _get(cls, translator, value):
        '''
        Function for performing the letter translation
        '''
        return "".join([translator.get(c) for c in value])

    def get_mutated(self, value):
        '''
        Returns the mutated letter corresponding to the given normal letter
        '''
        if self.normal_dict is None:
            self._load()
        return self._get(self.normal_dict, value)

    def get_normal(self, value):
        '''
        Returns the normal letter corresopnding to the given mutated letter
        '''
        if self.mutated_dict is None:
            self._load()
        return self._get(self.mutated_dict, value)
