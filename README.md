PythonforBuildingAnalysts
=========================

Set of IPython notebook tutorials to teach scripting to Building Simulation Experts and Analysts

This collection of IPython notebooks and supporting documentation/files is meant to give building energy simulation experts an overview of the useful libraries available as well as some practical scenarios in building simulation workflows.

A very [useful youtube video](https://www.youtube.com/watch?v=H6dLGQw9yFQ) to explain the IPython notebook format is available.

To use the notebooks, you will need to have Python installed on your machine along with quite a few of the libraries. The best way to do this is to use the [Canopy Free edition](https://www.enthought.com/products/canopy/).

##An overview of the notebooks is as follows:

[00-Introduction and Python Basics.ipynb](http://nbviewer.ipython.org/github/cmiller8/PythonforBuildingAnalysts/blob/master/00-Introduction%20and%20Python%20Basics.ipynb) -- this notebook is meant to give an overview of the basic Python library functions and flow controls. It is not well annotated quite yet, so other [more general Python overviews](https://www.youtube.com/watch?v=gGKd19EtmqY&list=PLFD8B7CCCDB784595) could be better for very basic beginners.

[01-LibraryBasics - Numpy.ipynb](http://nbviewer.ipython.org/github/cmiller8/PythonforBuildingAnalysts/blob/master/01-LibraryBasics%20-%20Numpy.ipynb) -- This notebook overviews the [NumPy](http://www.numpy.org/) library and is based on [another set of tutorials.](https://github.com/jrjohansson/scientific-python-lectures). Feel free to skip this tutorial if you aren't interested in the basics of how Python/Numpy creates arrays for mathematical calculations.

[02-LibraryBasics - Scipy.ipynb](http://nbviewer.ipython.org/github/cmiller8/PythonforBuildingAnalysts/blob/master/02-LibraryBasics%20-%20Scipy.ipynb) -- This notebook is similar to the last in that it describes a fundamental library, [Scipy](http://www.scipy.org/), which has hundreds of scientific functions for machine learning, statistics, etc. Feel free to skip unless you're curious.

[03-LibraryBasics - Matplotlib.ipynb](http://nbviewer.ipython.org/github/cmiller8/PythonforBuildingAnalysts/blob/master/03-LibraryBasics%20-%20Matplotlib.ipynb) -- The basics of the main plotting library in Python. A good review that can be supplemented by checking out the [Matplotlib gallery](http://matplotlib.org/gallery.html)

[04-LibraryBasics - Pandas.ipynb](http://nbviewer.ipython.org/github/cmiller8/PythonforBuildingAnalysts/blob/master/04-LibraryBasics%20-%20Pandas.ipynb) -- THIS LIBRARY IS USEFUL! - I can't stress [Pandas](http://pandas.pydata.org/) enough for time-series data analysis. Whether you're post-processing simulation data or crunching measured datasets, this library is money. This tutorial was developed by the creator of Pandas, Wes McKinney, and you can see him [demo it on youtube.](https://www.youtube.com/watch?v=w26x-z-BdWQ&feature=youtu.be)

[05-LibraryBasics - eppy.ipynb](http://nbviewer.ipython.org/github/cmiller8/PythonforBuildingAnalysts/blob/master/05-LibraryBasics%20-%20eppy.ipynb) -- eppy is a brilliant EnergyPlus IDF file text manipulation library created by [Santosh Phillip](https://github.com/santoshphilip). This notebook is based on his tutorial. In a nutshell, you use this library to auto-create your millions of parametric E+ runs for calibration, etc. Note: you'll have to [install the eppy package](https://pypi.python.org/pypi/eppy/0.4.6) to use this notebook

[06-Scenarios - EnergyPlus Post-Processing 1 - Plotting Output CSV.ipynb](http://nbviewer.ipython.org/github/cmiller8/PythonforBuildingAnalysts/blob/master/06-Scenarios%20-%20EnergyPlus%20Post-Processing%201%20-%20Plotting%20Output%20CSV.ipynb) -- This notebook is a practical scenario based on analyzing a huge .csv output from EnergyPlus which has hundreds of columns. It includes some advanced techniques and is not very well annotated yet (work in progress).

[07-Scenarios - EnergyPlus Post-Processing 2 - Comparing Simulation and Measured.ipynb](http://nbviewer.ipython.org/github/cmiller8/PythonforBuildingAnalysts/blob/master/07-Scenarios%20-%20EnergyPlus%20Post-Processing%202%20-%20Comparing%20Simulation%20and%20Measured.ipynb) -- This is a notebook where I compare output data from EnergyPlus with some measured heating data. This notebook also has many advanced techniques using the Pandas library. Better annotation is on its way.

08-Scenarios - An eppy Scenario -- haven't had the time to create this yet. Santosh, perhaps you have a more implemented example

[09-Scenarios - Measured Data Visualization and R Integration.ipynb](http://nbviewer.ipython.org/github/cmiller8/PythonforBuildingAnalysts/blob/master/09-Scenarios%20-%20Measured%20Data%20Visualization%20and%20R%20Integration.ipynb) -- A big .csv file (80+ MB) from a real chilled water plant is loaded, visualized, and some of the data is passed to R to fit an ARIMA model (psuedo-successfully)

[10-Scenarios - VRV Performance Curve Maker.ipynb](http://nbviewer.ipython.org/github/cmiller8/PythonforBuildingAnalysts/blob/master/10-Scenarios%20-%20VRV%20Performance%20Curve%20Maker.ipynb) -- A super crude notebook with code I used to create VRV performance curve coefficients for EnergyPlus from raw manufacturer data. Its sort of an advanced and obscure notebook.

##Please feel free to upload your own notebooks to enhance this list of learning resources for building performance analysts!

This work is licensed under a [Creative Commons Attribution 3.0 Unported License](http://creativecommons.org/licenses/by/3.0/).
