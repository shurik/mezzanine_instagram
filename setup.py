from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='mezzanine_instagram',
    version='v0.0.1.dev1',
    description='Django app that integrates Mezzanine CMS with Instagram',
    long_description=long_description,
    url='https://github.com/shurik/mezzanine_instagram',
    author='Sasha Vladimirskiy',
    author_email='sasha@butchershop.co',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='django mezzanine cms instagram',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[
        'setuptools',
        'Mezzanine==3.1.10',
        'python-instagram',
        'django-braces',
    ],
    extras_require={
        'dev': ['check-manifest', 'ipdb', 'ipython'],
        'test': ['coverage'],
    },
    package_data={
        'sample': [],
    },
    data_files=[],
    entry_points={
        'console_scripts': [
        ],
    },
)
