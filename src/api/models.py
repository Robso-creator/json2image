from pydantic import BaseModel, validator, Field
from typing import Union, Tuple, Literal, Annotated, Optional
from enum import Enum
import re

CORES_FIXAS = {"white", "black", "green", "yellow", "red", "pink"}

# class ElementType(str, Enum):
#     TEXT = "text"
#     IMAGE = "image"
#     SHAPE = "shape"

class ElementFont(str, Enum):
    NUNITO = "Nunito"
    # ROBOTO = "Roboto"
    # ARIAL = "Arial"
    # TIMES_NEW_ROMAN = "Times New Roman"

PositionType = Union[
    Tuple[int, int],
    Literal["center", "top-center", "bottom-center"]
]

class TextElement(BaseModel):
    type: Literal["text"]
    position: PositionType
    value: str
    font: str
    size: int
    color: str
    bold: Optional[Literal["True", "False"]] = "False"
    italic: Optional[Literal["True", "False"]] = "False"

    @validator("color")
    def valida_cor(cls, v):
        if v.lower() in CORES_FIXAS:
            return v
        # regex para código hexadecimal (#FFF ou #FFFFFF)
        if re.match(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', v):
            return v
        raise ValueError('Cor deve ser "white", "black" ou um código hexadecimal válido')

class ShapeElement(BaseModel):
    type: Literal["shape"]
    position: PositionType
    color: str
    size: PositionType
    shape: str
    border_size: Optional[int] = Field(None, alias="border-size")
    border_color: Optional[str] = Field(None, alias="border-color")
    rotation: Optional[float] = 0

    @validator("color")
    def valida_cor(cls, v):
        if v.lower() in CORES_FIXAS:
            return v
        # regex para código hexadecimal (#FFF ou #FFFFFF)
        if re.match(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', v):
            return v
        raise ValueError('Cor deve ser "white", "black" ou um código hexadecimal válido')


#TODO Criar logica para textos de multiplas linhas
class MultiLineTextElement(BaseModel):
    type: Literal["multi_line_text"]
    position: PositionType
    value: str
    font: str
    size: int
    color: str
    width: int
    line_height: Optional[int] = Field(None, alias="line-height")
    bold: Optional[Literal["True", "False"]] = "False"
    italic: Optional[Literal["True", "False"]] = "False"

    @validator("color")
    def valida_cor(cls, v):
        if v.lower() in CORES_FIXAS:
            return v
        # regex para código hexadecimal (#FFF ou #FFFFFF)
        if re.match(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', v):
            return v
        raise ValueError('Cor deve ser "white", "black" ou um código hexadecimal válido')



class ImageElement(BaseModel):
    type: Literal["image"]
    position: PositionType
    url: str
    size: Tuple[int, int]
    rotation: Optional[float] = 0

    @validator("url")
    def valida_url(cls, v):
        if not v.startswith("http://") and not v.startswith("https://"):
            raise ValueError('URL deve começar com "http://" ou "https://"')
        return v

Element = Annotated[Union[TextElement, ShapeElement, MultiLineTextElement, ImageElement], Field(discriminator="type")]

class Image(BaseModel):
    h: int
    w: int
    background: str
    elements: list[Element]