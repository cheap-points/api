from pydantic import BaseModel

class Flights(BaseModel):
    key: str
    date: str
    day: int
    month: int
    year: int
    price: int
    origin: str
    destination: str
    origin_city: str
    destination_city: str
    region: str
    subregion: str
    country: str
    continents: str
    #description: str | None = None
    #price: float
    #tax: float | None = None
    #tags: list[str] = []
