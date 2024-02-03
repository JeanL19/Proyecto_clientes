from config.db import cursor, conexion
from fastapi import FastAPI
from models.client_date import Client

app = FastAPI()

clientes = [
    {

    "id": 1,
    "cliente": "Admin",
    "contacto": "admin@admin.com",
    "fecha_ingreso": "22 de Enero 2024",
    "diagnostico": "Programando",
    "tipo": "Escritorio",
    "marca_modelo": "Asus H-61MK",
    "estado": "Tirando Codigo",
},
{

    "id": 2,
    "cliente": "moder",
    "contacto": "moder@admin.com",
    "fecha_ingreso": "22 de Enero 2024",
    "diagnostico": "Moderando",
    "tipo": "Monitor",
    "marca_modelo": "None",
    "estado": "Observando",
}
]

@app.get('/')
async def message():
    return "Bienvenido a la base de clientes"

@app.get('/clientes')
async def get_clients():
    return clientes

@app.get('/clientes/{id}')
async def get_client_Id(id: int):
    return list(filter(lambda item: item["id"] == id, clientes))

@app.get('/clientes/')
async def get_client_By_model(tipo: str, marca_modelo: str):
    return list(filter(lambda item: item['tipo'] == tipo or item['marca_modelo'] == marca_modelo, clientes))

@app.put('/clientes/{id}')
async def update_client(id: int, client: Client):
    for index, item in enumerate(clientes):
        if item['id'] == id:
            clientes[index]['cliente'] == client.cliente
            clientes[index]['contacto'] == client.contacto
            clientes[index]['fecha_ingreso'] == client.fecha_ingreso
            clientes[index]['diagnostico'] == client.diagnostico
            clientes[index]['tipo'] == client.tipo
            clientes[index]['marca_modelo'] == client.marca_modelo
            clientes[index]['estado'] == client.estado
    return clientes

@app.post('/new_cliente/')
def create_cliente(client:Client):
    clientes.append(client)
    return clientes

@app.delete('/delete_cliemte/{id}')
def delete_cliemtes(id:int):
    for item in clientes:
        if item['id']==id:
            clientes.remove(item)
    return clientes

