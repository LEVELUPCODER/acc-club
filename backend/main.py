from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from routes import registrations, projects, team

# Initialize FastAPI app
app = FastAPI(
    title="ACC Club API",
    description="Analytics & Consultancy Club Backend API",
    version="1.0.0",
    docs_url="/docs",
    openapi_url="/openapi.json"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:5173", "file:///", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(registrations.router)
app.include_router(projects.router)
app.include_router(team.router)

# Health check endpoint
@app.get("/health")
async def health_check():
    """API health check endpoint"""
    return {
        "status": "healthy",
        "service": "ACC Club Backend API",
        "version": "1.0.0"
    }

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint with API information"""
    return {
        "message": "Welcome to ACC Club Backend API",
        "documentation": "/docs",
        "openapi": "/openapi.json",
        "endpoints": {
            "registrations": "/api/registrations",
            "projects": "/api/projects",
            "team": "/api/team"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
