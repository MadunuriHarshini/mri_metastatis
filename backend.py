from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
import torch
from PIL import Image
import io

app = FastAPI()
model = nested_unet  # Load your best performing model
model.eval()

@app.post("/segment")
async def segment_image(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read()))
    # Preprocess image (resize, normalize, etc.)
    input_tensor = preprocess_image(image)  # Define preprocess_image function
    with torch.no_grad():
        output = model(input_tensor)
    segmentation = postprocess_output(output)  # Define postprocess_output function
    return JSONResponse(content={"segmentation_result": segmentation.tolist()})

# Run using `uvicorn filename:app --reload`
