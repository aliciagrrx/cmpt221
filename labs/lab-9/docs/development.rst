.. _`Development`:

Development
===========
This section is intended for developers that want to create a fix or develop an enhancement to the CMPT221 application.

Code of Conduct
---------------
All contributors are expected to follow the coding conventions and style guidelines set by the maintainers. This includes writing clean, readable Python code, adhering to Flask and SQLAlchemy best practices, and documenting changes appropriately.

Repository
----------
The repository for CMPT221 is on Github: https://github.com/aliciagrrx/cmpt221.git

Development Environment
-----------------------
A `Python virtual environment`_ is recommended. Once the virtual environment is activated, clone the CMPT221 repository and prepare the development environment with 

.. _Python virtual environment: https://virtualenv.pypa.io/en/latest/

.. code-block:: text

    $ git clone https://github.com/aliciagrrx/cmpt221.git
    $ cd CMPT221
    $ pip install -r requirements.txt

This will install all local prerequisites needed for ``CMPT221`` to run.

Pytest
-------------------
Unit tests are developed using Pytest. To run the test suite, issue:

.. code-block:: text

    $ cd tests
    $ pytest test_app.py

Build Documentation
-------------------
The Github pages site is used to publish documentation for the CMPT221 application at https://aliciagrrx.github.io/cmpt221/

To build the documentation, issue:

.. code-block:: text
    
    $ cd docs
    $ make html
    # windows users without make installed use:
    $ make.bat html

The top-level document to open with a web-browser will be  ``docs/_build/html/index.html``.

To publish the page, copy the contents of the directory ``docs/_build/html`` into the branch
``gh-pages``. Then, commit and push to ``gh-pages``.