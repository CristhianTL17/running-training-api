from fastapi import FastAPI

from app.database import engine, Base

from app.routes.sessions import router as sessions_router
from app.routes.users import router as users_router
from app.routes.plans import router as plans_router
from app.routes.auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(sessions_router)
app.include_router(users_router)
app.include_router(plans_router)
app.include_router(auth_router)


@app.get("/")
def root():
    return {"message": "Running API"}
