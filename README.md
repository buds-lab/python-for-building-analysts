PythonforBuildingAnalysts
=========================

Set of IPython notebook tutorials to teach scripting to Building Simulation Experts and Analysts

This collection of IPython notebooks and supporting documentation/files is meant to give building energy simulation experts an overview of the useful libraries available as well as some practical scenarios in building simulation workflows.

A very [useful youtube video](https://www.youtube.com/watch?v=H6dLGQw9yFQ) to explain the IPython notebook format is available.

To use the notebooks, you will need to have Python installed on your machine along with quite a few of the libraries. The best way to do this is to use the [Canopy Free edition](https://www.enthought.com/products/canopy/).

##An overview of the notebooks is as follows:

0_PythonBaseLibraries:

[0_IntroductionandPythonBasics.ipynb](http://nbviewer.ipython.org/github/cmiller8/PythonforBuildingAnalysts/blob/master/0_PythonBaseLibraries/0_IntroductionandPythonBasics.ipynb) -- this notebook is meant to give an overview of the basic Python library functions and flow controls. It is not well annotated quite yet, so other [more general Python overviews](https://www.youtube.com/watch?v=gGKd19EtmqY&list=PLFD8B7CCCDB784595) could be better for very basic beginners.

[1_NumpyLibrary.ipynb](http://nbviewer.ipython.org/github/cmiller8/PythonforBuildingAnalysts/blob/master/0_PythonBaseLibraries/1_NumpyLibrary.ipynb) -- This notebook overviews the [NumPy](http://www.numpy.org/) library and is based on [another set of tutorials.](https://github.com/jrjohansson/scientific-python-lectures). Feel free to skip this tutorial if you aren't interested in the basics of how Python/Numpy creates arrays for mathematical calculations.

[2_ScipyLibrary.ipynb](http://nbviewer.ipython.org/github/cmiller8/PythonforBuildingAnalysts/blob/master/0_PythonBaseLibraries/2_ScipyLibrary.ipynb) -- This notebook is similar to the last in that it describes a fundamental library, [Scipy](http://www.scipy.org/), which has hundreds of scientific functions for machine learning, statistics, etc. Feel free to skip unless you're curious.

[3_MatplotlibLibrary.ipynb](http://nbviewer.ipython.org/github/cmiller8/PythonforBuildingAnalysts/blob/master/0_PythonBaseLibraries/3_MatplotlibLibrary.ipynb) -- The basics of the main plotting library in Python. A good review that can be supplemented by checking out the [Matplotlib gallery](http://matplotlib.org/gallery.html)

1_PandasTutorial:

[Pandas_DataAnalysisLibrary.ipynb](http://nbviewer.ipython.org/github/cmiller8/PythonforBuildingAnalysts/blob/master/1_PandasTutorial/Pandas_DataAnalysisLibrary.ipynb) -- THIS LIBRARY IS USEFUL! - I can't stress [Pandas](http://pandas.pydata.org/) enough for time-series data analysis. Whether you're post-processing simulation data or crunching measured datasets, this library is money. This tutorial was developed by the creator of Pandas, Wes McKinney, and you can see him [demo it on youtube.](https://www.youtube.com/watch?v=w26x-z-BdWQ&feature=youtu.be)

2_AnalyzingEnergyPlusOutputFile:

[EnergyPlusOutFileAnalysis.ipynb](http://nbviewer.ipython.org/github/cmiller8/PythonforBuildingAnalysts/blob/master/2_AnalyzingEnergyPlusOutputFile/EnergyPlusOutFileAnalysis.ipynb) -- This notebook is a practical scenario based on analyzing a huge .csv output from EnergyPlus which has hundreds of columns. It includes some advanced techniques and is not very well annotated yet (work in progress).

3_EppyTutorial:

[Eppy_EnergyPlusInputFileManipulation.ipynb](http://nbviewer.ipython.org/github/cmiller8/PythonforBuildingAnalysts/blob/master/3_EppyTutorial/Eppy_EnergyPlusInputFileManipulation.ipynb) -- eppy is a brilliant EnergyPlus IDF file text manipulation library created by [Santosh Phillip](https://github.com/santoshphilip). This notebook is based on his tutorial. In a nutshell, you use this library to auto-create your millions of parametric E+ runs for calibration, etc. Note: you'll have to [install the eppy package](https://pypi.python.org/pypi/eppy/0.4.6) to use this notebook

4_ParametericInputFileCreation:

[eppy%20IDF%20file%20manipulation.ipynb](http://nbviewer.ipython.org/github/cmiller8/PythonforBuildingAnalysts/blob/master/4_ParametericInputFileCreation/eppy%20IDF%20file%20manipulation.ipynb) -- The goal of this tutorial is to show how to use the eppy library in a realistic setting by performing the following tasks: splitting an IDF file into 'modules' that can be developed individually, reassembling the modules into IDF files for simulation, creating parametric run files from a single IDF file and a spreadsheet

5_ModelCalibration:

[ComparingMeasuredAndSimulatedData.ipynb](http://nbviewer.ipython.org/github/cmiller8/PythonforBuildingAnalysts/blob/master/5_ModelCalibration/ComparingMeasuredAndSimulatedData.ipynb) -- This notebook follows part of the calibration process outlined in the IBPSA-USA 2014 Conference Paper entitled: BIM-EXTRACTED ENERGYPLUS MODEL CALIBRATION FOR RETROFIT ANALYSIS OF A HISTORICALLY LISTED BUILDING IN SWITZERLAND

<!--08-Scenarios - An eppy Scenario -- haven't had the time to create this yet. Santosh, perhaps you have a more implemented example-->

<!--[09-Scenarios - Measured Data Visualization and R Integration.ipynb](http://nbviewer.ipython.org/github/cmiller8/PythonforBuildingAnalysts/blob/master/09-Scenarios%20-%20Measured%20Data%20Visualization%20and%20R%20Integration.ipynb) -- A big .csv file (80+ MB) from a real chilled water plant is loaded, visualized, and some of the data is passed to R to fit an ARIMA model (psuedo-successfully)-->

<!--[10-Scenarios - VRV Performance Curve Maker.ipynb](http://nbviewer.ipython.org/github/cmiller8/PythonforBuildingAnalysts/blob/master/10-Scenarios%20-%20VRV%20Performance%20Curve%20Maker.ipynb) -- A super crude notebook with code I used to create VRV performance curve coefficients for EnergyPlus from raw manufacturer data. Its sort of an advanced and obscure notebook.-->

##Please feel free to upload your own notebooks to enhance this list of learning resources for building performance analysts!

Background  
----------

If you are unfamiliar with IPython Notebook you can start with http://ipython.org/notebook


Installation  
------------

* Prerequisites  
One of the following distributions is needed. Please note that even if you have Python installed it is important to have one of these distributions installed and the binary for this installation in your path. This is because these distributions come packaged with all the supplementary libraries needed and these have been historically difficult to install separately.

  * EPD Free Enthought Python Distribution from http://enthought.com
  * Anaconda Python from http://continuum.io
  * Development has been done on v 1.5 of Anaconda distribution but EPD Free should work just as well.

* The following steps assume you have installed one of the distributions mentioned in prerequisites.

* From a zip or tar file
    * download the zip or tar file 
    * unpack the file to a directory called learnds
    * cd to the 'notebooks' subdirectory
    * start IPython Notebook 'ipython notebook --pylab=inline'
 
* From the git repo
    * clone the repo
    * cd to 'notebooks'
    * start IPython Notebook 'ipython notebook --pylab=inline'

This work is licensed under a [Creative Commons Attribution 3.0 Unported License](http://creativecommons.org/licenses/by/3.0/).
