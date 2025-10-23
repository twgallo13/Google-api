from __future__ import annotations
import os
from google.cloud import storage

def list_buckets():
    client = storage.Client()
    buckets = [b.name for b in client.list_buckets()]
    print("Buckets:", buckets)

def upload_test_file(bucket_name: str):
    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob("hello-from-sample.txt")
    blob.upload_from_string("Hello from Google-api sample!")
    print(f"Uploaded hello-from-sample.txt to gs://{bucket_name}")

def list_blobs(bucket_name: str):
    client = storage.Client()
    blobs = [b.name for b in client.list_blobs(bucket_name)]
    print(f"Objects in gs://{bucket_name}:", blobs)

if __name__ == "__main__":
    list_buckets()
    bucket_name = os.getenv("BUCKET_NAME")
    if bucket_name:
        upload_test_file(bucket_name)
        list_blobs(bucket_name)
    else:
        print("Set BUCKET_NAME env var to test an upload.")
