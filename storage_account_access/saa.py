from azure.storage.blob import BlobServiceClient


class SAA:
    def __init__(self):
        connection_string = "<your_storage_connection_string>"
        container_name = "<your_container_name>"
        blob_name = "<blob_name>"
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        self.blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    def uploadFile(self, path_to_local_file):
        with open(path_to_local_file, "rb") as data:
            self.blob_client.upload_blob(data)
        return self.blob_client.url