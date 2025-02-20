from google.cloud import bigquery
from google.oauth2 import service_account

# Replace with your service account file path
key_path = "/Users/gahyejeon/Documents/aiPrograms/prototype/prototype-451312-849e49cb3136.json"

# Create credentials and client
credentials = service_account.Credentials.from_service_account_file(key_path)
client = bigquery.Client(credentials=credentials, project='prototype-451312')

# Try to list datasets
try:
    datasets = list(client.list_datasets())
    print("Datasets:")
    for dataset in datasets:
        print(f"- {dataset.dataset_id}")
except Exception as e:
    print(f"Error: {e}")