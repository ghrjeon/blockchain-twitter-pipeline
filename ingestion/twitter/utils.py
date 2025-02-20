
from google.oauth2 import service_account
from google.cloud import storage

# Load Google Credentials and Initialize BigQuery Client
key_path = "../google-keypair.json"
credentials = service_account.Credentials.from_service_account_file(key_path)

def read_blob(bucket_name, blob_name):
    """Reads a blob from the specified bucket."""
    # Initialize a storage client
    storage_client = storage.Client().from_service_account_json(key_path)

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
    storage_client = storage.Client().from_service_account_json(key_path)

    # Get the bucket
    bucket = storage_client.bucket(bucket_name)

    # List all blobs in the bucket
    blobs = bucket.list_blobs()

    blob_list = []
    for blob in blobs:
      blob_list.append(blob.name)
    return blob_list

def upload_blob(bucket_name, source_file_name, destination_blob_name):
  # bucket_name = Name of your bucket
  # source_file_name = The path to your file to upload
  # destination_blob_name = name of your destination object
  storage_client = storage.Client().from_service_account_json(key_path)
  bucket = storage_client.bucket(bucket_name)
  blob = bucket.blob(destination_blob_name)

  generation_match_precondition = 1

  blob.upload_from_filename(source_file_name)

  print(
      f"File {source_file_name} uploaded to {destination_blob_name}."
  )