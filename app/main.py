from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.core.settings import Settings
from app.helpers.response import BaseFailResponse
from app.v1 import v1_router


app = FastAPI(
    title=Settings.PROJECT_NAME,
    version=Settings.VERSION
)
app.include_router(v1_router)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc) -> JSONResponse:
    return JSONResponse(
        content=BaseFailResponse(detail="Validation error").model_dump(),
        status_code=status.HTTP_400_BAD_REQUEST
    )
