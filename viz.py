import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from .config import FIGURES

def ensure_dirs():
    FIGURES.mkdir(parents=True, exist_ok=True)

def line_defect_rate(df: pd.DataFrame):
    fig = px.line(df, x="Date", y="DefectRate", color="DefectStatus",
                  title="Defect Rate Over Time (colored by Defect Status)")
    return fig

def scatter_driver(df: pd.DataFrame, x: str, y="DefectRate"):
    fig = px.scatter(df, x=x, y=y, color="DefectStatus",
                     trendline="ols",
                     title=f"{y} vs {x}")
    return fig

def risk_score_trend(df: pd.DataFrame):
    fig = px.line(df, x="Date", y="RiskScore", color="RiskBucket",
                  title="Composite Risk Score Over Time")
    return fig

def pareto_contributors(contrib_df: pd.DataFrame):
    fig = go.Figure()
    fig.add_bar(x=contrib_df["Feature"], y=contrib_df["Count"], name="Count")
    fig.add_scatter(x=contrib_df["Feature"], y=contrib_df["CumulativePct"],
                    name="Cumulative %", yaxis="y2")
    fig.update_layout(
        title="Pareto: Most Frequent Risk Contributors",
        yaxis=dict(title="Count"),
        yaxis2=dict(title="Cumulative %", overlaying="y", side="right", tickformat=".0%"),
        xaxis=dict(tickangle=-30),
        legend=dict(orientation="h")
    )
    return fig

def control_chart(df: pd.DataFrame, col="DefectRate", window=30):
    # Rolling mean and sigma bands (simple SPC-style visualization)
    s = df[col]
    mean = s.rolling(window).mean()
    sigma = s.rolling(window).std()
    ucl = mean + 3 * sigma
    lcl = mean - 3 * sigma

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df["Date"], y=s, mode="lines", name=col))
    fig.add_trace(go.Scatter(x=df["Date"], y=mean, mode="lines", name="Rolling Mean"))
    fig.add_trace(go.Scatter(x=df["Date"], y=ucl, mode="lines", name="UCL (+3σ)", line=dict(dash="dash")))
    fig.add_trace(go.Scatter(x=df["Date"], y=lcl, mode="lines", name="LCL (-3σ)", line=dict(dash="dash")))
    fig.update_layout(title=f"Control Chart (Rolling) for {col}")
    return fig

def save_fig(fig, filename: str):
    ensure_dirs()
    out = FIGURES / filename
    fig.write_image(str(out.with_suffix(".png")), scale=2)
    fig.write_html(str(out.with_suffix(".html")))
