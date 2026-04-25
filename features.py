import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

RISK_FEATURES = [
    "DowntimePercentage",
    "DeliveryDelay",
    "StockoutRate",
    "SafetyIncidents",
    "MaintenanceHours",
    "EnergyConsumption",
]

INVERT_FEATURES = [
    "SupplierQuality",
    "WorkerProductivity",
    "QualityScore",
    "EnergyEfficiency",
]

def add_time_index(df: pd.DataFrame, start_date="2025-01-01", freq="D") -> pd.DataFrame:
    """
    Dataset likely has no time column. We create a deterministic pseudo-time index
    so we can visualize trends. This is a portfolio project, not a regulated record.
    """
    df = df.copy()
    dates = pd.date_range(start=start_date, periods=len(df), freq=freq)
    df["Date"] = dates
    df["Week"] = df["Date"].dt.to_period("W").astype(str)
    df["Month"] = df["Date"].dt.to_period("M").astype(str)
    return df

def compute_risk_score(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Ensure features exist
    missing = [c for c in (RISK_FEATURES + INVERT_FEATURES) if c not in df.columns]
    if missing:
        # Keep going gracefully: compute risk score with whatever is present
        present_risk = [c for c in RISK_FEATURES if c in df.columns]
        present_inv = [c for c in INVERT_FEATURES if c in df.columns]
    else:
        present_risk = RISK_FEATURES
        present_inv = INVERT_FEATURES

    # Build matrix: "risk up" features positive; "good" features inverted so that low quality increases risk
    cols = present_risk + present_inv
    X = df[cols].copy()

    # Invert good features: lower values -> higher risk
    for c in present_inv:
        X[c] = -X[c]

    # Standardize
    scaler = StandardScaler()
    Z = scaler.fit_transform(X)

    # Weighted sum (simple, explainable; can refine later)
    weights = np.ones(Z.shape[1])
    risk = (Z * weights).sum(axis=1) / weights.sum()

    df["RiskScore"] = risk

    # Buckets for clean viz
    df["RiskBucket"] = pd.qcut(df["RiskScore"], q=3, labels=["Low", "Medium", "High"])

    return df

def risk_contributors(df: pd.DataFrame, top_n=6) -> pd.DataFrame:
    """
    Identify which features most often contribute to high risk (by absolute z-score).
    """
    df = df.copy()
    cols = [c for c in (RISK_FEATURES + INVERT_FEATURES) if c in df.columns]
    X = df[cols].copy()
    for c in [c for c in INVERT_FEATURES if c in X.columns]:
        X[c] = -X[c]

    Z = (X - X.mean()) / X.std(ddof=0)
    # For each row, rank absolute contributions
    absZ = Z.abs()
    top = absZ.apply(lambda row: row.nlargest(top_n).index.tolist(), axis=1)
    exploded = top.explode().value_counts().reset_index()
    exploded.columns = ["Feature", "Count"]
    exploded["CumulativePct"] = exploded["Count"].cumsum() / exploded["Count"].sum()
    return exploded
