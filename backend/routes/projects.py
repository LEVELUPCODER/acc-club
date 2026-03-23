from fastapi import APIRouter, HTTPException, status
from typing import List
from schemas import ProjectCreate, Project, SuccessResponse

router = APIRouter(prefix="/api/projects", tags=["Projects"])

# In-memory storage (replace with database in production)
projects_db = [
    {
        "id": 1,
        "title": "Market Analysis Dashboard",
        "description": "Real-time market trends visualization using data analytics",
        "domain": "Finance",
        "status": "active",
        "created_at": "2024-01-15T00:00:00",
        "updated_at": "2024-03-20T00:00:00"
    },
    {
        "id": 2,
        "title": "Business Strategy Optimization",
        "description": "Strategic planning framework for emerging startups",
        "domain": "Strategy",
        "status": "active",
        "created_at": "2024-02-10T00:00:00",
        "updated_at": "2024-03-18T00:00:00"
    }
]

@router.post("/", response_model=SuccessResponse, status_code=status.HTTP_201_CREATED)
async def create_project(project: ProjectCreate):
    """Create a new project"""
    try:
        new_project = {
            "id": max([p["id"] for p in projects_db], default=0) + 1,
            "title": project.title,
            "description": project.description,
            "domain": project.domain,
            "status": project.status,
            "created_at": "2024-03-23T00:00:00",
            "updated_at": "2024-03-23T00:00:00"
        }
        projects_db.append(new_project)
        return {
            "success": True,
            "message": "Project created successfully",
            "data": new_project
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.get("/", response_model=SuccessResponse)
async def list_projects(domain: str = None, status_filter: str = None):
    """Get all projects with optional filtering"""
    try:
        filtered_projects = projects_db
        
        if domain:
            filtered_projects = [p for p in filtered_projects if p["domain"] == domain]
        
        if status_filter:
            filtered_projects = [p for p in filtered_projects if p["status"] == status_filter]
        
        return {
            "success": True,
            "message": f"Retrieved {len(filtered_projects)} projects",
            "data": {
                "projects": filtered_projects,
                "total": len(filtered_projects)
            }
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.get("/{project_id}", response_model=SuccessResponse)
async def get_project(project_id: int):
    """Get a specific project by ID"""
    try:
        project = next((p for p in projects_db if p["id"] == project_id), None)
        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found"
            )
        return {
            "success": True,
            "message": "Project retrieved successfully",
            "data": project
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.put("/{project_id}", response_model=SuccessResponse)
async def update_project(project_id: int, project_update: ProjectCreate):
    """Update a project"""
    try:
        project = next((p for p in projects_db if p["id"] == project_id), None)
        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found"
            )
        project.update({
            "title": project_update.title,
            "description": project_update.description,
            "domain": project_update.domain,
            "status": project_update.status,
            "updated_at": "2024-03-23T00:00:00"
        })
        return {
            "success": True,
            "message": "Project updated successfully",
            "data": project
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.delete("/{project_id}", response_model=SuccessResponse)
async def delete_project(project_id: int):
    """Delete a project"""
    try:
        global projects_db
        project = next((p for p in projects_db if p["id"] == project_id), None)
        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Project not found"
            )
        projects_db = [p for p in projects_db if p["id"] != project_id]
        return {
            "success": True,
            "message": "Project deleted successfully",
            "data": {"id": project_id}
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
