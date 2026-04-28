from fastapi import APIRouter, Depends, HTTPException
from models import RunCreate, RunShow, RunUpdate
from database import get_session, Runs
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func, not_
from auth import require_auth

router = APIRouter()


@router.post("/run", response_model=RunShow)
async def post_run(run: RunCreate, session: Session = Depends(get_session), _=Depends(require_auth)) -> RunShow:
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

    # Todo I may want to separate out rook runs as I tend to rapid fire those and you can die far quicker. I also rarely get kills as rook
    if total_runs > 0:
        # Successful runs based on exfil being true
        total_successful_exfils = session.query(Runs).where(Runs.exfiled).count()
        # Determine exfil rate
        exfil_rate = format((total_successful_exfils / total_runs), ".0%")
        stats["exfil_rate"] = exfil_rate
        # K/D Ratio
        total_elims = session.query(func.sum(Runs.runner_downs)).scalar()
        stats["total_elims"] = total_elims
        # total deaths
        total_deaths = session.query(Runs).where(not_(Runs.exfiled)).count()
        if total_deaths == 0:
            total_deaths = 1
        print(total_deaths)
        # Calculate k/d ratio
        elims_ratio = format(total_elims / total_deaths, ".2f")
        stats["kd_ratio"] = elims_ratio
    else:
        # Set exfil rate to 0 if there are no runs.
        stats["exfil_rate"] = 0

    return stats


@router.patch("/run_edit/{id_num}", response_model=RunShow)
async def edit_run(
    id_num: int, run_update: RunUpdate, session: Session = Depends(get_session), _=Depends(require_auth)
) -> RunShow:
    try:
        # Retrieve the run that needs to be edited from the database
        run_to_edit = session.query(Runs).where(Runs.id == id_num).first()
        # If no run is found
        if not run_to_edit:
            raise HTTPException(status_code=404, detail="No run matching that ID")
        # Create a set of the fields that were edited.
        fields = (
            run_update.model_fields_set
        )  # model_fields_set shows the fields that were filled in when it was initialized.
        for field in fields:
            # Change the fields by cycling through and retreiving the values.
            setattr(run_to_edit, field, getattr(run_update, field))
        # Commit the changes to the database.
        session.commit()
        # Refresh run_to_edit with the changes
        session.refresh(run_to_edit)
        # Return the changes for the user to see
        return run_to_edit
    except IntegrityError as e:
        print(e)
        session.rollback()
        raise HTTPException(status_code=422, detail="Error in editing data no changes were made.")


@router.delete("/delete_run/{id_num}")
async def delete_run(id_num: int, session: Session = Depends(get_session), _=Depends(require_auth)):
    try:
        # Get Sqlalchemy orm object to delete
        run_to_delete = session.query(Runs).where(Runs.id == id_num).first()
        if not run_to_delete:
            raise HTTPException(status_code=404, detail="A run with that ID doesn't exist.")
        session.delete(run_to_delete)
        session.commit()

        return {"Message": "Delete Success"}
    except Exception as e:
        print(e)
        session.rollback()
        raise
