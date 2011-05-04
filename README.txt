Introduction
============

Dexterity is a content-type development tool for Plone. It supports Through-
The-Web and filesystem development of new content types for Plone.

zopeskel.dexterity provides a mechanism to quickly create Dexterity add on
skeletons. It also makes it easy to add new content types to an existing
skeleton. New content types built with this tool will support round-trip
elaboration with Dexterity's TTW schema editor.

This is a development tool. You should be familiar with Plone and buildout to
use it. You should have already installed Dexterity in your Plone development
instance and be ready to start learning to use it.

Installation
============

Add these lines into buildout::

  [buildout]
  parts = 
     zopeskel
  
  [zopeskel]
  recipe = zc.recipe.egg
  eggs = 
     ZopeSkel
     PasteScript
     zopeskel.dexterity
     ${buildout:eggs}
  
And run the buildout

Usage
======

Creating a dexterity product, typically done in your buildout's src
directory::

  ../bin/zopeskel dexterity

Adding a contenttype skeleton::

  cd yourbuildout/src/your-product
  ../bin/paster addcontent dexterity_content

Adding a behavior skeleton::

  cd yourbuildout/src/your-product
  ../bin/paster addcontent dexterity_behavior
 
Notes
=====

Egg Directories
---------------

In order to support local commands, ZopeSkel/Paster will create Paste,
PasteDeploy and PasteScript eggs inside your product. These are only needed
for development. You can and should remove them from your add-on distribution.

Errors
------

If you hit and error like this::

  pkg_resources.DistributionNotFound: plone.app.relationfield: Not Found for: my.product (did you run python setup.py develop?) 

when attempting to run `paster addcontent`, then you need to ensure that
Paster knows about all the relevant eggs from your buildout.

Add `${instance:eggs}` to your `paster` section in your buildout, thusly::

  [zopeskel]
  recipe = zc.recipe.egg
  eggs = 
     ...
     ${instance:eggs}
  entry-points = paster=paste.script.command:run
  
where `instance` is the name of your ``plone.recipe.zope2instance`` section.
Re-run the buildout and the issue should be resolved.
