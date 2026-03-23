@echo off
REM ACC Club Backend Setup Script for Windows

echo ========================================
echo ACC Club Backend - Setup Script
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org
    pause
    exit /b 1
)

echo [1/4] Creating virtual environment...
python -m venv venv
if errorlevel 1 (
    echo Error: Failed to create virtual environment
    pause
    exit /b 1
)

echo [2/4] Activating virtual environment...
call venv\Scripts\activate.bat

echo [3/4] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo [4/4] Creating .env file...
copy .env.example .env >nul 2>&1

echo.
echo ========================================
echo Setup completed successfully!
echo ========================================
echo.
echo To start the server, run:
echo   venv\Scripts\activate.bat
echo   python main.py
echo.
echo API Documentation will be available at:
echo   http://localhost:8000/docs
echo.
pause
