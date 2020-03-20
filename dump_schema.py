from enum import Enum
from typing import List, Tuple
from pydantic import BaseModel, Field


class Image(BaseModel):
    source: str
    dimensions: Tuple[int, int]


class EdgeClass(str, Enum):
    ridge = "ridge"
    eave = "eave"
    rake = "rake"
    hip = "hip"
    valley = "valley"


class RoofLine(BaseModel):
    origin: Tuple[float, float]
    destination: Tuple[float, float]
    classification: EdgeClass


class View(BaseModel):
    image: Image
    roof_lines: List[RoofLine]


class Input(BaseModel):
    """
    This is the input to my awesome service
    """

    views: List[View]

    class Config:
        title = "Input"


file = open("schema.json", "w+")
file.write(Input.schema_json(indent=2))
file.close()
