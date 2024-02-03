from config.db import cursor, conexion
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/clientes")
async def obtener_clientes():
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    return clientes

@app.get("/clientes/{name}")
async def obtener_clientes(name: str):
    cursor.execute("SELECT * FROM clientes WHERE Nombre = '"+str(name)+"'")
    clientes = cursor.fetchall()
    return clientes

@app.get("/clientes/{id}") ### no funciona aun si puedes buscale solucion porfis
async def obtener_clientes(id: int):
    cursor.execute("SELECT * FROM clientes WHERE id = '"+str(id)+"'")
    clientes = cursor.fetchall()
    return clientes

@app.post("/crear-cliente")
async def crear_cliente(Nombre: str, Contacto: str, Fecha_ingreso: str, Tipo: str, Marca: str, Modelo: str, Diagnostico: str, Estado: str):
    cursor.execute("INSERT INTO clientes (Nombre, Contacto, Fecha_ingreso, Tipo, Marca, Modelo, Diagnostico, Estado) VALUES ('"+Nombre+"', '"+str(Contacto)+"', '"+Fecha_ingreso+"', '"+Tipo+"', '"+Marca+"', '"+Modelo+"', '"+Diagnostico+"', '"+Estado+"' )")
    conexion.commit()
    return {"mensaje": "Cliente creado correctamente"}

@app.put("/actualizar-cliente/{name}")
async def actualizar_cliente(name: str, newEstado: str):
    cursor.execute("UPDATE clientes SET Estado = '"+newEstado+"' WHERE Nombre = '"+str(name)+"'")
    conexion.commit()
    return {"mensaje": "cliente actualizado correctamente"}

@app.delete('/eliminar_cliente/{id}')
async def eliminar_cliente(id:int):
    cursor.execute("DELETE FROM clientes WHERE id = '"+str(id)+"'")
    conexion.commit()
    return {"messaje": "Cliente Eliminado Correctamente"}



