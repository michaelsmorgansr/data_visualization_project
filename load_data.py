import pandas as pd
from .config import DATA_RAW, RAW_FILENAME

def load_raw() -> pd.DataFrame:
    path = DATA_RAW / RAW_FILENAME
    if not path.exists():
        raise FileNotFoundError(
            f"Missing dataset at {path}. Put the Kaggle CSV in data/raw and name it '{RAW_FILENAME}'."
        )
    return pd.read_csv(path)

def basic_clean(df: pd.DataFrame) -> pd.DataFrame:
    # Standardize column names (optional)
    df = df.copy()
    df.columns = [c.strip() for c in df.columns]
    return df
