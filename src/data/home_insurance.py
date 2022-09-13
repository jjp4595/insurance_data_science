import pandas as pd
import numpy as np
import logging
from constants import PROJECT_DIR
from src.utils.decorators import log_time

logger = logging.getLogger(__name__)


class Housingdata:
    def _run(self) -> "pd.DataFrame":
        return self._load().pipe(self._clean)

    def _load(self) -> "pd.DataFrame":
        df = pd.read_csv(PROJECT_DIR / "data/raw/home_insurance.csv", header=0)
        return df

    @log_time
    def _clean(self, df: "pd.DataFrame") -> "pd.DataFrame":
        """Prepare the input data for training

        Args:
            df (pd.DataFrame): raw data

        # TODO

        Returns:
            Clean dataset
        """

        # Missing values
        df = df[df["POL_STATUS"].notnull()]

        # Clean target variable
        df = df[df["POL_STATUS"] != "Unknown"]
        df["lapse"] = np.where(df["POL_STATUS"] == "Lapsed", 1, 0)

        # Create dummy variables for categorical variables (one hot encode)
        categorical_cols = [
            "CLAIM3YEARS",
            "BUS_USE",
            "AD_BUILDINGS",
            "APPR_ALARM",
            "CONTENTS_COVER",
            "P1_SEX",
            "BUILDINGS_COVER",
            "P1_POLICY_REFUSED",
            "APPR_LOCKS",
            "FLOODING",
            "NEIGH_WATCH",
            "SAFE_INSTALLED",
            "SEC_DISC_REQ",
            "SUBSIDENCE",
            "LEGAL_ADDON_POST_REN",
            "HOME_EM_ADDON_PRE_REN",
            "HOME_EM_ADDON_POST_REN",
            "GARDEN_ADDON_PRE_REN",
            "GARDEN_ADDON_POST_REN",
            "KEYCARE_ADDON_PRE_REN",
            "KEYCARE_ADDON_POST_REN",
            "HP1_ADDON_PRE_REN",
            "HP1_ADDON_POST_REN",
            "HP2_ADDON_PRE_REN",
            "HP2_ADDON_POST_REN",
            "HP3_ADDON_PRE_REN",
            "HP3_ADDON_POST_REN",
            "MTA_FLAG",
            "OCC_STATUS",
            "OWNERSHIP_TYPE",
            "PROP_TYPE",
            "PAYMENT_METHOD",
            "P1_EMP_STATUS",
            "P1_MAR_STATUS",
        ]

        for col in categorical_cols:
            dummies = pd.get_dummies(df[col], drop_first=True, prefix=col)
            df = pd.concat([df, dummies], 1)

        # Impute missing value
        df["RISK_RATED_AREA_B_imputed"] = df["RISK_RATED_AREA_B"].fillna(
            df["RISK_RATED_AREA_B"].mean()
        )
        df["RISK_RATED_AREA_C_imputed"] = df["RISK_RATED_AREA_C"].fillna(
            df["RISK_RATED_AREA_C"].mean()
        )
        df["MTA_FAP_imputed"] = df["MTA_FAP"].fillna(0)
        df["MTA_APRP_imputed"] = df["MTA_APRP"].fillna(0)
        return df
