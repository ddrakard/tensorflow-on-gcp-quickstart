# Setting up a venv virtual Python environment

[venv](https://docs.python.org/3/library/venv.html) is a free tool that sets
up a virtual Python environment (an execution environment with a specific
version of the Python interpreter and installed dependency
[packages](https://packaging.python.org/tutorials/installing-packages/)).

This is very useful because it means your project will only use packages that
were installed specifically for it, and not any other packages that may be on
your computer. This ensures that you become aware of all the package
dependencies that your project is using. This is essential so that when the
project is run in a Docker image (which is the method this project uses), it
contains all the dependencies it needs.

There are other utilities which do the same thing as you can use if you are
experienced.

This guide is to set up venv on the command line. Some tools (not using the
command-line) may set up venv in other ways.

1. You should have Python 3 and [pip](https://pypi.org/project/pip/) already
   installed on your computer.
2. Open a command-line prompt in the base directory of this project.
3. Install venv if it is not installed already: `pip install virtualenv`.
4. Create the virtual environment: `python3 -m venv venv`.
   This creates a virtual environment in the directory `venv` directly under 
   the project base directory.
5. Activate the virtual environment. **You must do this whenever you open a
   command-line.**
   - On Linux or Mac: `source venv/bin/activate`
   - On Windows: `venv\Scripts\activate.bat`