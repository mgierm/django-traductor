import os
import uuid
from setuptools import setup
from setuptools import find_packages
from pip._internal.req import parse_requirements

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.md')).read()
install_requirements = parse_requirements(os.path.join(PROJECT_ROOT, 'requirements.txt'), session=uuid.uuid1())
requirements = [str(ir.req) for ir in install_requirements]

setup(
    name='django-traductor',
    version='0.1',
    packages=find_packages(),
    description='A simple django application for automatic translations',
    long_description=README,
    author='Mikołaj Giermek @mgierm',
    author_email='mgierm@gmail.com',
    url='https://github.com/mgierm/django-traductor',
    license='MIT',
    install_requires=[
        'Django>=2.2,<3.0',
    ]
)
