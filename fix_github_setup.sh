#!/bin/bash

# Quick fix for GitHub repository setup
echo "🔧 Fixing GitHub Repository Setup"
echo "=================================="
echo ""

# Check if we're in the right directory
if [ ! -f "app.py" ]; then
    echo "❌ app.py not found. Please run this script from the project directory."
    exit 1
fi

echo "✅ Found project files."
echo ""

# Set the correct GitHub username
github_username="clichedcarbide2v"
repo_name="congress-indexes"

echo "📋 Repository Details:"
echo "  Username: $github_username"
echo "  Repository: $repo_name"
echo "  URL: https://github.com/$github_username/$repo_name"
echo ""

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "🔧 Initializing Git repository..."
    git init
    echo "✅ Git repository initialized"
else
    echo "✅ Git repository already exists"
fi

# Remove any existing remote
git remote remove origin 2>/dev/null

# Add all files
echo "📁 Adding files to Git..."
git add .
echo "✅ Files added to Git"

# Make initial commit
echo "💾 Creating initial commit..."
git commit -m "Initial commit: Congress Indexes Dashboard

- Flask web application with both indexes
- Interactive dashboard with charts and tables
- Real-time data loading and CSV export
- Responsive design with Tailwind CSS
- Ready for Vercel deployment"
echo "✅ Initial commit created"

# Add remote origin with correct username
echo "🔗 Adding remote origin..."
git remote add origin https://github.com/$github_username/$repo_name.git
echo "✅ Remote origin added"

# Push to GitHub
echo ""
echo "📤 Pushing to GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 SUCCESS! Your repository is now on GitHub!"
    echo ""
    echo "📋 Repository URL: https://github.com/$github_username/$repo_name"
    echo ""
    echo "📋 Next Steps:"
    echo "1. Visit: https://github.com/$github_username/$repo_name"
    echo "2. Verify all files are uploaded correctly"
    echo "3. Follow the DEPLOYMENT_GUIDE.md to deploy to Vercel"
    echo ""
    echo "🔗 Quick Deploy to Vercel:"
    echo "https://vercel.com/new/clone?repository-url=https://github.com/$github_username/$repo_name"
    echo ""
else
    echo ""
    echo "❌ Failed to push to GitHub."
    echo ""
    echo "🔧 Troubleshooting:"
    echo "1. Make sure you have access to the repository"
    echo "2. Check your Git credentials"
    echo "3. Try: git remote set-url origin https://YOUR_TOKEN@github.com/$github_username/$repo_name.git"
    echo ""
fi 