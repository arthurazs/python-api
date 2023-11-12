r""""Simple async client module (httpx).

usage: poetry run src\client.py
"""
import asyncio
import logging

import httpx

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)


async def run(url: str) -> None:
    """Get url content."""
    logger.info(url)
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
    logger.info(r)
    logger.info(r.status_code)
    logger.info(r.headers["content-type"])
    logger.info("%s\n", r.text)


for link in ("http://127.0.0.1:8000/", "http://127.0.0.1:8000/books/123"):
    asyncio.run(run(link))
