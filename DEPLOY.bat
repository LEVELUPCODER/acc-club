@echo off
REM ACC Club - Fast Deployment to Vercel
REM This script pushes to GitHub and provides Vercel deployment commands

echo.
echo ========================================
echo ACC Club - FAST DEPLOYMENT SCRIPT
echo ========================================
echo.

REM Check if Git is installed
git --version > nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed.
    echo Install from: https://git-scm.com/download/win
    pause
    exit /b 1
)

REM Initialize Git repo if needed
if not exist .git (
    echo [1/4] Initializing Git repository...
    git init
    git add .
    git commit -m "ACC Club - Initial deployment"
) else (
    echo [1/4] Git repository already initialized
)

REM Check if remote exists
git remote get-url origin > nul 2>&1
if errorlevel 1 (
    echo.
    echo [2/4] ERROR: Git remote not set
    echo.
    echo You need to create a GitHub repository first:
    echo 1. Go to https://github.com/new
    echo 2. Create a repository called 'acc-club'
    echo 3. Copy the repository URL
    echo 4. Run this command:
    echo    git remote add origin YOUR_GITHUB_URL
    echo    git push -u origin main
    echo.
    pause
    exit /b 1
)

echo [2/4] Staging changes...
git add .

REM Check if there are changes to commit
git diff --cached --quiet
if errorlevel 1 (
    echo [3/4] Committing changes...
    git commit -m "ACC Club deployment updates"
) else (
    echo [3/4] No new changes to commit
)

echo [4/4] Pushing to GitHub...
git push -u origin main

if errorlevel 1 (
    echo.
    echo ERROR: Git push failed
    echo Check your GitHub credentials and try again
    pause
    exit /b 1
)

echo.
echo ========================================
echo SUCCESS! Now deploy to Vercel:
echo ========================================
echo.
echo OPTION A - Vercel CLI (Recommended):
echo   1. Install: npm install -g vercel
echo   2. Run: vercel
echo   3. Follow the prompts
echo.
echo OPTION B - Vercel Web (Easiest):
echo   1. Go to: https://vercel.com/new
echo   2. Click "Import Git Repository"
echo   3. Paste: https://github.com/YOUR_USERNAME/acc-club
echo   4. Click Import and Deploy
echo.
echo OPTION C - Vercel CLI One-Liner:
echo   npm install -g vercel ^&^& vercel
echo.
echo ========================================
echo Your app will be live at:
echo   https://acc-club.vercel.app
echo ========================================
echo.
echo Next: Update API_BASE_URL in index.html
echo Change: http://localhost:8000/api
echo To: https://acc-club.vercel.app/api
echo.
pause
