from setuptools import setup

with open("README", 'r') as f:
    long_description = f.read()

setup(
   name='DAT',
   version='0.0',
   description='Deep Analysis of Text / Deep Anal in Text',
   license="GNU",
   long_description=long_description,
   author='Shchablo',
   author_email='Shchablo@gmail.com',
   url="-",
   packages=[''],
   install_requires=['bar', 'greek'],
   scripts=[
            'scripts',
            'units',
           ]
)
