from setuptools import setup

setup(
    name='pyduino',
    version='0.1.0',
    author='Alejandro Guirao',
    author_email='lekumberri@gmail.com',
    packages=['pyduino'],
    url='https://github.com/lekum/pyduino',
    license='LICENSE',
    description='Python library to interface with Arduino via serial connection',
    long_description=open('README.md').read(),
    install_requires=[
        "pyserial >= 2.7"
    ]
)
