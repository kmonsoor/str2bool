#!/usr/bin/env python

from setuptools import setup

import str2bool

setup(name='str2bool',
      version=str2bool.__version__,
      description='String to Boolean conversion',
      author='Khaled Monsoor',
      author_email='k@kmonsoor.com',
      maintainer='Khaled Monsoor',
      maintainer_email='k@kmonsoor.com',
      url='https://github.com/kmonsoor/str2bool',
      packages=['str2bool'],
      license='MIT',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Intended Audience :: Information Technology',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Utilities',
          'Topic :: Text Processing',
      ],
      install_requires=[],
      # entry_points={},
      )
