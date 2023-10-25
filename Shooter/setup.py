"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['Shooter.py']
DATA_FILES = ['space_2-02.png','Start 1-02.png','rocket_1.png','bullet.png','ufo_3.png','Start 2-02.png','Start 3-02.png','rocket_2-02.png','rocket_3-03.png','bùm bùm by mint-02.png','instruction-02.png','game over-02.png','702k_rcbl_211015 [Converted]-04.png']
OPTIONS = {
 'iconfile':'icon.icns',
 'argv_emulation': True,
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
