import asyncio
import os

import httpx
from dotenv import dotenv_values

config = dotenv_values(".env.dev")
url1: str | None = config.get("URL1")
url2: str | None = config.get("URL2")
url3: str | None = config.get("URL3")


async def fetch1(client: httpx.AsyncClient):
    try:
        res = await client.get(url1)
        data = res.json()
        print(f"Fetching from {fetch1.__name__}: {data.get('apiVersion')}")
    except Exception as e:
        print(f"Exceptions : {e}")


async def fetch2(client: httpx.AsyncClient):
    try:
        res = await client.get(url2)
        data = res.json()
        print(f"Fetching from {fetch2.__name__}: {data}")
    except Exception as e:
        print(f"Exceptions : {e}")


async def fetch3(client: httpx.AsyncClient):
    try:
        res = await client.get(url2)
        data = res.json()
        print(f"Fetching from {fetch3.__name__}: {data}")
    except Exception as e:
        print(f"Exceptions : {e}")


async def main():
    """
         1. tasks = [fetch(url1), fetch(url2), fetch(url3)]

    Your 'tasks' list looks like this:
    [ 📦 Coroutine 1 (Paused), 📦 Coroutine 2 (Paused), 📦 Coroutine 3 (Paused) ]

         2. await asyncio.gather(*tasks)

    This opens all 3 boxes, registers them with the Event Loop, and says:
    "Fire all of their initial network requests right now."

         3. await client.get(url)

    This is the exact line where the function pauses. It yields control back
    to the main loop manager, saying: "I am waiting on network I/O. Wake me up
    when bytes start hitting the network interface card."

    """

    async with httpx.AsyncClient() as client:
        await asyncio.gather(fetch1(client), fetch2(client), fetch3(client))


if __name__ == "__main__":
    asyncio.run(main())
