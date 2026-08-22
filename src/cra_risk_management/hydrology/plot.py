"""Plotting utilities for hydrological data and backwater curves."""

from collections.abc import Sequence

import numpy as np
import pandas as pd
from matplotlib.axes import Axes

from cra_risk_management import constants, validation
from cra_risk_management.hydrology import data, predict


def time_stripe(
    df: pd.DataFrame,
    year: int | None = None,
    ax: Axes | None = None,
) -> Axes:
    """Plot the time stripe of the dataset.

    Parameters
    ----------
    df : pd.DataFrame
        The dataset.
    year : int | None, optional
        The year to plot, by default None.
    ax : Axes | None, optional
        The axes to plot on, by default None.

    Returns
    -------
    Axes
        The axes with the time stripe plotted.

    """
    resolved_ax = validation.check_ax(ax)
    df_prob = data.get_probability_dataset(df, year=year)
    resolved_ax.fill_between(
        df_prob.index,
        df_prob[0.0],
        df_prob[1.0],
        facecolor="C0",
        alpha=0.3,
        label="Variabilidad nivel",
    )
    resolved_ax.fill_between(
        df_prob.index,
        df_prob[0.1],
        df_prob[0.9],
        facecolor="C0",
        alpha=0.3,
    )
    resolved_ax.fill_between(
        df_prob.index,
        df_prob[0.25],
        df_prob[0.75],
        facecolor="C0",
        alpha=0.3,
    )
    resolved_ax.plot(df_prob.index, df_prob[0.5], color="C0")
    resolved_ax.set(xlim=[df_prob.index[0], df_prob.index[-1]])
    resolved_ax.text(
        x=df_prob.index[-1],
        y=df_prob[0.0].iloc[-1],
        s="Min",
        ha="right",
        va="center",
        fontsize="small",
    )
    resolved_ax.text(
        x=df_prob.index[-1],
        y=df_prob[0.1].iloc[-1],
        s="10%",
        ha="right",
        va="center",
        fontsize="small",
    )
    resolved_ax.text(
        x=df_prob.index[-1],
        y=df_prob[0.25].iloc[-1],
        s="25%",
        ha="right",
        va="center",
        fontsize="small",
    )
    resolved_ax.text(
        x=df_prob.index[-1],
        y=df_prob[0.5].iloc[-1],
        s="50%",
        ha="right",
        va="center",
        fontsize="small",
    )
    resolved_ax.text(
        x=df_prob.index[-1],
        y=df_prob[0.75].iloc[-1],
        s="75%",
        ha="right",
        va="center",
        fontsize="small",
    )
    resolved_ax.text(
        x=df_prob.index[-1],
        y=df_prob[0.9].iloc[-1],
        s="90%",
        ha="right",
        va="center",
        fontsize="small",
    )
    resolved_ax.text(
        x=df_prob.index[-1],
        y=df_prob[1.0].iloc[-1],
        s="Max",
        ha="right",
        va="center",
        fontsize="small",
    )
    return resolved_ax


def plot_year(
    df_year: pd.DataFrame,
    ax: Axes | None = None,
    label: str | None = None,
) -> Axes:
    """Plot the year.

    Parameters
    ----------
    df_year : pd.DataFrame
        The dataset.
    ax : Axes | None, optional
        The axes to plot on, by default None.
    label : str | None, optional
        The label to plot, by default None.

    Returns
    -------
    Axes
        The axes with the year plotted.

    """
    resolved_ax = validation.check_ax(ax)
    resolved_ax.plot(df_year["datetime"], df_year["datum"], color="black", label=label)
    return resolved_ax


def add_intakes_to_backwater_plot(
    ax: Axes,
    intakes: Sequence[tuple[str, float]],
) -> Axes:
    """Add intakes to the backwater plot.

    Parameters
    ----------
    ax : Axes
        The axes to plot on.
    intakes : Sequence[tuple[str, float]]
        The intakes to add.

    Returns
    -------
    Axes
        The axes with the intakes added.

    """
    for i, (name, distance) in enumerate(intakes):
        label = None if i != 0 else "Bocatomas"
        ax.axvline(x=distance, color="gray", linestyle="--", linewidth=1, label=label)
        ax.text(
            x=distance,
            y=0.70,
            s=name,
            rotation=90,
            ha="right",
            va="center",
            fontsize="small",
            transform=ax.get_xaxis_transform(),
        )
    return ax


def add_stations_to_backwater_plot(
    ax: Axes,
    stations: Sequence[tuple[str, float]],
) -> Axes:
    """Add stations to the backwater plot.

    Parameters
    ----------
    ax : Axes
        The axes to plot on.
    stations : Sequence[tuple[str, float]]
        The stations to add.

    Returns
    -------
    Axes
        The axes with the stations added.

    """
    x_stations = [x[1] for x in stations]
    ax.scatter(
        x=x_stations,
        y=np.full_like(x_stations, 0.98, dtype=float),
        c="#BA8E23",
        transform=ax.get_xaxis_transform(),
        marker="v",
        label="Estaciones IDEAM",
    )
    for name, distance in stations:
        ax.text(
            x=distance,
            y=0.98,
            s=name,
            ha="center",
            va="bottom",
            fontsize="small",
            transform=ax.get_xaxis_transform(),
        )
    return ax


def add_stripes_to_backwater_plot(
    ax: Axes,
    x: pd.DataFrame,
    x_position: float,
) -> Axes:
    """Add stripes to the backwater plot.

    Parameters
    ----------
    ax : Axes
        The axes to plot on.
    x : pd.DataFrame
        The data to plot.
    x_position : float
        The x position of the stripes.

    Returns
    -------
    Axes
        The axes with the stripes added.

    """
    ax.fill_between(
        x.index,
        x[0.0],
        x[1.0],
        facecolor="C0",
        alpha=0.3,
        label="Variabilidad nivel",
    )
    ax.fill_between(x.index, x[0.1], x[0.9], facecolor="C0", alpha=0.3)
    ax.fill_between(x.index, x[0.25], x[0.75], facecolor="C0", alpha=0.3)
    ax.plot(x.index, x[0.5], color="C0")
    ax.text(
        x=x_position,
        y=x[0.0].iloc[0],
        s="Min",
        ha="left",
        va="center",
        fontsize="small",
    )
    ax.text(
        x=x_position,
        y=x[0.1].iloc[0],
        s="10%",
        ha="left",
        va="center",
        fontsize="small",
    )
    ax.text(
        x=x_position,
        y=x[0.25].iloc[0],
        s="25%",
        ha="left",
        va="center",
        fontsize="small",
    )
    ax.text(
        x=x_position,
        y=x[0.5].iloc[0],
        s="50%",
        ha="left",
        va="center",
        fontsize="small",
    )
    ax.text(
        x=x_position,
        y=x[0.75].iloc[0],
        s="75%",
        ha="left",
        va="center",
        fontsize="small",
    )
    ax.text(
        x=x_position,
        y=x[0.9].iloc[0],
        s="90%",
        ha="left",
        va="center",
        fontsize="small",
    )
    ax.text(
        x=x_position,
        y=x[1.0].iloc[0],
        s="Max",
        ha="left",
        va="center",
        fontsize="small",
    )
    return ax


def magdalena_river_backwater(ax: Axes | None = None) -> Axes:
    """Plot the backwater curve of the Magdalena River.

    Parameters
    ----------
    ax : Axes | None, optional
        The axes to plot on, by default None.

    Returns
    -------
    Axes
        The axes with the backwater curve plotted.

    """
    resolved_ax = validation.check_ax(ax)
    df = data.load_dataset(29037020)
    x = pd.DataFrame(
        {
            109.5: df.quantile(constants.DEFAULT_PERCENTILES)["datum"],
            35.71: df.quantile(constants.DEFAULT_PERCENTILES)["datum"].map(
                predict.rio_magdalena_sitio_nuevo,
            ),
            20.00: df.quantile(constants.DEFAULT_PERCENTILES)["datum"].map(
                predict.rio_magdalena_tebsa_bquilla,
            ),
            0.000: df.quantile(constants.DEFAULT_PERCENTILES)["datum"].map(
                lambda _x: 0,
            ),
        },
    ).T
    t = pd.Series(
        [
            df.sort_values("datetime").iloc[-1]["datum"],
            predict.rio_magdalena_sitio_nuevo(
                df.sort_values("datetime").iloc[-1]["datum"],
            ),
            predict.rio_magdalena_tebsa_bquilla(
                df.sort_values("datetime").iloc[-1]["datum"],
            ),
            0,
        ],
    )
    resolved_ax = add_intakes_to_backwater_plot(
        resolved_ax,
        constants.BOCATOMAS_RIO_MAGDALENA,
    )
    resolved_ax = add_stations_to_backwater_plot(
        resolved_ax,
        constants.ESTACIONES_RIO_MAGDALENA,
    )
    resolved_ax = add_stripes_to_backwater_plot(resolved_ax, x, 109.5)
    resolved_ax.plot(x.index, t, color="black", label="Nivel actual")
    resolved_ax.xaxis.set_inverted(True)
    return resolved_ax


def canal_dique_backwater(ax: Axes | None = None) -> Axes:
    """Plot the backwater curve of the Canal del Dique.

    Parameters
    ----------
    ax : Axes | None, optional
        The axes to plot on, by default None.

    Returns
    -------
    Axes
        The axes with the backwater curve plotted.

    """
    resolved_ax = validation.check_ax(ax)
    df = data.load_dataset(29037020)
    x = pd.DataFrame(
        {
            0.000: df.quantile(constants.DEFAULT_PERCENTILES)["datum"],
            31.30: df.quantile(constants.DEFAULT_PERCENTILES)["datum"].map(
                predict.canal_dique_villa_rosa,
            ),
        },
    ).T
    t = pd.Series(
        [
            df.sort_values("datetime").iloc[-1]["datum"],
            predict.canal_dique_villa_rosa(
                df.sort_values("datetime").iloc[-1]["datum"],
            ),
        ],
    )
    resolved_ax = add_intakes_to_backwater_plot(
        resolved_ax,
        constants.BOCATOMAS_CANAL_DIQUE,
    )
    resolved_ax = add_stations_to_backwater_plot(
        resolved_ax,
        constants.ESTACIONES_CANAL_DIQUE,
    )
    resolved_ax = add_stripes_to_backwater_plot(resolved_ax, x, 0.0)
    resolved_ax.plot(x.index, t, color="black", label="Nivel actual")
    resolved_ax.xaxis.set_inverted(True)
    return resolved_ax
