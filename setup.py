from setuptools import setup, find_packages
import os

version = '1.5.2'

setup(name='zopeskel.dexterity',
      version=version,
      description="ZopeSkel templates for dexterity",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Zope3",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Framework :: Buildout",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone dexterity paster templates zopeskel',
      # Credit original author:
      # author='Izhar Firdaus',
      # author_email='izhar@inigo-tech.com',
      author='ZopeSkel Development Team',
      author_email='zopeskel@lists.plone.org',
      url='http://svn.plone.org/svn/collective/zopeskel.dexterity',
      license='GPL 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['zopeskel'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'PasteScript',
          'PasteDeploy',
          'Paste',
          'ZopeSkel<=3.0dev'
          # -*- Extra requirements: -*-
      ],
      setup_requires=["PasteScript"],
      entry_points="""
      # -*- Entry points: -*-
      [paste.paster_create_template]
      dexterity = zopeskel.dexterity.dexterity:Dexterity

      [zopeskel.zopeskel_sub_template]
      dexterity_content = zopeskel.dexterity.localcommands.dexterity:DexterityContent
      dexterity_behavior = zopeskel.dexterity.localcommands.dexterity:DexterityBehavior
      """,
      )
