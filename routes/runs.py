from fastapi import APIRouter, Depends, HTTPException
from models import RunCreate, RunShow
from database import get_session, Runs
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func
from typing import Dict

router = APIRouter()


@router.post("/run", response_model=RunShow)
async def post_run(run: RunCreate, session: Session = Depends(get_session)) -> RunShow:
    """_Post a new run to the database_.

    Args:
        run (RunCreate): _Pydantic model of a run_.
        session (Session, optional): _SQLAlchemy Session_. Defaults to Depends(get_session).

    Raises:
        HTTPException: _description_

    Returns:
        _RunShow_: _Dict of the run just posted, based off SQLAlchemy ORM_.
    """
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
        # Todo probably implement logging to handle the exception.
        print(e)
        session.rollback()
        raise HTTPException(status_code=400, detail="Invalid Entry")


@router.get("/all_runs", response_model=list[RunShow])
async def get_run(session: Session = Depends(get_session)) -> list[RunShow]:
    """_Displays all runs from the database_.

    Args:
        session (Session, optional): _SQLAlchemy session_. Defaults to Depends(get_session).

    Returns:
        RunShow: _Pydantic Model that takes a SQL ORM Object and displays it as a list_.
    """
    all_runs = session.query(Runs).all()

    return all_runs


@router.get("/stats")
async def show_stats(session: Session = Depends(get_session)) -> dict:
    """

    Args:
        session (Session, optional): _SqlAlchemy Session_ that is retrieved with get_session method. Defaults to Depends(get_session).
    """

    # Ini stats dict
    stats = {}
    # Total Runs
    total_runs = session.query(Runs).count()
    stats["total_runs"] = total_runs
    if total_runs > 0:
        # Successful runs based on exfil being true
        total_successful_exfils = session.query(Runs).where(Runs.exfiled).count()
        # Determine exfil rate
        exfil_rate = format((total_successful_exfils / total_runs), ".0%")
        stats["exfil_rate"] = exfil_rate
        # K/D Ratio
        total_elims = session.query(func.sum(Runs.runner_downs)).scalar()
        stats["total_elims"] = total_elims
        # Calculate k/d ratio
        elims_ratio = format(total_elims / total_runs, ".2f")
        stats["kd_ratio"] = elims_ratio
    else:
        # Set exfil rate to 0 if there are no runs.
        stats["exfil_rate"] = 0

    return stats
