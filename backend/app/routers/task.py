from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.schemas.task import TaskCreate,TaskUpdate,TaskResponse
from app.crud.task import(
  create_task,
  get_tasks,
  get_task,
  update_task,
  delete_task
)

router=APIRouter(prefix="/tasks",tags=["Tasks"])

@router.post("/",response_model=TaskResponse)
def create(task:TaskCreate,db:Session=Depends(get_db)):
  return create_task(db,task)

@router.get("/", response_model=list[TaskResponse])
def read_all(db: Session = Depends(get_db)):
    return get_tasks(db)

@router.get("/{task_id}", response_model=TaskResponse)
def read_one(task_id: int, db: Session = Depends(get_db)):
    task = get_task(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return task

@router.put("/{task_id}", response_model=TaskResponse)
def update(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    updated = update_task(db, task_id, task)

    if not updated:
        raise HTTPException(status_code=404, detail="Task not found")

    return updated

@router.delete("/{task_id}")
def delete(task_id: int, db: Session = Depends(get_db)):
    deleted = delete_task(db, task_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")

    return {"message": "Task deleted successfully"}