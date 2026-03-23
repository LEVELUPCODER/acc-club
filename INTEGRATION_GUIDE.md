# ACC Club - Integration Guide

## Frontend-Backend Connection

This document explains how the ACC Club website (frontend) is connected to the FastAPI backend API.

## 🔗 Connection Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│  User Browser                                               │
│  ┌───────────────────────────────────────────────┐         │
│  │                                               │         │
│  │  index.html (Frontend)                        │         │
│  │  ├── HTML/CSS/JavaScript                      │         │
│  │  └── Makes HTTP requests to Backend API       │         │
│  │                                               │         │
│  └───────────────────────────────────────────────┘         │
│            ↓ HTTP Requests                                  │
│            ↓ import registrationData                        │
│            ↓ fetch('/api/registrations', ...)               │
│            ↓                                                │
│  ┌─────────────────────────────────────────────┐           │
│  │                                             │           │
│  │  Backend Server (localhost:8000)            │           │
│  │  ┌─────────────────────────────────────┐   │           │
│  │  │  FastAPI Application                │   │           │
│  │  ├─ main.py (Entry point)              │   │           │
│  │  ├─ routes/                            │   │           │
│  │  │  ├─ registrations.py                │   │           │
│  │  │  ├─ projects.py                     │   │           │
│  │  │  └─ team.py                         │   │           │
│  │  ├─ schemas.py (Data validation)       │   │           │
│  │  └─ utils.py (Helper functions)        │   │           │
│  │                                        │   │           │
│  │  In-Memory Storage (or Database)       │   │           │
│  │  ├─ registrations_db                   │   │           │
│  │  ├─ projects_db                        │   │           │
│  │  └─ team_db                            │   │           │
│  │                                        │   │           │
│  └─────────────────────────────────────────┘   │           │
│            ↑ JSON Response                      │           │
│            ↑ { success, message, data }         │           │
│            ↑                                    │           │
│  HTTP Response ←──────────────────────────────┘           │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## 🌐 API Communication

### Base URLs

| Component | URL | Purpose |
|-----------|-----|---------|
| Frontend | `file:///path/to/index.html` | Website interface |
| Backend API | `http://localhost:8000` | API server |
| API Base | `http://localhost:8000/api` | API endpoint base |
| Documentation | `http://localhost:8000/docs` | Interactive API docs |

### Request Flow

1. **User Action**: Click "Join ACC Club"
2. **Frontend**: Collect form data from HTML inputs
3. **Frontend**: Convert data to JSON format
4. **Frontend**: Send HTTP POST to `http://localhost:8000/api/registrations`
5. **Backend**: Receive request at `/api/registrations` endpoint
6. **Backend**: Validate data using Pydantic schemas
7. **Backend**: Store in in-memory list (or database)
8. **Backend**: Send JSON response: `{ success: true, data: {...} }`
9. **Frontend**: Display success screen with confirmation

## 📝 Frontend Implementation

### API Configuration in HTML

```javascript
// Located in index.html
const API_BASE_URL = "http://localhost:8000/api";
```

### Registration Form Submission

```javascript
// In index.html - submitRegistration() function
async function submitRegistration(event) {
    event.preventDefault();
    
    // Collect form data
    const registrationData = {
        name: "John Doe",
        email: "john@example.com",
        phone: "9876543210",
        enrollment_no: "2021001234",
        department: "Computer Science",
        semester: 4,
        why_join: "Interested in analytics..."
    };
    
    try {
        // Send to backend
        const response = await fetch(`${API_BASE_URL}/registrations`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(registrationData),
        });
        
        // Get response
        const result = await response.json();
        
        if (result.success) {
            // Show success screen
            // Display confirmation details
        } else {
            // Show error message
        }
    } catch (error) {
        // Handle connection error
        console.error("Error:", error);
    }
}
```

### Loading Team Members from API

```javascript
// In index.html - loadTeamMembers() function
async function loadTeamMembers() {
    try {
        const response = await fetch(`${API_BASE_URL}/team`);
        const result = await response.json();
        
        if (result.success && result.data) {
            // Process team members
            result.data.forEach(member => {
                console.log(`${member.name} - ${member.position}`);
            });
        }
    } catch (error) {
        console.warn("Could not load team:", error);
    }
}
```

### Checking Backend Connection

```javascript
// In index.html - checkBackendConnection() function
async function checkBackendConnection() {
    try {
        const response = await fetch("http://localhost:8000/health");
        const result = await response.json();
        if (result.status === "healthy") {
            console.log("✓ Backend connected!");
            return true;
        }
    } catch (error) {
        console.warn("Backend not available");
        return false;
    }
}
```

## 🛠️ Backend Implementation

### Request Handler (routes/registrations.py)

```python
# Backend endpoint that receives registration requests
from fastapi import APIRouter
from schemas import RegistrationCreate, Registration, SuccessResponse

@router.post("/", response_model=SuccessResponse, status_code=201)
async def create_registration(registration: RegistrationCreate):
    # Validate data (Pydantic does this automatically)
    # Store in database/memory
    new_reg = {
        "id": get_next_id(registrations_db),
        **registration.dict(),
        "status": "pending",
        "created_at": datetime.utcnow()
    }
    registrations_db.append(new_reg)
    
    # Return success response
    return {
        "success": True,
        "message": "Registration created successfully",
        "data": new_reg
    }
```

### CORS Configuration

```python
# In main.py - Enable cross-origin requests from frontend
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "file://",  # Allow file:// protocol
    ],
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Data Validation (schemas.py)

```python
from pydantic import BaseModel, EmailStr

class RegistrationCreate(BaseModel):
    email: EmailStr           # Validated email format
    name: str                 # Required string
    enrollment_no: str        # Required string (10 digits)
    department: str           # Required string
    semester: int             # Required integer (1-8)
    why_join: str            # Required string (20-1000 chars)
    phone: str               # Optional phone number

# Frontend data is validated against this schema
# If data doesn't match, 422 error is returned
```

## 📊 Data Flow Examples

### Example 1: Submit Registration

**Frontend (index.html)**
```javascript
// User fills form and clicks Submit
const formData = {
    name: "Alice",
    email: "alice@university.edu",
    phone: "9876543210",
    enrollment_no: "2021001001",
    department: "Computer Science",
    semester: 4,
    why_join: "Want to learn analytics"
};

fetch("http://localhost:8000/api/registrations", {
    method: "POST",
    body: JSON.stringify(formData)
})
```

**Backend (routes/registrations.py)**
```python
# Receives registration request
# Validates against RegistrationCreate schema
# Stores in registrations_db list
# Returns: { "success": true, "data": { id: 1, ... } }
```

**Frontend Response**
```javascript
// Shows success screen with enrollment number
// Updates localStorage with registration data
```

---

### Example 2: Load Team Members

**Frontend (index.html)**
```javascript
// On page load
fetch("http://localhost:8000/api/team")
```

**Backend (routes/team.py)**
```python
# Returns pre-populated team members list
# { "success": true, "data": [ 
#     { "id": 1, "name": "Anant", "position": "President" },
#     ...
#   ]
# }
```

## ✅ Connection Checklist

- [x] Frontend HTML has `API_BASE_URL` configured
- [x] Frontend has `async` functions for API calls
- [x] Backend has CORS middleware enabled
- [x] Backend has route handlers for `/api/*` endpoints
- [x] Backend validates data with Pydantic schemas
- [x] Backend returns JSON responses
- [x] Frontend handles both success and error responses
- [x] Frontend shows loading states

## 🧪 Testing the Connection

### Test 1: Health Check
```bash
curl http://localhost:8000/health
# Should return: { "status": "healthy" }
```

### Test 2: Registration Submission
```bash
curl -X POST http://localhost:8000/api/registrations \
  -H "Content-Type: application/json" \
  -d '{
    "name":"Test",
    "email":"test@test.com",
    "phone":"9876543210",
    "enrollment_no":"2021001001",
    "department":"CS",
    "semester":4,
    "why_join":"Test"
  }'
```

### Test 3: List Registrations
```bash
curl http://localhost:8000/api/registrations
# Should return list of registrations
```

### Test 4: API Documentation
```
Open in browser: http://localhost:8000/docs
Try endpoints interactively
```

## 🔍 Debugging Connection Issues

### Issue: "Failed to fetch" error

**Cause**: Backend not running or CORS not configured

**Solution**:
```bash
# Check if backend is running
curl http://localhost:8000/health

# If not running, start it:
cd backend
python main.py

# Check CORS configuration in backend/main.py
```

### Issue: Registration form doesn't submit

**Cause**: Form validation failed or API error

**Solution**:
1. Open browser DevTools (F12)
2. Go to Console tab
3. Look for error messages
4. Check Network tab for API request status
5. Verify form data is valid

### Issue: No response from backend

**Cause**: Backend crashed or port occupied

**Solution**:
```bash
# Check if port 8000 is in use
netstat -ano | findstr :8000  # Windows
lsof -i :8000                 # macOS/Linux

# Kill process or change port in .env
PORT=8001
```

## 📦 Deployment Considerations

### Changing API URL for Production

When deploying to production, update the API URL:

```javascript
// In index.html - Change this:
const API_BASE_URL = "http://localhost:8000/api";

// To this (example for Heroku):
const API_BASE_URL = "https://acc-club-api.herokuapp.com/api";

// Or use environment-based configuration:
const API_BASE_URL = 
    window.location.hostname === "localhost"
        ? "http://localhost:8000/api"
        : "https://api.accclub.com/api";
```

### Backend CORS for Production

```python
# In backend/config.py or main.py - Update allowed origins:
ALLOWED_ORIGINS = [
    "http://localhost:3000",      # Development
    "https://accclub.vercel.app", # Production frontend
    "https://accclub.com",        # Production domain
]
```

## 📚 Related Documentation

- [Backend API Docs](backend/README.md)
- [Frontend HTML](index.html)
- [Backend Configuration](backend/config.py)
- [CORS Setup](backend/main.py)
- [Data Schemas](backend/schemas.py)

## ✨ Summary

The ACC Club application is now fully integrated with:

✅ **Frontend** → User interface for registration and viewing club info
✅ **Backend** → RESTful API handling business logic and data
✅ **Communication** → HTTP JSON requests/responses
✅ **Validation** → Data validation on both frontend and backend
✅ **Error Handling** → Comprehensive error messages and logging
✅ **Documentation** → Auto-generated API docs at `/docs`

Everything is ready for development, testing, and deployment! 🚀
