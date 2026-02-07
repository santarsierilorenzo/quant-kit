Welcome to Quant-Kit's documentation!
====================================
Quant-Kit is a Python package that provides a collection of widely used
metrics in quantitative finance.

The package is designed to be easy to use and offers high-level functions
that can be seamlessly integrated into your codebase. In addition to
computing performance and risk metrics, Quant-Kit allows you to generate
complete performance reports.

This documentation includes function signatures as well as detailed
explanations of how and why each metric is implemented.

Installation
------------
Quant-Kit can be installed using ``pip``:

.. code-block:: bash

   pip install quant-kit

Import
~~~~~~~~~~~~~~~~~~~~
The recommended import pattern is the following:

.. code-block:: python

   import quant_kit as qt

Example
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import quant_kit as qt

   returns = np.array([0.2, 0.3, -0.5, 0.7, 0.2, 0.1, -0.7])

   qt.sharpe_ratio(
       returns,
       frequency="D",
   )


.. toctree::
   :maxdepth: 2
   :hidden:

   api/index
