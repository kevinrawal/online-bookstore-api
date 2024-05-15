from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    """_summary_

    Returns:
        _type_: _description_
    """
    return {"message": "mkfvkfvkfdm World"}

if __name__ == "__main__":
    uvicorn.run(app)
