from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routers
from app.api.v1 import health

app = FastAPI(
    docs_url="/api/docs",
    openapi_url="/api/openapi.json"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Router
app.include_router(health.router, prefix="/api")
