#!/bin/bash

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║       ACC CLUB - START FRONTEND & BACKEND                      ║"
echo "║       Analytics & Consultancy Club                             ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Check if backend folder exists
if [ ! -d "backend" ]; then
    echo "ERROR: Backend folder not found!"
    echo "Make sure you're in the ACC CLUB project directory."
    exit 1
fi

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 is not installed!"
    echo "Please install Python from https://www.python.org/downloads/"
    exit 1
fi

echo "[1/4] Checking Python installation..."
python3 --version
echo ""

echo "[2/4] Starting Backend Server..."
echo ""
echo "Backend will start at: http://localhost:8000"
echo "API Documentation: http://localhost:8000/docs"
echo ""
sleep 2

# Start backend in background
cd backend
python3 main.py > ../backend.log 2>&1 &
BACKEND_PID=$!
echo "Backend PID: $BACKEND_PID"
cd ..

echo "[3/4] Waiting for backend to start..."
sleep 3

echo ""
echo "[4/4] Opening Frontend in Browser..."
sleep 1

# Open in browser based on OS
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    open index.html
else
    # Linux
    xdg-open index.html 2>/dev/null || echo "Please open index.html manually"
fi

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                   ✓ STARTUP COMPLETE                          ║"
echo "║                                                                ║"
echo "║  Frontend:  Opening in your default browser                   ║"
echo "║  Backend:   http://localhost:8000                             ║"
echo "║  API Docs:  http://localhost:8000/docs                        ║"
echo "║                                                                ║"
echo "║  Backend is running with PID: $BACKEND_PID                    ║"
echo "║  Logs: backend.log                                            ║"
echo "║                                                                ║"
echo "║  To stop backend:  kill $BACKEND_PID                          ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# Keep script running
wait
