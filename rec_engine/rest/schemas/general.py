from pydantic import BaseModel

class GeneralErrorResponseSchema(BaseModel):
    message: str