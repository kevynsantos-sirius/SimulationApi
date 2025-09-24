# app.py
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/user/current")
async def get_current_user():
    # aqui você pode simular os dados ou puxar de um banco real
    permissions = {
        "documentCreate": True,
        "documentDelete": False,
        "documentMove": True,
        "folderEdit": True,
        "folderDelete": False
    }

    data_permissions = {
        "folderCreate": True
    }

    response_data = {
        "permissions": permissions,
        "datapermissions": data_permissions
    }

    return JSONResponse(content=response_data)
