'''
codejam - Package for all modules related to codejam solutions
'''

try:
    __version__ = \
        __import__('pkg_resources').get_distribution(__name__).version
except ImportError:
    __version__ = 'unknown'
