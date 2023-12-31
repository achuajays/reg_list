from pydantic import BaseModel


class R(BaseModel):
    id : int
    name : str 
    cource : str
    email : str