# 🎬 API de Upload e Streaming de Vídeos com FastAPI + MinIO

Esta é uma API construída com **FastAPI** que permite fazer upload, listar e fazer streaming de vídeos armazenados no **MinIO Play** (compatível com S3 da AWS).  
Ideal para aplicações que precisam de upload e reprodução de mídia diretamente do backend.

---

## 🚀 Funcionalidades

- 📤 Upload de arquivos de vídeo (`multipart/form-data`)
- 🎥 Streaming e download de vídeos por filename
- 📂 Listagem de vídeos disponíveis no bucket
- 🌐 Suporte a CORS (liberado para qualquer origem por padrão)

---

## 📦 Requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)
- Conexão com a internet (para acessar o MinIO Play)

---

## 🛠️ Instalação

### 1. Instale as dependências

```bash
pip install fastapi uvicorn minio python-multipart
```

---

## ▶️ Executando a API

Execute o servidor com o Uvicorn:

```bash
uvicorn main:app --reload
```

- `main` é o nome do arquivo Python onde está o código (ex: `main.py`)
- `app` é a instância do FastAPI criada no código

Se o seu arquivo tiver outro nome, ajuste `main:app` no comando.

---

## 🌐 Endpoints disponíveis

| Método | Endpoint            | Descrição                                 |
|--------|---------------------|-------------------------------------------|
| POST   | `/upload/`          | Faz upload de um vídeo                    |
| GET    | `/download/{nome}`  | Faz o streaming/download do vídeo         |
| GET    | `/list/`            | Lista todos os vídeos disponíveis no MinIO|

---

## ☁️ Configuração do MinIO

Esta API utiliza o **MinIO Play**, um ambiente público e gratuito de testes oferecido pelo MinIO.

- **Host**: `https://play.min.io`
- **Access Key**: `Q3AM3UQ867SPQQA43P2F`
- **Secret Key**: `zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG`
- **Bucket usado**: `meus-videos` (criado automaticamente se não existir)

---

## 🔒 CORS

O middleware de CORS está configurado para aceitar qualquer origem (`*`).  
Isso facilita o uso com front-ends locais ou externos sem bloqueios por política de mesma origem.

Para produção, **recomenda-se** definir os domínios específicos:

```python
allow_origins=["https://seu-dominio.com"]
```

---

## 🧪 Exemplos de uso com `curl`

### Upload de vídeo:
```bash
curl -F "file=@video.mp4" http://localhost:8000/upload/
```

### Listar vídeos:
```bash
curl http://localhost:8000/list/
```

### Download (streaming):
```bash
curl http://localhost:8000/download/video.mp4 --output video.mp4
```

---

## 📂 Estrutura do Projeto (sugestão)

```
📁 seu-projeto/
├── main.py               # Código principal da API
├── README.md             # Este arquivo
└── requirements.txt      # Lista de dependências
```



## 📄 Licença

Este projeto é de uso livre para fins educacionais, testes e protótipos.  
Você pode modificar, distribuir e usar como desejar.

---

