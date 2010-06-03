Installation
============

Add these lines into buildout::

  [buildout]
  parts = 
     paster
  
  [paster]
  eggs = zc.recipe.egg
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
  