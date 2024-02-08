from azure.storage.blob import BlobServiceClient


class SAA:
    def __init__(self):
        self.connection_string = "DefaultEndpointsProtocol=https;AccountName=alexalkhatibstorage;AccountKey=SZWaBMCDNd9ui1WkSI8KEkmaaUy1zKSQpYk+muL1yHsNthqdxutarx++/lPsvl85gQ2xUOSn3Q4y+AStFLS3Mg==;EndpointSuffix=core.windows.net"
        self.container_name = "container"


    def createBlob(self, blob_name):
        blob_service_client = BlobServiceClient.from_connection_string(self.connection_string)
        return blob_service_client.get_blob_client(container=self.container_name, blob=blob_name)

    def uploadFile(self, path_to_local_file, username):
        with open(path_to_local_file, "rb") as data:
            blob_client = self.createBlob(username + path_to_local_file)
            blob_client.upload_blob(data)
        return blob_client.url