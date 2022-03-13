from setuptools import setup

APP = ['IEEECitationCreator.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'iconfile': 'IEEECitationCreator.icns', 
    }

setup(
    app=APP,
    name='IEEE Citation Creator', 
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)