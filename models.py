from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional


class RunCreate(BaseModel):
    """This defines the incoming data of a run."""

    shell: str
    map_name: str
    exfiled: bool
    exfil_amount: int
    uesc_elims: int
    rook_friends: bool
    team_mates_rezzed: int
    runner_downs: int


class RunShow(RunCreate):
    # Tells pydantic to read data from object attributes rather than expecting a dict
    model_config = ConfigDict(from_attributes=True)
    # Include the 2 fields that RunCreate does not have
    id: int
    date: datetime


class RunUpdate(BaseModel):
    shell: Optional[str] = None
    map_name: Optional[str] = None
    exfiled: Optional[bool] = None
    exfil_amount: Optional[int] = None
    uesc_elims: Optional[int] = None
    rook_friends: Optional[bool] = None
    team_mates_rezzed: Optional[int] = None
    runners_down: Optional[int] = None
