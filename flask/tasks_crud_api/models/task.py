from dataclasses import dataclass, field


@dataclass
class Task:
    id: int
    title: str
    description: str
    completed: bool = field(default_factory=lambda: False)

    def to_dict(self):
        return self.__dict__
