from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, CheckConstraint, Boolean, Integer, DateTime
from sqlalchemy.sql import func
from datetime import datetime


class Base(DeclarativeBase):
    # Base is aware of all the classes that inherit from it so it should be the main one I call
    pass


class Runs(Base):
    __tablename__ = "Runs"

    id: Mapped[int] = mapped_column(primary_key=True)
    # Shell mappings with limitations on what shells can actually be input
    shell: Mapped[str] = mapped_column(
        String,
        CheckConstraint(
            "shell IN ('assassin','destroyer','triage','vandal','thief','rook','recon')",
            name="ck_runs_shell_allowed_values",
        ),
    )
    map_name: Mapped[str] = mapped_column(
        String,
        CheckConstraint(
            "map_name IN ('perimeter','dire marsh','outpost','cryo archive')", name="ck_map_name_allowed_values"
        ),
    )
    exfiled: Mapped[bool] = mapped_column(Boolean, default=False)  # Todo do I really want this to default to False?
    exfil_amount: Mapped[int] = mapped_column(Integer, default=0)
    date: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    runner_downs: Mapped[int] = mapped_column(Integer, default=0)
    uesc_elims: Mapped[int] = mapped_column(Integer, default=0)
    rook_friends: Mapped[bool] = mapped_column(Boolean, default=False)
    team_mates_rezzed: Mapped[int] = mapped_column(Integer, default=0)

    def __repr__(self) -> str:
        return f"Run(id={self.id}, shell={self.shell},exfiled={self.exfiled},amount={self.exfil_amount},date={self.date},runner_downs={self.runner_downs},uesc_elims={self.uesc_elims})"
