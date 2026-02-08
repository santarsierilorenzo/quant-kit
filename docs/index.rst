.. image:: _static/logo.svg
   :align: right
   :height: 8.5rem


Quant-Kit
=========

A clean, modern Python library for quantitative finance metrics.

Quant-Kit provides a collection of widely used performance and risk metrics
designed for research, backtesting, and portfolio analysis. The API is
high-level, composable, and easy to integrate into existing codebases.

In addition to individual metrics, Quant-Kit emphasizes *clarity* and
*correctness*, offering documentation that explains not only how each metric
is computed, but also why specific design choices were made.


.. raw:: html

   <div class="sd-container-fluid sd-mb-4">
     <div class="sd-row sd-g-3">

       <div class="sd-col sd-col-auto">
         <a class="sd-btn sd-btn-primary sd-rounded-pill"
            href="installation/index.html">
           <span class="bz-emoji">🚀</span>
           Get Started
         </a>
       </div>

       <div class="sd-col sd-col-auto">
         <a class="sd-btn sd-btn-outline-secondary sd-rounded-pill"
            href="https://github.com/santarsierilorenzo/quant-kit">
           <span class="sd-octicon sd-octicon-mark-github"></span>
           View on GitHub
         </a>
       </div>

     </div>
   </div>


Overview
~~~~~~~~

.. grid:: 3
   :gutter: 2

   .. grid-item-card:: 📊 Performance Metrics
      :link: api/returns.html

      Portfolio and strategy performance metrics such as cumulative returns,
      Sharpe ratio, drawdowns, volatility, and related statistics.

   .. grid-item-card:: ⚠️ Risk Analysis
      :link: api/risk.html

      Downside and tail-risk measures, including value-at-risk,
      expected shortfall, and stress-oriented indicators.

   .. grid-item-card:: 🧪 Research Tools
      :link: api/research.html

      Utilities designed for quantitative research workflows, including
      factor analysis helpers and strategy evaluation tools.


.. toctree::
   :hidden:
   :maxdepth: 2

   installation/index
   api/index
