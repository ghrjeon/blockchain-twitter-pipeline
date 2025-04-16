import requests
import urllib.parse
import time
import json
from datetime import datetime, timedelta
import os
from google.cloud import storage
from google.oauth2 import service_account
from dotenv import load_dotenv

load_dotenv()

bucket_name = "twitter_blobs"
key_path = "../google-keypair.json"

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    # bucket_name = Name of your bucket
    # source_file_name = The path to your file to upload
    # destination_blob_name = name of your destination object

    credentials = service_account.Credentials.from_service_account_file(key_path)
    storage_client = storage.Client(credentials=credentials, project='prototype-451312')

    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )


def save_tweets(tweets, filename):
    # Create 'data' directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    filepath = os.path.join('data', filename)
    # Append to existing file if it exists, otherwise create new
    mode = 'a' if os.path.exists(filepath) else 'w'
    with open(filepath, mode) as f:
        for tweet in tweets:
            json.dump(tweet, f)
            f.write('\n')


def fetch_all_tweets(since_date, until_date, ecosystem, likes):
    # Generate filename with current date
    cursor = None
    page = 1
    filename = f"tweets_{ecosystem}_{since_date}_{until_date}.jsonl"

    encoded_ecosystem = urllib.parse.quote(ecosystem)

    # TWITTER FILTER CONFIGURATIONS 
    query = f"{encoded_ecosystem}%20min_faves%3A{likes}%20until%3A{until_date}%20since%3A{since_date}%20-filter%3Areplies%20-filter%3Aretweets%20-filter%3Aquotes%20lang%3Aen"

    while True:
        print(f"\nFetching page {page}...")
        tweets, cursor = get_tweets(query, cursor)
        
        if tweets:
            source_path = os.path.abspath(os.path.join('data', filename))
            save_tweets(tweets, filename)
            upload_blob(bucket_name, source_path, filename)     
            print(f"Saved {len(tweets)} tweets to {filename}")
            os.remove(source_path)     

        if not cursor:  # No more pages
            print("No more pages to fetch")
            break
            
        page += 1
        time.sleep(1)  # Add delay between requests to respect rate limits

def get_tweets(query, cursor=None):
    # Define the base URL and query parameters
    base_url = "https://api.socialdata.tools/twitter/search"
    
    # Construct URL with parameters
    url = f"{base_url}?query={query}"

    # Add cursor if provided
    if cursor:
        url += f"&cursor={cursor}"

    headers = {
        "Authorization": f"Bearer {os.getenv('SOCIALDATA_API_KEY')}",
        "Accept": "application/json"
    }
    print(url)

    # Make the GET request
    response = requests.get(url, headers=headers)

    # Handle the response
    if response.status_code == 200:
        data = response.json()
        return data.get('tweets', []), data.get('next_cursor')
    else:
        print(f"Error: {response.status_code}")
        return [], None


if __name__ == "__main__":
    # Set the end date and start date
    end_date = datetime.now().date()
    original_start_date = end_date - timedelta(days=7)

    # Configure the number of likes for each ecosystem
    ecosystem_config = {
        "ethereum": 1000,
        "solana": 1000,
        "bitcoin": 2000,
        "defi": 2000,
        "nft": 2000,
        "depin": 700,
    }

    # Loop through each ecosystem and fetch tweets
    for ecosystem, likes in ecosystem_config.items():
        start_date = original_start_date  
        while start_date < end_date:
            next_date = start_date + timedelta(days=1)
            since_date = urllib.parse.quote(start_date.strftime('%Y-%m-%d'))
            until_date = urllib.parse.quote(next_date.strftime('%Y-%m-%d')) 
            print(since_date, until_date)

            fetch_all_tweets(since_date, until_date, ecosystem, likes)
            start_date = next_date 
    