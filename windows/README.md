# Using Python on Windows

These instructions are tailored for the Surface Pro computers provided by the lab. If you are using a different computer your steps may vary slightly.

## Set up Powershell

Powershell lets us get to the Windows commandline. We will use the commandline to run the python programs.

Open Powershell
```shell
cd OneDrive
cd Documents
mkdir PythonClass
cd PythonClass
```

## Check your Python version

When you write a new program you should use the latest version of Python. Python can tell you what version is installed. At the time of this writing that is 3.12.4. Do you have the latest version installed?

Switch to Powershell
```shell
python --version
```

## Set up Windows Explorer

Windows Explorer (the file explorer; not IE which was the Internet Explorer) lets us see and manage files on our computer. We will use it along with the commandline to manage the files we are creating.

Open Windows Explorer
* Click on "Documents" in left nav bar
* Is the "PythonClass" directory there? If not, click on refresh.
* Double-click on "PythonClass" to open it

## Set up Notepad

We will use Notepad to edit the Python files. If you go further into Python development you will likely want a full-featured development environment.

Open Notepad

## Write your first Python program

Switch to Notepad
* Type in a program
  * `print("Hello world!")`
* File->Save
  * Navigate to the "PythonClass" directory
  * File Name: `hello.py`

Switch to Powershell
* Run the program
  * `python hello.py`
* Did it work?

## Create a Python Virtual Environment

The best practice is to run Python programs in a virtual environment. The details of why that matters are beyond this class. If you are curious, you can read more about virtual environments and why they are necessary in the [RealPython primer](https://realpython.com/python-virtual-environments-a-primer/).

Switch to Powershell
```shell
python -m venv venv
.\venv\Scripts\activate
```
Note that your prompt now begins with `(venv)`

## Start the Class

The files for this class are hosted on GitHub. This is a popular place to store source code.

Open Edge (or any other browser)
* Navigate to https://github.com/Dcolt/PlotPython
* Follow the instructions in the README
