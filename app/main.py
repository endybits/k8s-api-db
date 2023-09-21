import os

from fastapi import FastAPI

from app.db import db_connection
app = FastAPI()

@app.get("/")
def hello():
    print(db_connection())
    return {
        "hello": "This is a container service workin on K8s",
        "from Pod": f"{os.environ.get('HOSTNAME', 'DEFAULT_ENV')}",
        "db connection": f"{db_connection()}"
    }