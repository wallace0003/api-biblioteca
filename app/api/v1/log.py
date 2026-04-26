from fastapi import APIRouter, Depends, HTTPException
from app.services.log_service import LogService
from app.schemas.log import LogResponse
from app.db.mongo.mongo_client import MongoClientManager
from typing import List
from app.api.dependecies import get_mongo


router = APIRouter()


def get_log_service(mongo: MongoClientManager = Depends(get_mongo)):
    return LogService(mongo)


@router.get("/", response_model=List[LogResponse])
def get_logs(service: LogService = Depends(get_log_service)):
    try:
        return service.get_all()
    except Exception as e:
        return{
            "error" : "Not found"
        }

@router.get("/event/{event}", response_model=List[LogResponse])
def get_logs_by_event(event: str, service: LogService = Depends(get_log_service)):
    try:
        return service.get_by_event(event)
    except Exception as e:
        return{
            "error" : "Not found"
        }

@router.get("/{log_id}", response_model=LogResponse)
def get_log(log_id: str, service: LogService = Depends(get_log_service)):
    try:
        log = service.get_by_id(log_id)

        if not log:
            raise HTTPException(status_code=404, detail="Log not found")

        return log
    except Exception as e:
        return{
            "error" : "Not found"
        }


@router.delete("/{log_id}")
def delete_log(log_id: str, service: LogService = Depends(get_log_service)):
    try:
        success = service.delete(log_id)

        if not success:
            raise HTTPException(status_code=404, detail="Log not found")

        return {"message": "Log deleted successfully"}
    except Exception as e:
        return{
            "error" : "Not found"
        }


@router.delete("/")
def delete_all_logs(service: LogService = Depends(get_log_service)):
    try:
        count = service.delete_all()
        return {"deleted": count}

    except Exception as e:
        return{
            "error" : "Not found"
        }
