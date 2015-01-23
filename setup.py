from setuptools import setup

setup(name='lunch',
      version='0.1',
      description='The lunch recommendation system for Ridibooks employees',
      url='http://github.com/minsoopark/RidiLunch',
      author='Minsoo Park',
      author_email='minsoo1003@gmail.com',
      license='MIT',
      packages=['lunch'],
      zip_safe=False,
      entry_points = {
        'console_scripts': ['lunch=lunch.command_line:main'],
      })
