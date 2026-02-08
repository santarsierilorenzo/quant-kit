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

   <div class="cta-row">
     <a class="cta-pill cta-primary" href="getting_started.html">
       <span class="cta-icon">🚀</span>
       <span class="cta-text">Get Started</span>
     </a>

     <a class="cta-pill cta-secondary"
        href="https://github.com/your-org/quant-kit">
       <span class="cta-icon">
         <svg height="20" viewBox="0 0 16 16" width="20"
              aria-hidden="true" fill="currentColor">
           <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54
                    2.29 6.53 5.47 7.59.4.07.55-.17.55-.38
                    0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49
                    -2.69-.94-.09-.23-.48-.94-.82-1.13
                    -.28-.15-.68-.52-.01-.53.63-.01
                    1.08.58 1.23.82.72 1.21 1.87.87
                    2.33.66.07-.52.28-.87.51-1.07
                    -1.78-.2-3.64-.89-3.64-3.95
                    0-.87.31-1.59.82-2.15-.08-.2
                    -.36-1.02.08-2.12 0 0 .67-.21
                    2.2.82a7.62 7.62 0 0 1 2-.27
                    c.68 0 1.36.09 2 .27
                    1.53-1.04 2.2-.82 2.2-.82
                    .44 1.1.16 1.92.08 2.12
                    .51.56.82 1.27.82 2.15
                    0 3.07-1.87 3.75-3.65 3.95
                    .29.25.54.73.54 1.48
                    0 1.07-.01 1.93-.01 2.2
                    0 .21.15.46.55.38A8.013
                    8.013 8.013 0 0 0 16 8
                    c0-4.42-3.58-8-8-8Z"/>
         </svg>
       </span>
       <span class="cta-text">View on GitHub</span>
     </a>
   </div>


Overview
--------

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

   getting_started
   api/index
