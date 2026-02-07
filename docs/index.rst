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


Usage
-----

Installation
~~~~~~~~~~~~

Quant-Kit can be installed using ``pip``:

.. code-block:: bash

   pip install quant-kit


Import
~~~~~~

The recommended import pattern is the following:

.. code-block:: python

   import quant_kit as qt


Roadmap
-------

Metrics module
~~~~~~~~~~~~~~

- ``sharpe_ratio``
- ``sortino_ratio``
- ``calmar_ratio``
- ``omega_ratio``
- ``hit_rate``
- ``period_hit_rate``
- ``skew``
- ``excess_kurtosis``
- ``tracking_error``
- ``information_ratio``


Returns module
~~~~~~~~~~~~~~

- ``cum_returns``
- ``annual_return``
- ``active_return``
- ``aggregate_returns``


Risk module
~~~~~~~~~~~

- ``drawdown``
- ``max_drawdown``
- ``annual_vola``
- ``downside_risk``
- ``upside_risk``
- ``time_underwater``
- ``drawdown_stats``
- ``tail_ratio``


Rolling
~~~~~~~

- ``rolling_metric``
