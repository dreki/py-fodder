from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(name='fodder',
      version='1.0.1',
      description=u"feature-oriented development",
      long_description=long_description,
      classifiers=[],
      keywords='oop',
      author=u"Sean Gilbertson",
      author_email='sean.gilbertson@gmail.com',
      url='https://github.com/dreki/py-fodder',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click'
      ],
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      fodder=fodder.scripts.cli:cli
      """
      )
