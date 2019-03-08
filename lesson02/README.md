# Lesson II: Image Classification

## Prerequisite
 - Python 3.6.5 installed
 - Sample data set (https://github.com/OlafenwaMoses/IdenProf/releases/download/v1.0/idenprof-jpg.zip)
 - Trained model which achieved 79% accuracy (https://github.com/OlafenwaMoses/IdenProf/releases/download/v1.0/idenprof_061-0.7933.h5)  
## Installation
You might need to run below libraries installation in virtual environment.
### Create and activate virtual environment (recommend)
Check whether you have valid Python version by run ```$ python --version``` and expected to see ```Python 3.6.3``` as an output.
If you have other version, uninstall current version and reinstall (https://www.python.org/ftp/python/3.6.3/python-3.6.3-amd64.exe).
Next is to check ```pip``` version by run ```$ pip --version```. And if there is pip installed on your machine, the version number will be shown at the beginning of an output.

Then run upgrade pip to the latest version
```bash
$ pip install --upgrade pip --user
```
Run to check pip version again and should see ```pip 19.0.3``` or newer version

Install virtualenv library if doesn't have
```bash
$ pip install virtualenv
```
Create virtual environment and activate it
```bash
$ virtualenv -p python imagedetection
$ imagedetection\Scripts\activate.bat
```  
### Upgrade absl-py
```bash
$ pip install --upgrade absl-py
```
### Tensorflow
```bash
$ pip install tensorflow
```  
### Numpy
```bash
$ pip install numpy
```  
### SciPy
```bash
$ pip install scipy
```  
### OpenCV
```bash
$ pip install opencv-python
```  
### Pillow
```bash
$ pip install pillow
```  
### Matplotlib
```bash
$ pip install matplotlib
```  
### H5py
```bash
$ pip install h5py
```  
### Keras
```bash
$ pip install keras
```  
### ImageAI
```bash
$ pip install https://github.com/OlafenwaMoses/ImageAI/releases/download/2.0.2/imageai-2.0.2-py3-none-any.whl
```  
## Training model
Edit ```idenprof/json/model_class.json``` to c

Run model_training.py
```bash
$ python model_training.py
```

# Practice
Train image recognition model which could detect at least 5 different jobs with at least 50% confidence. 


## References
Professional images dataset (OlafenwaMoses/IdenProf)  
- https://github.com/OlafenwaMoses/IdenProf  
