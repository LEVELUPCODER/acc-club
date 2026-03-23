"""
Constants and configuration values for ACC Club Backend API
"""

from enum import Enum

# ==============================================================================
# REGISTRATION CONSTANTS
# ==============================================================================

class RegistrationStatus(str, Enum):
    """Registration status enum"""
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


REGISTRATION_STATUS_VALUES = [
    RegistrationStatus.PENDING.value,
    RegistrationStatus.APPROVED.value,
    RegistrationStatus.REJECTED.value,
]

REGISTRATION_STATUSES = {
    "pending": "Awaiting approval",
    "approved": "Registration approved",
    "rejected": "Registration rejected",
}

# Validation limits
REGISTRATION_LIMITS = {
    "name_min": 3,
    "name_max": 100,
    "email_max": 255,
    "enrollment_no_length": 10,
    "why_join_min": 20,
    "why_join_max": 1000,
    "phone_min": 10,
    "phone_max": 20,
    "semester_min": 1,
    "semester_max": 8,
}

VALID_DEPARTMENTS = [
    "Computer Science",
    "Mechanical Engineering",
    "Electrical Engineering",
    "Civil Engineering",
    "Electronics & Communication",
    "Chemical Engineering",
    "Biotechnology",
    "Engineering Physics",
    "Business Administration",
    "Other",
]


# ==============================================================================
# PROJECT CONSTANTS
# ==============================================================================

class ProjectStatus(str, Enum):
    """Project status enum"""
    PLANNING = "planning"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ON_HOLD = "on_hold"


PROJECT_STATUS_VALUES = [
    ProjectStatus.PLANNING.value,
    ProjectStatus.IN_PROGRESS.value,
    ProjectStatus.COMPLETED.value,
    ProjectStatus.ON_HOLD.value,
]

PROJECT_STATUSES = {
    "planning": "Project in planning phase",
    "in_progress": "Project currently in progress",
    "completed": "Project completed successfully",
    "on_hold": "Project temporarily on hold",
}

VALID_DOMAINS = [
    "Finance",
    "Strategy",
    "Operations",
    "Market Research",
    "Data Analytics",
    "Business Development",
    "Technology",
    "Human Resources",
    "Sustainability",
    "Other",
]

PROJECT_LIMITS = {
    "name_min": 5,
    "name_max": 255,
    "description_min": 20,
    "description_max": 2000,
    "domain_max": 100,
    "max_members_min": 1,
    "max_members_max": 100,
}


# ==============================================================================
# TEAM MEMBER CONSTANTS
# ==============================================================================

class TeamPosition(str, Enum):
    """Team position enum"""
    PRESIDENT = "Club President"
    VICE_PRESIDENT = "Vice President"
    FINANCE_HEAD = "Finance Head"
    STRATEGY_HEAD = "Strategy Head"
    OPERATIONS_HEAD = "Operations Manager"
    CORE_MEMBER = "Core Member"
    MEMBER = "Member"


TEAM_POSITIONS = [position.value for position in TeamPosition]

TEAM_MEMBER_LIMITS = {
    "name_min": 3,
    "name_max": 255,
    "position_max": 255,
    "bio_max": 1000,
    "email_max": 255,
    "domain_max": 100,
    "phone_max": 20,
}


# ==============================================================================
# USER CONSTANTS
# ==============================================================================

USER_LIMITS = {
    "name_min": 3,
    "name_max": 255,
    "email_max": 255,
    "enrollment_no_length": 10,
    "department_max": 100,
    "phone_max": 20,
}


# ==============================================================================
# API RESPONSE CONSTANTS
# ==============================================================================

class ResponseMessage(str, Enum):
    """Standard response messages"""
    SUCCESS = "Operation successful"
    REGISTRATION_CREATED = "Registration created successfully"
    REGISTRATION_APPROVED = "Registration approved successfully"
    REGISTRATION_REJECTED = "Registration rejected"
    REGISTRATION_RETRIEVED = "Registration retrieved successfully"
    REGISTRATION_UPDATED = "Registration updated successfully"
    REGISTRATION_DELETED = "Registration deleted successfully"
    
    PROJECT_CREATED = "Project created successfully"
    PROJECT_RETRIEVED = "Project retrieved successfully"
    PROJECT_UPDATED = "Project updated successfully"
    PROJECT_DELETED = "Project deleted successfully"
    
    TEAM_MEMBER_ADDED = "Team member added successfully"
    TEAM_MEMBER_RETRIEVED = "Team member retrieved successfully"
    TEAM_MEMBER_UPDATED = "Team member updated successfully"
    TEAM_MEMBER_DELETED = "Team member deleted successfully"
    
    ITEMS_RETRIEVED = "Items retrieved successfully"
    NOT_FOUND = "Resource not found"
    INVALID_REQUEST = "Invalid request parameters"
    DUPLICATE_ENTRY = "Resource already exists"
    UNAUTHORIZED = "Unauthorized access"
    FORBIDDEN = "Access forbidden"
    SERVER_ERROR = "Internal server error"


# ==============================================================================
# PAGINATION CONSTANTS
# ==============================================================================

PAGINATION = {
    "default_page_size": 10,
    "max_page_size": 100,
    "default_skip": 0,
}


# ==============================================================================
# CORS CONSTANTS
# ==============================================================================

ALLOWED_FRONTENDS = [
    "http://localhost:3000",           # React default
    "http://localhost:5173",           # Vite default
    "http://localhost:8080",           # Vue default
    "http://localhost:5000",           # Flask default
    "http://localhost:3001",           # Next.js alternative
    "file://",                         # Local file access
    "http://127.0.0.1:3000",          # Localhost alternative
    "http://127.0.0.1:5173",
]

CORS_ALLOW_METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
CORS_ALLOW_HEADERS = ["Content-Type", "Authorization"]


# ==============================================================================
# API DOCUMENTATION CONSTANTS
# ==============================================================================

API_TITLE = "ACC Club API"
API_VERSION = "1.0.0"
API_DESCRIPTION = "Analytics & Consultancy Club Backend API"
API_CONTACT = {
    "name": "ACC Club Support",
    "email": "support@accclub.com",
}

TAGS_METADATA = [
    {
        "name": "registrations",
        "description": "Member registration operations",
    },
    {
        "name": "projects",
        "description": "Project management operations",
    },
    {
        "name": "team",
        "description": "Team member management operations",
    },
    {
        "name": "health",
        "description": "API health and status checks",
    },
]


# ==============================================================================
# LOGGING CONSTANTS
# ==============================================================================

LOG_LEVELS = {
    "DEBUG": 10,
    "INFO": 20,
    "WARNING": 30,
    "ERROR": 40,
    "CRITICAL": 50,
}

LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


# ==============================================================================
# TIMEZONE CONSTANTS
# ==============================================================================

DEFAULT_TIMEZONE = "UTC"
INDIA_TIMEZONE = "Asia/Kolkata"


# ==============================================================================
# FILE UPLOAD CONSTANTS
# ==============================================================================

MAX_UPLOAD_SIZE = 10 * 1024 * 1024  # 10MB
ALLOWED_IMAGE_TYPES = ["image/jpeg", "image/png", "image/gif", "image/webp"]
ALLOWED_DOCUMENT_TYPES = [
    "application/pdf",
    "application/msword",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
]


# ==============================================================================
# CACHE CONSTANTS
# ==============================================================================

CACHE_EXPIRY = {
    "team_members": 3600,      # 1 hour
    "projects": 1800,          # 30 minutes
    "registrations": 300,      # 5 minutes
}


# ==============================================================================
# FEATURE FLAGS
# ==============================================================================

FEATURES = {
    "authentication": False,           # JWT authentication enabled
    "database": False,                 # Database integration enabled
    "file_upload": False,              # File upload enabled
    "email_notification": False,       # Email notifications enabled
    "rate_limiting": False,            # Rate limiting enabled
    "caching": False,                  # Response caching enabled
}


# ==============================================================================
# ERROR CODES
# ==============================================================================

class ErrorCode(str, Enum):
    """Custom error codes"""
    VALIDATION_ERROR = "VALIDATION_ERROR"
    NOT_FOUND = "NOT_FOUND"
    DUPLICATE_ENTRY = "DUPLICATE_ENTRY"
    UNAUTHORIZED = "UNAUTHORIZED"
    FORBIDDEN = "FORBIDDEN"
    SERVER_ERROR = "SERVER_ERROR"
    DATABASE_ERROR = "DATABASE_ERROR"
    EXTERNAL_SERVICE_ERROR = "EXTERNAL_SERVICE_ERROR"


# ==============================================================================
# DEFAULT DATA
# ==============================================================================

# Sample projects for initialization
DEFAULT_PROJECTS = [
    {
        "id": 1,
        "name": "Market Analysis Q1 2024",
        "description": "Comprehensive market analysis covering industry trends, competitive landscape, and growth opportunities for Q1 2024.",
        "domain": "Finance",
        "status": "planning",
    },
    {
        "id": 2,
        "name": "Business Strategy Review",
        "description": "Strategic review of business operations, identifying key areas for improvement and growth potential.",
        "domain": "Strategy",
        "status": "in_progress",
    },
]

# Sample team members
DEFAULT_TEAM = [
    {
        "id": 1,
        "name": "Anant Chaudhary",
        "position": "Club President",
        "domain": "Executive",
        "bio": "Visionary leader with expertise in analytics and strategic planning.",
        "is_active": True,
    },
    {
        "id": 2,
        "name": "Mohit Raj",
        "position": "Finance Head",
        "domain": "Finance",
        "bio": "Financial expert focused on data-driven decision making.",
        "is_active": True,
    },
    {
        "id": 3,
        "name": "Tushar Kumar",
        "position": "Strategy Head",
        "domain": "Strategy",
        "bio": "Strategic thinker dedicated to organizational excellence.",
        "is_active": True,
    },
    {
        "id": 4,
        "name": "Ravi Ranjan",
        "position": "Operations Manager",
        "domain": "Operations",
        "bio": "Operations specialist ensuring smooth execution of all projects.",
        "is_active": True,
    },
]


if __name__ == "__main__":
    print("ACC Club Backend Constants")
    print("=" * 80)
    print(f"Valid Departments: {len(VALID_DEPARTMENTS)}")
    print(f"Valid Domains: {len(VALID_DOMAINS)}")
    print(f"Default Projects: {len(DEFAULT_PROJECTS)}")
    print(f"Default Team Members: {len(DEFAULT_TEAM)}")
    print(f"Allowed Frontends: {len(ALLOWED_FRONTENDS)}")
