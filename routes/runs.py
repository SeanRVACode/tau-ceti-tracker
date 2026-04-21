from fastapi import APIRouter, Depends, HTTPException
from models import RunCreate
from database import get_session, Runs
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

router = APIRouter()


@router.post("/run")
async def post_run(run: RunCreate, session: Session = Depends(get_session)):
    try:
        # Turn the entry into a dict
        run_dict = run.model_dump()
        # Create object of the run
        current_run = Runs(**run_dict)
        # Have the session add the run
        session.add(current_run)
        # Commit the session
        session.commit()
        # Refresh the session with current_run argument so that the entry can be returned
        session.refresh(current_run)
        return current_run
    except IntegrityError as e:
        session.rollback()
        raise HTTPException(status_code=400, detail="Invalid Entry")


@router.get("/all_runs")
async def get_run(session: Session = Depends(get_session)):
    all_runs = session.query(Runs).all()

    return all_runs
