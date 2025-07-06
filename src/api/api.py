from fastapi import FastAPI
from src.app import generate_image_pil
from src.api.models import Image
from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse
import uuid
from io import BytesIO
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/v1/generate")
def generate(image: Image):
    img = generate_image_pil(height=image.h, width=image.w, background=image.background, elements=image.elements)
    image_id = str(uuid.uuid4())
    file_name = f"generated_{image_id}.png"
    img.save(file_name)

    return {"message": "Imagem gerada", "image_id": image_id}

@app.get("/v1/image/{image_id}")
def read_file(image_id: str):
    path = f"generated_{image_id}.png"
    return FileResponse(path, media_type="image/png")

@app.post("/generate")
def generate(image: Image):
    img = generate_image_pil(height=image.h, width=image.w, background=image.background, elements=image.elements)

    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    return StreamingResponse(buf, media_type="image/png")

