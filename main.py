from fastapi import FastAPI , HTTPException 
from fastapi.middleware.cors import CORSMiddleware
from database import *

app = FastAPI()


origins = ['http://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers=['*'],
)

@app.get('/')
async def get_v():
    responce = await fetch()
    return responce

@app.post('/p/')
async def get_p(t : R):
    responce = await create_list(t.dict())
    if responce:
        return "record created"
    raise HTTPException(400,'no record created')

@app.delete('/d/{item_id}')
async def get_d(item_id : int ):
    responce = await delete(item_id)
    if responce:
        return "record deleted"
    raise HTTPException(404,'no record  found to delete')

