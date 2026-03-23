from fastapi import APIRouter, HTTPException, status
from schemas import TeamMemberCreate, TeamMember, SuccessResponse

router = APIRouter(prefix="/api/team", tags=["Team"])

# In-memory storage (replace with database in production)
team_db = [
    {
        "id": 1,
        "name": "Anant Chaudhary",
        "position": "Club President",
        "email": "anant@accclub.in",
        "bio": "Visionary leader driving ACC's mission to empower students with advanced analytics and strategic consulting expertise",
        "created_at": "2024-01-01T00:00:00"
    },
    {
        "id": 2,
        "name": "Mohit Raj",
        "position": "Finance Head",
        "email": "mohit@accclub.in",
        "bio": "Financial analyst specializing in investment strategies, market analytics, and data-driven financial forecasting",
        "created_at": "2024-01-02T00:00:00"
    },
    {
        "id": 3,
        "name": "Tushar Kumar",
        "position": "Strategy Head",
        "email": "tushar@accclub.in",
        "bio": "Strategic consultant with expertise in business planning, market analysis, and competitive positioning strategies",
        "created_at": "2024-01-03T00:00:00"
    },
    {
        "id": 4,
        "name": "Ravi Ranjan",
        "position": "Operations Manager",
        "email": "ravi@accclub.in",
        "bio": "Operations expert ensuring seamless execution of events, projects, and initiatives with precision and efficiency",
        "created_at": "2024-01-04T00:00:00"
    }
]

@router.post("/", response_model=SuccessResponse, status_code=status.HTTP_201_CREATED)
async def add_team_member(member: TeamMemberCreate):
    """Add a new team member"""
    try:
        new_member = {
            "id": max([m["id"] for m in team_db], default=0) + 1,
            "name": member.name,
            "position": member.position,
            "email": member.email,
            "bio": member.bio or "",
            "created_at": "2024-03-23T00:00:00"
        }
        team_db.append(new_member)
        return {
            "success": True,
            "message": "Team member added successfully",
            "data": new_member
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.get("/", response_model=SuccessResponse)
async def list_team_members():
    """Get all team members"""
    try:
        return {
            "success": True,
            "message": f"Retrieved {len(team_db)} team members",
            "data": {
                "team": team_db,
                "total": len(team_db)
            }
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.get("/{member_id}", response_model=SuccessResponse)
async def get_team_member(member_id: int):
    """Get a specific team member by ID"""
    try:
        member = next((m for m in team_db if m["id"] == member_id), None)
        if not member:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Team member not found"
            )
        return {
            "success": True,
            "message": "Team member retrieved successfully",
            "data": member
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.put("/{member_id}", response_model=SuccessResponse)
async def update_team_member(member_id: int, member_update: TeamMemberCreate):
    """Update a team member"""
    try:
        member = next((m for m in team_db if m["id"] == member_id), None)
        if not member:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Team member not found"
            )
        member.update({
            "name": member_update.name,
            "position": member_update.position,
            "email": member_update.email,
            "bio": member_update.bio
        })
        return {
            "success": True,
            "message": "Team member updated successfully",
            "data": member
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

@router.delete("/{member_id}", response_model=SuccessResponse)
async def remove_team_member(member_id: int):
    """Remove a team member"""
    try:
        global team_db
        member = next((m for m in team_db if m["id"] == member_id), None)
        if not member:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Team member not found"
            )
        team_db = [m for m in team_db if m["id"] != member_id]
        return {
            "success": True,
            "message": "Team member removed successfully",
            "data": {"id": member_id}
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )
