# GitHub Repository Setup Guide

This guide will help you create and set up the GitHub repository for the Congress Indexes project.

## Step 1: Create GitHub Repository

### 1.1 Go to GitHub
1. Open your browser and go to [github.com](https://github.com)
2. Sign in to your account (or create one if you don't have it)

### 1.2 Create New Repository
1. Click the **"+"** icon in the top right corner
2. Select **"New repository"**
3. Fill in the repository details:
   - **Repository name**: `congress-indexes` (or your preferred name)
   - **Description**: `Congress Trading Indexes Dashboard - Real-time congressional trading data visualization`
   - **Visibility**: Choose Public or Private
   - **Initialize with**: Leave unchecked (we'll add files manually)

4. Click **"Create repository"**

## Step 2: Prepare Your Local Files

### 2.1 Create Project Directory
```bash
# Create a new directory for your project
mkdir congress-indexes
cd congress-indexes
```

### 2.2 Copy All Project Files
Make sure you have all these files in your directory:

**Core Application Files:**
- `app.py` - Main Flask application
- `congress_buys_index.py` - Congress Buys Index
- `congress_equity_exposure_index.py` - Equity Exposure Index
- `congress_equity_exposure_config.py` - Configuration
- `requirements.txt` - Dependencies
- `vercel.json` - Vercel configuration

**Templates:**
- `templates/index.html` - Main dashboard
- `templates/congress_buys.html` - Congress Buys page
- `templates/congress_equity_exposure.html` - Equity Exposure page

**Documentation:**
- `README.md` - Project documentation
- `DEPLOYMENT_GUIDE.md` - Vercel deployment guide
- `GITHUB_SETUP_GUIDE.md` - This file

**Supporting Files:**
- `config.py` - Original config
- `test_index.py` - Test scripts
- `validate_equity_exposure_index.py` - Validation scripts
- Any other files from your current directory

## Step 3: Initialize Git Repository

### 3.1 Initialize Git
```bash
# Initialize git repository
git init

# Add all files to git
git add .

# Make initial commit
git commit -m "Initial commit: Congress Indexes Dashboard

- Flask web application with both indexes
- Interactive dashboard with charts and tables
- Real-time data loading and CSV export
- Responsive design with Tailwind CSS
- Ready for Vercel deployment"
```

### 3.2 Connect to GitHub
```bash
# Add the remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/congress-indexes.git

# Push to GitHub
git push -u origin main
```

## Step 4: Verify Repository Setup

### 4.1 Check GitHub Repository
1. Go to your GitHub repository URL
2. Verify all files are uploaded correctly
3. Check that the README.md displays properly

### 4.2 Test Local Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Test the application (use a different port if 5000 is busy)
python3 app.py --port 5001
```

## Step 5: Repository Settings (Optional)

### 5.1 Add Repository Topics
1. Go to your repository on GitHub
2. Click **"About"** section
3. Click the gear icon next to **"Topics"**
4. Add relevant topics:
   - `congress`
   - `trading`
   - `dashboard`
   - `flask`
   - `python`
   - `vercel`
   - `data-visualization`

### 5.2 Add Repository Description
Update the repository description to be more descriptive:
```
Congress Trading Indexes Dashboard - Real-time visualization of congressional trading activity with interactive charts, configurable timeframes, and CSV export functionality.
```

### 5.3 Enable GitHub Pages (Optional)
If you want to host documentation:
1. Go to **Settings** → **Pages**
2. Select **"Deploy from a branch"**
3. Choose **"main"** branch and **"/docs"** folder
4. Click **"Save"**

## Step 6: Create Issues and Projects (Optional)

### 6.1 Create Sample Issues
Create some sample issues to track development:

**Issue 1: Add Real Data Integration**
- Title: "Integrate QuiverQuant API for real congressional data"
- Description: "Replace sample data with real congressional trading data from QuiverQuant API"

**Issue 2: Add Authentication**
- Title: "Implement user authentication system"
- Description: "Add login/logout functionality for private data access"

**Issue 3: Mobile Optimization**
- Title: "Improve mobile user experience"
- Description: "Enhance responsive design for better mobile usability"

### 6.2 Create Project Board
1. Go to **Projects** tab
2. Click **"New project"**
3. Choose **"Board"** template
4. Name it **"Congress Indexes Development"**
5. Add columns: **To Do**, **In Progress**, **Done**

## Step 7: Set Up Branch Protection (Recommended)

### 7.1 Protect Main Branch
1. Go to **Settings** → **Branches**
2. Click **"Add rule"**
3. Set **Branch name pattern** to `main`
4. Enable:
   - ✅ **Require a pull request before merging**
   - ✅ **Require status checks to pass before merging**
   - ✅ **Include administrators**
5. Click **"Create"**

## Step 8: Add Collaborators (Optional)

### 8.1 Invite Team Members
1. Go to **Settings** → **Collaborators**
2. Click **"Add people"**
3. Enter GitHub usernames or email addresses
4. Choose appropriate permissions

## Step 9: Connect to Vercel

### 9.1 Deploy to Vercel
1. Follow the [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
2. Connect your GitHub repository to Vercel
3. Deploy the application

### 9.2 Add Deployment Badge
Add this to your README.md:
```markdown
[![Deploy to Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/YOUR_USERNAME/congress-indexes)
```

## Step 10: Continuous Updates

### 10.1 Regular Commits
```bash
# Make changes to your code
# Then commit and push
git add .
git commit -m "Description of changes"
git push origin main
```

### 10.2 Version Tags
```bash
# Create version tags for releases
git tag -a v1.0.0 -m "Initial release"
git push origin v1.0.0
```

## Troubleshooting

### Common Issues

1. **Port 5000 in use**:
   ```bash
   # Use a different port
   python3 app.py --port 5001
   ```

2. **Git authentication issues**:
   ```bash
   # Use GitHub CLI or personal access token
   git remote set-url origin https://YOUR_TOKEN@github.com/YOUR_USERNAME/congress-indexes.git
   ```

3. **Missing files**:
   ```bash
   # Check what files are tracked
   git status
   
   # Add missing files
   git add missing_file.py
   git commit -m "Add missing file"
   ```

## Next Steps

1. **Deploy to Vercel** using the deployment guide
2. **Add real API integration** for live data
3. **Set up monitoring** and analytics
4. **Create documentation** for users
5. **Add tests** for reliability

---

**Your GitHub repository is now ready! 🎉**

The repository contains all the necessary files for the Congress Indexes Dashboard and is ready for deployment to Vercel. 