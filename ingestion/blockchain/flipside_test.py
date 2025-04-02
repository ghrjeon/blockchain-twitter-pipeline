from flipside import Flipside
from google.cloud import bigquery
from google.oauth2 import service_account
import pandas as pd
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# from flipside import Flipside
# flipside_api_key = '19304979-7a77-478d-91c2-75397c86fde9'
# flipside = Flipside(flipside_api_key, "https://api-v2.flipsidecrypto.xyz")
# sql = f"""select platform_name, count(*) as sales_count 
# from ethereum.nft.ez_nft_sales 
# where block_timestamp > current_date - interval '30 days' 
# group by platform_name 
# order by sales_count desc
# limit 8"""
# query_result_set = flipside.query(sql)
# print(query_result_set)


# Load Flipside API Key and Initialize Flipside Client
flipside_api_key = os.getenv('FLIPSIDE_API_KEY')
flipside = Flipside(flipside_api_key, "https://api-v2.flipsidecrypto.xyz")

sql = f"""
select
  platform_name,
  count(*) as sales_count
from ethereum.nft.ez_nft_sales
where block_timestamp > current_date - interval '30 days'
group by platform_name
order by sales_count desc
limit 8
    """

query_result_set = flipside.query(sql)
print(query_result_set)
# data = [{'address': record['address']
#         } for record in query_result_set.records]
# df = pd.DataFrame(data)
# print(df.head())

# print(query_result_set)


# print(df.head())

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