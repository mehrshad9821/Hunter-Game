Quick start

Mypy can be installed using pip:

$ python3 -m pip install -U mypy
If you want to run the latest version of the code, you can install from git:

$ python3 -m pip install -U git+git://github.com/python/mypy.git
Now, if Python on your system is configured properly (else see "Troubleshooting" below), you can type-check the statically typed parts of a program like this:

$ mypy PROGRAM
You can always use a Python interpreter to run your statically typed programs, even if they have type errors:

$ python3 PROGRAM
Web site and documentation

Documentation and additional information is available at the web site:

http://www.mypy-lang.org/

Or you can jump straight to the documentation:

http://mypy.readthedocs.io/

Troubleshooting

Depending on your configuration, you may have to run pip3 like this:

$ python3 -m pip install -U mypy
This should automatically installed the appropriate version of mypy's parser, typed-ast. If for some reason it does not, you can install it manually:

$ python3 -m pip install -U typed-ast
If the mypy command isn't found after installation: After either pip3 install or setup.py install, the mypy script and dependencies, including the typing module, will be installed to system-dependent locations. Sometimes the script directory will not be in PATH, and you have to add the target directory to PATH manually or create a symbolic link to the script. In particular, on Mac OS X, the script may be installed under /Library/Frameworks:

/Library/Frameworks/Python.framework/Versions/<version>/bin
In Windows, the script is generally installed in \PythonNN\Scripts. So, type check a program like this (replace \Python34 with your Python installation path):

C:\>\Python34\python \Python34\Scripts\mypy PROGRAM
Working with virtualenv

If you are using virtualenv, make sure you are running a python3 environment. Installing via pip3 in a v2 environment will not configure the environment to run installed modules from the command line.

$ python3 -m pip install -U virtualenv
$ python3 -m virtualenv env
Quick start for contributing to mypy

If you want to contribute, first clone the mypy git repository:

$ git clone --recurse-submodules https://github.com/python/mypy.git
From the mypy directory, use pip to install mypy:

$ cd mypy
$ python3 -m pip install -U .
Replace python3 with your Python 3 interpreter. You may have to do the above as root. For example, in Ubuntu:

$ sudo python3 -m pip install -U .








