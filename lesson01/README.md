# Lesson I: AI 101

## Software installation

### Homebrew Installation
MacOSX
```bash
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
``` 

### Python 3.6.5 Installation
Windows
- Download binary file from website www.python.org (https://www.python.org/ftp/python/3.6.5/python-3.6.5-amd64.exe)
- Then install it

MacOSX
```bash
$ brew install https://raw.githubusercontent.com/Homebrew/homebrew-core/f2a764ef944b1080be64bd88dca9a1d80130c558/Formula/python.rb
```

### Upgrade pip 
```bash
$ python3 -m pip install --upgrade pip
```

### Using virtual environment
Create virtual environment
```bash
$ virtualenv -p python3 myenv
```

Activate virtual environment
```bash
$ source ./myenv/bin/activate
```

Deactivate virtual environment
```bash
$ deactivate
```

### Install required library
This command assummed that you are in root project folder which has requirements.txt in there
```bash
$ pip install -r requirements.txt
```

## Q&A
Q: How to check Python version?
A: Run command ```$ python --version``` or ```$ python3 --version``` depends on which version is installed on your machine.

Q: How can I check my pip version?  
A: Run command ```$ pip --version```

## References

### Tools
Homebrew: https://brew.sh
Python: https://www.python.org
Docker: https://www.docker.com
PyCharm: https://www.jetbrains.com/pycharm
Visual Studio Code: https://code.visualstudio.com
GitHub: https://www.github.com
PyTorch: https://pytorch.org
