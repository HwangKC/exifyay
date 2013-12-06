from distutils.core import setup
from distutils.sysconfig import get_python_lib


setup(
    name="exifyay",
    version='0.1.0',
    packages=['exifyay'],
    package_dir={'exifyay': '/Users/sp/Code/exifyay/bindings'},
    package_data={'exifyay': ['exifyay.so']},
    author='Simon Pantzare',
    author_email='simon@narrativeteam.com',
    description='Yay, Exif!',
    license='LGPL',
    keywords='exif',
    url='http://github.com/Memoto/exifyay',
    )
