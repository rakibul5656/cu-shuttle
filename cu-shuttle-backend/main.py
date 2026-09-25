# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import create_database
from routers import location


app = FastAPI(
    title="CU Shuttle Live API",
    version="1.0.0"
)


# ============================================================
# CORS
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============================================================
# DATABASE
# ============================================================

create_database()


# ============================================================
# ROUTERS
# ============================================================

app.include_router(location.router)


# ============================================================
# HOME
# ============================================================

@app.get("/")
def home():

    return {
        "status": "online",
        "service": "CU Shuttle Live API"
    }