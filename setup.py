from setuptools import setup, find_packages
import os

version = '1.1b2'

setup(name='zopeskel.dexterity',
      version=version,
      description="Paster templates for dexterity",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "Framework :: Zope3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone dexterity',
      author='Izhar Firdaus',
      author_email='izhar@inigo-tech.com',
      url='http://svn.plone.org/svn/collective/zopeskel.dexterity',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['zopeskel'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'PasteScript',
          'ZopeSkel'
          # -*- Extra requirements: -*-
      ],
      setup_requires=["PasteScript"],
      entry_points="""
      # -*- Entry points: -*-
      [paste.paster_create_template]
      dexterity = zopeskel.dexterity.dexterity:Dexterity

      [zopeskel.zopeskel_sub_template]
      dexterity_content = zopeskel.dexterity.localcommands.dexterity:DexterityContent
      dexterity_content_field = zopeskel.dexterity.localcommands.dexterity:ContentDexterityField
      dexterity_behavior = zopeskel.dexterity.localcommands.dexterity:DexterityBehavior
      dexterity_behavior_field = zopeskel.dexterity.localcommands.dexterity:BehaviorDexterityField
      dexterity_view = zopeskel.dexterity.localcommands.dexterity:DexterityView

      """,
      )
