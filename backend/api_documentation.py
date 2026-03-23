"""
Advanced API Documentation and Examples for ACC Club Backend
"""

API_DOCUMENTATION = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                    ACC CLUB BACKEND API DOCUMENTATION                        ║
║                              Version 1.0.0                                   ║
╚══════════════════════════════════════════════════════════════════════════════╝

═══════════════════════════════════════════════════════════════════════════════
1. BASE SETUP & REQUIREMENTS
═══════════════════════════════════════════════════════════════════════════════

Base URL: http://localhost:8000 (Development)
API Documentation: http://localhost:8000/docs (Swagger UI)
Alternative Docs: http://localhost:8000/redoc (ReDoc)
OpenAPI JSON: http://localhost:8000/openapi.json

Environment: 
- Python 3.8+
- FastAPI 0.104+
- Uvicorn
- SQLAlchemy (for database integration)
- Pydantic v2.5+


═══════════════════════════════════════════════════════════════════════════════
2. CORE ENDPOINTS OVERVIEW
═══════════════════════════════════════════════════════════════════════════════

HEALTH & INFO:
├── GET  /                           → API information
└── GET  /health                     → Health check

REGISTRATIONS:
├── POST   /api/registrations                      → Create new registration
├── GET    /api/registrations                      → List all registrations
├── GET    /api/registrations/{id}                 → Get specific registration
├── PATCH  /api/registrations/{id}/approve        → Approve registration
└── PATCH  /api/registrations/{id}/reject         → Reject registration

PROJECTS:
├── POST   /api/projects             → Create project
├── GET    /api/projects             → List projects (with filters)
├── GET    /api/projects/{id}        → Get specific project
├── PUT    /api/projects/{id}        → Update project
└── DELETE /api/projects/{id}        → Delete project

TEAM MEMBERS:
├── POST   /api/team                 → Add team member
├── GET    /api/team                 → List team members
├── GET    /api/team/{id}            → Get specific member
├── PUT    /api/team/{id}            → Update member
└── DELETE /api/team/{id}            → Delete member


═══════════════════════════════════════════════════════════════════════════════
3. DETAILED ENDPOINT DOCUMENTATION
═══════════════════════════════════════════════════════════════════════════════

──────────────────────────────────────────────────────────────────────────────
3.1 REGISTRATIONS ENDPOINTS
──────────────────────────────────────────────────────────────────────────────

CREATE REGISTRATION (POST /api/registrations)
──────────────────────────────────────────────────────────────────────────────
Description: Create a new member registration
Status Code: 201 Created
Authorization: None

Request Body:
{
    "email": "student@example.com",
    "name": "John Doe",
    "enrollment_no": "2021001001",
    "department": "Computer Science",
    "semester": 4,
    "why_join": "Interested in analytics and consultancy projects",
    "phone": "9876543210"
}

Response (Success):
{
    "success": true,
    "message": "Registration created successfully",
    "data": {
        "id": 1,
        "email": "student@example.com",
        "name": "John Doe",
        "enrollment_no": "2021001001",
        "department": "Computer Science",
        "semester": 4,
        "why_join": "Interested in analytics and consultancy projects",
        "phone": "9876543210",
        "status": "pending",
        "created_at": "2024-01-15T10:30:00"
    }
}

Response (Error):
{
    "success": false,
    "message": "Validation error",
    "data": {
        "field": "email",
        "error": "Invalid email format"
    }
}

Validation Rules:
- email: Valid email format required
- name: 3-100 characters
- enrollment_no: 10 digits (YYYYXXXXXX format)
- department: Valid department
- semester: 1-8
- why_join: 20-1000 characters
- phone: Optional, 10 digits if provided

──────────────────────────────────────────────────────────────────────────────

LIST REGISTRATIONS (GET /api/registrations)
──────────────────────────────────────────────────────────────────────────────
Description: Get list of all registrations with optional filters
Status Code: 200 OK
Authorization: None

Query Parameters:
- status: Filter by status (pending, approved, rejected) - Optional
- skip: Number of records to skip (default: 0) - Optional
- limit: Number of records to return (default: 10, max: 100) - Optional

Example Request: GET /api/registrations?status=pending&skip=0&limit=10

Response:
{
    "success": true,
    "message": "Registrations retrieved successfully",
    "data": [
        {
            "id": 1,
            "email": "student1@example.com",
            "name": "John Doe",
            "status": "pending",
            "created_at": "2024-01-15T10:30:00",
            ...
        },
        {
            "id": 2,
            "email": "student2@example.com",
            "name": "Jane Smith",
            "status": "approved",
            "created_at": "2024-01-16T11:15:00",
            ...
        }
    ],
    "pagination": {
        "total": 50,
        "page": 1,
        "pages": 5,
        "limit": 10,
        "skip": 0
    }
}

──────────────────────────────────────────────────────────────────────────────

GET SPECIFIC REGISTRATION (GET /api/registrations/{id})
──────────────────────────────────────────────────────────────────────────────
Description: Retrieve a specific registration by ID
Status Code: 200 OK
Authorization: None

Path Parameters:
- id: Registration ID (integer)

Example Request: GET /api/registrations/1

Response:
{
    "success": true,
    "message": "Registration retrieved successfully",
    "data": {
        "id": 1,
        "email": "student@example.com",
        "name": "John Doe",
        "enrollment_no": "2021001001",
        "department": "Computer Science",
        "semester": 4,
        "why_join": "Interested in analytics",
        "phone": "9876543210",
        "status": "pending",
        "created_at": "2024-01-15T10:30:00",
        "reviewed_at": null
    }
}

Error Response (404):
{
    "success": false,
    "message": "Registration not found",
    "data": null
}

──────────────────────────────────────────────────────────────────────────────

APPROVE REGISTRATION (PATCH /api/registrations/{id}/approve)
──────────────────────────────────────────────────────────────────────────────
Description: Approve a pending registration
Status Code: 200 OK
Authorization: Admin only (future implementation)

Path Parameters:
- id: Registration ID

Example Request: PATCH /api/registrations/1/approve

Response:
{
    "success": true,
    "message": "Registration approved successfully",
    "data": {
        "id": 1,
        "status": "approved",
        "reviewed_at": "2024-01-15T15:45:00"
    }
}

──────────────────────────────────────────────────────────────────────────────

REJECT REGISTRATION (PATCH /api/registrations/{id}/reject)
──────────────────────────────────────────────────────────────────────────────
Description: Reject a registration with optional reason
Status Code: 200 OK
Authorization: Admin only (future implementation)

Path Parameters:
- id: Registration ID

Request Body:
{
    "rejection_reason": "Does not meet eligibility criteria"
}

Response:
{
    "success": true,
    "message": "Registration rejected",
    "data": {
        "id": 1,
        "status": "rejected",
        "rejection_reason": "Does not meet eligibility criteria",
        "reviewed_at": "2024-01-15T15:45:00"
    }
}


──────────────────────────────────────────────────────────────────────────────
3.2 PROJECTS ENDPOINTS
──────────────────────────────────────────────────────────────────────────────

CREATE PROJECT (POST /api/projects)
──────────────────────────────────────────────────────────────────────────────
Description: Create a new project
Status Code: 201 Created

Request Body:
{
    "name": "Market Analysis Q1 2024",
    "description": "Comprehensive market analysis for Q1 2024",
    "domain": "Finance",
    "status": "planning"
}

Response:
{
    "success": true,
    "message": "Project created successfully",
    "data": {
        "id": 1,
        "name": "Market Analysis Q1 2024",
        "description": "Comprehensive market analysis for Q1 2024",
        "domain": "Finance",
        "status": "planning",
        "created_at": "2024-01-15T10:00:00"
    }
}

──────────────────────────────────────────────────────────────────────────────

LIST PROJECTS (GET /api/projects)
──────────────────────────────────────────────────────────────────────────────
Description: Get list of projects with optional filters
Query Parameters:
- domain: Filter by domain (Finance, Strategy, Operations, etc.) - Optional
- status: Filter by status (planning, in_progress, completed) - Optional
- skip: Number to skip (default: 0) - Optional
- limit: Records to return (default: 10) - Optional

Example: GET /api/projects?domain=Finance&status=in_progress

Response:
{
    "success": true,
    "message": "Projects retrieved successfully",
    "data": [
        {
            "id": 1,
            "name": "Market Analysis Q1 2024",
            "description": "Comprehensive market analysis",
            "domain": "Finance",
            "status": "planning",
            "created_at": "2024-01-15T10:00:00"
        }
    ],
    "pagination": { ... }
}

──────────────────────────────────────────────────────────────────────────────

GET PROJECT (GET /api/projects/{id})
──────────────────────────────────────────────────────────────────────────────
Description: Get specific project details
Path Parameters:
- id: Project ID

Example: GET /api/projects/1

Response:
{
    "success": true,
    "message": "Project retrieved successfully",
    "data": {
        "id": 1,
        "name": "Market Analysis Q1 2024",
        "description": "Comprehensive market analysis for Q1 2024",
        "domain": "Finance",
        "status": "planning",
        "created_at": "2024-01-15T10:00:00",
        "updated_at": "2024-01-15T10:00:00"
    }
}

──────────────────────────────────────────────────────────────────────────────

UPDATE PROJECT (PUT /api/projects/{id})
──────────────────────────────────────────────────────────────────────────────
Description: Update project details
Path Parameters:
- id: Project ID

Request Body:
{
    "name": "Market Analysis Q1 2024 - Updated",
    "status": "in_progress"
}

Response:
{
    "success": true,
    "message": "Project updated successfully",
    "data": { ... updated project }
}

──────────────────────────────────────────────────────────────────────────────

DELETE PROJECT (DELETE /api/projects/{id})
──────────────────────────────────────────────────────────────────────────────
Description: Delete a project
Path Parameters:
- id: Project ID

Response:
{
    "success": true,
    "message": "Project deleted successfully"
}


──────────────────────────────────────────────────────────────────────────────
3.3 TEAM ENDPOINTS
──────────────────────────────────────────────────────────────────────────────

CREATE TEAM MEMBER (POST /api/team)
──────────────────────────────────────────────────────────────────────────────
Description: Add new team member
Status Code: 201 Created

Request Body:
{
    "name": "Anant Chaudhary",
    "position": "Club President",
    "domain": "Executive",
    "bio": "Experienced leader",
    "email": "anant@example.com",
    "phone": "9876543210",
    "linkedin": "https://linkedin.com/in/anant",
    "twitter": "https://twitter.com/anant",
    "github": "https://github.com/anant"
}

Response:
{
    "success": true,
    "message": "Team member added successfully",
    "data": {
        "id": 1,
        "name": "Anant Chaudhary",
        "position": "Club President",
        "domain": "Executive",
        "bio": "Experienced leader",
        "email": "anant@example.com",
        "is_active": true,
        "created_at": "2024-01-15T10:00:00"
    }
}

──────────────────────────────────────────────────────────────────────────────

LIST TEAM MEMBERS (GET /api/team)
──────────────────────────────────────────────────────────────────────────────
Description: Get all team members
Query Parameters:
- skip: Records to skip (default: 0)
- limit: Records to return (default: 10)

Response:
{
    "success": true,
    "message": "Team members retrieved successfully",
    "data": [
        {
            "id": 1,
            "name": "Anant Chaudhary",
            "position": "Club President",
            "domain": "Executive",
            "is_active": true,
            "created_at": "2024-01-15T10:00:00"
        }
    ],
    "pagination": { ... }
}

──────────────────────────────────────────────────────────────────────────────

GET TEAM MEMBER (GET /api/team/{id})
──────────────────────────────────────────────────────────────────────────────
Description: Get specific team member
Path Parameters:
- id: Team member ID

Response:
{
    "success": true,
    "message": "Team member retrieved successfully",
    "data": {
        "id": 1,
        "name": "Anant Chaudhary",
        "position": "Club President",
        "domain": "Executive",
        "bio": "Experienced leader",
        "email": "anant@example.com",
        "phone": "9876543210",
        "linkedin": "https://linkedin.com/in/anant",
        "twitter": "https://twitter.com/anant",
        "github": "https://github.com/anant",
        "is_active": true,
        "created_at": "2024-01-15T10:00:00"
    }
}

──────────────────────────────────────────────────────────────────────────────

UPDATE TEAM MEMBER (PUT /api/team/{id})
──────────────────────────────────────────────────────────────────────────────
Description: Update team member
Path Parameters:
- id: Team member ID

Request Body: (all fields optional)
{
    "bio": "Updated bio",
    "is_active": true
}

Response:
{
    "success": true,
    "message": "Team member updated successfully",
    "data": { ... updated member }
}

──────────────────────────────────────────────────────────────────────────────

DELETE TEAM MEMBER (DELETE /api/team/{id})
──────────────────────────────────────────────────────────────────────────────
Description: Remove team member
Path Parameters:
- id: Team member ID

Response:
{
    "success": true,
    "message": "Team member deleted successfully"
}


═══════════════════════════════════════════════════════════════════════════════
4. ERROR RESPONSES
═══════════════════════════════════════════════════════════════════════════════

400 Bad Request:
{
    "detail": "Invalid request parameters"
}

404 Not Found:
{
    "detail": "Resource not found"
}

409 Conflict:
{
    "detail": "Resource already exists"
}

500 Internal Server Error:
{
    "detail": "Internal server error"
}


═══════════════════════════════════════════════════════════════════════════════
5. COMMON PATTERNS
═══════════════════════════════════════════════════════════════════════════════

FILTERING EXAMPLE:
GET /api/registrations?status=approved&skip=0&limit=5

PAGINATION EXAMPLE:
GET /api/team?limit=20&skip=20  # Page 2 with 20 items per page

ERROR HANDLING:
Always check "success" field:
- true: Operation successful, data in "data" field
- false: Operation failed, error in "message" field

CORS HEADERS:
All endpoints support CORS for frontend integration from:
- http://localhost:3000
- http://localhost:5173
- file:// protocol


═══════════════════════════════════════════════════════════════════════════════
6. TESTING THE API
═══════════════════════════════════════════════════════════════════════════════

Using cURL:
curl -X POST http://localhost:8000/api/registrations \\
  -H "Content-Type: application/json" \\
  -d '{"email":"test@example.com","name":"John Doe",...}'

Using Python Requests:
import requests
url = "http://localhost:8000/api/registrations"
data = {...}
response = requests.post(url, json=data)
print(response.json())

Using Thunder Client / Postman:
1. Import OpenAPI JSON: http://localhost:8000/openapi.json
2. Or manually create requests from documentation above

Web Browser (Swagger UI):
1. Navigate to: http://localhost:8000/docs
2. All endpoints listed with interactive Try It Out
3. Automatic schema validation and documentation


═══════════════════════════════════════════════════════════════════════════════
7. RESPONSE FORMATS
═══════════════════════════════════════════════════════════════════════════════

Success Response Format:
{
    "success": true,
    "message": "Operation successful",
    "data": { ... },
    "pagination": { ... } // Optional, included for list endpoints
}

Error Response Format:
{
    "success": false,
    "message": "Error description",
    "data": null
}

List Response Format:
{
    "success": true,
    "message": "Items retrieved",
    "data": [ ... ],
    "pagination": {
        "total": 100,
        "page": 1,
        "pages": 10,
        "limit": 10,
        "skip": 0
    }
}

"""

def print_api_docs():
    """Print API documentation to console"""
    print(API_DOCUMENTATION)


if __name__ == "__main__":
    print_api_docs()
