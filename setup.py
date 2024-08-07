from setuptools import setup, find_packages
from cardgames.__init__ import __version__

setup(
    name='cardgames',
    version=__version__,
    author='patrickwright8',
    description='A Python package to explore ML and game theory in card games.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/patrickwright8/pokerbot',
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
