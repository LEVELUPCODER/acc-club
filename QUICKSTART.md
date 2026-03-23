# 🚀 ACC Club - Quick Start Guide

Start the entire application with **one command**:

## Windows

```bash
START.bat
```

Or manually:
```bash
python backend/main.py
# Then open index.html in your browser
```

## macOS / Linux

```bash
bash START.sh
```

Or manually:
```bash
cd backend && python3 main.py &
open index.html  # macOS
# or
xdg-open index.html  # Linux
```

---

## What Just Happened? ✨

✅ **Backend**: FastAPI server running at `http://localhost:8000`
✅ **Frontend**: Website opened in your default browser
✅ **Connected**: Frontend can now submit forms to backend API

---

## Try It Out 🎯

### 1. **Join the Club**
   - Click **"Join ACC Club"** button
   - Fill 4-step registration form
   - Submit and get your enrollment number

### 2. **See API Docs**
   - Open `http://localhost:8000/docs` in browser
   - Explore all 14 endpoints interactively
   - Try requests directly from browser

### 3. **Check Connection**
   - Run: `python check_connection.py`
   - Verify all components are connected

---

## File Locations 📁

| File | Purpose |
|------|---------|
| `index.html` | Main website interface |
| `README.md` | Full project documentation |
| `INTEGRATION_GUIDE.md` | Frontend-backend connection details |
| `START.bat` / `START.sh` | One-click startup scripts |
| `check_connection.py` | Connection diagnostic tool |
| `backend/` | FastAPI backend server (21 files) |

---

## Common Issues & Fixes 🔧

### **"Backend not running" error?**
```bash
cd backend
python main.py
```

### **Port 8000 already in use?**
```bash
# Windows
netstat -ano | findstr :8000

# macOS/Linux  
lsof -i :8000
```

### **Python not found?**
```bash
# Install Python from python.org
# Or use package manager:
brew install python3  # macOS
apt install python3   # Ubuntu/Debian
```

### **Can't see form data after submit?**
```bash
# Open DevTools (F12) → Console tab
# Look for error messages
# Check Network tab for API requests
```

---

## Next Steps 📊

1. **Test Registration**: Fill form and submit
2. **View API Docs**: Open `/docs` endpoint
3. **Check Logs**: Look in `backend/logs/` directory
4. **Read Full Guide**: See `INTEGRATION_GUIDE.md`

---

## API Endpoints 🔌

| Method | Endpoint | Purpose |
|--------|----------|---------|
| `GET` | `/health` | Check if backend is running |
| `GET` | `/docs` | Interactive API documentation |
| `POST` | `/api/registrations` | Submit new registration |
| `GET` | `/api/registrations` | List all registrations |
| `GET` | `/api/team` | Get team members |
| `GET` | `/api/projects` | Get projects |

---

## That's It! 🎉

Your full-stack ACC Club application is ready to use!

**Questions?** See `README.md` or `INTEGRATION_GUIDE.md` for detailed documentation.

**Need help?** Run: `python check_connection.py`
