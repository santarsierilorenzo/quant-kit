Installation
=============
Quant-Kit can be installed using ``pip``:

.. code-block:: bash

   pip install quant-kit

Import
~~~~~~~~~~~~~~~~~~~~
The recommended import pattern is the following:

.. code-block:: python

   import sigmaquant as qt

For subpackage-oriented imports:

.. code-block:: python

   from sigmaquant.performance import sharpe_ratio, drawdown
   from sigmaquant.research.autocorr import ljung_box

Example
~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import sigmaquant as qt

   returns = np.array([0.2, 0.3, -0.5, 0.7, 0.2, 0.1, -0.7])

   qt.sharpe_ratio(
       returns,
       frequency="D",
   )

.. toctree::
   :maxdepth: 1
