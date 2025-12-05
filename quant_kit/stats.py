from typing import Iterable
import numpy as np


def sharpe_ratio(
    returns: Iterable[float],
    period: str = "daily",
    annualize: bool = True,
    risk_free: float = 0.0,
) -> float:
    """
    Compute the Sharpe ratio for a series of returns.

    Parameters
    ----------
    returns : Iterable[float]
        Sequence of returns.
    period : str
        Frequency of returns: "daily", "weekly", or "monthly".
    annualize : bool
        If True, scale the Sharpe ratio to annual frequency.
    risk_free : float
        Risk-free rate per period (same frequency as `returns`).

    Returns
    -------
    float
        Sharpe ratio.
    """
    ret_arr = np.array(returns, dtype=float)
    mean = ret_arr.mean() - risk_free
    std = ret_arr.std(ddof=1)

    if std == 0:
        raise ValueError("Standard deviation is zero.")

    if period == "daily":
        periods = 252
    elif period == "weekly":
        periods = 52
    elif period == "monthly":
        periods = 12
    else:
        raise ValueError(f"Unsupported period: {period}")

    scale = np.sqrt(periods) if annualize else 1.0

    return mean / std * scale
