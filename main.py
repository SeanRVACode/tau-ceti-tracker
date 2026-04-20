from fastapi import FastAPI
from database import Base
from contextlib import asynccontextmanager
from sqlalchemy import create_engine


DATABASE_URL = "sqlite+pysqlite:///:memory:"


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create the engine
    engine = create_engine(DATABASE_URL, echo=True)
    # Create all the tables and check to see if they exist.
    Base.metadata.create_all(engine=engine)  # This knows which database to apply this to based on the engine
    yield
    pass


app = FastAPI(lifespan=lifespan)


def main():
    print("Hello from tau-ceti-tracker!")


if __name__ == "__main__":
    main()
