from enum import Enum, auto

class State(Enum):
    NEW = auto()
    FAILED = auto()
    DELETE = auto()
    FILTERED = auto()

    def __str__(self) -> str:
        return self.name