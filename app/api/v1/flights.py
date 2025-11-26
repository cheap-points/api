from fastapi import APIRouter, HTTPException
from services.v1.flights_services import (
    search as service_search
)

router = APIRouter()

@router.get("/search", summary="Listar todos os itens")
def search(origin: str = None, destination: str = None, day: int = None, month: int = None, year: int = None, price: int = None, key: str = None):
    return service_search(origin = origin, destination = destination, day = day, month = month, year = year, price = price, key = key)
