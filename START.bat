@echo off
echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║       ACC CLUB - START FRONTEND & BACKEND                      ║
echo ║       Analytics & Consultancy Club                             ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.

REM Check if backend folder exists
if not exist "backend" (
    echo ERROR: Backend folder not found!
    echo Make sure you're in the ACC CLUB project directory.
    pause
    exit /b 1
)

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH!
    echo Please install Python from https://www.python.org/downloads/
    echo Remember to check "Add Python to PATH" during installation.
    pause
    exit /b 1
)

echo [1/4] Checking Python installation...
python --version
echo.

echo [2/4] Starting Backend Server...
echo.
echo Backend will start at: http://localhost:8000
echo API Documentation: http://localhost:8000/docs
echo.
timeout /t 2 /nobreak

REM Start backend in new window
start cmd /k "cd backend && python main.py"

echo [3/4] Waiting for backend to start...
timeout /t 3 /nobreak

echo.
echo [4/4] Opening Frontend in Browser...
timeout /t 1 /nobreak

REM Open the index.html in default browser
start "" "index.html"

echo.
echo ╔════════════════════════════════════════════════════════════════╗
echo ║                   ✓ STARTUP COMPLETE                          ║
echo ║                                                                ║
echo ║  Frontend:  Opening in your default browser                   ║
echo ║  Backend:   http://localhost:8000                             ║
echo ║  API Docs:  http://localhost:8000/docs                        ║
echo ║                                                                ║
echo ║  Note: Backend runs in a separate window                      ║
echo ║  Close the backend window to stop the server                  ║
echo ╚════════════════════════════════════════════════════════════════╝
echo.
pause
