from setuptools import setup

setup(name='nb-templater',
      version='0.1',
      description='Tool to programmatically generate Jupyter notebook files',
      url='http://github.com/ismailuddin/jupyter-nb-templater',
      author='Ismail Uddin',
      license='GPLv3',
      scripts=['bin/nb-templater'],
      packages=['nb-templater'],
      install_requires=[
          'nbformat',
      ],
      zip_safe=False)