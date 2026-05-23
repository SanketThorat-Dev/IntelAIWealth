from fastapi import FastAPI
from Backend.app.api.routes.upload import router as upload_router

app = FastAPI(
    title="IntelAIWealth API",
    description="AI-powered personal finance intelligence platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to IntelAIWealth API"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }

# Register routers
app.include_router(upload_router)