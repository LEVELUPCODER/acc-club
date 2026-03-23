# ACC Club Backend API

Backend API for the Analytics & Consultancy Club website built with **FastAPI** and Python.

## Features

- 🚀 **Fast Performance** - Built with FastAPI for high performance
- 📊 **Project Management** - Manage club projects and initiatives
- 👥 **Member Management** - Handle registrations and team members
- 📝 **Comprehensive API** - RESTful endpoints for all operations
- 🔄 **CORS Enabled** - Cross-origin resource sharing for frontend integration
- 📚 **Auto Documentation** - Interactive API documentation with Swagger UI

## Project Structure

```
ACC-CLUB-BACKEND/
├── main.py                 # Application entry point
├── schemas.py              # Pydantic data models
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── routes/
│   ├── __init__.py
│   ├── registrations.py   # Registration endpoints
│   ├── projects.py        # Project management endpoints
│   └── team.py            # Team member endpoints
└── README.md              # This file
```

## Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Create virtual environment**

```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
# or
source venv/bin/activate      # On macOS/Linux
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Configure environment**

```bash
cp .env.example .env
# Edit .env if needed
```

4. **Run the server**

```bash
python main.py
# or
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at: **http://localhost:8000**

## API Documentation

### Interactive Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc
- **OpenAPI Schema**: http://localhost:8000/openapi.json

### Available Endpoints

#### Health Check

- `GET /health` - Check API status
- `GET /` - API info and available endpoints

#### Registrations

- `POST /api/registrations` - Create new registration
- `GET /api/registrations` - List all registrations
- `GET /api/registrations/{id}` - Get specific registration
- `PATCH /api/registrations/{id}/approve` - Approve registration
- `PATCH /api/registrations/{id}/reject` - Reject registration

#### Projects

- `POST /api/projects` - Create new project
- `GET /api/projects` - List all projects
- `GET /api/projects/{id}` - Get specific project
- `PUT /api/projects/{id}` - Update project
- `DELETE /api/projects/{id}` - Delete project

#### Team Members

- `POST /api/team` - Add team member
- `GET /api/team` - List all team members
- `GET /api/team/{id}` - Get specific team member
- `PUT /api/team/{id}` - Update team member
- `DELETE /api/team/{id}` - Remove team member

## Example Requests

### Create Registration

```bash
curl -X POST "http://localhost:8000/api/registrations" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "phone": "+919876543210",
    "year": 2,
    "branch": "Computer Science",
    "interests": ["Finance", "Analytics"]
  }'
```

### List Projects

```bash
curl -X GET "http://localhost:8000/api/projects?domain=Finance"
```

### Get Team Members

```bash
curl -X GET "http://localhost:8000/api/team"
```

## Response Format

All endpoints return standardized JSON responses:

### Success Response

```json
{
  "success": true,
  "message": "Operation completed successfully",
  "data": {
    "id": 1,
    "name": "Example"
  }
}
```

### Error Response

```json
{
  "success": false,
  "error": "Error message",
  "details": {}
}
```

## Development

### Run with auto-reload

```bash
uvicorn main:app --reload
```

### Run tests (when added)

```bash
pytest
```

## Future Enhancements

- [ ] Database integration (SQLAlchemy + SQLite/PostgreSQL)
- [ ] User authentication (JWT tokens)
- [ ] Email verification
- [ ] File upload support
- [ ] Advanced filtering and search
- [ ] Analytics dashboard endpoints
- [ ] WebSocket support for real-time updates
- [ ] Unit tests

## Technologies Used

- **FastAPI** - Modern Python web framework
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation
- **SQLAlchemy** - ORM (for future database integration)

## API Deployment

### Using Heroku

1. Create `Procfile`:

```
web: uvicorn main:app --host 0.0.0.0 --port $PORT
```

2. Deploy:

```bash
git push heroku main
```

### Using Docker

Create `Dockerfile`:

```dockerfile
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

MIT License - Feel free to use this project

## Contact

For questions or support, contact the ACC Club team at **info@accclub.in**

---

**ACC Club** - Analytics & Consultancy Club Backend API v1.0.0
