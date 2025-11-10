# Healthcare Patient Analytics Pipeline (Azure End-to-End)

## Project Overview
This project demonstrates a complete Azure data engineering workflow for healthcare analytics. Patient admission data is ingested, processed, warehoused, analyzed, and visualized, mimicking a typical use case for hospitals and insurance.

### Workflow Steps
1. **Data Ingestion**: Azure Data Factory imports raw CSV patient records from Azure Blob Storage.
2. **Processing**: Azure Databricks (PySpark notebook) cleans, transforms, and aggregates patient metrics.
3. **Warehousing**: Data stored in Azure SQL Data Warehouse using star schema for admissions, diagnoses, and billing.
4. **Cost Monitoring**: Azure Cost Management APIs track cloud spend during the pipeline.
5. **Visualization**: Power BI dashboard built over warehouse data for reporting (admissions, cost, disease prevalence).

## Repo Structure
- `/data/`: Sample data files (CSV, anonymized patient admissions)
- `/notebooks/`: Databricks PySpark notebook with code and comments
- `/sql/`: Data warehouse schema (DDL, example queries)
- `/ADF/`: Azure Data Factory pipeline JSON templates & README
- `/cost-monitoring/`: Cost analysis scripts/notebooks
- `/PowerBI/`: Instructions for building dashboards and sample PBIX files
- `/docs/`: Architecture diagram and process workflow images
- README.md: Project documentation

## Setup Instructions
1. Clone repo, set up Azure resources (minimal tier for cost control)
2. Load sample data to Blob Storage
3. Deploy ADF pipeline (see /ADF/README.md)
4. Run Databricks notebook (/notebooks/patient_etl_demo.ipynb) for transformations
5. Load processed data to Data Warehouse (run /sql/DDL.sql)
6. Use cost-monitoring notebook/script for spend tracking
7. Build Power BI dashboard, connect to warehouse

## Workflow Diagram
See `/docs/azure_healthcare_etl_flow.png`

## Learning Focus
- Clean, modular, commented code
- Cloud resources cost control
- Step-by-step guidance for beginners

---

For any issues or contributions, fork the repo and open a PR.
