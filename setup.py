from setuptools import setup, find_packages
import os

version = '1.1a1'

setup(name='collective.dexteritypaste',
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
      url='http://svn.plone.org/svn/collective/collective.dexteritypaste',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'PasteScript',
          'ZopeSkel',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      [paste.paster_create_template]
      dexterity = collective.dexteritypaste.dexterity:Dexterity

      [zopeskel.zopeskel_sub_template]
      dexterity_content = collective.dexteritypaste.localcommands.dexterity:DexterityContent
      dexterity_content_field = collective.dexteritypaste.localcommands.dexterity:ContentDexterityField
      dexterity_behavior = collective.dexteritypaste.localcommands.dexterity:DexterityBehavior
      dexterity_behavior_field = collective.dexteritypaste.localcommands.dexterity:BehaviorDexterityField
      dexterity_view = collective.dexteritypaste.localcommands.dexterity:DexterityView

      """,
      )
