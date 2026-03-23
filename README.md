# ACC Club - Complete Project

Analytics & Consultancy Club Full-Stack Application

## 📁 Project Structure

```
ACC CLUB/
├── index.html              # Frontend website
├── fix_gallery.py          # Gallery utility script
├── START.bat              # Windows startup script
├── START.sh               # macOS/Linux startup script
├── backend/               # Complete FastAPI backend
│   ├── main.py            # Backend entry point
│   ├── config.py          # Configuration
│   ├── schemas.py         # Data models
│   ├── constants.py       # Constants & enums
│   ├── utils.py           # Utility functions
│   ├── database.py        # Database configuration
│   ├── models.py          # SQLAlchemy models
│   ├── logging_config.py  # Logging setup
│   ├── requirements.txt   # Python dependencies
│   ├── .env.example       # Environment template
│   ├── .gitignore         # Git ignore patterns
│   ├── setup.bat          # Backend setup (Windows)
│   ├── setup.sh           # Backend setup (Unix)
│   ├── README.md          # Backend documentation
│   ├── ROADMAP.md         # Development roadmap
│   ├── DEPLOYMENT_SUMMARY.md
│   ├── PROJECT_OVERVIEW.md
│   ├── api_documentation.py
│   ├── quick_start.py
│   ├── test_runner.py
│   └── routes/            # API endpoints
│       ├── registrations.py  # Registration endpoints
│       ├── projects.py       # Project endpoints
│       └── team.py           # Team endpoints
└── README.md             # This file
```

## 🚀 Quick Start

### Option 1: Automated Start (Recommended)

**Windows:**
```bash
START.bat
```

**macOS/Linux:**
```bash
bash START.sh
chmod +x START.sh  # First time only
```

This will automatically:
1. Check Python installation
2. Start the backend server
3. Open the frontend in your browser

### Option 2: Manual Start

**Terminal 1 - Backend:**
```bash
cd backend
python -m venv venv              # First time only
venv\Scripts\activate            # Windows
# or: source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt  # First time only
python main.py
```

**Terminal 2 - Frontend:**
```bash
# Open index.html in your browser
```

## 🔗 Connection Status

**Frontend** ↔️ **Backend**

- Frontend: `index.html` (file protocol)
- Backend: `http://localhost:8000`
- API Documentation: `http://localhost:8000/docs`

### Frontend Features Connected to Backend:

✅ **Registration Form** → POST `/api/registrations`
- Submits member applications to backend
- Displays confirmation with enrollment number

✅ **Team Members Section** → GET `/api/team`
- Displays team member information
- Currently static, ready for dynamic loading

✅ **Projects Section** → GET `/api/projects`
- Project listing and details
- Currently static, ready for dynamic loading

## 📋 API Endpoints Available

### Health & Info
- `GET /` - API information
- `GET /health` - Health check

### Registrations
- `POST /api/registrations` - Submit registration
- `GET /api/registrations` - List all registrations
- `GET /api/registrations/{id}` - Get registration details
- `PATCH /api/registrations/{id}/approve` - Approve registration
- `PATCH /api/registrations/{id}/reject` - Reject registration

### Projects
- `POST /api/projects` - Create project
- `GET /api/projects` - List projects
- `GET /api/projects/{id}` - Get project details
- `PUT /api/projects/{id}` - Update project
- `DELETE /api/projects/{id}` - Delete project

### Team Members
- `POST /api/team` - Add team member
- `GET /api/team` - List team members
- `GET /api/team/{id}` - Get team member details
- `PUT /api/team/{id}` - Update team member
- `DELETE /api/team/{id}` - Delete team member

## 📝 Frontend Integration

The frontend is already configured to communicate with the backend:

```javascript
// API endpoint configured in index.html
const API_BASE_URL = "http://localhost:8000/api";

// Example: Submit registration
async function submitRegistration(event) {
    const response = await fetch(`${API_BASE_URL}/registrations`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(registrationData)
    });
    const result = await response.json();
    // Handle response...
}
```

## 🎨 Frontend Features

- **Dark Blue Professional Theme** with glass morphism design
- **Responsive Design** with Tailwind CSS
- **Multi-step Registration Form** with validation
- **Interactive Navigation** with smooth scrolling
- **Team Member Profiles** with bio and social links
- **Gallery Section** with modal preview
- **Service Cards** highlighting club offerings

## ⚙️ Backend Features

- **14 API Endpoints** across 3 modules
- **Auto-generated Documentation** (Swagger UI + ReDoc)
- **Data Validation** with Pydantic
- **CORS Support** for cross-origin requests
- **In-memory Storage** (ready for database)
- **Comprehensive Logging** system
- **Error Handling** with proper status codes

## 🔧 Configuration

### Backend Setup

1. **First time setup:**
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows or: source venv/bin/activate
pip install -r requirements.txt
```

2. **Configure environment (.env):**
```bash
copy .env.example .env  # Windows or: cp .env.example .env
```

3. **Edit .env as needed:**
```
DEBUG=True
HOST=0.0.0.0
PORT=8000
ALLOWED_ORIGINS=http://localhost:3000,http://localhost:5173,file:///
```

### Frontend Configuration

Frontend automatically detects backend at `http://localhost:8000`

To change API endpoint, edit `index.html`:
```javascript
const API_BASE_URL = "http://your-api-domain:8000/api";
```

## 📊 Testing

### Test Registration Form
1. Open `index.html` in browser
2. Click "Join ACC Club" button
3. Fill in registration form
4. Click "Submit"
5. See confirmation with enrollment number

### Test API Endpoints
```bash
# In backend folder:
python test_runner.py --all

# Or in browser:
http://localhost:8000/docs  # Interactive Swagger UI
```

## 🐛 Troubleshooting

### Backend Not Starting
```
Problem: "Port 8000 already in use"
Solution: 
  - Change port in backend/.env (PORT=8001)
  - Or find and kill process using port 8000
```

### No Backend Connection
```
Problem: Registration form shows "Connection error"
Solution:
  - Ensure backend is running: python backend/main.py
  - Check if http://localhost:8000/health works
  - Verify backend folder exists at backend/
```

### CORS Error in Browser
```
Problem: "CORS policy" error in console
Solution:
  - CORS is already configured in backend
  - If using different origin, update ALLOWED_ORIGINS in backend/.env
  - Restart backend server
```

### Python Not Found
```
Problem: "python: command not found"
Solution:
  - Install Python 3.8+ from https://www.python.org/downloads/
  - Make sure to check "Add Python to PATH"
  - Restart terminal
```

## 📖 Documentation

- **Backend README**: `backend/README.md` - Complete API documentation
- **API Examples**: `backend/api_documentation.py` - Detailed endpoint examples
- **Quick Start**: `backend/quick_start.py` - Setup guide
- **Roadmap**: `backend/ROADMAP.md` - Future enhancements and deployment

## 🚀 Deployment Ready

The application is production-ready with:
- ✅ API Documentation (auto-generated)
- ✅ Error Handling
- ✅ Input Validation
- ✅ CORS Configuration
- ✅ Logging System
- 🟡 Database Integration (see ROADMAP)
- 🟡 Authentication (see ROADMAP)
- 🟡 Email Notifications (see ROADMAP)

## 📋 Next Steps

1. **Immediate:**
   - Run `START.bat` or `bash START.sh`
   - Test registration form
   - Verify API documentation at `/docs`

2. **Short Term (1-2 weeks):**
   - Add database integration (see `backend/ROADMAP.md`)
   - Implement authentication system
   - Set up email notifications

3. **Medium Term (1-2 months):**
   - Deploy to production (Cloud Run, Heroku, etc.)
   - Add monitoring and alerting
   - Collect analytics

## 📞 Support

- **API Docs**: Open `http://localhost:8000/docs` in browser
- **Backend Docs**: See `backend/README.md`
- **Issues**: Check backend logs at `backend/logs/`
- **Tests**: Run `python backend/test_runner.py`

## 📄 License

ACC Club - Analytics & Consultancy Club

---

**Happy Coding!** 🎉

For questions or issues, refer to the backend documentation or check the API docs at `http://localhost:8000/docs`
