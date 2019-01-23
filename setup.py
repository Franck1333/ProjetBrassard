#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#Aides : Using set-me-up.py from https://gist.github.com/ojii/3906682 ,
#Aides : The generator "set-me-up.py" need a "__init__.py" file in the main root directorie to work .

#HOW INSTALL AND USE THIS PROJECT:
#in the console : sudo python setup.py install
#And all the depencies will be installed with the Project

#git clone https://github.com/Franck1333/ProjetBrassard.git

from setuptools import setup, find_packages

setup(
    name='ProjetBrassard',
    version="1.13",
    author='Franck Rochat',
    author_email='rochat.franck@gmail.com',
    description='This Project give you useful details about the environement where you are by Using an USB GPS and some API with an Internet Connection',
    url='https://github.com/Franck1333/ProjetBrassard',
    license='lgpl',
    packages=find_packages(),
    include_package_data=True,
    install_requires=["geopy==1.18.1","pyowm==2.9"], #Get the Dependencies from Pypi (pip install)
    dependency_links=['https://github.com/pimoroni/hyperpixel.git','https://github.com/csparpa/pyowm.git'], #Get the Dependencies via HTTP(s)
)
