import sys
from google.cloud import storage

def compose_file(bucket_name, first_blob_name, second_blob_name, destination_blob_name):
    """Concatenate source blobs into destination blob."""
    bucket_name = "sanket-python-bucket"
    first_blob_name = "sample/file1"
    second_blob_name = "sample/emptyfile"
    destination_blob_name = "sample/file3"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    destination = bucket.blob(destination_blob_name)
    destination.content_type = "text/plain"


    sources = [bucket.get_blob(first_blob_name), bucket.get_blob(second_blob_name)]
    destination.compose(sources)

    print(
        "New composite object {} in the bucket {} was created by combining {} and {}".format(
            destination_blob_name, bucket_name, first_blob_name, second_blob_name
        )
    )
    return destination




if __name__ == "__main__":
    compose_file(
        bucket_name=sys.argv[0],
        first_blob_name=sys.argv[0],
        second_blob_name=sys.argv[0],
        destination_blob_name=sys.argv[0],
    )

