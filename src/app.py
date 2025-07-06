from PIL import Image, ImageDraw, ImageFont
from src.api.models import Element, PositionType
from src.api.models import TextElement
import math

def rotate_point(x, y, cx, cy, angle_degrees):
    angle = math.radians(angle_degrees)
    dx = x - cx
    dy = y - cy
    qx = cx + dx * math.cos(angle) - dy * math.sin(angle)
    qy = cy + dx * math.sin(angle) + dy * math.cos(angle)
    return (qx, qy)


def generate_image_pil(height: int, width: int, background: str, elements: list[Element]):
    img = Image.new("RGBA", size=(height, width), color=background)
    draw = ImageDraw.Draw(img)

    font_mapping = {
        "Nunito": {
            "bold": "Nunito-Bold",
            "italic": "Nunito-Italic",
            "regular": "Nunito-Regular",
            "bold_italic": "Nunito-BoldItalic",
        }
    }

    for element in elements:
        if element.type == "text":
            bold = False
            italic = False
            if element.bold == "True":
                bold = True
            elif element.italic == "True":
                italic = True

            font_variation = "regular"
            if bold and italic:
                font_variation = "bold_italic"
            elif bold:
                font_variation = "bold"
            elif italic:
                font_variation = "italic"
            print(font_mapping[element.font][font_variation], bool(element.bold), element.bold)
            font = ImageFont.truetype(f"src/{element.font}/{font_mapping[element.font][font_variation]}.ttf", element.size)

            if isinstance(element.position, str):
                if element.position == "center":
                    bbox = draw.textbbox((0, 0), element.value, font=font)
                    text_width = bbox[2] - bbox[0]
                    text_height = bbox[3] - bbox[1]

                    x = (img.width - text_width) // 2
                    y = (img.height - text_height) // 2 - bbox[1]
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
                    y = img.height - text_height - bbox[1] - 10  # 10 pixels from the bottom
                    pos = (x, y)
            else:
                pos = element.position

            draw.text(pos, element.value, font=font, fill=element.color)

        elif element.type == "shape":
            if element.shape == "rectangle":
                if isinstance(element.position, str):
                    ## implementar posicoes fixas
                    xy = [element.position[0],
                          element.position[1],
                          element.position[0] + element.size[0],
                          element.position[1] + element.size[1]]
                else:
                    xy = [element.position[0],
                          element.position[1],
                          element.position[0] + element.size[0],
                          element.position[1] + element.size[1]]
                draw.rectangle(xy, fill=element.color, outline=element.border_color, width=element.border_size)

            elif element.shape == "polygon":
                if isinstance(element.position, str):
                    ## implementar posicoes fixas
                    xy = [element.position[0],
                          element.position[1],
                          element.position[0] + element.size[0],
                          element.position[1] + element.size[1],
                          element.position[0] - element.size[0],
                          element.position[1] - element.size[1]
                          ]
                else:
                    xy = [(element.position[0], element.position[1]),
                          (element.position[0] + element.size[0],
                          element.position[1] + element.size[1]),
                          (element.position[0],
                          element.position[1] + element.size[1])]



                draw.polygon(xy, fill=element.color, outline=element.border_color, width=element.border_size)

    return img


if __name__ == '__main__':
    els = [{"type": "text", "position": (300, 200), "font": "Nunito", "color": "white", "size": 175}]
    elements_objects = [Element(
        type=TextElement(el['type']),
        position=PositionType(el['position']),
        font=el['font'],
        color=el['color'],
        size=el['size'],
        value=el.get('value', '')  # ou coloque um valor default se quiser
    ) for el in els]
    tt = generate_image_pil(height=1080, width=1080, background="black", elements=elements_objects)
    tt.show()

    # {
    #     "type": "shape",
    #     "position": "bottom-center",
    #     "color": "white",
    #     "size": [20, 20],
    #     "border-size": 2,
    #     "border-color": "white",
    #     "shape": "square"
    # }
