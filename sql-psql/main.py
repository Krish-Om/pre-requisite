from contextlib import asynccontextmanager

from fastapi import FastAPI, HTTPException

from db import SessionDep, Users, add_user, get_users, init_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def get_all_users(session: SessionDep):
    users = get_users(session)
    return users


@app.post("/", status_code=201)
async def create_user(session: SessionDep, name: str, email: str, password: str):
    if not name or not email or not password:
        raise HTTPException(
            status_code=400, detail="Name, email, and password are required"
        )
    user = Users(name=name, email=email, password=password)
    add_user(session, user)
    print(user)
    return user


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
