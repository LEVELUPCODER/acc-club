from fastapi import APIRouter, HTTPException, status
from typing import List
from schemas import RegistrationCreate, Registration, SuccessResponse

router = APIRouter(prefix="/api/registrations", tags=["Registrations"])

# In-memory storage (replace with database in production)
registrations_db = []

@router.post("/", response_model=SuccessResponse, status_code=status.HTTP_201_CREATED)
async def create_registration(registration: RegistrationCreate):
    """Create a new member registration"""
    try:
        new_reg = {
            "id": len(registrations_db) + 1,
            "name": registration.name,
            "email": registration.email,
            "phone": registration.phone,
            "year": registration.year,
            "branch": registration.branch,
            "interests": registration.interests or [],
            "status": "pending",
            "created_at": "2024-03-23T00:00:00"
        }
        registrations_db.append(new_reg)
        return {
            "success": True,
            "message": "Registration created successfully",
            "data": {"id": new_reg["id"], "status": "pending"}
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Registration failed: {str(e)}"
        )

@router.get("/", response_model=SuccessResponse)
async def list_registrations(status_filter: str = None, limit: int = 100, offset: int = 0):
    """Get all registrations with optional filtering"""
    try:
        filtered_regs = registrations_db
        
        if status_filter:
            filtered_regs = [r for r in filtered_regs if r["status"] == status_filter]
        
        paginated = filtered_regs[offset:offset + limit]
        
        return {
            "success": True,
            "message": f"Retrieved {len(paginated)} registrations",
            "data": {
                "registrations": paginated,
                "total": len(filtered_regs),
                "limit": limit,
                "offset": offset
            }
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.get("/{registration_id}", response_model=SuccessResponse)
async def get_registration(registration_id: int):
    """Get a specific registration by ID"""
    try:
        reg = next((r for r in registrations_db if r["id"] == registration_id), None)
        if not reg:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Registration not found"
            )
        return {
            "success": True,
            "message": "Registration retrieved successfully",
            "data": reg
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.patch("/{registration_id}/approve", response_model=SuccessResponse)
async def approve_registration(registration_id: int):
    """Approve a registration"""
    try:
        reg = next((r for r in registrations_db if r["id"] == registration_id), None)
        if not reg:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Registration not found"
            )
        reg["status"] = "approved"
        return {
            "success": True,
            "message": "Registration approved successfully",
            "data": {"id": registration_id, "status": "approved"}
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.patch("/{registration_id}/reject", response_model=SuccessResponse)
async def reject_registration(registration_id: int):
    """Reject a registration"""
    try:
        reg = next((r for r in registrations_db if r["id"] == registration_id), None)
        if not reg:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Registration not found"
            )
        reg["status"] = "rejected"
        return {
            "success": True,
            "message": "Registration rejected",
            "data": {"id": registration_id, "status": "rejected"}
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
