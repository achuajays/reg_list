from model import R
import motor.motor_asyncio

c = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017/')
d = c.reg
collection = d.reg_li


async def fetch():
    l = []
    c = collection.find({})
    async for i in c:
        l.append(R(**i))
    return l


async def create_list(todo):
    d  = todo
    r = await collection.insert_one(d)
    return r 

async def delete(id):
    await collection.delete_one({'id':id})
    return True

