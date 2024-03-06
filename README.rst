BACT: Berlin Accelerator Control Toolkit
========================================

Publishing code soon. stay tuned.

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

   python3 development_install.py

should install all required packages in your virtual environment.







