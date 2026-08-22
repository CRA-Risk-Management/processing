"""Hydrological predictive models for water level stations."""


def rio_magdalena_tebsa_bquilla(level: float, limit: float = 0.05) -> float:
    """Predict water level for TEBSA station in Barranquilla on Magdalena River.

    Parameters
    ----------
    level : float
        The reference water level.
    limit : float, optional
        Minimum limit for the predicted level, by default 0.05.

    Returns
    -------
    float
        The predicted water level.

    """
    predicted_level = -0.550 + 0.287 * level
    if predicted_level > limit:
        return predicted_level
    return limit


def rio_magdalena_sitio_nuevo(level: float, limit: float = 0.230) -> float:
    """Predict water level for Sitio Nuevo station on Magdalena River.

    Parameters
    ----------
    level : float
        The reference water level.
    limit : float, optional
        Minimum limit for the predicted level, by default 0.230.

    Returns
    -------
    float
        The predicted water level.

    """
    predicted_level = -0.795 + 0.456 * level
    if predicted_level > limit:
        return predicted_level
    return limit


def canal_dique_villa_rosa(level: float, limit: float = 0.10) -> float:
    """Predict water level for Villa Rosa station on Canal del Dique.

    Parameters
    ----------
    level : float
        The reference water level.
    limit : float, optional
        Minimum limit for the predicted level, by default 0.10.

    Returns
    -------
    float
        The predicted water level.

    """
    predicted_level = -0.18 * level + level
    if predicted_level > limit:
        return predicted_level
    return limit
