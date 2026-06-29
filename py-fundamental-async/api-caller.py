import dotenv
import requests
from dotenv import dotenv_values

config = dotenv_values(".env.dev")
url1: str | None = config.get("URL1")
url2: str | None = config.get("URL2")
url3: str | None = config.get("URL3")


def run():
    try:
        r1 = requests.get(url1)
        r2 = requests.get(url2)
        r3 = requests.get(url3)
        if not r1:
            raise Exception("Error fetching with url1")
        if not r2:
            raise Exception("Error fetching with r2")
        if not r3:
            raise Exception("Error fetching with r3")

        print(r1.json())
        print(r2.json())
        print(r3.json())
    except Exception as e:
        print(f"Error: {e}")


run()
