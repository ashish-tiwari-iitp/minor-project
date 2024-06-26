from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='nsga2',
    version='1.0',
    description='Multiobjective NSGA 2',
    long_description='Multiobjective NSGA 2',
    url='',
    author='--',
    author_email='ashish.tiwari.education@gmail.com',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    keywords='nsga2 multi-objective',
    license='MIT',
    install_requires=['tqdm'],
)
