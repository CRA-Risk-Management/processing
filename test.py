"""Testing snippets."""

import logging
from typing import Final

logger = logging.getLogger(__name__)


SONGS: Final[dict[int, str]] = {
    1: "SKINNY",
    2: "LUNCH",
    3: "CHIHIRO",
    4: "BIRDS OF A FEATHER",
    5: "WILDFLOWER",
    6: "THE GREATEST",
    7: "L'AMOUR DE MA VIE",
    8: "THE DINER",
    9: "BITTERSUITE",
    10: "BLUE",
    11: "HIT ME HARD AND SOFT",
}


def hi(name: str) -> None:
    """Make an special salute.

    Parameters
    ----------
    name: str
        Person name.
    """
    logger.debug("Hello estimated %s, have a good day", name)


def hit_me_hard_and_soft(track_number: int = 4) -> str:
    """Get a song from the best album ever.

    Parameters
    ----------
    track_number : int, optional
        Desired track number, by default 4.

    Returns
    -------
    str
        Song to play.

    """
    logger.debug("Picked song: %s", SONGS[track_number])
    return f"You have to play {SONGS[track_number]}"


if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")
    hit_me_hard_and_soft()
