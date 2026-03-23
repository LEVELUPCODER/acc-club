from datetime import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List

# User Models
class UserBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    phone: Optional[str] = None

class UserCreate(UserBase):
    password: str = Field(..., min_length=6)

class UserUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# Registration Models
class RegistrationBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    email: EmailStr
    phone: str = Field(..., regex=r"^\+?1?\d{9,15}$")
    year: int = Field(..., ge=1, le=4)
    branch: str = Field(..., min_length=1)
    interests: Optional[List[str]] = None

class RegistrationCreate(RegistrationBase):
    pass

class Registration(RegistrationBase):
    id: int
    status: str = "pending"  # pending, approved, rejected
    created_at: datetime
    
    class Config:
        from_attributes = True

# Project Models
class ProjectBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    description: str
    domain: str  # Finance, Technology, Strategy
    status: str = "active"  # active, completed, on_hold

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

# Team Member Models
class TeamMemberBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    position: str
    email: EmailStr
    bio: Optional[str] = None

class TeamMemberCreate(TeamMemberBase):
    pass

class TeamMember(TeamMemberBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

# Response Models
class SuccessResponse(BaseModel):
    success: bool = True
    message: str
    data: Optional[dict] = None

class ErrorResponse(BaseModel):
    success: bool = False
    error: str
    details: Optional[dict] = None
