#!/bin/bash

# Congress Indexes - GitHub Repository Setup Script
# This script helps you set up your GitHub repository

echo "🚀 Congress Indexes - GitHub Repository Setup"
echo "=============================================="
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "❌ Git is not installed. Please install Git first."
    exit 1
fi

# Check if we're in the right directory
if [ ! -f "app.py" ]; then
    echo "❌ app.py not found. Please run this script from the project directory."
    exit 1
fi

echo "✅ Found project files. Starting setup..."
echo ""

# Get GitHub username
read -p "Enter your GitHub username (e.g., clichedcarbide2v): " github_username

if [ -z "$github_username" ]; then
    echo "❌ GitHub username is required."
    exit 1
fi

# Validate GitHub username format (no @ symbols, no spaces)
if [[ "$github_username" == *"@"* ]] || [[ "$github_username" == *" "* ]]; then
    echo "❌ Invalid GitHub username format. Please enter your GitHub username (not email)."
    echo "   Example: clichedcarbide2v (not cliched.carbide2v@icloud.com)"
    exit 1
fi

# Get repository name
read -p "Enter repository name (default: congress-indexes): " repo_name
repo_name=${repo_name:-congress-indexes}

echo ""
echo "📋 Repository Details:"
echo "  Username: $github_username"
echo "  Repository: $repo_name"
echo "  URL: https://github.com/$github_username/$repo_name"
echo ""

# Confirm setup
read -p "Continue with setup? (y/N): " confirm
if [[ ! $confirm =~ ^[Yy]$ ]]; then
    echo "❌ Setup cancelled."
    exit 1
fi

echo ""
echo "🔧 Setting up Git repository..."

# Initialize git if not already done
if [ ! -d ".git" ]; then
    git init
    echo "✅ Initialized Git repository"
else
    echo "✅ Git repository already exists"
fi

# Add all files
git add .
echo "✅ Added all files to Git"

# Make initial commit
git commit -m "Initial commit: Congress Indexes Dashboard

- Flask web application with both indexes
- Interactive dashboard with charts and tables
- Real-time data loading and CSV export
- Responsive design with Tailwind CSS
- Ready for Vercel deployment"

echo "✅ Created initial commit"

# Add remote origin
git remote add origin https://github.com/$github_username/$repo_name.git
echo "✅ Added remote origin"

# Push to GitHub
echo ""
echo "📤 Pushing to GitHub..."
git push -u origin main

if [ $? -eq 0 ]; then
    echo ""
    echo "🎉 SUCCESS! Your repository is now on GitHub!"
    echo ""
    echo "📋 Next Steps:"
    echo "1. Visit: https://github.com/$github_username/$repo_name"
    echo "2. Verify all files are uploaded correctly"
    echo "3. Follow the DEPLOYMENT_GUIDE.md to deploy to Vercel"
    echo ""
    echo "🔗 Quick Links:"
    echo "  Repository: https://github.com/$github_username/$repo_name"
    echo "  Deploy to Vercel: https://vercel.com/new/clone?repository-url=https://github.com/$github_username/$repo_name"
    echo ""
    echo "📚 Documentation:"
    echo "  - README.md - Project overview"
    echo "  - DEPLOYMENT_GUIDE.md - Vercel deployment"
    echo "  - GITHUB_SETUP_GUIDE.md - Detailed GitHub setup"
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