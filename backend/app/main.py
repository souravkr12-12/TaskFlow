from fastapi import FastAPI
from app.database import Base,engine
from app.models import Task
from app.routers.task import router
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI(
  title="TaskFlow API",
  description="A production-ready Task Management API built with FastAPI.",
  version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
def root():
  return{
    "message":"Welcome to TaskFlow API 🚀"
  }
