import os
import azure.functions as func
import logging
from azure.cosmos import CosmosClient, PartitionKey
import random
import uuid

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Obtener la configuración de Cosmos DB desde variables de entorno
    endpoint = os.environ["COSMOSDB_ENDPOINT"]
    key = os.environ["COSMOSDB_KEY"]
    database_name = os.environ["COSMOSDB_DATABASE"]
    container_name = os.environ["COSMOSDB_CONTAINER"]

    # Crear cliente de Cosmos DB
    client = CosmosClient(endpoint, key)
    database = client.get_database_client(database=database_name)
    container = database.get_container_client(container=container_name)

    # Generar número aleatorio
    number = random.randint(0, 10)

    # Crear un ID único para el nuevo documento
    unique_id = str(uuid.uuid4())

    # Crear y Insertar el documento en Cosmos DB
    item = {"id": unique_id, "number": number}
    try:
        container.upsert_item(item)
        return func.HttpResponse(f"Number {number} inserted into Cosmos DB with ID {unique_id}", status_code=200)
    except Exception as e:
        logging.error(f"Error inserting item into Cosmos DB: {e}")
        return func.HttpResponse(f"Failed to insert item into Cosmos DB", status_code=500)
