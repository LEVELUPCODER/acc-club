"""
ACC CLUB - Connection Status Checker
Verify that frontend and backend are properly connected
"""

import subprocess
import time
import sys
import json
from urllib.request import urlopen, Request
from urllib.error import URLError

print("""
╔════════════════════════════════════════════════════════════════╗
║            ACC CLUB - CONNECTION STATUS CHECK                  ║
║                                                                ║
║  This script verifies that the frontend and backend are        ║
║  properly connected and ready to use.                          ║
╚════════════════════════════════════════════════════════════════╝
""")

def check_python():
    """Check if Python is available"""
    print("[1/5] Checking Python Installation...")
    try:
        result = subprocess.run(['python', '--version'], capture_output=True, text=True)
        print(f"  ✓ Python {result.stdout.strip()}")
        return True
    except Exception as e:
        print(f"  ✗ Python not found: {e}")
        return False

def check_backend_files():
    """Check if backend folder and files exist"""
    print("[2/5] Checking Backend Files...")
    import os
    
    backend_path = "backend"
    required_files = ['main.py', 'config.py', 'requirements.txt']
    
    if os.path.exists(backend_path):
        print(f"  ✓ Backend folder exists: {backend_path}/")
        
        for file in required_files:
            file_path = os.path.join(backend_path, file)
            if os.path.exists(file_path):
                print(f"    ✓ {file}")
            else:
                print(f"    ✗ {file} missing!")
                return False
        return True
    else:
        print(f"  ✗ Backend folder not found: {backend_path}/")
        return False

def check_frontend_file():
    """Check if frontend HTML exists"""
    print("[3/5] Checking Frontend Files...")
    import os
    
    if os.path.exists('index.html'):
        print("  ✓ Frontend file exists: index.html")
        
        # Check if API configuration is present
        with open('index.html', 'r') as f:
            content = f.read()
            if 'API_BASE_URL' in content and 'localhost:8000' in content:
                print("  ✓ API configuration found in HTML")
                return True
            else:
                print("  ⚠ API configuration not found in HTML")
                return False
    else:
        print("  ✗ Frontend file not found: index.html")
        return False

def check_backend_running():
    """Check if backend is running"""
    print("[4/5] Checking Backend Connection...")
    
    try:
        # Try to connect to health endpoint
        request = Request('http://localhost:8000/health', method='GET')
        response = urlopen(request, timeout=2)
        data = json.loads(response.read().decode('utf-8'))
        
        if data.get('status') == 'healthy':
            print("  ✓ Backend is running and healthy")
            print(f"    URL: http://localhost:8000")
            print(f"    Status: {data.get('status')}")
            return True
        else:
            print("  ⚠ Backend response unexpected")
            return False
            
    except URLError as e:
        print(f"  ✗ Backend not responding")
        print(f"    Error: {e.reason}")
        print(f"    To start backend: python backend/main.py")
        return False
    except Exception as e:
        print(f"  ✗ Error connecting to backend: {e}")
        return False

def check_api_endpoints():
    """Check if API endpoints are accessible"""
    print("[5/5] Checking API Endpoints...")
    
    endpoints = [
        ('GET', '/health', 'http://localhost:8000/health'),
        ('GET', '/docs', 'http://localhost:8000/docs'),
        ('GET', '/api/team', 'http://localhost:8000/api/team'),
    ]
    
    backend_running = False
    
    for method, name, url in endpoints:
        try:
            request = Request(url, method=method)
            response = urlopen(request, timeout=2)
            print(f"  ✓ {method} {name} - OK ({response.status})")
            backend_running = True
        except Exception as e:
            print(f"  ✗ {method} {name} - Failed")
    
    return backend_running

def print_next_steps(frontend_ok, backend_ok):
    """Print recommendations based on status"""
    print("\n" + "="*64)
    print("NEXT STEPS")
    print("="*64 + "\n")
    
    if frontend_ok and backend_ok:
        print("✓ Everything is connected and ready!")
        print("\n1. Open your browser and navigate to:")
        print("   • Frontend: file:///path/to/index.html")
        print("   • API Docs: http://localhost:8000/docs")
        print("\n2. Test the registration form by:")
        print("   • Clicking 'Join ACC Club' button")
        print("   • Filling in the form")
        print("   • Submitting registration")
        print("\n3. Check API documentation at:")
        print("   • http://localhost:8000/docs (Swagger UI)")
        print("   • http://localhost:8000/redoc (ReDoc)")
    
    elif frontend_ok and not backend_ok:
        print("⚠ Frontend is ready but backend is not running!")
        print("\nTo start the backend:")
        print("  Windows: python backend/main.py")
        print("  macOS/Linux: python3 backend/main.py")
        print("\nOr use the automated startup script:")
        print("  Windows: START.bat")
        print("  macOS/Linux: bash START.sh")
    
    elif not frontend_ok and backend_ok:
        print("⚠ Backend is running but frontend is not properly configured!")
        print("\nPlease check:")
        print("  • index.html exists in the project root")
        print("  • API_BASE_URL is configured in HTML")
    
    else:
        print("✗ Both frontend and backend need setup")
        print("\nTo start everything:")
        print("  Windows: START.bat")
        print("  macOS/Linux: bash START.sh")
        print("\nOr manually:")
        print("  1. Install dependencies: pip install -r backend/requirements.txt")
        print("  2. Start backend: python backend/main.py")
        print("  3. Open index.html in browser")
    
    print("\n" + "="*64 + "\n")

def main():
    """Run all checks"""
    
    results = {
        'python': check_python(),
        'backend_files': check_backend_files(),
        'frontend_files': check_frontend_file(),
        'backend_running': check_backend_running(),
    }
    
    # Only check endpoints if backend is running
    if results['backend_running']:
        results['api_endpoints'] = check_api_endpoints()
    
    print("\n" + "="*64)
    print("SUMMARY")
    print("="*64)
    
    for check, status in results.items():
        status_str = "✓" if status else "✗"
        check_name = check.replace('_', ' ').title()
        print(f"  {status_str} {check_name}: {'OK' if status else 'FAILED'}")
    
    print("="*64)
    
    # Print recommendations
    frontend_ok = results['frontend_files']
    backend_ok = results['backend_running'] or (results['python'] and results['backend_files'])
    
    print_next_steps(frontend_ok, backend_ok)
    
    # Return exit code
    all_ok = all(results.values())
    return 0 if all_ok else 1

if __name__ == "__main__":
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print("\n\nCheck cancelled by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        sys.exit(1)
