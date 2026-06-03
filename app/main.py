from fastapi import FastAPI

from app.database import engine, Base

from app.routes.sessions import router as sessions_router
from app.routes.users import router as users_router
from app.routes.plans import router as plans_router
from app.routes.auth import router as auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(sessions_router)
app.include_router(users_router)
app.include_router(plans_router)
app.include_router(auth_router)


@app.get("/")
def root():
    return {"message": "Running API"}
