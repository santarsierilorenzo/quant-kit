from __future__ import annotations

from .utils import periods_per_year, _PANDAS_RULE
from typing import Iterable, Literal, Union
from .typing import ArrayLike, Frequency
import pandas as pd
import numpy as np


def cum_returns(
    returns: ArrayLike,
    kind: Literal["simple", "pnl", "log"] = "simple",
    starting_value: float = 0.0,
) -> ArrayLike:
    """
    Compute cumulative performance over time.

    This function transforms a sequence of returns or profit-and-loss (PnL)
    values into a cumulative performance series. The aggregation method
    depends on the selected ``kind`` parameter.

    Parameters
    ----------
    returns : array-like
        Input sequence of returns or PnL values. The interpretation of the
        input depends on the ``kind`` parameter.

        This is typically a one-dimensional array-like object such as a
        ``numpy.ndarray`` or ``pandas.Series``.

    kind : {"simple", "pnl", "log"}, optional
        Type of input values.

        - ``"simple"``: simple (decimal) returns, compounded multiplicatively
        - ``"log"``: log-returns, aggregated additively
        - ``"pnl"``: additive profit-and-loss values

    starting_value : float, optional
        Initial cumulative level.

    Returns
    -------
    pandas.Series or numpy.ndarray
        Cumulative performance series. The output type matches the input
        type when possible.

      
    Notes
    -----
    For simple returns, cumulative performance is computed using multiplicative
    compounding:

    .. math::

        R_t = \prod_{i=1}^{t} (1 + r_i) - 1

    For log-returns and PnL values, cumulative performance is computed using
    an additive aggregation:

    .. math::

        R_t = \sum_{i=1}^{t} r_i

    Missing values (NaNs) in the input series are treated as zeros prior to
    aggregation.
    """

    if kind not in {"simple", "pnl", "log"}:
        raise ValueError("`kind` must be one of {'simple', 'pnl', 'log'}.")

    if isinstance(returns, pd.Series):
        values = returns.fillna(0.0)
    else:
        values = np.asarray(list(returns), dtype=float)
        values[np.isnan(values)] = 0.0

    if kind == "simple":
        return starting_value + np.cumprod(1.0 + values) - 1.0

    return starting_value + np.cumsum(values)


def annual_return(
    returns: ArrayLike,
    frequency: Frequency,
    kind: Literal["simple", "log", "pnl"] = "simple",
) -> float:
    """
    Compute the annualized performance of a return or PnL series.

    Simple and log returns are annualized using the CAGR.
    PnL values are annualized using the arithmetic mean.

    Parameters
    ----------
    returns : array-like
        Sequence of returns or PnL values.

    frequency : str
        Sampling frequency of the input series.

    kind : {"simple", "log", "pnl"}, optional
        Input type.

    Notes
    -----
    NaN values are treated as zeros.

    Simple returns:

    .. math::

        CAGR = [\prod_{k=1}^{N} (1 + R_k)]^{1 / years} - 1


    """

    if kind not in {"simple", "log", "pnl"}:
        raise ValueError("`kind` must be one of {'simple', 'log', 'pnl'}.")
    
    if not isinstance(returns, (pd.Series, np.ndarray)):
        values = np.asarray(returns)
    else:
        values = returns.copy()

    values[np.isnan(values)] = 0.0

    n_years = len(values) / periods_per_year(frequency)

    if n_years <= 0:
        raise ValueError("Not enough data to annualize.")

    if kind == "simple":
        total_return = np.prod(1.0 + values)
        return total_return ** (1.0 / n_years) - 1.0

    if kind == "log":
        return np.exp(np.sum(values) / n_years) - 1.0

    # kind == "pnl"
    return float(np.sum(values) / n_years)


def active_return(
    returns: Iterable[float],
    factor_returns: Iterable[float],
) -> np.ndarray:
    """
    Compute active returns relative to a benchmark or factor.

    Active returns are defined as the difference between portfolio
    returns and benchmark (or factor) returns.

    Parameters
    ----------
    returns
        Time series of portfolio returns.
    factor_returns
        Time series of benchmark or factor returns. The two series
        must be aligned in time and have the same length.

    Returns
    -------
    numpy.ndarray
        Array of active returns.

    Raises
    ------
    ValueError
        If the input series have different lengths.
    """
    ret_arr = np.asarray(list(returns), dtype=float)
    fac_arr = np.asarray(list(factor_returns), dtype=float)

    if ret_arr.shape[0] != fac_arr.shape[0]:
        raise ValueError(
            "returns and factor_returns must have the same length."
        )

    return ret_arr - fac_arr


def aggregate_returns(
    returns: pd.Series,
    frequency: Frequency = "Y",
    kind = "simple",
) -> pd.Series:
    """
    Aggregate returns or PnL to a target frequency.

    Parameters
    ----------
    returns
        Time series indexed by datetime.
    frequency
        Target aggregation frequency:
        - "D": daily
        - "W": weekly
        - "M": monthly
        - "Y": yearly
    kind
        Type of input values:
        - "simple": compound simple returns
        - "log": additive log-returns
        - "pnl": additive monetary PnL

    Returns
    -------
    pandas.Series
        Aggregated time series.
    """
    if not isinstance(returns, pd.Series):
        raise TypeError("`returns` must be a pandas Series.")

    if kind not in {"simple", "pnl", "log"}:
        raise ValueError("`kind` must be one of {simple, pnl, log}.")

    out = returns.copy()
    out.index = pd.to_datetime(out.index)
    out = out.sort_index().fillna(0.0)

    rule = _PANDAS_RULE[frequency]

    if kind in {"pnl", "log"}:
        return out.resample(rule).sum()

    # simple returns: compound within each period
    return out.resample(rule).apply(
        lambda x: np.prod(1.0 + x) - 1.0
    )
