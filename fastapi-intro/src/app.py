from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from starlette import status

app = FastAPI()


# Added pydantic model
class Hero(BaseModel):
    name: str
    id: int


class HeroResponse(BaseModel):
    name: str


flash = Hero(id=1, name="Flash")
batman = Hero(id=2, name="Batman")
hero_db = [flash, batman]


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/heroes", status_code=200)
def get_heroes():
    try:
        if hero_db.__len__() == 0:
            raise HTTPException(status_code=404, detail="Heroes not found")
        return hero_db
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")


@app.get("/heroes/{id}", status_code=200, response_model=HeroResponse)
def get_hero_by_id(id: int) -> HeroResponse | None:
    try:
        hero = [h for h in hero_db if h.id == id]
        hero_response = HeroResponse(name=hero[0].name) if hero else None

        print(hero)
        if not hero:
            raise HTTPException(
                status_code=404, detail=f"Hero not found with the id : {id}"
            )
        return hero_response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error{e}")


@app.post("/", status_code=201)
def create_hero(hero: Hero):
    try:
        hero = hero_db.pop()
        prev_len = hero_db.__len__()
        if not hero.name and not hero.id:
            raise HTTPException(
                status_code=400, detail="id or name should not be blank"
            )
        hero_db.append(hero)
        if hero_db.__len__() > prev_len:
            return "Hero added success!"
        return hero
    except Exception as e:
        print(f"Error : {e}")
        raise
