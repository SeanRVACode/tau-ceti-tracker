from fastapi import APIRouter
from models import RunCreate

router = APIRouter()


@router.post("/run")
async def post_run(run: RunCreate):
    return {"message": "Run Created"}
