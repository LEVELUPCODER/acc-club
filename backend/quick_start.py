"""
Quick Start Guide for ACC Club Backend API
Run this file to see setup and usage instructions
"""

import sys
import os

QUICK_START = """
╔══════════════════════════════════════════════════════════════════════════════╗
║             ACC CLUB BACKEND API - QUICK START GUIDE                         ║
║                          Get up and running in 5 minutes                     ║
╚══════════════════════════════════════════════════════════════════════════════╝


═══════════════════════════════════════════════════════════════════════════════
STEP 1: INSTALLATION (For Windows Users)
═══════════════════════════════════════════════════════════════════════════════

Option A - Automated (Recommended)
──────────────────────────────────────────────────────────────────────────────
1. Double-click: setup.bat
2. Wait for installation to complete
3. Skip to STEP 3

Option B - Manual Installation
──────────────────────────────────────────────────────────────────────────────
1. Download Python 3.8+ from https://www.python.org/downloads/
   → Check "Add Python to PATH" during installation

2. Open Command Prompt (Win + R → cmd)

3. Navigate to project directory:
   cd e:\\PROJECTS\\ACC-CLUB-BACKEND

4. Create virtual environment:
   python -m venv venv

5. Activate virtual environment:
   venv\\Scripts\\activate

6. Install dependencies:
   pip install -r requirements.txt

7. Verify installation:
   pip list


═══════════════════════════════════════════════════════════════════════════════
STEP 2: CONFIGURATION
═══════════════════════════════════════════════════════════════════════════════

1. Copy environment template:
   - Copy .env.example to .env:
     copy .env.example .env

2. Edit .env (optional for development):
   - DEBUG=True                    # Enable debug logs
   - PORT=8000                     # API port
   - HOST=0.0.0.0                  # Bind to all interfaces

3. For production (future):
   - Update SECRET_KEY with random string
   - Change DEBUG=False
   - Configure DATABASE_URL for PostgreSQL
   - Set ALLOWED_ORIGINS for CORS


═══════════════════════════════════════════════════════════════════════════════
STEP 3: START THE API SERVER
═══════════════════════════════════════════════════════════════════════════════

Option A - Simple Start
──────────────────────────────────────────────────────────────────────────────
Make sure virtual environment is activated, then:

    python main.py

Expected output:
    INFO:     Uvicorn running on http://0.0.0.0:8000
    INFO:     Started server process [XXXX]

Option B - Advanced Start with Auto-reload
──────────────────────────────────────────────────────────────────────────────
    uvicorn main:app --reload --host 0.0.0.0 --port 8000

Option C - Production Start
──────────────────────────────────────────────────────────────────────────────
    uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4


═══════════════════════════════════════════════════════════════════════════════
STEP 4: VERIFY API IS RUNNING
═══════════════════════════════════════════════════════════════════════════════

Open your web browser and navigate to:

1. Interactive API Documentation (Swagger UI):
   → http://localhost:8000/docs

2. Alternative Documentation (ReDoc):
   → http://localhost:8000/redoc

3. API Info Endpoint:
   → http://localhost:8000/

Expected response:
{
    "success": true,
    "message": "Welcome to ACC Club API",
    "version": "1.0.0"
}

4. Health Check:
   → http://localhost:8000/health

Expected response:
{
    "status": "healthy",
    "database": "initialized"
}


═══════════════════════════════════════════════════════════════════════════════
STEP 5: TEST THE API
═══════════════════════════════════════════════════════════════════════════════

Method A - Using Swagger UI (Recommended for beginners)
──────────────────────────────────────────────────────────────────────────────
1. Go to http://localhost:8000/docs
2. Click on any endpoint (e.g., POST /api/registrations)
3. Click "Try it out"
4. Fill in the example data
5. Click "Execute"
6. See the response in the Response section

Method B - Using Command Line (cURL)
──────────────────────────────────────────────────────────────────────────────
Test registration endpoint:
curl -X POST http://localhost:8000/api/registrations \\
  -H "Content-Type: application/json" \\
  -d "{
    \"email\": \"test@example.com\",
    \"name\": \"Test User\",
    \"enrollment_no\": \"2021001001\",
    \"department\": \"CS\",
    \"semester\": 4,
    \"why_join\": \"Love analytics\"
  }"

Test team endpoint:
curl -X GET http://localhost:8000/api/team


═══════════════════════════════════════════════════════════════════════════════
STEP 6: API ENDPOINTS QUICK REFERENCE
═══════════════════════════════════════════════════════════════════════════════

REGISTRATIONS
──────────────
Create:  POST /api/registrations
List:    GET /api/registrations
Get:     GET /api/registrations/{id}
Approve: PATCH /api/registrations/{id}/approve
Reject:  PATCH /api/registrations/{id}/reject

PROJECTS
──────────────
Create:  POST /api/projects
List:    GET /api/projects
Get:     GET /api/projects/{id}
Update:  PUT /api/projects/{id}
Delete:  DELETE /api/projects/{id}

TEAM MEMBERS
──────────────
Create:  POST /api/team
List:    GET /api/team
Get:     GET /api/team/{id}
Update:  PUT /api/team/{id}
Delete:  DELETE /api/team/{id}


═══════════════════════════════════════════════════════════════════════════════
STEP 7: INTEGRATE WITH FRONTEND (ACC Club Website)
═══════════════════════════════════════════════════════════════════════════════

Update the website's JavaScript to call backend endpoints:

Example: Submit registration form to backend
──────────────────────────────────────────────────────────────────────────────

document.getElementById('registrationForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const formData = {
        email: document.getElementById('email').value,
        name: document.getElementById('name').value,
        enrollment_no: document.getElementById('enrollment_no').value,
        department: document.getElementById('department').value,
        semester: parseInt(document.getElementById('semester').value),
        why_join: document.getElementById('why_join').value,
        phone: document.getElementById('phone').value
    };
    
    try {
        const response = await fetch('http://localhost:8000/api/registrations', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });
        
        const result = await response.json();
        
        if (result.success) {
            alert('Registration successful!');
            // Handle success
        } else {
            alert('Error: ' + result.message);
            // Handle error
        }
    } catch (error) {
        alert('Connection error: ' + error.message);
    }
});

Example: Load team members from API
──────────────────────────────────────────────–────────────────────────────────

async function loadTeamMembers() {
    try {
        const response = await fetch('http://localhost:8000/api/team');
        const result = await response.json();
        
        if (result.success) {
            const teamContainer = document.getElementById('team-container');
            result.data.forEach(member => {
                const memberHTML = `
                    <div class="team-member">
                        <h3>${member.name}</h3>
                        <p>${member.position}</p>
                        <p>${member.bio}</p>
                    </div>
                `;
                teamContainer.innerHTML += memberHTML;
            });
        }
    } catch (error) {
        console.error('Error loading team:', error);
    }
}

loadTeamMembers();


═══════════════════════════════════════════════════════════════════════════════
STEP 8: TROUBLESHOOTING
═══════════════════════════════════════════════════════════════════════════════

Problem: "Python not found"
Solution: 
  - Install Python from https://www.python.org/downloads/
  - Make sure to check "Add to PATH" during installation
  - Restart Command Prompt

Problem: Port 8000 already in use
Solution:
  - Change port: python main.py --port 8001
  - Or kill existing process: fuser -k 8000/tcp

Problem: "Module not found" error
Solution:
  - Ensure virtual environment is activated
  - Run: pip install -r requirements.txt
  - Verify: pip list should show fastapi, uvicorn, etc.

Problem: CORS errors from frontend
Solution:
  - Update ALLOWED_ORIGINS in .env
  - Add frontend URL: http://localhost:3000
  - Restart API server

Problem: Database connection error
Solution:
  - For development: Use SQLite (default)
  - Database file created: acc_club.db
  - If error persists, delete .db file and restart


═══════════════════════════════════════════════════════════════════════════════
STEP 9: NEXT STEPS
═══════════════════════════════════════════════════════════════════════════════

1. Database Integration (Optional):
   - Uncomment database code in main.py
   - Configure PostgreSQL connection string
   - Run database migrations

2. Authentication:
   - Implement JWT token generation
   - Add login endpoint
   - Secure admin endpoints

3. Advanced Features:
   - File uploads (project files, member photos)
   - WebSocket for real-time notifications
   - Email integration for confirmations
   - Analytics and reporting

4. Deployment:
   - Deploy to Heroku, Railway, or Cloud Run
   - Set up CI/CD pipeline
   - Configure production database
   - Enable HTTPS/SSL


═══════════════════════════════════════════════════════════════════════════════
STEP 10: PROJECT STRUCTURE
═══════════════════════════════════════════════════════════════════════════════

ACC-CLUB-BACKEND/
├── main.py                      # FastAPI application entry point
├── config.py                    # Configuration management
├── schemas.py                   # Pydantic data models
├── models.py                    # SQLAlchemy database models (future use)
├── database.py                  # Database connection & session
├── utils.py                     # Utility functions
├── logging_config.py            # Logging configuration
├── api_documentation.py         # API documentation
├── quick_start.py               # This file
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment variables template
├── .gitignore                   # Git ignore rules
├── README.md                    # Full documentation
├── setup.bat                    # Windows setup script
├── setup.sh                     # Unix setup script
└── routes/                      # API route modules
    ├── __init__.py
    ├── registrations.py         # Registration endpoints
    ├── projects.py              # Project endpoints
    └── team.py                  # Team member endpoints


═══════════════════════════════════════════════════════════════════════════════
NEED HELP?
═══════════════════════════════════════════════════════════════════════════════

Documentation Files:
- README.md              → Complete API documentation
- api_documentation.py   → Detailed endpoint examples
- .env.example           → Configuration reference

Interactive Help:
- http://localhost:8000/docs  → Try API endpoints live
- http://localhost:8000/redoc  → Browse documentation

Logs:
- logs/app.log           → Application logs
- logs/error.log         → Error logs
- logs/access.log        → Request logs


═══════════════════════════════════════════════════════════════════════════════
READY? LET'S GO! 🚀
═══════════════════════════════════════════════════════════════════════════════

1. ✅ Open setup.bat
2. ✅ Wait for installation
3. ✅ Run: python main.py
4. ✅ Open: http://localhost:8000/docs
5. ✅ Start testing!

Good luck with the ACC Club Backend! 🎉

"""

def show_quick_start():
    """Display quick start guide"""
    print(QUICK_START)

def check_environment():
    """Check if environment is properly set up"""
    print("\n" + "="*80)
    print("ENVIRONMENT CHECK")
    print("="*80 + "\n")
    
    # Check Python version
    print(f"✓ Python version: {sys.version}")
    
    # Check if virtual environment is activated
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✓ Virtual environment: Active")
    else:
        print("⚠ Virtual environment: Not activated")
        print("  Run: venv\\Scripts\\activate (Windows)")
        print("  Run: source venv/bin/activate (macOS/Linux)")
    
    # Check if requirements are installed
    try:
        import fastapi
        print(f"✓ FastAPI: {fastapi.__version__}")
    except ImportError:
        print("✗ FastAPI: Not installed - Run: pip install -r requirements.txt")
    
    try:
        import pydantic
        print(f"✓ Pydantic: {pydantic.__version__}")
    except ImportError:
        print("✗ Pydantic: Not installed")
    
    try:
        import uvicorn
        print(f"✓ Uvicorn: {uvicorn.__version__}")
    except ImportError:
        print("✗ Uvicorn: Not installed")
    
    print("\n" + "="*80 + "\n")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="ACC Club Backend Quick Start")
    parser.add_argument("--check", action="store_true", help="Check environment setup")
    parser.add_argument("--guide", action="store_true", help="Show quick start guide (default)")
    
    args = parser.parse_args()
    
    if args.check:
        check_environment()
    else:
        show_quick_start()
        print("\nRun 'python quick_start.py --check' to verify your environment")
