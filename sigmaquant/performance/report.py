from __future__ import annotations

from typing import Callable, Iterable, Literal
from datetime import datetime

import pandas as pd
import numpy as np

from ..custom_typing import ArrayLike, Frequency
from ..utils import periods_per_year
from .metrics import (
    calmar_ratio,
    excess_kurtosis,
    hit_rate,
    information_ratio,
    omega_ratio,
    sharpe_ratio,
    skew,
    sortino_ratio,
    tracking_error,
)
from .report_models import Metric, PortfolioReport, Section
from .returns import annual_return, cum_returns
from .risk import (
    annual_vola,
    drawdown_stats,
    downside_risk,
    max_drawdown,
    tail_ratio,
    upside_risk,
)

SeriesKind = Literal["simple", "log", "pnl"]


def ascii_report(
    returns: ArrayLike,
    frequency: Frequency,
    *,
    strategy_name: str = "Portfolio",
    benchmark_returns: Iterable[float] | None = None,
    kind: SeriesKind = "simple",
    starting_value: float = 0.0,
    risk_free: float = 0.0,
    mar: float = 0.0,
    required_return: float = 0.0,
    currency: str = "$",
    width: int = 66,
) -> PortfolioReport:
    """
    Build a structured portfolio report with ASCII rendering support.

    Parameters
    ----------
    returns
        Strategy return or PnL series.
    frequency
        Sampling frequency of the input series.
    strategy_name
        Label shown in the report header.
    benchmark_returns
        Optional benchmark or factor series. When provided, tracking error
        and information ratio are included.
    kind
        Type of the input series. Supported values are ``simple``, ``log``,
        and ``pnl``.
    starting_value
        Starting value passed to cumulative and drawdown computations.
    risk_free
        Per-period risk-free rate used for the Sharpe ratio.
    mar
        Minimum acceptable return used for the Sortino ratio.
    required_return
        Annual required return used for the Omega ratio.
    currency
        Currency symbol used when formatting PnL-based absolute metrics.
    width
        Total line width for the rendered report.

    Returns
    -------
    PortfolioReport
        Structured report object with ASCII rendering helpers.
    """
    values = _to_numpy(returns)
    if values.size == 0:
        raise ValueError("`returns` must contain at least one observation.")

    benchmark = (
        None if benchmark_returns is None else _to_numpy(benchmark_returns)
    )

    if benchmark is not None and benchmark.size != values.size:
        raise ValueError(
            "`benchmark_returns` must have the same length as `returns`."
        )

    if width < 40:
        raise ValueError("`width` must be at least 40.")

    annualization = periods_per_year(frequency)
    header_date = datetime.today().strftime("%Y-%m-%d")
    is_pnl = kind == "pnl"

    format_magnitude = _make_magnitude_formatter(
        is_pnl=is_pnl,
        currency=currency,
    )
    magnitude_unit = "currency" if is_pnl else "percent"

    total_return_value = _total_return(
        returns=returns,
        kind=kind,
        starting_value=starting_value,
    )
    annual_return_value = _annualized_total(
        returns=returns,
        frequency=frequency,
        kind=kind,
    )

    dd_stats = drawdown_stats(
        returns,
        kind=kind,
        starting_value=starting_value,
    )
    max_dd_value = max_drawdown(
        returns,
        kind=kind,
        starting_value=starting_value,
    )

    avg_dd_value = _safe_get_float(dd_stats, "Avg Drawdown")
    max_tuw_value = _safe_get_float(dd_stats, "Max Time Underwater")
    avg_tuw_value = _safe_get_float(dd_stats, "Avg Time Underwater")

    sections: list[Section] = [
        Section(
            title="RETURN METRICS",
            metrics=[
                Metric(
                    name="Total Return",
                    value=format_magnitude(total_return_value),
                    raw_value=total_return_value,
                    unit=magnitude_unit,
                ),
                Metric(
                    name="Annualized Return",
                    value=format_magnitude(annual_return_value),
                    raw_value=annual_return_value,
                    unit=magnitude_unit,
                ),
            ],
        ),
        Section(
            title="RISK METRICS",
            metrics=[
                Metric(
                    name="Annualized Volatility",
                    value=format_magnitude(annual_vola(values, frequency)),
                    raw_value=annual_vola(values, frequency),
                    unit=magnitude_unit,
                ),
                Metric(
                    name="Downside Risk",
                    value=format_magnitude(downside_risk(values)),
                    raw_value=downside_risk(values),
                    unit=magnitude_unit,
                ),
                Metric(
                    name="Upside Risk",
                    value=format_magnitude(upside_risk(values)),
                    raw_value=upside_risk(values),
                    unit=magnitude_unit,
                ),
                Metric(
                    name="Skewness",
                    value=_format_float(skew(values)),
                    raw_value=skew(values),
                    unit="float",
                ),
                Metric(
                    name="Excess Kurtosis",
                    value=_format_float(excess_kurtosis(values)),
                    raw_value=excess_kurtosis(values),
                    unit="float",
                ),
            ],
        ),
        Section(
            title="RISK-ADJUSTED PERFORMANCE",
            metrics=[
                Metric(
                    name="Sharpe Ratio",
                    value=_format_float(
                        sharpe_ratio(
                            values,
                            frequency,
                            risk_free=risk_free,
                        )
                    ),
                    raw_value=sharpe_ratio(
                        values,
                        frequency,
                        risk_free=risk_free,
                    ),
                    unit="float",
                ),
                Metric(
                    name="Sortino Ratio",
                    value=_format_float(
                        sortino_ratio(
                            values,
                            frequency,
                            mar=mar,
                        )
                    ),
                    raw_value=sortino_ratio(
                        values,
                        frequency,
                        mar=mar,
                    ),
                    unit="float",
                ),
                Metric(
                    name="Calmar Ratio",
                    value=_format_float(
                        calmar_ratio(
                            values,
                            frequency,
                            kind=kind,
                        )
                    ),
                    raw_value=calmar_ratio(
                        values,
                        frequency,
                        kind=kind,
                    ),
                    unit="float",
                ),
                Metric(
                    name="Omega Ratio",
                    value=_format_float(
                        omega_ratio(
                            values,
                            required_return,
                            frequency,
                        )
                    ),
                    raw_value=omega_ratio(
                        values,
                        required_return,
                        frequency,
                    ),
                    unit="float",
                ),
            ],
        ),
        Section(
            title="DRAWDOWN ANALYSIS",
            metrics=[
                Metric(
                    name="Maximum Drawdown",
                    value=format_magnitude(max_dd_value),
                    raw_value=max_dd_value,
                    unit=magnitude_unit,
                ),
                Metric(
                    name="Average Drawdown",
                    value=format_magnitude(avg_dd_value),
                    raw_value=avg_dd_value,
                    unit=magnitude_unit,
                ),
                Metric(
                    name="Max Time Underwater",
                    value=_format_periods(max_tuw_value),
                    raw_value=max_tuw_value,
                    unit="periods",
                ),
                Metric(
                    name="Avg Time Underwater",
                    value=_format_periods(avg_tuw_value),
                    raw_value=avg_tuw_value,
                    unit="periods",
                ),
            ],
        ),
        Section(
            title="DISTRIBUTION",
            metrics=[
                Metric(
                    name="Hit Rate",
                    value=_format_percent(hit_rate(values)),
                    raw_value=hit_rate(values),
                    unit="percent",
                ),
                Metric(
                    name="Tail Ratio",
                    value=_format_float(tail_ratio(values)),
                    raw_value=tail_ratio(values),
                    unit="float",
                ),
            ],
        ),
    ]

    if benchmark is not None:
        tracking_error_value = tracking_error(values, benchmark)
        information_ratio_value = information_ratio(values, benchmark)

        risk_adjusted_section = sections[2]
        risk_adjusted_section.metrics.extend(
            [
                Metric(
                    name="Tracking Error",
                    value=format_magnitude(tracking_error_value),
                    raw_value=tracking_error_value,
                    unit=magnitude_unit,
                ),
                Metric(
                    name="Information Ratio",
                    value=_format_float(information_ratio_value),
                    raw_value=information_ratio_value,
                    unit="float",
                ),
            ]
        )

    return PortfolioReport(
        title="PORTFOLIO PERFORMANCE REPORT",
        strategy_name=strategy_name,
        sample_size=values.size,
        date=header_date,
        annualization=annualization,
        sections=sections,
        width=width,
    )


def _to_numpy(values: ArrayLike) -> np.ndarray:
    """Convert an array-like object to a 1D float NumPy array."""
    if isinstance(values, np.ndarray):
        arr = np.asarray(values, dtype=float)
    else:
        arr = np.asarray(list(values), dtype=float)

    arr = np.ravel(arr)
    return arr[~np.isnan(arr)]


def _total_return(
    returns: ArrayLike,
    kind: SeriesKind,
    starting_value: float,
) -> float:
    """Compute the final cumulative value for the input series."""
    cumulative = cum_returns(
        returns,
        kind=kind,
        starting_value=starting_value,
    )
    cumulative_array = np.asarray(cumulative, dtype=float)

    if cumulative_array.size == 0:
        return np.nan

    return float(cumulative_array[-1])


def _annualized_total(
    returns: ArrayLike,
    frequency: Frequency,
    kind: SeriesKind,
) -> float:
    """
    Compute annualized return or annualized PnL.

    For ``simple`` and ``log`` inputs this returns an annualized return.
    For ``pnl`` inputs this returns average annualized PnL.
    """
    values = _to_numpy(returns)
    if values.size == 0:
        return np.nan

    annualization = periods_per_year(frequency)

    if kind == "pnl":
        return float(np.nanmean(values) * annualization)

    return float(annual_return(returns, frequency, kind=kind))


def _make_magnitude_formatter(
    *,
    is_pnl: bool,
    currency: str,
) -> Callable[[float], str]:
    """Create a formatter for percent- or currency-like magnitudes."""
    if is_pnl:
        return lambda value: _format_currency(value, currency)

    return _format_percent


def _safe_get_float(mapping: object, key: str) -> float:
    """Safely extract a float from a dict-like object."""
    if isinstance(mapping, pd.Series):
        return _coerce_float(mapping.get(key, np.nan))

    if isinstance(mapping, dict):
        return _coerce_float(mapping.get(key, np.nan))

    return np.nan


def _coerce_float(value: object) -> float:
    """Convert a generic object to float."""
    try:
        return float(value)
    except (TypeError, ValueError):
        return np.nan


def _format_percent(value: float) -> str:
    """Format a float as percentage."""
    if np.isnan(value):
        return "n/a"

    return f"{value * 100:,.2f} %"


def _format_currency(value: float, currency: str) -> str:
    """Format a float as currency with the symbol on the right."""
    if np.isnan(value):
        return "n/a"

    return f"{value:,.2f}{currency}"


def _format_float(value: float) -> str:
    """Format a generic float."""
    if np.isnan(value):
        return "n/a"

    return f"{value:,.2f}"


def _format_periods(value: float | int) -> str:
    """Format a time-underwater value in periods."""
    value_float = float(value)

    if np.isnan(value_float):
        return "n/a"

    if value_float.is_integer():
        return f"{int(value_float)} periods"

    return f"{value_float:.2f} periods"
