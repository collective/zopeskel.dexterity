Installation
============

Add these lines into buildout::

  [buildout]
  parts = 
     paster
  
  [paster]
  recipe = zc.recipe.egg
  eggs = 
     ZopeSkel
     PasteScript
     PasteDeploy
     zopeskel.dexterity
     ${buildout:eggs}
  entry-points = paster=paste.script.command:run
  
And run the buildout

Usage
======

Creating a dexterity product::

  /path/to/paster create -t dexterity

Adding a contenttype skeleton::

  cd /path/to/product/root
  /path/to/paster addcontent dexterity_content

Adding a behavior skeleton::

  cd /path/to/product/root
  /path/to/paster addcontent dexterity_behavior

Adding a view::

  cd /path/to/product/root
  /path/to/paster addcontent dexterity_view

Adding a field to the content type schema::

  cd /path/to/product/root
  /path/to/paster addcontent dexterity_content_field
  
Adding a field to a behavior schema::

  cd /path/to/product/root
  /path/to/paster addcontent dexterity_behavior_field
 
Note
====

If you hit and error like this::

  pkg_resources.DistributionNotFound: plone.app.relationfield: Not Found for: my.product (did you run python setup.py develop?) 

when attempting to run `paster addcontent`, then you need to ensure that
Paster knows about all the relevant eggs from your buildout.

Add `${instance:eggs}` to your `paster` section in your buildout, thusly::

  [paster]
  recipe = zc.recipe.egg
  eggs = 
     ...
     ${instance:eggs}
  entry-points = paster=paste.script.command:run
  
where `instance` is the name of your ``plone.recipe.zope2instance`` section.
Re-run the buildout and the issue should be resolved.
