# Blockchain Twitter Analytics

Hello! Welcome to Rosalyn's Blockchain Twitter Analytics, designed to provide insights into daily blockchain trends and key topics discussed across crypto Twitter utilizing modern data science and engineering tools.

https://rosalyn.observablehq.cloud/rosalyn-analytics/

## Content
- Keywords Dashboard: Reports daily keywords in crypto twitter across the ecosystem.
- Tweets Dashboard: Provides a list of top tweets with high attention.
- Blockchain Dashboard: Reports users and transaction data across blockchain ecosystems. 

## Pipeline
1. Ingests Blockchain Twitter data using APIs
2. Infers keywords and trends using OpenAI LLM
3. Cleans and models data using DBT and Python on BigQuery
4. Creates APIs on Google Cloud Buckets
5. Creates dashboards using Observable

## Next steps
- Convert pipeline into incremental ingestion.
- Automate dag using GitHub Actions workflow or Airflow

## Stacks used
Data Lake/Warehousing: BigQuery, Google Cloud Buckets <br>
Data Modeling: DTB, Python <br>
Data Visualization: Observabl.js, D3.js <br>
APIs: Flipside Crypto, SocialData, OpenAI <br>

# Directory Structure  

      .
      ├── dbt_rosalyn/            # DBT for data modeling using BigQuery
      │   ├── macros/             # Macros 
      │   └── models/             # Models
      │       ├── blockchain/     # Blockchain models   
      │       └── twitter/        # Twitter models
      ├── ingestion/              # Ingestion scripts
      │   ├── blockchain/         # Blockchain data ingestion using Flipside Crypto
      │   │   ├── transactions.py # Transactions ingestion   
      │   │   ├── users.py        # Users ingestion
      │   ├── twitter/            # Twitter data ingestion using SocialData
      │   │   ├── scrape.py       # Ingest with filter configurations
      │   │   ├── clean.py        # Clean raw data
      │   │   └── infer.py        # Infer keywords with OpenAI
      │   └── ingest.py           # Script to run all ingestion processes
      └── observable/             # Visualize in dashboard framework

# Requirements
- Python 3.11+
- Node.js 18+
- DBT Core and BigQuery Adapter
- Google Cloud Libraries and Credentials
- Flipside Crypto SDK
- Observable Framework
- API keys (Flipside crypto, SocialData, and OpenAI)

 
