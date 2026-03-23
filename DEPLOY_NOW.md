# 🚀 ACC Club - Deploy in 3 Steps

## Step 1: Push to GitHub (Run This)

**Windows:**
```bash
DEPLOY.bat
```

**macOS/Linux:**
```bash
bash DEPLOY.sh
```

This will:
- ✅ Initialize Git
- ✅ Commit all files
- ✅ Push to GitHub

## Step 2: Deploy to Vercel (Pick One)

### Option A: Vercel CLI (Fastest)
```bash
npm install -g vercel
vercel
```
Follow prompts → Done!

### Option B: Web Dashboard (Easiest)
1. Go to [vercel.com/new](https://vercel.com/new)
2. Click "Import Git Repository"
3. Paste your GitHub URL: `https://github.com/YOUR_USERNAME/acc-club`
4. Click "Deploy"
5. Wait 1-2 minutes → Live!

## Step 3: Update Frontend URL

After deployment, you'll get a URL like: `https://acc-club.vercel.app`

Edit `index.html`:
- Find: `const API_BASE_URL = "http://localhost:8000/api"`
- Replace with: `const API_BASE_URL = "https://acc-club.vercel.app/api"`

Then:
```bash
git add index.html
git commit -m "Update API URL for Vercel"
git push
```

---

## ✅ Done!

Your app is now live at `https://acc-club.vercel.app` 🎉

### Test It
1. Open your Vercel domain
2. Click "Join ACC Club"
3. Fill form and submit
4. See success screen

### View Logs
```bash
vercel logs
```

### Custom Domain
Add your own domain in Vercel Dashboard → Settings → Domains

---

## ⚠️ Prerequisites

- **GitHub Account**: [github.com/signup](https://github.com/signup)
- **Vercel Account**: [vercel.com/signup](https://vercel.com/signup) (free)
- **Git Installed**: [git-scm.com](https://git-scm.com)
- **Node.js** (for Vercel CLI): [nodejs.org](https://nodejs.org)

---

## If Something Goes Wrong

**"git push failed"**
→ Set up GitHub SSH key or use personal access token

**"Vercel build error"**
→ Check: `vercel logs`

**"CORS error"**
→ Update `api/index.py` → redeploy

---

**Need help?** See VERCEL_DEPLOYMENT.md for detailed guide
