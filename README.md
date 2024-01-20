# README para API de Azure Functions

## Descripción
Este proyecto contiene una serie de Azure Functions desarrolladas para una prueba de concepto, diseñadas para trabajar con Azure Cosmos DB y proporcionar una interfaz de API para realizar varias operaciones.

## Funciones Incluidas
1. **Saludo Inicial**: Responde con un mensaje de bienvenida.
2. **Saludo Personalizado**: Responde con un saludo personalizado si se proporciona un nombre.
3. **Inserción/Actualización de Números**: Permite insertar o actualizar un número en Azure Cosmos DB.
4. **Recuperar Número**: Obtiene un número almacenado previamente en Azure Cosmos DB.

## Requisitos
- Python 3.6 o superior.
- Azure Functions Core Tools.
- Cuenta de Azure con una suscripción activa.
- Azure Cosmos DB cuenta y clave.

## Configuración Local
1. **Instalación de Dependencias**:
   - Cree un archivo `requirements.txt` en la raíz del proyecto con las siguientes dependencias:
     ```
     azure-functions
     azure-cosmos
     ```
   - Instale las dependencias ejecutando:
     ```
     pip install -r requirements.txt
     ```

2. **Variables de Entorno**:
   - Establecer las siguientes variables en el archivo `local.settings.json`:
     ```
     {
       "IsEncrypted": false,
       "Values": {
         "FUNCTIONS_WORKER_RUNTIME": "python",
         "AzureWebJobsFeatureFlags": "EnableWorkerIndexing",
         "AzureWebJobsStorage": "<your-storage-connection-string>",
         "COSMOS_DB_ENDPOINT": "<your-cosmos-db-endpoint>",
         "COSMOS_DB_KEY": "<your-cosmos-db-key>",
         "COSMOS_DB_DATABASE_NAME": "ToDoList",
         "COSMOS_DB_CONTAINER_NAME": "Items"
       }
     }
     ```

## Ejecución Local
Para iniciar las funciones localmente, ejecute el siguiente comando en su terminal:
```
func start
```

## Despliegue
Para desplegar el proyecto a Azure, utilice el siguiente comando:
```
func azure functionapp publish <name-app-funtions>
```
Asegúrese de haber configurado previamente su entorno de Azure CLI con las credenciales adecuadas.

## Uso
- **Saludo Inicial**: Acceda a la URL de la función sin parámetros adicionales.
- **Saludo Personalizado**: Utilice la ruta `/hello/{name}` para recibir un saludo personalizado.
- **Inserción/Actualización de Números**: Envíe una solicitud POST a `/number` con un cuerpo JSON que contenga el número a almacenar.
- **Recuperar Número**: Realice una solicitud GET a `/remember` para recuperar el número almacenado.

## Notas Adicionales
- Asegúrese de que las configuraciones y las claves de Azure Cosmos DB sean correctas y estén actualizadas.
- Revise los logs para depurar en caso de errores o problemas durante la ejecución.