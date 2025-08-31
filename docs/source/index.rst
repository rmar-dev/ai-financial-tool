New Python Project Documentation
=================================

Welcome to the New Python Project documentation! This project demonstrates modern Python development practices and provides a solid foundation for building Python applications.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   getting_started
   installation
   api/index
   development
   examples/index
   changelog

Overview
--------

This project is designed with the following principles:

* **Modern Python**: Uses Python 3.9+ with type hints and modern syntax
* **Testing**: Comprehensive test suite with pytest
* **Code Quality**: Automated formatting with Black, import sorting with isort, and linting with flake8
* **Type Safety**: Static type checking with mypy
* **Development Workflow**: Pre-commit hooks ensure code quality
* **Documentation**: Comprehensive documentation with examples

Features
--------

Core Features
~~~~~~~~~~~~~

* Modular architecture with clean separation of concerns
* Comprehensive logging and error handling
* Environment-based configuration
* Extensible design patterns

Development Tools
~~~~~~~~~~~~~~~~~

* Virtual environment management
* Automated testing with coverage reporting
* Code formatting and linting
* Type checking
* Pre-commit hooks
* Documentation generation

Package Management
~~~~~~~~~~~~~~~~~~

* Modern packaging with ``pyproject.toml``
* Separate development and production dependencies
* Easy installation and distribution

Quick Start
-----------

.. code-block:: bash

   # Clone the repository
   git clone <repository-url>
   cd new-python-project

   # Create and activate virtual environment
   python -m venv venv
   .\venv\Scripts\Activate.ps1  # Windows
   source venv/bin/activate     # macOS/Linux

   # Install dependencies
   pip install -r requirements-dev.txt
   pip install -e .

   # Verify installation
   python src/new_python_project/main.py
   pytest

Project Structure
-----------------

.. code-block:: text

   new-python-project/
   ├── src/new_python_project/  # Main source code
   ├── tests/                   # Test suite
   ├── docs/                    # Documentation
   ├── scripts/                 # Development scripts
   ├── config/                  # Configuration files
   ├── requirements.txt         # Production dependencies
   ├── requirements-dev.txt     # Development dependencies
   ├── pyproject.toml          # Project configuration
   └── README.md               # Project overview

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
