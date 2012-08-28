# -*- coding: utf-8 -*-

from distutils.core import setup
    
'''
IMPORTANTE: los campos que se describen a continuación deben ser rellenados en su totalidad.
Aquellos campos que NO SE VAYAN A UTILIZAR, se deben BORRAR.
'''

setup(name='fvislib',
      version='0.1',
      author='Jesús Gómez and Daniel Ampuero',
      author_email='jgomez@funvisis.gob.ve, danielmaxx@gmail.com',
      url='https://github.com/funvisis/fvislib/tags',
      download_url='http://code.funvisis.gob.ve/funvisis/',
      description='A library made for common use functions and utils',
      package_dir={'':'src'},
      packages=['funvisis', 'funvisis.utils', 'funvisis.misc'],
      requires=['django (>=1.3)'],
      classifiers=['Development Status :: Alpha',
                   'Intended Audience :: Developers',
                   'Natural Language :: Spanish',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python :: 2.6+',
                   'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
                   'License :: OSI Approved :: GNU Affero General Public License v3',
                   'Topic :: Django',
                  ],
     )
