if __name__ == "__main__":
    import uvicorn
    from fastapi import FastAPI
    app = FastAPI()
    uvicorn.run(app=create_app(), host="0.0.0.0", port=8000,log_level="info")