from setuptools import setup

setup(name='rlunch',
      version='0.3.1',
      description='The lunch recommendation system for Ridibooks employees',
      url='http://github.com/minsoopark/RidiLunch',
      author='Minsoo Park',
      author_email='minsoo1003@gmail.com',
      license='MIT',
      packages=['rlunch'],
      zip_safe=False,
      install_requires=[
          'rullet >= 0.1.2',
          'click >= 3.3'
      ],
      entry_points={
          'console_scripts': ['rlunch=rlunch.command_line:main'],
      })
