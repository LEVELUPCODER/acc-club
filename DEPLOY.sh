#!/bin/bash
# ACC Club - Fast Deployment to Vercel
# This script pushes to GitHub and provides Vercel deployment commands

echo ""
echo "========================================"
echo "ACC Club - FAST DEPLOYMENT SCRIPT"
echo "========================================"
echo ""

# Check if Git is installed
if ! command -v git &> /dev/null; then
    echo "ERROR: Git is not installed."
    echo "Install from: https://git-scm.com/download/linux"
    exit 1
fi

# Initialize Git repo if needed
if [ ! -d .git ]; then
    echo "[1/4] Initializing Git repository..."
    git init
    git add .
    git commit -m "ACC Club - Initial deployment"
else
    echo "[1/4] Git repository already initialized"
fi

# Check if remote exists
if ! git remote get-url origin &> /dev/null; then
    echo ""
    echo "[2/4] ERROR: Git remote not set"
    echo ""
    echo "You need to create a GitHub repository first:"
    echo "1. Go to https://github.com/new"
    echo "2. Create a repository called 'acc-club'"
    echo "3. Copy the repository URL"
    echo "4. Run this command:"
    echo "   git remote add origin YOUR_GITHUB_URL"
    echo "   git push -u origin main"
    echo ""
    exit 1
fi

echo "[2/4] Staging changes..."
git add .

# Check if there are changes to commit
if ! git diff --cached --quiet; then
    echo "[3/4] Committing changes..."
    git commit -m "ACC Club deployment updates"
else
    echo "[3/4] No new changes to commit"
fi

echo "[4/4] Pushing to GitHub..."
git push -u origin main

if [ $? -ne 0 ]; then
    echo ""
    echo "ERROR: Git push failed"
    echo "Check your GitHub credentials and try again"
    exit 1
fi

echo ""
echo "========================================"
echo "SUCCESS! Now deploy to Vercel:"
echo "========================================"
echo ""
echo "OPTION A - Vercel CLI (Recommended):"
echo "  1. Install: npm install -g vercel"
echo "  2. Run: vercel"
echo "  3. Follow the prompts"
echo ""
echo "OPTION B - Vercel Web (Easiest):"
echo "  1. Go to: https://vercel.com/new"
echo "  2. Click 'Import Git Repository'"
echo "  3. Paste: https://github.com/YOUR_USERNAME/acc-club"
echo "  4. Click Import and Deploy"
echo ""
echo "OPTION C - Vercel CLI One-Liner:"
echo "  npm install -g vercel && vercel"
echo ""
echo "========================================"
echo "Your app will be live at:"
echo "  https://acc-club.vercel.app"
echo "========================================"
echo ""
echo "Next: Update API_BASE_URL in index.html"
echo "Change: http://localhost:8000/api"
echo "To: https://acc-club.vercel.app/api"
echo ""
