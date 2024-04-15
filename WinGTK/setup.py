# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(name='WinGTK',
      version='1.0.0',
      description='DLL package for GTK Windows',
      url='https://www.dschoni.de',
      author='Dschoni',
      author_email='scripting@dschoni.de',
      license='MIT',
      packages=find_packages(),
      package_data={'':['bin/*.dll','lib/**','share/**']}, # This is the most important line.
      zip_safe=False)