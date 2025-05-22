from PIL import Image, ImageDraw, ImageFont
from src.models import Element, PositionType
from src.models import ElementType


def generate_image_pil(height: int, width: int, background: str, elements: list[Element]):
    img = Image.new("RGBA", size=(height, width), color=background)
    draw = ImageDraw.Draw(img)

    for element in elements:
        if element.type == "text":
            font = ImageFont.truetype(f"src/{element.font}.ttf", element.size)

            if isinstance(element.position, str):
                if element.position == "center":
                    bbox = draw.textbbox((0, 0), element.value, font=font)
                    text_width = bbox[2] - bbox[0]
                    text_height = bbox[3] - bbox[1]

                    x = (img.width - text_width) // 2
                    y = (img.height - text_height) // 2  - bbox[1]
                    pos = (x, y)
                elif element.position == "top-center":
                    bbox = draw.textbbox((0, 0), element.value, font=font)
                    text_width = bbox[2] - bbox[0]

                    x = (img.width - text_width) // 2
                    y = 15 - bbox[1]
                    pos = (x, y)
                elif element.position == "bottom-center":
                    bbox = draw.textbbox((0, 0), element.value, font=font)
                    text_width = bbox[2] - bbox[0]
                    text_height = bbox[3] - bbox[1]

                    x = (img.width - text_width) // 2
                    y = img.height - text_height  - bbox[1] - 10 # 10 pixels from the bottom
                    pos = (x, y)
            else:
                pos = element.position


            draw.text(pos, element.value, font=font, fill=element.color)

    return img

if __name__ == '__main__':
    els = [{"type": "text", "position": (300, 200), "font": "Nunito", "color": "white", "size": 175}]
    elements_objects = [Element(
        type=ElementType(el['type']),
        position=PositionType(el['position']),
        font=el['font'],
        color=el['color'],
        size=el['size'],
        value=el.get('value', '')  # ou coloque um valor default se quiser
    ) for el in els]
    tt = generate_image_pil(height=1080, width=1080, background="black", elements=elements_objects)
    tt.show()