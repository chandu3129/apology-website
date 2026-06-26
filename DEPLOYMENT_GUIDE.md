# 🚀 DEPLOYMENT GUIDE TO VERCEL

Follow these steps to deploy your apology website to Vercel and make it publicly accessible!

## Step 1: Install Git (if not already installed)

Download Git from: https://git-scm.com/download/win

After installation, restart your terminal.

## Step 2: Initialize Git & Push to GitHub

1. Open PowerShell in your project folder (C:\Users\tarig\Documents\apology-website)

2. Run these commands:

```powershell
git config --global user.name "chandu3129"
git config --global user.email "your-email@gmail.com"  # Use your actual email

git init
git add .
git commit -m "Initial commit: Apology website for my girlfriend"
git branch -M main
git remote add origin https://github.com/chandu3129/apology-website.git
git push -u origin main
```

**Note**: You may need to generate a GitHub Personal Access Token:
- Go to: https://github.com/settings/tokens
- Click "Generate new token"
- Select scopes: repo, workflow
- Copy the token and use it as your password when git prompts

## Step 3: Create Vercel Account & Deploy

1. Go to: https://vercel.com/signup
2. Click "Continue with GitHub"
3. Authorize Vercel to access your GitHub account
4. Click "New Project"
5. Select "apology-website" repository
6. Configure:
   - Framework Preset: **Other**
   - Root Directory: **./server**
   - Build Command: **npm install**
   - Output Directory: Leave empty
   - Start Command: **npm start**

7. Add Environment Variables (if needed):
   - Skip this for now

8. Click "Deploy"

## Step 4: Set Up GitHub Actions for Auto-Deployment

Once deployed, every time you push to GitHub, Vercel will automatically redeploy!

## Step 5: Share Your URL!

After deployment, Vercel will give you a URL like:
```
https://apology-website-xi.vercel.app
```

Share this link with your girlfriend! 💕

## Troubleshooting

**Issue**: "Cannot find module 'sqlite3'"
- Fix: Vercel might have issues with sqlite3. Try using a different database or the serverless functions approach.

**Issue**: "Port already in use"
- Fix: The server is already running. Stop it and restart: Ctrl+C then npm start

**Issue**: CORS errors
- Fix: Already configured in the code with cors middleware

## Quick Commands Reference

```powershell
# Check git status
git status

# Commit new changes
git add .
git commit -m "Your message"
git push

# Check if server is running
curl http://localhost:3000
```

## Next Steps

1. ✅ Install Git
2. ✅ Push code to GitHub (Step 2)
3. ✅ Deploy to Vercel (Step 3)
4. ✅ Share public URL with girlfriend
5. 💕 Watch her reaction!

---

**Need Help?**
- Vercel Docs: https://vercel.com/docs
- GitHub Help: https://docs.github.com
- Express Docs: https://expressjs.com

Good luck! 💕
