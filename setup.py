from setuptools import setup, find_packages

setup(
    name = "codejam",
    version = "0.0.1",
    author = "Daniel Damiani",
    author_email = "dsdamiani@gmail.com",
    description = ("Python versions of Google Codejam problems."),
    license = "BSD",
    keywords = "codejam google",
    url = "None",
    package_dir={'': 'src'},
    packages=find_packages('src'),
    entry_points={
        'console_scripts': [
            'codejam-runner = codejam.main:main',
        ],
    }
)
