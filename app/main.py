import uvicorn
from fastapi import FastAPI
from routes import user_route

app = FastAPI()
app.include_router(user_route.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(app)
