import logging
from pathlib import Path
from constants import PROJECT_DIR, LOGGING_DIR
from src.utils.logging import configure_logging
import pandas as pd
from datetime import datetime

logger = logging.getLogger(__name__)
debug = False


def build_features():
    """Feature engineering scripts

    Args:
        None

    Returns:
        None, CSV written to data folder.
    """
    configure_logging(
        LOGGING_DIR / "modelling-data-feature-engineering.log", debug, logger
    )
    logger.info("Beginning feature engineering!")

    df = pd.read_csv(Path(PROJECT_DIR / "data/interim/cleaned_data.csv"))

    # 4. Create age features
    df["age"] = (
        datetime.strptime("2013-01-01", "%Y-%m-%d")
        - pd.to_datetime(df["P1_DOB"])  # , format="%Y-%m-%d"
    ).dt.days // 365
    df["property_age"] = 2013 - df["YEARBUILT"]
    df["cover_length"] = 2013 - pd.to_datetime(df["COVER_START"]).dt.year

    df.to_csv(Path(PROJECT_DIR / "data/processed/processed_data.csv"))
    logger.info("Feature engineering finished!")

    return None


if __name__ == "__main__":
    try:
        build_features()
    except Exception as ex:
        logger.exception(str(ex))
        print(str(ex))
        raise ex
