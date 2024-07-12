BACT: Berlin Accelerator Control Toolkit
========================================

Publishing code soon. stay tuned.


HAve a look to the status page of the `subpackages dashboard`_

.. _`subpackages dashboard` : subpackages_dashboard.md


Following other package belong to this toolkit
----------------------------------------------

* bact-archiver see https://github.com:hz-b/bact-archiver

Cloning and installing
----------------------

Cloning `bact` and its subrepositories
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In an empty directory issue the command

.. code-block:: shell

     git clone https://github.com/hz-b/bact.git -b dev/feature/orbit-response-measurement bact


then change into `bact`. In this directory issue

.. code-block:: shell

    git submodule update --recursive --init



which pulls all subrepositiories. Now all subrepositories should be available

Installing packages
~~~~~~~~~~~~~~~~~~~

This requires two steps:

* making a python virtual environment
* installing all packages contained within bact

To make the virtual environment run

.. code-block:: sh

    python3 -m venv venv


Then activate this environemnt using

.. code-block:: sh

   . ./venv/bin/activate


Now you should have an active virtual environment. Run

.. code-block:: shell

   python -m pip install `python list_package_names.py | grep -v archiver`

should install all required packages in your virtual environment. Please note this
will not install the archiver module, as it requires some prerequisites for building
its core. Please have a look to the directory `archiver/core` how to install it.


Running orbit response matrix example
-------------------------------------

If you have the package https://github.com/hz-b/dt4acc installed you
can run it using

.. code-block:: shell

    python3 custom/bessyii/bluesky/scripts/measure_steerer_response.py --full-run








