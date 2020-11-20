Cloning the git repository
==========================



Adding a new repository to bact
===============================

As a first step create the separate repository.

Then in the appropriate place in the tree add the module
with (e.g. for bact-archiver-local)

.. code:: shell

   git submodule add git@github.com:hz-bbact-archiver-local


The initialise the module with

.. code:: shell

   git submodule init


Add the module (and in case .gitmodules is not yet part of the
repository add it too) with

.. code:: shell

   git commit -a -m "Added bact-archiver-local as submodule"


.. code :: shell
