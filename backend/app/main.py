from fastapi import FastAPI
from app.database import Base,engine
from app.models import Task
from app.routers.task import router
app=FastAPI(
  title="TaskFlow API",
  version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(router)

@app.get("/")
def root():
  return{
    "message":"Welcome to TaskFlow API 🚀"
  }
