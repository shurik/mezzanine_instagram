from setuptools import setup, find_packages
import os

version = '0.2dev'

setup(name='Mezzanine_Instagram',
      version=version,
      description="A simple Instagram app for Mezzanine/Django",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='',
      author='Aleksandr Vladimirskiy',
      author_email='aleksandr@butchershopcreative.com',
      url='http://www.butchershopcreative.com/',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['mezzanine'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'python-instagram',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
