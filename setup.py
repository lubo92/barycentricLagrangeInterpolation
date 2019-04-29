from setuptools import setup

setup(name='barycentricLagrangeInterpolation',
      version='1.0.0',
      description='package contains functionality for barycentric Lagrange interpolation and spectral differentiation',
      author='Wolfgang Lubowski',
      author_email='w.lub92@gmail.com',
      packages=['barycentricLagrangeInterpolation'],
      python_requires='>=3.0',
      install_requires=['numpy','matplotlib'],
      classifiers=[
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4'
      ],
      zip_safe=False)
