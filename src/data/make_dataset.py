# -*- coding: utf-8 -*-
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from src.data.home_insurance import Housingdata
from constants import PROJECT_DIR, LOGGING_DIR
from src.utils.logging import configure_logging

logger = logging.getLogger(__name__)
debug = False


def main():
    """Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    """
    configure_logging(LOGGING_DIR / "modelling-data-collation.log", debug, logger)

    logger.info("making final data set from raw data")
    df = Housingdata()._run()
    df.to_csv(Path(PROJECT_DIR / "data/processed/processed_data.csv"))


if __name__ == "__main__":
    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
