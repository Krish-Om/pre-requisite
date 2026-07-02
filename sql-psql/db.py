from typing import Annotated

from dotenv import dotenv_values
from fastapi import Depends
from sqlalchemy import ForeignKey, String, Text, create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, relationship

config = dotenv_values(".env")

POSTGRES_USER = config["POSTGRES_USER"] or "postgres"
POSTGRES_PASSWORD = config["POSTGRES_PASSWORD"] or "mysecret"
POSTGRES_HOST = config["POSTGRES_HOST"] or "localhost"
POSTGRES_PORT = config["POSTGRES_PORT"] or "5432"
POSTGRES_DB = config["POSTGRES_DB"] or "mydb"

engine = create_engine(
    f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}",
)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]


class Base(DeclarativeBase):
    pass


class Users(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255))
    password: Mapped[str] = mapped_column(String(255))
    notes: Mapped[list[Notes]] = relationship("Notes", back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id}, name='{self.name}', email='{self.email}', notes={self.notes})"


class Notes(Base):
    __tablename__ = "notes"
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped[Users] = relationship("Users")

    def __repr__(self) -> str:
        return f"Note(id={self.id}, title='{self.title}', content='{self.content}', user_id={self.user_id})"


def init_db():
    Base.metadata.create_all(engine)


def get_users(session: SessionDep) -> list[Users]:
    users = session.scalars(select(Users)).all()
    return users


def get_notes(session: SessionDep):
    notes = session.scalars(select(Notes)).all()
    print(notes)


def add_user(session: SessionDep, user: Users):
    try:
        if user:
            session.add(user)
            session.commit()
        else:
            raise ValueError("User data is required")
    except Exception as e:
        session.rollback()
        print(e)


def run(session: SessionDep):
    init_db()
    add_user(session)
    users = get_users(session)
    print(f"users[0]: {users[0]}")

    get_notes(session)


if __name__ == "__main__":
    with Session(engine) as session:
        run(session)
