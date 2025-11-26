from fastapi import FastAPI
from api.v1 import flights

app = FastAPI()

app.include_router(flights.router, prefix="/api/v1")
#app.include_router(users.router, prefix="/api/v1")
#app.include_router(orders.router, prefix="/api/v1")
