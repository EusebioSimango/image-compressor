from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from PIL import Image
import time
import io
import os

app = FastAPI()

async def delete_image(path):
    time.sleep(10)
    print(f'image {path} deleted')

def compress_image(image, filename):
    try:
        image_bytes = io.BytesIO(image)
        output_filename = os.path.join('./compressed_images', str( "me_you" + filename))
        with Image.open(image_bytes) as img:
            img = img.convert(mode='RGB')
            img.save(output_filename, optimize=True, quality=20, format='JPEG')
            
        if (os.path.exists(output_filename)):
            # await delete_image(output_filename)
            return output_filename
    except Exception as e:
        print(f'error {str(e)} occured')


@app.get('/')
def index():
    return { 'msg': 'This is a file compressor made by Eusebio Simango' }


@app.post('/process-image')
async def process_image(file: UploadFile):
    _file = await file.read()
    compressed_image = compress_image(_file, file.filename)
    return FileResponse(compressed_image, headers={"Content-Disposition": f"attachment; filename={file.filename}"})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8080)

