"""
Configuration settings for ACC Club Backend API
"""

import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
HOST = os.getenv("HOST", "0.0.0.0")
PORT = int(os.getenv("PORT", 8000))
API_VERSION = os.getenv("API_VERSION", "1.0.0")

# CORS Configuration
ALLOWED_ORIGINS = os.getenv(
    "ALLOWED_ORIGINS",
    "http://localhost:3000,http://localhost:5173,file:///"
).split(",")

# API Settings
API_TITLE = "ACC Club API"
API_DESCRIPTION = "Analytics & Consultancy Club Backend API"
API_DOCS_URL = "/docs"
API_OPENAPI_URL = "/openapi.json"

# Database Configuration (for future use)
DATABASE_URL = os.getenv("DATABASE_URL", None)

# JWT Configuration (for future use)
SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

# Pagination
DEFAULT_PAGE_SIZE = 10
MAX_PAGE_SIZE = 100

# File Upload (for future use)
MAX_UPLOAD_SIZE = 10 * 1024 * 1024  # 10MB

print(f"""
╔════════════════════════════════════════╗
║   ACC Club Backend API Configuration   ║
╚════════════════════════════════════════╝
Debug Mode: {DEBUG}
Host: {HOST}
Port: {PORT}
API Version: {API_VERSION}
Database: {'Configured' if DATABASE_URL else 'Not configured (using in-memory storage)'}
CORS Origins: {len(ALLOWED_ORIGINS)} configured
""")
