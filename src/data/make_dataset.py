# -*- coding: utf-8 -*-
import logging
from pathlib import Path
from src.data.home_insurance import Housingdata
from constants import PROJECT_DIR, LOGGING_DIR
from src.utils.logging import configure_logging

logger = logging.getLogger(__name__)
debug = False


def build_dataset():
    """Runs data pre-processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../interim).
    """
    configure_logging(LOGGING_DIR / "modelling-data-collation.log", debug, logger)

    logger.info("Beginning data pre-processing")
    df = Housingdata()._run()
    df.to_csv(Path(PROJECT_DIR / "data/interim/cleaned_data.csv"))
    logger.info("Data pre-processing finished")
    return None


if __name__ == "__main__":
    try:
        build_dataset()
    except Exception as ex:
        logger.exception(str(ex))
        print(str(ex))
        raise ex
