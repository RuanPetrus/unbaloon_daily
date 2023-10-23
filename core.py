import os
from dataclasses import dataclass
from datetime import datetime

SEP = os.path.sep
DIR_PATH = os.path.dirname(os.path.realpath(__file__)) + SEP
RESOURCES_PATH = DIR_PATH + "resources" + SEP

@dataclass
class Problem:
    website: str
    id: str
    rating: int
    date: datetime

    def __eq__(self, other) -> bool:
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)


@dataclass
class Users:
    name: str
    cf_rating: int
    atcoder_rating: int
