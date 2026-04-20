from fastapi import APIRouter, Depends
from models import RunCreate
from database import get_session

router = APIRouter()


@router.post("/run")
async def post_run(run: RunCreate,Session(Depends(engine))):
    with Session as session:
        return {"message": "Run Created"}
