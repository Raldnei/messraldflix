from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
from minio import Minio
import io
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(title="API de Upload/Streaming de Vídeos")


# Configuração CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # para liberar todas origens, ou colocar o domínio do front, ex: ["http://localhost:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Cliente MinIO Play ( [E GRATUITO)])
client = Minio(
    "play.min.io",
    access_key="Q3AM3UQ867SPQQA43P2F",
    secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
    secure=True
)

BUCKET = "meus-videos"

# Garante que o bucket exista
if not client.bucket_exists(BUCKET):
    client.make_bucket(BUCKET)

# ----------------------------
# Endpoints
# ----------------------------

@app.post("/upload/")
async def upload(file: UploadFile = File(...)):
    """Upload de vídeo para o MinIO Play"""
    data = await file.read()
    client.put_object(
        BUCKET,
        file.filename,
        io.BytesIO(data),
        length=len(data),
        content_type=file.content_type
    )
    return {"msg": f"Vídeo '{file.filename}' enviado com sucesso!"}

@app.get("/download/{filename}")
def download(filename: str):
    """Faz download completo do vídeo"""
    try:
        response = client.get_object(BUCKET, filename)
        return StreamingResponse(response, media_type="video/mp4")
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Vídeo não encontrado: {filename}")

@app.get("/list/")
def list_videos():
    """Lista todos os vídeos no bucket"""
    objects = client.list_objects(BUCKET)
    videos = [obj.object_name for obj in objects]
    return {"videos": videos} 