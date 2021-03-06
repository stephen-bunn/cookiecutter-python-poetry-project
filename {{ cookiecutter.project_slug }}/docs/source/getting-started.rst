.. _getting-started:

===============
Getting Started
===============

| **Welcome to {{ cookiecutter.title }}!**
| This page should hopefully provide you with enough information to get you started using {{ cookiecutter.title }}.

Installation and Setup
======================

Installing the package should be super duper simple as we utilize Python's setuptools.

.. code-block:: bash

   $ poetry add {{ cookiecutter.project_slug }}
   $ # or if you're old school...
   $ pip install {{ cookiecutter.project_slug }}

Or you can build and install the package from the git repo.

.. code-block:: bash

   $ git clone {{cookiecutter.github_url}}.git
   $ cd ./{{ cookiecutter.project_slug }}
   $ python setup.py install
