from PIL import Image, ImageDraw, ImageFont

# with Image.open("teste.png") as im:

# draw = ImageDraw.Draw(im)
txt = Image.new("RGBA", size=(1024, 1024), color="black")
draw = ImageDraw.Draw(txt)
font = ImageFont.truetype("Nunito.ttf", 75)

image_w, image_h = txt.size
_, _, text_w, text_h = draw.textbbox((0, 0), "Hello World", font=font)
# middle centered text
draw.text(((image_w - text_w) / 2, (image_h - (text_h * 1.2)) / 2), "Hello World", font=font, fill="yellow")
# top centered text
draw.text(((image_w - text_w) / 2, (image_h - text_h * 1.2) * .1), "Hello World", font=font, fill="yellow")
# bottom centered text
draw.text(((image_w - text_w) / 2, (image_h - text_h) * .9), "Hello World", font=font, fill="yellow")

# write to stdout
draw.line((0, 0) + txt.size, fill=128)
draw.line((0, txt.size[1], txt.size[0], 0), fill=128)
# breakpoint()
# im.save(sys.stdout, "PNG")
txt.show()