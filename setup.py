# -*- coding: utf-8 -*-

from distutils.core import setup
    
'''
IMPORTANTE: los campos que se describen a continuación deben ser rellenados en su totalidad.
Aquellos campos que NO SE VAYAN A UTILIZAR, se deben BORRAR.
'''

setup(name='fvislib',
      version='1.0',
      author='Jesús Gómez and Daniel Ampuero',
      author_email='jgomez@funvisis.gob.ve and danielmaxx@gmail.com',
      url='http://code.funvisis.gob.ve/funvisis/LoL',
      download_url='http://code.funvisis.gob.ve/funvisis/',
      description='A library made for common use functions and utils',
      packages=['fvislib', 'fvislib.utils', 'fvislib.misc'],
      classifiers=['Development Status :: Alpha',
                   'Intended Audience :: Developers',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2.6+',
                   'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                   'License :: OSI Approved :: GNU Affero General Public License v3',
                   'Topic :: Internet',
                   'Topic :: Scientific/Engineering :: GIS',
                  ],
       requires=['django (>=1.3)', 'PIL (>=1.1.6)'],
     )
