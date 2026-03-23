"""
SQLAlchemy database models for ACC Club API
These models are prepared for future database integration.
Currently using in-memory storage; uncomment and configure to use with SQLite/PostgreSQL.
"""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, Enum
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()


class RegistrationStatus(str, enum.Enum):
    PENDING = "pending"
    APPROVED = "approved"
    REJECTED = "rejected"


class ProjectStatus(str, enum.Enum):
    PLANNING = "planning"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ON_HOLD = "on_hold"


class UserModel(Base):
    """User model for database"""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    name = Column(String(255), nullable=False)
    enrollment_no = Column(String(50), nullable=False)
    department = Column(String(100), nullable=False)
    semester = Column(Integer, nullable=False)
    phone = Column(String(20), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class RegistrationModel(Base):
    """Registration model for database"""
    __tablename__ = "registrations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False, index=True)
    email = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
    enrollment_no = Column(String(50), nullable=False)
    department = Column(String(100), nullable=False)
    semester = Column(Integer, nullable=False)
    why_join = Column(Text, nullable=False)
    phone = Column(String(20), nullable=True)
    status = Column(Enum(RegistrationStatus), default=RegistrationStatus.PENDING, index=True)
    rejection_reason = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, index=True)
    reviewed_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class ProjectModel(Base):
    """Project model for database"""
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    domain = Column(String(100), nullable=False, index=True)
    status = Column(Enum(ProjectStatus), default=ProjectStatus.PLANNING, index=True)
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)
    team_lead_id = Column(Integer, nullable=True)
    max_members = Column(Integer, nullable=True)
    created_by = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class TeamMemberModel(Base):
    """Team member model for database"""
    __tablename__ = "team_members"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    position = Column(String(255), nullable=False, index=True)
    domain = Column(String(100), nullable=True)
    bio = Column(Text, nullable=True)
    email = Column(String(255), nullable=True, unique=True, index=True)
    phone = Column(String(20), nullable=True)
    linkedin = Column(String(500), nullable=True)
    twitter = Column(String(500), nullable=True)
    github = Column(String(500), nullable=True)
    profile_image_url = Column(String(500), nullable=True)
    is_active = Column(Boolean, default=True, index=True)
    joined_date = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class ProjectMemberModel(Base):
    """Project member association model for database"""
    __tablename__ = "project_members"

    id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, nullable=False, index=True)
    user_id = Column(Integer, nullable=False, index=True)
    role = Column(String(100), nullable=True)
    joined_date = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)


# ==============================================================================
# INITIALIZATION GUIDE FOR DATABASE INTEGRATION
# ==============================================================================
"""
When ready to integrate database:

1. Install SQLAlchemy:
   pip install sqlalchemy

2. Create database session in models.py or separate session.py:
   from sqlalchemy import create_engine
   from sqlalchemy.orm import sessionmaker
   
   DATABASE_URL = "sqlite:///./acc_club.db"  # Development
   # or "postgresql://user:password@localhost/acc_club"  # Production
   
   engine = create_engine(DATABASE_URL)
   SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
   Base.metadata.create_all(bind=engine)

3. Add to requirements.txt:
   sqlalchemy>=2.0.0
   alembic>=1.8.0  # for migrations

4. Update endpoints to query database instead of in-memory lists

5. Create migrations using Alembic:
   alembic init migrations
   alembic revision --autogenerate -m "Initial migration"
   alembic upgrade head

6. Update main.py to initialize database:
   from models import Base, engine
   Base.metadata.create_all(bind=engine)
"""
