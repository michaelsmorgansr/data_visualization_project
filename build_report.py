from .load_data import load_raw, basic_clean
from .features import add_time_index, compute_risk_score, risk_contributors
from .viz import (
    line_defect_rate, scatter_driver, risk_score_trend,
    pareto_contributors, control_chart, save_fig
)

DRIVERS = [
    "SupplierQuality",
    "DeliveryDelay",
    "DowntimePercentage",
    "MaintenanceHours",
    "StockoutRate",
    "WorkerProductivity",
]

def main():
    df = basic_clean(load_raw())

    df = add_time_index(df, start_date="2025-01-01", freq="D")
    df = compute_risk_score(df)

    # Core visuals
    save_fig(line_defect_rate(df), "01_defect_rate_trend")
    save_fig(risk_score_trend(df), "02_risk_score_trend")
    save_fig(control_chart(df, col="DefectRate", window=30), "03_control_chart_defect_rate")

    for i, d in enumerate([x for x in DRIVERS if x in df.columns], start=4):
        save_fig(scatter_driver(df, d), f"{i:02d}_driver_{d.lower()}")

    contrib = risk_contributors(df, top_n=6)
    save_fig(pareto_contributors(contrib), "99_pareto_risk_contributors")

    print("Done. Check reports/figures for outputs.")

if __name__ == "__main__":
    main()
