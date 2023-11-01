from fastapi import FastAPI
import uvicorn

from routes.api import router as api_router

def create_app() -> FastAPI:
    app_ = FastAPI()
    app_.include_router(api_router)
    return app_


app = create_app()


@app.get("/")
def read_root():
    return {"message": "Recommendation Engine is Up and Running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9000, reload=True, log_level="info")
