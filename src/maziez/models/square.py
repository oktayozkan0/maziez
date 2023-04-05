from dataclasses import dataclass

from maziez.models.border import Border
from maziez.models.role import Role


@dataclass(frozen=True)
class Square:
    index: int
    row: int
    column: int
    border: Border
    role: Role = Role.NONE
