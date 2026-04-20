from routes import runs
from fastapi import FastAPI
from database import Runs
from contextlib import asynccontextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


DATABASE_URL = "sqlite+pysqlite:///:memory:"


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create the engine
    engine = create_engine(DATABASE_URL, echo=True)
    # Create the session
    session = Session(engine)
    # Create all the tables and check to see if they exist.
    Runs.metadata.create_all()
    yield
    pass


app = FastAPI(lifespan=lifespan)


def main():
    print("Hello from tau-ceti-tracker!")


if __name__ == "__main__":
    main()
