""""Simple async api server module (litestar).

usage: poetry run uvicorn src.server:app
"""
from litestar import Litestar, get


@get("/")
async def hello_world() -> str:
    """Return hello message text."""
    return "Hello, world!"


@get("/books/{book_id:int}")
async def get_book(book_id: int) -> dict[str, int]:
    """Return book ID in json."""
    return {"book_id": book_id}


app = Litestar([hello_world, get_book])
