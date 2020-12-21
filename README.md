# Barycentric Lagrange Interpolation

## References
This package was developed by Wolfgang Lubowski for a project in fluid dynamics and heat transfer with the title "Solution of Prandtl’s boundary layer equations with a spectral collocation method based on barycentric Lagrange interpolation" supervised by Stefan Braun, institute of fluid mechanics and heat transfer, TU Wien in May 2020.

The implementation closely follows these papers:

R. Baltensperger and M. R. Trummer. Spectral differencing with a twist. SIAM J. Sci. Comp., 24(5):1465–1487, 2003.

J.-P. Berrut and L. N. Trefethen. Barycentric lagrange interpolation. SIAM Rev., 46(3):501–517, 2004.

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

## Literature and Mathematical Background
The code provided in this package closeley follows this paper:

[Berrut, Jean-Paul, and Trefethen, Lloyd N. "Barycentric lagrange interpolation." SIAM review 46.3 (2004): 501-517.] (https://people.maths.ox.ac.uk/trefethen/barycentric.pdf)

## Examples
An usage example Jupyter notebook is provided in the file example.ipynb.

## Applications
I wrote this class as a utility class for a differential equation solver. For details see my other repositories.

## Contact
If you have any questions - on the application of this package as well as on the mathematical background - don't hesitate to send an email to <w.lub92@gmail.com>.
