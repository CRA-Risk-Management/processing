"""Hydrological data fetching and processing utilities."""

from collections.abc import Sequence
from http import HTTPStatus
from typing import Final

import pandas as pd
import requests

from cra_risk_management.constants import API_URL, DEFAULT_PERCENTILES
from cra_risk_management.validation import (
    check_df_integrity,
    check_year,
    remove_feb_29th,
)

DEFAULT_TIMEOUT: Final[int] = 30
FEB_MONTH: Final[int] = 2
FEB_LEAP_DAY: Final[int] = 29
DAYS_IN_COMMON_YEAR: Final[int] = 365


def load_dataset(station_id: int) -> pd.DataFrame:
    """Load the dataset for a given station ID.

    Parameters
    ----------
    station_id : int
        The ID of the station.

    Returns
    -------
    pd.DataFrame
        The dataset for the given station ID.

    Raises
    ------
    RuntimeError
        If the API response status code is not 200 OK.

    """
    url = f"{API_URL}/hidrometorological/datasets/{station_id}"
    response = requests.get(url, timeout=DEFAULT_TIMEOUT)
    if response.status_code != HTTPStatus.OK:
        msg = f"Failed to fetch dataset for station {station_id}: {response.text}"
        raise RuntimeError(msg)
    df = pd.DataFrame.from_records(response.json()).set_index("id")
    df.index.name = None
    df["datetime"] = pd.to_datetime(df["datetime"])
    return df


def get_dataset_year(df: pd.DataFrame, year: int | None = None) -> pd.DataFrame:
    """Get the dataset for a given year.

    Parameters
    ----------
    df : pd.DataFrame
        The dataset for the given station ID.
    year : int | None, optional
        The year to get the dataset for, by default None.

    Returns
    -------
    pd.DataFrame
        The dataset for the given year with leap days removed.

    """
    year_val = check_year(year)
    df_copy = df.copy()
    df_copy = check_df_integrity(df_copy)
    df_copy = df_copy.loc[
        (df_copy["datetime"] >= f"{year_val}-01-01") & (df_copy["datetime"] <= f"{year_val}-12-31")
    ].copy()
    return remove_feb_29th(df_copy)


def get_probability_dataset(
    df: pd.DataFrame,
    year: int | None = None,
    percentiles: Sequence[float] = DEFAULT_PERCENTILES,
) -> pd.DataFrame:
    """Get the probability dataset for a given year.

    Parameters
    ----------
    df : pd.DataFrame
        The dataset for the given station ID.
    year : int | None, optional
        The year to get the dataset for, by default None.
    percentiles : Sequence[float], optional
        The percentiles to get the dataset for, by default DEFAULT_PERCENTILES.

    Returns
    -------
    pd.DataFrame
        The probability dataset for the given year.

    """
    year_val = check_year(year)
    df_copy = df.copy()
    df_copy = check_df_integrity(df_copy)
    df_copy["month"], df_copy["day"] = (
        df_copy["datetime"].dt.month,
        df_copy["datetime"].dt.day,
    )
    df_copy = df_copy.loc[~((df_copy["month"] == FEB_MONTH) & (df_copy["day"] == FEB_LEAP_DAY))]
    df_quantiles = df_copy.groupby(["month", "day"])["datum"].quantile(percentiles).unstack().reset_index()  # ruff: ignore[pandas-use-of-dot-pivot-or-unstack]
    df_quantiles = df_quantiles.drop(columns=["month", "day"])
    idx = pd.date_range(f"{year_val}-01-01", f"{year_val}-12-31", freq="D")
    if len(idx) > DAYS_IN_COMMON_YEAR:
        idx = idx.drop([f"{year_val}-02-29"])
    return df_quantiles.set_index(idx)
