from setuptools import setup, find_packages

setup(
    name='pokerbot',
    version='0.1.0',
    author='patrickwright8',
    description='A Python package to explore ML and game theory in Poker.',
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
