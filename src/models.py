from pydantic import BaseModel, validator
from typing import Union, Tuple, Literal
from enum import Enum
import re

CORES_FIXAS = {"white", "black"}

class ElementType(str, Enum):
    TEXT = "text"
    IMAGE = "image"
    SHAPE = "shape"

class ElementFont(str, Enum):
    NUNITO = "Nunito"
    # ROBOTO = "Roboto"
    # ARIAL = "Arial"
    # TIMES_NEW_ROMAN = "Times New Roman"

PositionType = Union[
    Tuple[int, int],
    Literal["center", "top-center", "bottom-center"]
]

class Element(BaseModel):
    type: ElementType
    position: PositionType
    value: str
    font: str
    size: int
    color: str

    @validator("color")
    def valida_cor(cls, v):
        if v.lower() in CORES_FIXAS:
            return v
        # regex para código hexadecimal (#FFF ou #FFFFFF)
        if re.match(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', v):
            return v
        raise ValueError('Cor deve ser "white", "black" ou um código hexadecimal válido')

class Image(BaseModel):
    h: int
    w: int
    background: str
    elements: list[Element]