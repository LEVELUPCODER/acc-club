"""
Vercel Serverless FastAPI Handler for ACC Club
Minimal version that works reliably on Vercel
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from datetime import datetime
import json

# Initialize FastAPI app
app = FastAPI(
    title="ACC Club API",
    description="Analytics & Consultancy Club Backend API",
    version="1.0.0",
    docs_url="/docs",
    openapi_url="/openapi.json"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==================== DATA MODELS ====================

class Registration(BaseModel):
    name: str
    email: EmailStr
    phone: str
    enrollment_no: str
    department: str
    semester: int
    why_join: str

class Team(BaseModel):
    id: int
    name: str
    position: str
    description: str
    email: str
    social_links: Optional[dict] = None

class Project(BaseModel):
    id: int
    name: str
    description: str
    category: str
    status: str
    team_lead: str

# ==================== IN-MEMORY DATA ====================

registrations_db = []
team_db = [
    {
        "id": 1,
        "name": "Anant Chaudhary",
        "position": "President",
        "description": "Visionary leader | Market analysis expert | 5+ years experience",
        "email": "anant@accclub.com",
        "social_links": {"linkedin": "linkedin.com/in/anant"}
    },
    {
        "id": 2,
        "name": "Mohit Raj",
        "position": "Finance Head",
        "description": "Financial strategist | Budget management specialist | CFA candidate",
        "email": "mohit@accclub.com",
        "social_links": {"linkedin": "linkedin.com/in/mohit"}
    },
    {
        "id": 3,
        "name": "Tushar Kumar",
        "position": "Strategy Lead",
        "description": "Business strategist | Corporate consultant | MBA graduate",
        "email": "tushar@accclub.com",
        "social_links": {"linkedin": "linkedin.com/in/tushar"}
    },
    {
        "id": 4,
        "name": "Ravi Ranjan",
        "position": "Operations Manager",
        "description": "Process optimization expert | Project coordinator | 3+ years experience",
        "email": "ravi@accclub.com",
        "social_links": {"linkedin": "linkedin.com/in/ravi"}
    }
]

projects_db = [
    {
        "id": 1,
        "name": "Market Analysis 2024",
        "description": "Comprehensive analysis of current market trends and opportunities",
        "category": "Finance",
        "status": "In Progress",
        "team_lead": "Mohit Raj"
    },
    {
        "id": 2,
        "name": "Business Strategy Workshop",
        "description": "Strategic planning and execution workshop for emerging businesses",
        "category": "Strategy",
        "status": "Active",
        "team_lead": "Tushar Kumar"
    }
]

# ==================== HEALTH & ROOT ENDPOINTS ====================

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "ACC Club API",
        "version": "1.0.0"
    }

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to ACC Club API",
        "documentation": "/docs",
        "endpoints": {
            "health": "/health",
            "registrations": "/api/registrations",
            "team": "/api/team",
            "projects": "/api/projects"
        }
    }

# ==================== REGISTRATION ENDPOINTS ====================

@app.post("/api/registrations")
async def create_registration(reg: Registration):
    """Create new registration"""
    registration = {
        "id": len(registrations_db) + 1,
        **reg.dict(),
        "status": "pending",
        "created_at": datetime.utcnow().isoformat()
    }
    registrations_db.append(registration)
    return {
        "success": True,
        "message": "Registration submitted successfully",
        "data": registration
    }

@app.get("/api/registrations")
async def get_registrations():
    """Get all registrations"""
    return {
        "success": True,
        "data": registrations_db,
        "count": len(registrations_db)
    }

@app.get("/api/registrations/{registration_id}")
async def get_registration(registration_id: int):
    """Get specific registration"""
    for reg in registrations_db:
        if reg["id"] == registration_id:
            return {"success": True, "data": reg}
    raise HTTPException(status_code=404, detail="Registration not found")

# ==================== TEAM ENDPOINTS ====================

@app.get("/api/team")
async def get_team():
    """Get all team members"""
    return {
        "success": True,
        "data": team_db,
        "count": len(team_db)
    }

@app.get("/api/team/{team_id}")
async def get_team_member(team_id: int):
    """Get specific team member"""
    for member in team_db:
        if member["id"] == team_id:
            return {"success": True, "data": member}
    raise HTTPException(status_code=404, detail="Team member not found")

# ==================== PROJECT ENDPOINTS ====================

@app.get("/api/projects")
async def get_projects():
    """Get all projects"""
    return {
        "success": True,
        "data": projects_db,
        "count": len(projects_db)
    }

@app.get("/api/projects/{project_id}")
async def get_project(project_id: int):
    """Get specific project"""
    for project in projects_db:
        if project["id"] == project_id:
            return {"success": True, "data": project}
    raise HTTPException(status_code=404, detail="Project not found")

# ==================== VERCEL HANDLER ====================

handler = app
