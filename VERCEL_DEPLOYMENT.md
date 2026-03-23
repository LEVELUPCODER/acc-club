# 🚀 ACC Club - Vercel Deployment Guide

Deploy your ACC Club application to Vercel in minutes!

## Prerequisites

- [Vercel account](https://vercel.com) (free tier available)
- [Git installed](https://git-scm.com)
- This ACC Club project on GitHub

## Step 1: Push to GitHub

Before deploying, your project needs to be on GitHub.

### Create GitHub Repository

```bash
# Navigate to your project
cd e:\PROJECTS\ACC\ CLUB

# Initialize Git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial ACC Club deployment"

# Create repository on GitHub at github.com/new

# Add remote and push
git remote add origin https://github.com/YOUR_USERNAME/acc-club.git
git branch -M main
git push -u origin main
```

## Step 2: Deploy to Vercel

### Option A: Using Vercel CLI (Fastest)

```bash
# Install Vercel CLI
npm install -g vercel

# Deploy from project directory
cd e:\PROJECTS\ACC\ CLUB
vercel

# Follow prompts:
# - Link to GitHub account
# - Select project
# - Choose settings
# - Deploy!
```

### Option B: Using Vercel Web Interface

1. Go to [vercel.com/new](https://vercel.com/new)
2. Click **"Import Git Repository"**
3. Paste your GitHub URL
4. Click **"Import"**
5. Configure project:
   - **Framework**: Other (since it's HTML + Python)
   - **Root Directory**: `.` (root)
   - **Build Command**: `pip install -r requirements.txt`
6. Click **"Deploy"**

## Step 3: Update Frontend URL

After deployment, Vercel gives you a domain like `acc-club.vercel.app`.

### Update index.html

Find this line in `index.html`:
```javascript
const API_BASE_URL = "http://localhost:8000/api";
```

Replace with your Vercel domain:
```javascript
const API_BASE_URL = "https://acc-club.vercel.app/api";
```

Then commit and push:
```bash
git add index.html
git commit -m "Update API base URL for Vercel deployment"
git push
```

## Project Structure for Vercel

```
ACC CLUB/
├── index.html              ← Frontend (served as static)
├── vercel.json             ← Vercel config ✨ NEW
├── .vercelignore           ← Exclude files ✨ NEW
├── requirements.txt        ← Python deps ✨ NEW
│
├── api/                    ← Serverless Python ✨ NEW
│   └── index.py           ← FastAPI handler
│
└── backend/               ← Backend modules
    ├── routes/
    │   ├── registrations.py
    │   ├── projects.py
    │   └── team.py
    ├── schemas.py
    ├── utils.py
    └── ... (other files)
```

## How It Works on Vercel

1. **Frontend**: `index.html` served as static file
2. **Backend API**: Python FastAPI running as serverless functions in `/api` directory
3. **Routing**: 
   - `/docs` → API documentation
   - `/api/*` → Serverless backend routes
   - Everything else → Static files

## Environment Variables (Optional)

To add environment variables for your Vercel deployment:

1. Go to your **Vercel Project Dashboard**
2. Click **Settings** → **Environment Variables**
3. Add variables:
   - `DATABASE_URL` (for future database integration)
   - `LOG_LEVEL` (debug/info/warning/error)
   - `CORS_ORIGINS` (allowed domains)

Example:
```
DATABASE_URL=postgresql://user:password@db.example.com/acc_club
LOG_LEVEL=info
CORS_ORIGINS=https://acc-club.vercel.app
```

## Deployment Checklist

- [ ] Project pushed to GitHub
- [ ] Vercel project created and deployed
- [ ] Vercel domain obtained (e.g., acc-club.vercel.app)
- [ ] `index.html` updated with correct API URL
- [ ] Changes pushed to GitHub
- [ ] Frontend loads in browser
- [ ] Registration form submits successfully
- [ ] Backend API responds with data
- [ ] `/docs` endpoint shows Swagger UI
- [ ] No CORS errors in browser console

## Test Your Deployment

### 1. Check Frontend
```
Open: https://acc-club.vercel.app
Should see the ACC Club website
```

### 2. Check API Health
```
curl https://acc-club.vercel.app/health
Response: { "status": "healthy", ... }
```

### 3. Check Documentation
```
Open: https://acc-club.vercel.app/docs
Should see Swagger UI with all endpoints
```

### 4. Test Registration
```
1. Open website
2. Click "Join ACC Club"
3. Fill 4-step form
4. Submit
5. Should see success screen with enrollment number
```

## Monitoring & Logs

### View Logs
```bash
# Using Vercel CLI
vercel logs

# Or via Web:
# 1. Go to Vercel Dashboard
# 2. Select your project
# 3. Click "Deployments"
# 4. Select latest deployment
# 5. View "Logs"
```

### Monitor Performance
Visit Vercel Dashboard → **Analytics** tab to see:
- Request count
- Response times
- Error rates
- Bandwidth usage

## Troubleshooting

### Issue: 502 Bad Gateway

**Cause**: Backend serverless function failing

**Solution**:
```bash
# Check logs
vercel logs

# Common issues:
# - Missing dependencies in requirements.txt
# - Import errors in api/index.py
# - Missing environment variables

# Redeploy:
git push  # Vercel auto-redeployes on git push
```

### Issue: CORS Error in Browser

**Cause**: Frontend URL not in allowed origins

**Solution**:
1. Open `api/index.py`
2. Update `allow_origins` list:
```python
allow_origins=[
    "https://acc-club.vercel.app",  # Add your domain
    "http://localhost:3000",
    "*"
]
```
3. Commit and push:
```bash
git add api/index.py
git commit -m "Update CORS origins"
git push
```

### Issue: API Timeouts

**Cause**: Serverless function taking too long

**Solution**:
- Check database queries
- Optimize backend logic
- Monitor in Vercel Analytics

### Issue: 404 on `/api/*` endpoints

**Cause**: Routing not configured correctly

**Solution**:
- Verify `vercel.json` routes are correct
- Check `api/index.py` imports work
- Verify backend files are uploaded

## Custom Domain

To use your own domain instead of `acc-club.vercel.app`:

1. Go to **Vercel Dashboard** → **Settings** → **Domains**
2. Enter your domain (e.g., `accclub.com`)
3. Follow DNS instructions from your domain registrar
4. Vercel will provision SSL certificate automatically

## Cost

**Vercel Pricing** (as of 2024):
- Frontend (static): Free tier included
- Backend (serverless): 
  - Free: 100 GB-hours/month
  - Paid: $0.50 per GB-hour additional

**Estimated cost**: FREE for most projects under free tier

## Next Steps

1. ✅ Deploy to Vercel
2. Test all features
3. Set up custom domain (optional)
4. Monitor performance
5. Plan future enhancements (database, auth, etc.)

## Support & Resources

- [Vercel Documentation](https://vercel.com/docs)
- [FastAPI on Vercel](https://vercel.com/guides/deploying-fastapi-with-vercel)
- [Environment Variables](https://vercel.com/docs/concepts/projects/environment-variables)
- [Custom Domains](https://vercel.com/docs/concepts/projects/domains)
- [Monitoring](https://vercel.com/docs/analytics)

## Rollback to Previous Deployment

If something goes wrong:

```bash
# Via Vercel CLI
vercel --prod  # Redeploy current version

# Via Dashboard:
# 1. Go to Deployments tab
# 2. Select previous working deployment
# 3. Click "Promote to Production"
```

---

## Summary

Your ACC Club application is now:
✅ Deployed on Vercel (global CDN)
✅ Accessible via `https://acc-club.vercel.app`
✅ Frontend + Backend running serverless
✅ Auto-scaled on demand
✅ Zero infrastructure management

**Enjoy your deployed application! 🎉**

---

**Questions?** Check the troubleshooting section or visit [vercel.com/docs](https://vercel.com/docs)
