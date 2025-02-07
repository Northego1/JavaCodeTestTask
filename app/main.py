import uvicorn
from fastapi import FastAPI
from api.v1 import routes




app = FastAPI()


app.include_router(routes.router)



if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)