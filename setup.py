from setuptools import setup

setup(name='hoerapi',
      version='1.0',
      description='',
      author='luto',
      author_email='m@luto.at',
      license='MIT',
      url='https://github.com/hoersuppe/hoerapi.py',
      packages=['hoerapi'],
      install_requires=[
       'requests',
       'pytest',
       'pytest-cov',
      ],
     )