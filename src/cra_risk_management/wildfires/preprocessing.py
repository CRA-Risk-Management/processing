"""Preprocessing functions for wildfire spatial datasets."""

from pathlib import Path

import geopandas
from prepare_wfs_data import prepare_data


def process_ororatech_data(file_path: Path | str) -> geopandas.GeoDataFrame:
    """Prepare OroraTech Wildfire Solutions data.

    Parameters
    ----------
    file_path : Path | str
        Path to the spatial file to process.

    Returns
    -------
    gpd.GeoDataFrame
        Processed wildfire GeoDataFrame.

    """
    gdf = geopandas.read_file(file_path)
    return prepare_data(gdf)
