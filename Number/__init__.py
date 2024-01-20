import os
import logging
import azure.functions as func
from azure.cosmos import CosmosClient
import uuid

def create_cosmos_client():
    """Crea y retorna un cliente de Cosmos DB."""
    endpoint = os.environ["COSMOS_DB_ENDPOINT"]
    key = os.environ["COSMOS_DB_KEY"]
    return CosmosClient(endpoint, key)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function for inserting or updating a number processed a request.')

    try:
        # Crear cliente de Cosmos DB
        client = create_cosmos_client()
        database = client.get_database_client(os.environ["COSMOS_DB_DATABASE_NAME"])
        container = database.get_container_client(os.environ["COSMOS_DB_CONTAINER_NAME"])

        # Obtener el número del cuerpo de la solicitud POST
        req_body = req.get_json()
        number = int(req_body.get("number", 0))  # Tomar el número del cuerpo, predeterminado a 0 si no se proporciona

        # Verificar si el número está dentro del rango válido
        if 0 <= number <= 10:
            # Consultar si ya existe un registro en la base de datos
            query = "SELECT * FROM c"
            results = list(container.query_items(query, enable_cross_partition_query=True))

            if results:
                # Si existe un registro, actualizar el número
                existing_item = results[0]
                existing_item["number"] = number
                container.upsert_item(existing_item)
            else:
                # Si no existe un registro, crear uno nuevo
                unique_id = str(uuid.uuid4())
                item = {"id": unique_id, "number": number}
                container.upsert_item(item)

            # Modificar aquí para el mensaje personalizado
            return func.HttpResponse(f"He memorizado el número {number}", status_code=200)
        else:
            return func.HttpResponse("El número debe estar entre 0 y 10", status_code=400)
    
    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse(f"Failed to insert/update item into Cosmos DB due to: {e}", status_code=500)
