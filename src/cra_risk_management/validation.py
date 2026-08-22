"""Validation and preprocessing helper functions."""

import datetime
import zoneinfo
from typing import Final

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.axes import Axes

TZ: Final[zoneinfo.ZoneInfo] = zoneinfo.ZoneInfo(key="America/Bogota")
MONTH_TO_DELETE: Final[int] = 2
DAY_TO_DELETE: Final[int] = 29

tz: zoneinfo.ZoneInfo = TZ
month_to_delete: int = MONTH_TO_DELETE
day_to_delete: int = DAY_TO_DELETE


def check_year(year: int | None) -> int:
    """Check and resolve the reference year.

    Parameters
    ----------
    year : int | None
        The input year, or None to use the current year in Colombian timezone.

    Returns
    -------
    int
        The resolved year.

    """
    if year is None:
        return datetime.datetime.now(tz=TZ).year
    return year


def check_df_integrity(df: pd.DataFrame) -> pd.DataFrame:
    """Check the integrity of the dataset.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to validate.

    Returns
    -------
    pd.DataFrame
        The validated DataFrame.

    Raises
    ------
    ValueError
        If neither 'datetime' nor 'datum' columns exist in the DataFrame.

    """
    if "datetime" not in df.columns and "datum" not in df.columns:
        msg = "'datetime' and 'datum' columns weren't encountered"
        raise ValueError(msg)
    return df


def remove_feb_29th(df: pd.DataFrame) -> pd.DataFrame:
    """Remove the 29th of February from the dataset.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing a 'datetime' column.

    Returns
    -------
    pd.DataFrame
        The DataFrame with February 29th rows removed.

    """
    return df.loc[
        ~(
            (df["datetime"].dt.month == MONTH_TO_DELETE)
            & (df["datetime"].dt.day == DAY_TO_DELETE)
        )
    ].copy()


def check_ax(ax: Axes | None) -> Axes:
    """Check and resolve matplotlib Axes.

    Parameters
    ----------
    ax : Axes | None
        Matplotlib Axes to check, or None to create a new subplot.

    Returns
    -------
    Axes
        The resolved Axes.

    """
    if ax is None:
        _, new_ax = plt.subplots()
        return new_ax
    return ax
