from openai import OpenAI
import os   

from google.cloud import bigquery
from google.oauth2 import service_account
from dotenv import load_dotenv

load_dotenv()

# Replace with your service account file path
key_path = "../google-keypair.json"
# Create credentials and client
credentials = service_account.Credentials.from_service_account_file(key_path)
bq_client = bigquery.Client(credentials=credentials, project='prototype-451312')

# Initialize OpenAI client
ai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


chains = ['ethereum', 'solana', "starknet", "avax",'bitcoin', 'defi', "nft", "depin"]
    
for chain in chains:
    # Example query
    query = f"""
        SELECT date, 
        text
    FROM `prototype-451312.Raw.{chain}_tweets`
    """ 

    # Execute the query
    df = bq_client.query(query).to_dataframe()

    # Group tweets by date
    daily_tweets = df.groupby('date')['text'].apply(list).reset_index()
    daily_tweets['keywords'] = None

    # Infer Keywords
    for index, row in daily_tweets.iterrows():
        date = row['date']
        tweets = row['text']
        
        # Create prompt with tweets
        keywords_prompt = f"""
        Please analyze the following tweets from {date} and identify 5 to 10 non-generic, 
        short keywords or phrases (no longer than three words) that describe the main 
        topics of discussion. 

        Each item must be distinct, avoiding duplicates, and must avoid overly generic 
        terms and topics (e.g., “crypto,” “news”, "blockchain ecosystem", etc.).

        Output exactly 5 to 10 items, separated by commas, with no additional commentary or 
        formatting.
        
        Tweets: {' '.join(tweets)}"""  
        
        completion = ai_client.chat.completions.create(
            model="gpt-4o-mini", 
            messages=[
                {"role": "user", "content": keywords_prompt},
            ]
        )
        
        print(completion.choices[0].message.content)
        
        daily_tweets.at[index, 'keywords'] = completion.choices[0].message.content
        print(f"Processed {date}: {completion.choices[0].message.content}")


    daily_tweets_processed = daily_tweets.drop(columns=['text'])
    
    table_id = f'prototype-451312.Raw.{chain}_keywords'  

    # Create job config
    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE",  # Options: WRITE_TRUNCATE, WRITE_APPEND, WRITE_EMPTY
    )

    try:
        # Load the data into BigQuery
        job = bq_client.load_table_from_dataframe(
            daily_tweets_processed,
            table_id,
            job_config=job_config
        )
        job.result()  

        print(f"Loaded {len(daily_tweets_processed)} rows into {table_id}")
    except Exception as e:
        print(f"Error loading data to BigQuery: {str(e)}")