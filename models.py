from pydantic import BaseModel


class RunCreate(BaseModel):
    """This defines the incoming data of a run."""

    shell: str
    map_name: str
    exfiled: bool
    exfil_amount: int
    uesc_elims: int
    rook_friends: bool
    team_mates_rezzed: int
