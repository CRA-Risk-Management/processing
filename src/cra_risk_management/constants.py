"""Constants for CRA Risk Management."""

from collections.abc import Sequence
from typing import Final

# TODO(me): SDK to fetch data for Python # ruff: ignore [missing-todo-link]
API_URL: Final[str] = "https://api-791856053294.us-central1.run.app"
DEFAULT_PERCENTILES: Final[Sequence[float]] = (0.0, 0.1, 0.25, 0.5, 0.75, 0.9, 1.0)

BOCATOMAS_RIO_MAGDALENA: Final[list[tuple[str, float]]] = [
    ("Calamar", 109.500),
    ("Suan", 101.340),
    ("Campo De La Cruz", 97.300),
    ("Ponedera", 60.860),
    ("Sabanagrande", 39.480),
    ("Malambo", 35.710),
    ("Galapa", 31.980),
    ("Barranquilla/Soledad", 21.860),
    ("Barranquilla Norte", 11.583),
    ("Puerto Colombia", 7.160),
    ("Bocas de Ceniza", 0.0),
]
BOCATOMAS_RÍO_MAGDALENA = BOCATOMAS_RIO_MAGDALENA  # ruff: ignore [non-ascii-name]

BOCATOMAS_CANAL_DIQUE: Final[list[tuple[str, float]]] = [
    ("Calamar", 0.0),
    ("Santa Lucía", 8.760),
    ("Manatí", 18.310),
    ("Compuertas", 25.300),
    ("Repelón", 30.710),
    ("Villa Rosa", 31.300),
]

ESTACIONES_RIO_MAGDALENA: Final[list[tuple[str, float]]] = [
    ("CALAMAR", 109.5),
    ("SITIO NUEVO", 35.71),
    ("TEBSA", 20.00),
]
ESTACIONES_RÍO_MAGDALENA = ESTACIONES_RIO_MAGDALENA  # ruff: ignore [non-ascii-name]

ESTACIONES_CANAL_DIQUE: Final[list[tuple[str, float]]] = [
    ("CALAMAR", 0.0),
]
