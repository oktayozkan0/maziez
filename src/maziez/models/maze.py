from dataclasses import dataclass
from typing import Iterator
from maziez.models.square import Square


@dataclass(frozen=True)
class Maze:
    squares: tuple[Square, ...]

    def __iter__(self) -> Iterator[Square]:
        return iter(self.squares)
    
    def __getitem__(self, index: int) -> Square:
        return self.squares[index]
