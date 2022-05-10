# Decimal (Arabic) to Roman Number Conversion - User Manual
This manual is intended to establish how the application is installed and used by users. 

## Table of contents
1. [System requirements](#system-requirements)
2. [Installation and execution](#installation-and-execution)
3. [Usage](#usage)

## System requirements
In order to be able to install and run the both the application and its tests, make sure you have installed in your machine the following programs:

* Git 2.36.0 or greater, available [here](https://git-scm.com/downloads).
* Python 3.10.1 or greater, available [here](https://www.python.org/downloads/).
* pip (Package Installer for Python) 21.2.4 or greater, available [here](https://pypi.org/project/pip/).

Please note that pip should come with every Python installation by default.

## Installation and execution
Beforehand, make sure to satisfy the requirements of this project. To install the application, follow these steps:

1. Open the terminal or console present in your operating system, such as Command Prompt (CMD) or Powershell for Windows, Konsole or Terminal on Linux distros or Terminal on MacOS.

2. Next, type the following command and, optionally, insert the path of the repository with the application:
``` 
git clone https://github.com/pamendez/Decimal-Roman-Conversion.git <path-to-repo>
```

3. After cloning the application, type the following command with the path of the repository
```
cd <path-to-repo>
```

4. Next, to execute the application, use the following command:
```
python convert.py
``` 

5. If everything worked, the message ```'Enter an arabic (decimal) number'``` will appear on the terminal on your screen, and with that you successfully installed this application.

## Usage
Once in the application, insert a numerical value greater or equal than one (1) and it's roman numeral equivalent will appear on screen.

If a zero or negative value is inserted instead, then an error will appear on screen.

## Execution of tests
Once installed the application, if you want to run the available unit tests make sure you have the [`pytest`](https://docs.pytest.org/en/7.1.x/contents.html) package installed on your machine. If it's not installed, use the following command:

```
Windows: pip install -U pytest
Linux/MacOS: python -m pip install -U pytest
```

Afterwards, simply use the following command on the terminal of your choice and on the root of the application to run the available unit tests

```
pytest test_convert.py
```