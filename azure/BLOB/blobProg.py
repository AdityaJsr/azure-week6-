from azure.storage.blob import BlobServiceClient
from azure.storage.blob import ContainerClient
from azure.storage.blob import BlobClient
from decouple import config
import os


key  = config("secret_key")
connection_string = key
service = BlobServiceClient.from_connection_string(conn_str=connection_string)

def createContainer():

    container_client = ContainerClient.from_connection_string(conn_str= connection_string, container_name="avinash")
    container_client.create_container()

def deleteContainer():
    try:
        container_client = ContainerClient.from_connection_string(conn_str= connection_string, container_name="avinash")
        container_client.delete_container()
    except Exception as e:
        print("Unable to delete the container due to : \n", e)

def uploadBlob():
    try:
        blob = BlobClient.from_connection_string(conn_str= connection_string, container_name="avinash", blob_name="upload")

        with open("D:/vs studio/bridgeLabz/week 6/azure/BLOB/upload/kakashi.png", "rb") as data:
            blob.upload_blob(data ,  blob_type="AppendBlob")

    except ConnectionError as ce:
        print("Could not connect : ", ce)
    except FileNotFoundError as fe:
        print("File not found \n ", fe)
    except Exception as e:
        print("exception ocuured" , e)

def main():
    # createContainer()
    # deleteContainer()
    uploadBlob()

if __name__ == "__main__":
    main()
