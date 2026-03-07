from typing import Optional, Dict, Any, List, Iterable
from dataclasses import dataclass, field
from statsmodels.stats import diagnostic
import numpy as np


@dataclass(frozen=True)
class AutocorrelationTest:
    """
    Container for autocorrelation diagnostic test results.

    Parameters
    ----------
    test_name : str
        Name of the statistical test.
    statistic : float | List[float] | None
        Value(s) of the test statistic. Some tests return one value per lag.
    p_value : float | List[float] | None
        P-value(s) associated with the test statistic.
    reject : bool
        True if the null hypothesis of no autocorrelation is rejected at the
        chosen significance level.
    info : dict[str, Any]
        Additional diagnostic information (e.g. number of lags used,
        degrees of freedom, sample size).
    """
    test_name: str
    statistic: Optional[float | List[float]]
    p_value: Optional[float | List[float]]
    reject: bool
    info: Dict[str, Any] = field(default_factory=dict)


def ljung_box(
    values: Iterable[float],
    lags: int | None = None,
    boxpierce: bool = False,
    model_df: int = 0,
    epsilon: float = 0.05
) -> AutocorrelationTest:
    """
    Ljung-Box (or Box-Pierce) test for autocorrelation.

    The test evaluates the joint null hypothesis that autocorrelations up to
    a specified lag are equal to zero.

    H0: rho_1 = rho_2 = ... = rho_k = 0
    H1: at least one rho_i != 0

    Parameters
    ----------
    values : Iterable[float]
        Time series observations.
    lags : int | None, default None
        Number of lags included in the test. If None, a default value
        proportional to log(sample_size) is used.
    boxpierce : bool, default False
        If True, compute the Box-Pierce statistic instead of Ljung-Box.
    model_df : int, default 0
        Number of parameters estimated in the model whose residuals are
        being tested. This adjusts the degrees of freedom of the test.
    epsilon : float, default 0.05
        Significance level used for the rejection decision.

    Returns
    -------
    AutocorrelationTest
        Structured container with statistic values, p-values, and the
        rejection decision.

    Notes
    -----
    The Ljung-Box statistic is

        Q = T (T + 2) * sum_{k=1}^h rho_k^2 / (T - k)

    which asymptotically follows a chi-square distribution with
    (h - model_df) degrees of freedom.
    """

    values = np.asarray(values)
    n = len(values)

    if lags is None:
        lags = int(np.log(n))

    test_name = "box_pierce" if boxpierce else "ljung_box"

    results = diagnostic.acorr_ljungbox(
        values,
        lags=lags,
        boxpierce=boxpierce,
        model_df=model_df
    )

    stat_key = "bp_stat" if boxpierce else "lb_stat"
    pval_key = "bp_pvalue" if boxpierce else "lb_pvalue"

    stat = np.asarray(results[stat_key])
    pval = np.asarray(results[pval_key])

    return AutocorrelationTest(
        test_name=test_name,
        statistic=stat.tolist(),
        p_value=pval.tolist(),
        reject=bool(np.any(pval <= epsilon)),
        info={"lags": lags, "model_df": model_df}
    )
