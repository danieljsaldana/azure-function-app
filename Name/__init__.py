import azure.functions as func
import logging

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.route_params.get('name')

    if name:
        return func.HttpResponse(f"Soy Goliat 🐶! Encantado de conocerte {name}!", status_code=200)
    else:
        return func.HttpResponse("Hola, me llamo Goliat. Si me indicas tu nombre en la ruta /nombre, puedo hacerte un saludo personalizado.", status_code=200)
