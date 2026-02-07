Quant-Kit
=========

Welcome!

Quant-Kit is a Python package that provides a collection of widely used
metrics in quantitative finance.

The package is designed to be easy to use and offers high-level functions
that can be seamlessly integrated into your codebase. In addition to
computing performance and risk metrics, Quant-Kit allows you to generate
complete performance reports.

This documentation includes function signatures as well as detailed
explanations of how and why each metric is implemented.


Table of Contents
-----------------

-  `Installation <#installation>`__
-  `Usage <#usage>`__
-  `API <#api>`__
-  `Support <#support>`__
-  `Contributing <#contributing>`__
-  `Documentation <#documentation>`__


Source location
---------------

Hosted on GitHub:
https://github.com/santarsierilorenzo/quant-kit


Installation
------------

::

    pip install quant-kit


Usage
-----

Basic Metrics

.. code-block:: python

   import quant_kit as qt
   import numpy as np
   
   returns = np.array([0.01, 0.02, 0.03, -0.04, -0.06, -0.02])

   qt.sharpe_ratio(returns)
   qt.max_drawdown(returns)


API
---

.. toctree::
   :maxdepth: 2

   api/index


Support
-------

For support, please open an issue on GitHub:

https://github.com/santarsierilorenzo/quant-kit/issues


Contributing
------------

Contributions are welcome. Please follow the standard GitHub workflow:
fork the repository, create a feature branch, add commits, and open a
pull request.


.. toctree::
   :maxdepth: 2
   :caption: Contents


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
