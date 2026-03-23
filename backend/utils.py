"""
Utility functions for ACC Club Backend API
"""

from datetime import datetime, timedelta
from typing import Optional, List, Any, Dict
import re
from fastapi import HTTPException, status


# ==============================================================================
# VALIDATION UTILITIES
# ==============================================================================

def validate_email(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """Validate phone number (10 digits, optional country code)"""
    pattern = r'^(\+\d{1,3})?[\s.-]?\d{10}$'
    return bool(re.match(pattern, phone.replace(" ", "")))


def validate_enrollment_no(enrollment_no: str) -> bool:
    """Validate enrollment number format"""
    # Typical format: 20XXXXXX (8 digits after 20)
    return bool(re.match(r'^\d{10}$', enrollment_no))


def validate_password(password: str) -> tuple[bool, str]:
    """
    Validate password strength.
    Returns: (is_valid, error_message)
    """
    if len(password) < 8:
        return False, "Password must be at least 8 characters long"
    if not any(c.isupper() for c in password):
        return False, "Password must contain uppercase letter"
    if not any(c.islower() for c in password):
        return False, "Password must contain lowercase letter"
    if not any(c.isdigit() for c in password):
        return False, "Password must contain digit"
    if not any(c in "!@#$%^&*" for c in password):
        return False, "Password must contain special character (!@#$%^&*)"
    return True, ""


# ==============================================================================
# PAGINATION UTILITIES
# ==============================================================================

def paginate_items(items: List[Any], skip: int = 0, limit: int = 10) -> List[Any]:
    """
    Paginate items list
    
    Args:
        items: List to paginate
        skip: Number of items to skip
        limit: Number of items to return
    
    Returns:
        Paginated items
    """
    return items[skip : skip + limit]


def get_pagination_metadata(
    total_items: int,
    skip: int = 0,
    limit: int = 10
) -> Dict[str, int]:
    """
    Generate pagination metadata
    
    Returns dict with: total, page, pages, limit, skip
    """
    pages = (total_items + limit - 1) // limit
    page = (skip // limit) + 1
    
    return {
        "total": total_items,
        "page": page,
        "pages": pages,
        "limit": limit,
        "skip": skip
    }


# ==============================================================================
# FILTER UTILITIES
# ==============================================================================

def filter_items_by_status(items: List[Dict], status: Optional[str]) -> List[Dict]:
    """Filter items by status"""
    if not status:
        return items
    return [item for item in items if item.get("status") == status]


def filter_items_by_domain(items: List[Dict], domain: Optional[str]) -> List[Dict]:
    """Filter items by domain"""
    if not domain:
        return items
    return [item for item in items if item.get("domain") == domain]


def filter_items_by_field(
    items: List[Dict],
    field: str,
    value: Optional[Any]
) -> List[Dict]:
    """Generic filter by field and value"""
    if value is None:
        return items
    return [item for item in items if item.get(field) == value]


# ==============================================================================
# DATE/TIME UTILITIES
# ==============================================================================

def get_current_timestamp() -> datetime:
    """Get current UTC timestamp"""
    return datetime.utcnow()


def add_days_to_date(date: datetime, days: int) -> datetime:
    """Add days to date"""
    return date + timedelta(days=days)


def is_within_date_range(
    check_date: datetime,
    start_date: datetime,
    end_date: datetime
) -> bool:
    """Check if date is within range"""
    return start_date <= check_date <= end_date


def format_timestamp(timestamp: datetime, format_str: str = "%Y-%m-%d %H:%M:%S") -> str:
    """Format timestamp as string"""
    return timestamp.strftime(format_str)


# ==============================================================================
# ERROR HANDLING UTILITIES
# ==============================================================================

def raise_not_found(resource: str, resource_id: Any):
    """Raise 404 Not Found error"""
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"{resource} with ID {resource_id} not found"
    )


def raise_bad_request(message: str):
    """Raise 400 Bad Request error"""
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail=message
    )


def raise_unauthorized(message: str = "Unauthorized"):
    """Raise 401 Unauthorized error"""
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail=message
    )


def raise_forbidden(message: str = "Access forbidden"):
    """Raise 403 Forbidden error"""
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=message
    )


def raise_conflict(resource: str, field: str):
    """Raise 409 Conflict error (duplicate)"""
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail=f"{resource} with this {field} already exists"
    )


# ==============================================================================
# STRING UTILITIES
# ==============================================================================

def slugify(text: str) -> str:
    """Convert text to slug format"""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text.strip('-')


def truncate_text(text: str, max_length: int = 100) -> str:
    """Truncate text with ellipsis"""
    if len(text) <= max_length:
        return text
    return text[:max_length].rstrip() + "..."


# ==============================================================================
# LIST UTILITIES
# ==============================================================================

def find_item_by_id(items: List[Dict], item_id: int) -> Optional[Dict]:
    """Find item in list by ID"""
    for item in items:
        if item.get("id") == item_id:
            return item
    return None


def remove_item_by_id(items: List[Dict], item_id: int) -> bool:
    """Remove item from list by ID"""
    for i, item in enumerate(items):
        if item.get("id") == item_id:
            items.pop(i)
            return True
    return False


def get_next_id(items: List[Dict]) -> int:
    """Get next ID for new item (simple incrementing)"""
    if not items:
        return 1
    return max(item.get("id", 0) for item in items) + 1


# ==============================================================================
# FORMATTING UTILITIES
# ==============================================================================

def format_currency(amount: float, currency: str = "₹") -> str:
    """Format amount as currency"""
    return f"{currency}{amount:,.2f}"


def format_percentage(value: float, decimals: int = 2) -> str:
    """Format value as percentage"""
    return f"{value:.{decimals}f}%"


def format_list_to_string(items: List[str], separator: str = ", ") -> str:
    """Convert list to readable string"""
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    return separator.join(items[:-1]) + f" and {items[-1]}"


# ==============================================================================
# SECURITY UTILITIES
# ==============================================================================

def mask_email(email: str) -> str:
    """Mask email for privacy: user***@example.com"""
    parts = email.split("@")
    if len(parts) != 2:
        return email
    username, domain = parts
    if len(username) <= 2:
        masked = "*" * len(username)
    else:
        masked = username[0] + "*" * (len(username) - 2) + username[-1]
    return f"{masked}@{domain}"


def mask_phone(phone: str) -> str:
    """Mask phone: +91-XXXX-XXXX99"""
    clean_phone = ''.join(filter(str.isdigit, phone))
    if len(clean_phone) < 4:
        return "*" * len(clean_phone)
    return "*" * (len(clean_phone) - 2) + clean_phone[-2:]


if __name__ == "__main__":
    # Test utilities
    print("Email validation:", validate_email("user@example.com"))
    print("Phone validation:", validate_phone("9876543210"))
    print("Pagination:", get_pagination_metadata(100, 0, 10))
    print("Slugify:", slugify("Hello World Test"))
    print("Mask email:", mask_email("user@example.com"))
