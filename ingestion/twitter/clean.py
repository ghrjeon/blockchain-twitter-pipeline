import os
import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud import storage

bucket_name = "twitter_blobs"
key_path = "../google-keypair.json"

def read_blob(bucket_name, blob_name):
    """Reads a blob from the specified bucket."""
    # Initialize a storage client
    credentials = service_account.Credentials.from_service_account_file(key_path)
    storage_client = storage.Client(credentials=credentials, project='prototype-451312')
    # Get the bucket
    bucket = storage_client.bucket(bucket_name)
    # Get the blob
    blob = bucket.blob(blob_name)
    # Download the blob as a string
    content = blob.download_as_text(encoding='utf-8')

    return content
def list_blobs(bucket_name):
    """Lists all the blobs in the specified bucket."""
    # Initialize a storage client
    credentials = service_account.Credentials.from_service_account_file(key_path)
    storage_client = storage.Client(credentials=credentials, project='prototype-451312')
    # Get the bucket
    bucket = storage_client.bucket(bucket_name)
    # List all blobs in the bucket
    blobs = bucket.list_blobs()
    blob_list = []
    for blob in blobs:
      blob_list.append(blob.name)
    return blob_list

# Create credentials and client
credentials = service_account.Credentials.from_service_account_file(key_path)
client = bigquery.Client(credentials=credentials, project='prototype-451312')


chains = ['ethereum', 'solana', "starknet", "avax",'bitcoin', 'defi', "nft","depin"]

for chain in chains:
    df_all = pd.DataFrame()

    # Read all blobs for the chain and concatenate them
    blobs = list_blobs(bucket_name)
    for blob in blobs:
        if chain in blob.lower():
            content = read_blob(bucket_name, blob)
            df = pd.read_json(content, lines=True)
            df_all = pd.concat([df_all, df])

            df_processed = pd.DataFrame({
                'date': df_all['tweet_created_at'].dt.date,
                'id': df_all['id'],
                'text': df_all['full_text'],
                'user_id': df_all['user'].apply(lambda x: x['id']),
                'user_name': df_all['user'].apply(lambda x: x['name']),
                'user_screen_name': df_all['user'].apply(lambda x: x['screen_name']),
                'user_followers_count': df_all['user'].apply(lambda x: x['followers_count']),
                'favorite_count': df_all['favorite_count'],
                'views_count': df_all['views_count'],
                'bookmark_count': df_all['bookmark_count'],
                'reply_count': df_all['reply_count'],
                'retweet_count': df_all['retweet_count'],
                'quote_count': df_all['quote_count'],
                'lang': df_all['lang'],
            })
            print(df_processed.head())

            table_id = f'prototype-451312.Raw.{chain}_tweets'  

            # Create job config
            job_config = bigquery.LoadJobConfig(
                write_disposition="WRITE_TRUNCATE",  # Options: WRITE_TRUNCATE, WRITE_APPEND, WRITE_EMPTY
            )

            try:
                # Load the data into BigQuery
                job = client.load_table_from_dataframe(
                    df_processed,
                    table_id,
                    job_config=job_config
                )
                job.result()  

                print(f"Loaded {len(df_processed)} rows into {table_id}")
            except Exception as e:
                print(f"Error loading data to BigQuery: {str(e)}")