from fastapi import FastAPI

from app import database, models, routes

app = FastAPI(
    title="Notes API",
    description="FastAPI + SQLAlchemy + SQLite Notes Management API",
    version="1.0.0"
)


@app.on_event("startup")
async def startup():
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


app.include_router(routes.router)


@app.get("/")
async def root():
    return {
        "message": "Notes API",
        "docs": "/docs",
        "redoc": "/redoc"
    }