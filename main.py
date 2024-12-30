from fastapi import FastAPI
from apis import user
from database.database import Base, engine
app = FastAPI()

Base.metadata.create_all(bind = engine)

app.include_router(user.router, prefix="/api/v1", tags=["users"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)