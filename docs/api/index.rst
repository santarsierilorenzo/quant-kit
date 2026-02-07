API Reference
====================================
The API expose the majority of functions that can be used in quant-kit, so for
the majority of use cases you don't need to import functions referring to
submodules. In this page you'll find the method exposed to the API.


**Roadmap**

Returns module
~~~~~~~~~~~~~~
- ``cum_returns``
- ``annual_return``
- ``active_return``
- ``aggregate_returns``

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

.. toctree::
   :maxdepth: 2

   api/index
