# Barycentric Lagrange Interpolation

## What does this package provide?
This package provides the functioalities to interpolate a one dimensional function known at some sampling points with a barycentric Lagrange method. Furthermore you can differentiate the interpolated function. Also higher derivatives are supported. All this functionality is implemented within a Python class in numpy. Plots are provided by matplotlib.

In order to make application easier, an example Jupyter notebook is also included.

## How do you install this package?
### Requirements
This package requires Python 3, numpy and matplotlib.
### Get the package
#### Option 1: Download as zip (no git installation required)
Download this package as zip. Unpack it wherever it is suitable for you. When unpacked, run the following command in the package's base directory:
```
python3 setup.py install
```
Or if your Python installation requires root permission:
```
sudo -H python3 setup.py install
```
#### Option 2: Clone the repository
Clone the repository from Github:
```
git clone https://github.com/lubo92/barycentricLagrangeInterpolation
```
Then run the following command in the package's base directory:
```
python3 setup.py install
```
Or if your Python installation requires root permission:
```
sudo -H python3 setup.py install
```

## Mathematical Background and Literature
The code provided in this package closeley follows this paper:

[Berrut, Jean-Paul, and Trefethen, Lloyd N. "Barycentric lagrange interpolation." SIAM review 46.3 (2004): 501-517.] (https://people.maths.ox.ac.uk/trefethen/barycentric.pdf)

## Examples
An usage example Jupyter notebook is provided in the file example.ipynb.

## Applications
I wrote this class as a utility class for a differential equation solver. For details see my other repositories.

## Contact
If you have any questions - on the application of this package as well as on the mathematical background - don't hesitate to send an email to <w.lub92@gmail.com>.