from setuptools import find_packages, setup
import os

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

setup(name='ok-redis',
      version='0.1.1',
      packages=find_packages(exclude=['test*']),
      license='MIT',
      description='Object-Key Mapper for Redis',
      long_description=README,
      url='https://github.com/mixxorz/ok-redis',
      author='Mitchel Cabuloy (mixxorz)',
      author_email='mixxorz@gmail.com',
      maintainer='Mitchel Cabuloy (mixxorz)',
      maintainer_email='mixxorz@gmail.com',
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Topic :: Database',
          'Topic :: Utilities',
      ],
      install_requires=['six'],
      zip_safe=False)
