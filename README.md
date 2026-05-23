# FastAPI + Docker + Azure (Lab 10 — Exercícios 10.3 e 10.4)

API RESTful em FastAPI conteinerizada com Docker e publicada no Azure App Service for Containers, com CI/CD via GitHub Actions.

## Stack
- Python 3.11
- FastAPI + Uvicorn
- Pydantic
- Docker
- Azure Container Registry (ACR)
- Azure App Service for Containers
- GitHub Actions (CI/CD)

## Estrutura do projeto
```
FastAPI_Docker/
├── main.py             # API FastAPI (CRUD em memória)
├── requirements.txt    # Dependências Python
├── Dockerfile          # Imagem da aplicação
├── .dockerignore       # Arquivos ignorados no build da imagem
├── .gitignore          # Arquivos ignorados no git
└── README.md
```

## Endpoints
| Método | Rota         | Descrição               | Status sucesso |
|--------|--------------|-------------------------|----------------|
| GET    | `/`          | Lista todos os itens    | 200            |
| GET    | `/{item_id}` | Retorna um item         | 200 / 404      |
| POST   | `/`          | Cria um item            | 201            |
| PUT    | `/{item_id}` | Atualiza um item        | 200 / 404      |
| DELETE | `/{item_id}` | Remove um item          | 200            |

Documentação interativa (Swagger UI): `/docs`

## Executar localmente (Docker)
```powershell
docker build -t fastapi-lab10 .
docker run -d -p 8000:8000 --name fastapi-lab10-container fastapi-lab10
```
Acessar: http://localhost:8000/ e http://localhost:8000/docs

Encerrar:
```powershell
docker stop fastapi-lab10-container
docker rm fastapi-lab10-container
```

## Deploy na Azure (resumo)
1. Push da imagem para o **Azure Container Registry**.
2. **App Service for Containers** consome a imagem do ACR.
3. **Deployment Center** do App Service conectado a este repositório GitHub gera o workflow `.github/workflows/main_<app>.yml` automaticamente.
4. Cada `git push` em `main` dispara o GitHub Actions, que faz build da imagem, push para o ACR e redeploy no App Service.

A aplicação publicada usa a variável de ambiente `PORT` injetada pelo App Service (fallback para 8000 em execução local) — ver `CMD` do Dockerfile.

## URL de produção
`https://<nome-do-app>.azurewebsites.net`

## Autor
André Tozi Magalhães — Lab 10, Exercícios 10.3 e 10.4.
