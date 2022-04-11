from setuptools import setup

APP = ['IEEECitationCreator.py']
DATA_FILES = []
OPTIONS = {
    'iconfile': 'type2.icns', 
    'argv_emulation': False,
    }

setup(
    app=APP,
    name='IEEE Citation Creator', 
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)