import io
from os.path import abspath, dirname, join
from setuptools import setup, find_packages

REQUIREMENTS = [
    'socketIO_client',
]

HERE = dirname(abspath(__file__))
LOAD_TEXT = lambda name: io.open(join(HERE, name), encoding='UTF-8').read()
DESCRIPTION = '\n\n'.join(LOAD_TEXT(_) for _ in [
    'README.md',
])

setup(
    name='smarthome_hub',
    version='0.0.1',
    description='Smarthome hub agent',
    author='Sungtaek Lee',
    author_email='leesungtaek@gmail.com',
    license='Apache License',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    url='https://github.com/sungtaek/Smarthome-hub',
    install_requires=REQUIREMENTS,
    packages=find_packages(),
)

