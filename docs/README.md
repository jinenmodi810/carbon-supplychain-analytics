# 🌿 Carbon Supply Chain Analytics

This project demonstrates an end-to-end data engineering pipeline for tracking and analyzing supplier-level carbon emissions in a supply chain. It combines **dbt**, **Snowflake**, and **Streamlit** to build a modern data platform ready for production.

## 📌 Features

- Raw carbon shipment data seeded into Snowflake
- Modular dbt project:
  - staging
  - intermediate
  - mart layers
  - with schema documentation and tests
- Fact table summarizing supplier CO2 emissions
- Streamlit dashboard to visualize:
  - total shipments
  - total CO2 emissions
  - average CO2 per shipment
  - supplier breakdown with sustainability ratings
- Ready to be deployed and orchestrated in dbt Cloud

## 🚀 Tech Stack

- **Snowflake** as the data warehouse
- **dbt Core + dbt Cloud** for transformation and orchestration
- **Streamlit** for front-end data visualization
- GitHub as the version control and collaboration platform

## 🛠️ How to Run Locally

1. Clone the repo
2. Install dependencies in a Python virtual environment
3. Set up your Snowflake profile (`~/.dbt/profiles.yml`)
4. Seed the data:
    ```bash
    dbt seed
    ```
5. Run transformations:
    ```bash
    dbt run
    ```
6. Launch the dashboard:
    ```bash
    streamlit run streamlit_app/app.py
    ```

## 🌐 dbt Cloud Deployment

This project is fully compatible with dbt Cloud:
- Connect your Snowflake account
- Link this GitHub repo
- Schedule production jobs

## 📊 Project Visual
![image](https://github.com/user-attachments/assets/ef2b0df2-5733-477c-8104-ea1b4e5b36ab)



## 👨‍💻 Author

*Built with professional data engineering best practices to showcase a complete analytics workflow.*

---
