"""
Logging configuration for ACC Club Backend API
"""

import logging
import logging.handlers
import os
from datetime import datetime

# Create logs directory
LOGS_DIR = "logs"
os.makedirs(LOGS_DIR, exist_ok=True)

# Log file paths
MAIN_LOG = os.path.join(LOGS_DIR, "app.log")
ERROR_LOG = os.path.join(LOGS_DIR, "error.log")
ACCESS_LOG = os.path.join(LOGS_DIR, "access.log")

# Log format
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
DETAILED_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s"

# Configure root logger
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

# Console handler (INFO level)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter(LOG_FORMAT)
console_handler.setFormatter(console_formatter)
root_logger.addHandler(console_handler)

# File handler for all logs (DEBUG level)
file_handler = logging.handlers.RotatingFileHandler(
    MAIN_LOG,
    maxBytes=10 * 1024 * 1024,  # 10MB
    backupCount=5,
    encoding='utf-8'
)
file_handler.setLevel(logging.DEBUG)
file_formatter = logging.Formatter(DETAILED_FORMAT)
file_handler.setFormatter(file_formatter)
root_logger.addHandler(file_handler)

# File handler for errors (ERROR level)
error_handler = logging.handlers.RotatingFileHandler(
    ERROR_LOG,
    maxBytes=10 * 1024 * 1024,  # 10MB
    backupCount=5,
    encoding='utf-8'
)
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(file_formatter)
root_logger.addHandler(error_handler)

# Create specific loggers
app_logger = logging.getLogger("app")
api_logger = logging.getLogger("api")
db_logger = logging.getLogger("database")
auth_logger = logging.getLogger("auth")

# Set their levels
app_logger.setLevel(logging.INFO)
api_logger.setLevel(logging.DEBUG)
db_logger.setLevel(logging.DEBUG)
auth_logger.setLevel(logging.INFO)

# Logging functions
def log_request(method: str, path: str, status_code: int, duration: float):
    """Log HTTP request"""
    api_logger.info(f"{method} {path} - {status_code} - {duration:.3f}s")


def log_db_operation(operation: str, entity: str, status: str):
    """Log database operation"""
    db_logger.debug(f"{operation} on {entity}: {status}")


def log_error(error: Exception, context: str = ""):
    """Log error with context"""
    app_logger.error(f"Error {context}: {str(error)}", exc_info=True)


def log_auth_attempt(email: str, success: bool, reason: str = ""):
    """Log authentication attempt"""
    status = "successful" if success else "failed"
    auth_logger.info(f"Auth attempt for {email}: {status} {reason}")


def log_startup():
    """Log application startup"""
    app_logger.info("=" * 60)
    app_logger.info("ACC Club Backend API Starting")
    app_logger.info(f"Timestamp: {datetime.now().isoformat()}")
    app_logger.info("=" * 60)


def log_shutdown():
    """Log application shutdown"""
    app_logger.info("=" * 60)
    app_logger.info("ACC Club Backend API Shutting Down")
    app_logger.info(f"Timestamp: {datetime.now().isoformat()}")
    app_logger.info("=" * 60)


if __name__ == "__main__":
    app_logger.info("Testing logging system")
    api_logger.debug("Debug message")
    db_logger.info("Database message")
    app_logger.error("Error message", exc_info=False)
    print(f"\nLog files created in: {os.path.abspath(LOGS_DIR)}")
