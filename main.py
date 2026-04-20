from fastapi import FastAPI
from database import Base, engine
from routes.runs import router
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):

    # Create all the tables and check to see if they exist.
    Base.metadata.create_all(engine)  # This knows which database to apply this to based on the engine
    yield
    # Code at this point will run once app is closed.


app = FastAPI(lifespan=lifespan)
app.include_router(router=router)


def main():
    print("Hello from tau-ceti-tracker!")


if __name__ == "__main__":
    main()
