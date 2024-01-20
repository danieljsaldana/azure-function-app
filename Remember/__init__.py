import os
import logging
import azure.functions as func
from azure.cosmos import CosmosClient

def create_cosmos_client():
    """Crea y retorna un cliente de Cosmos DB."""
    endpoint = os.environ["COSMOS_DB_ENDPOINT"]
    key = os.environ["COSMOS_DB_KEY"]
    return CosmosClient(endpoint, key)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function for getting a number processed a request.')

    try:
        # Crear cliente de Cosmos DB
        client = create_cosmos_client()
        database = client.get_database_client(os.environ["COSMOS_DB_DATABASE_NAME"])
        container = database.get_container_client(os.environ["COSMOS_DB_CONTAINER_NAME"])

        if req.method == "GET":
            # Consultar el número almacenado en Cosmos DB (asumimos que solo hay un número)
            query = "SELECT TOP 1 c.number FROM c"
            results = list(container.query_items(query, enable_cross_partition_query=True))

            if results:
                number = results[0]["number"]
                return func.HttpResponse(f"He memorizado el número {number}", status_code=200)
            else:
                return func.HttpResponse("No me has pedido que memorice ningun numero.", status_code=404)
        else:
            return func.HttpResponse("Esta función solo admite solicitudes GET", status_code=405)
    
    except Exception as e:
        logging.error(f"Error: {e}")
        return func.HttpResponse(f"Failed to query Cosmos DB due to: {e}", status_code=500)
