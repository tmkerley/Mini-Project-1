# Mini-project 1

## Purpose

This was to explore the matplotlib, numpy, scipy, and APIs. 

## Third-Party Packages

* Matplotlib Version 3.6.0
    install using pip:

        pip install matplotlib

    Support Website:

        https://matplotlib.org/stable/index.html#


* NumPy Version 1.23.0
    install using pip:

        pip install numpy

    Support Website:

        https://numpy.org/


* yFinance Version 0.1.63
    install using pip:

        pip install -i https://pypi.anaconda.org/ranaroussi/simple yfinance

    Dependencies:

        Python <https://www.python.org>`_ >= 2.7, 3.4+
        Pandas <https://github.com/pydata/pandas>`_ (tested to work with >=0.23.1)
        Numpy <http://www.numpy.org>`_ >= 1.11.1
        requests <http://docs.python-requests.org/en/master/>`_ >= 2.14.2
        lxml <https://pypi.org/project/lxml/>`_ >= 4.5.1

### Execution

Run the script and you will have the final chart in a sub-folder, relative to the script location.
### Final Notes

The file plot output was combined to one plot. This was intentionally done contrary to the instructions to minimze file clutter. I noticed that if the plots aren't assigned to a variable, they are assigned to a global placeholder. This will cause each set of data to plotted on the same chart. I added labels and color coding for clarity.