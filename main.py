from fastapi import FastAPI
from database import Base, engine
from routes.runs import router
from contextlib import asynccontextmanager
from auth import auth_router
from starlette.middleware.sessions import SessionMiddleware
import os
from dotenv import load_dotenv
from fastapi.staticfiles import StaticFiles


# Load the environment.
load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI):

    # Create all the tables and check to see if they exist.
    Base.metadata.create_all(engine)  # This knows which database to apply this to based on the engine
    yield
    # Code at this point will run once app is closed.


app = FastAPI(lifespan=lifespan)
app.include_router(router=auth_router)
app.include_router(router=router)
app.mount("/frontend/dist/index.html", StaticFiles(directory="./frontend/dist"))

app.add_middleware(SessionMiddleware, secret_key=os.getenv("secret_key"))


def main():
    print("Hello from tau-ceti-tracker!")


if __name__ == "__main__":
    main()
