from setuptools import find_packages, setup

import ok

setup(name='ok-redis',
      version=ok.__version__,
      description=ok.__doc__,
      url='https://github.com/mixxorz/ok-redis',
      author='Mitchel Cabuloy (mixxorz)',
      author_email='mixxorz@gmail.com',
      license='MIT',
      packages=find_packages(),
      zip_safe=False)
