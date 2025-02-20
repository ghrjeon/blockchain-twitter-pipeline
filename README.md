# Blockchain Twitter Analytics

A Blockchain and Twitter data pipeline that utilizes modern data science and engineering tools.

## Pipeline
1. Ingests Blockchain and Twitter data using APIs
2. Cleans and models data using DBT and Python on BigQuery
3. Creates APIs using DBT and Python on Google Storage Buckets
4. Creates dashboard and visualization using Observable

## Content
- Blockchain Dashboard: Reports users and transaction data across blockchain ecosystems. 
- Keywords Dashboard: Reports daily keywords in crypto twitter across the ecosystem.
- Tweets Dashboard: Provides a list of top tweets with high attention. 

## Next steps
- Convert pipeline into incremental ingestion.
- Automate dag using GitHub Actions workflow or Airflow

## Stacks used
Data Warehousing: BigQuery, Google Cloud Buckets <br>
Data Modeling: DTB, Python <br>
Data Visualization: Observabl.js, D3.js <br>
APIs: Flipside Crypto, SocialData, OpenAI <br>

# Directory Structure  

      .
      ├── dbt_rosalyn/            # DBT for data modeling using BigQuery
      ├── ingestion/              # Ingestion scripts
      │   ├── blockchain/         # Blockchain data ingestion using Flipside Crypto
      │   │   ├── transactions.py # Transactions ingestion   
      │   │   ├── users.py        # Users ingestion
      │   ├── twitter/            # Twitter data ingestion using SocialData
      │   │   ├── scrape.py       # Scrape with filter configurations
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

 
