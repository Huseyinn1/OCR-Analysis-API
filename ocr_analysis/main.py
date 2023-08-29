from fastapi import FastAPI
from ocr_analysis.api.routers import router

app = FastAPI()

app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("ocr_analysis.main:app", host="0.0.0.0", port=8000)