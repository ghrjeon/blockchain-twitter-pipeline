from flipside import Flipside
from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Load Flipside API Key and Initialize Flipside Client
flipside_api_key = os.getenv('FLIPSIDE_API_KEY')
flipside = Flipside(flipside_api_key, "https://api-v2.flipsidecrypto.xyz")


# Load Google Credentials and Initialize BigQuery Client
key_path = "../google-keypair.json"
credentials = service_account.Credentials.from_service_account_file(key_path)
client = bigquery.Client(credentials=credentials, project='prototype-451312')


# Map chains to their corresponding user fields
chain_tx = {
    'ethereum': ['from_address','to_address'],
    'base': ['from_address','to_address'],
    'optimism': ['from_address','to_address'],
    'arbitrum': ['from_address','to_address'],
    # 'monad': ['from_address','to_address'],
    # 'polygon': ['from_address','to_address'],
}

# Ingest Data from Flipside
# for chain in chain_tx:
sql = f"""
WITH contracts AS (
    SELECT DISTINCT address FROM optimism.core.dim_contracts
)
select * from contracts
    ORDER BY 1
    """

# Run the query against Flipside's query engine and await the results
query_result_set = flipside.query(sql)
data = [{'address': record['address']
        } for record in query_result_set.records]
# print(query_result_set)

# Convert to DataFrame
df = pd.DataFrame(data)

print(df.head())

    # Define BigQuery Table ID
    # table_id = f'prototype-451312.Raw.{chain}_daily_users'  

    # Define BigQuery Table Schema
    # schema = [
    #     bigquery.SchemaField("date", "TIMESTAMP"),
    #     bigquery.SchemaField("user_count", "INTEGER"),
    # ]

    # # Create BigQuery Load Job Config
    # job_config = bigquery.LoadJobConfig(
    #     schema=schema,
    #     write_disposition="WRITE_TRUNCATE",  # Options: WRITE_TRUNCATE, WRITE_APPEND, WRITE_EMPTY
    # )

    # try:
    #     # Load Data into BigQuery
    #     job = client.load_table_from_dataframe(
    #         df,
    #         table_id,
    #         job_config=job_config
    #     )
    #     job.result()  

    #     print(f"Loaded {len(df)} rows into {table_id}")
    # except Exception as e:
    #     print(f"Error loading data to BigQuery: {str(e)}")