# 🏭 Manufacturing Defect Analysis & Data Visualization

Welcome to my data visualization project focused on **manufacturing defects and operational performance**.  
This project uses a structured manufacturing dataset to explore which process, quality, and operational factors are associated with defective outcomes using **exploratory data analysis (EDA) and visualization techniques**.

The analysis is implemented as a **Jupyter notebook** and emphasizes interpretability and business relevance rather than predictive modeling.

---

## 📊 Project Overview

This project walks through a complete exploratory data analysis workflow:

- Loading and validating a real‑world manufacturing dataset
- Inspecting data structure, distributions, and class balance
- Visualizing defect vs non‑defect outcomes
- Exploring correlations between operational variables
- Comparing key manufacturing metrics by defect status
- Identifying potential drivers of defects through visual analysis

**Goal:**  
Understand how production, quality, maintenance, and operational variables relate to manufacturing defects, and identify areas for potential process improvement.

---

## 🛠 Skills Demonstrated

- Data loading and validation with **Pandas**
- Exploratory data analysis (EDA)
- Correlation analysis and interpretation
- Data visualization with **Matplotlib** and **Seaborn**
- Feature comparison using boxplots and scatterplots
- Clear, reproducible notebook‑based analysis
- Business‑oriented interpretation of technical results

---

## 📁 Dataset

The dataset used in this project is a **manufacturing operations and defect dataset** containing numeric production, quality, maintenance, and efficiency metrics.

### Dataset Characteristics
- Each row represents a manufacturing production instance
- Target variable: **`DefectStatus`**
  - `0` = Non‑defective
  - `1` = Defective
- All feature variables are numeric and continuous

### Key Features Include

- **ProductionVolume**
- **ProductionCost**
- **SupplierQuality**
- **DeliveryDelay**
- **DefectRate**
- **QualityScore**
- **MaintenanceHours**
- **DowntimePercentage**
- **InventoryTurnover**
- **StockoutRate**
- **WorkerProductivity**
- **SafetyIncidents**
- **EnergyConsumption**
- **EnergyEfficiency**
- **AdditiveProcessTime**
- **AdditiveMaterialCost**

The dataset is included directly in the repository and loaded locally by the notebook.

---

## 📈 Visualizations Included

The notebook generates multiple exploratory visualizations, including:

- Defect vs non‑defect class distribution
- Correlation heatmap of manufacturing metrics
- Ranked correlations with defect status
