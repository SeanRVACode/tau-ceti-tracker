from pydantic import BaseModel, ConfigDict
from datetime import datetime


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
