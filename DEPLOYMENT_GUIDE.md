# Congress Indexes - Vercel Deployment Guide

## Overview

This guide will help you deploy the Congress Indexes web application to Vercel. The application includes both the Congress Buys Index and Congress Equity Exposure Index with a modern web interface.

## Prerequisites

1. **GitHub Account**: You'll need a GitHub account to host your code
2. **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
3. **Python Knowledge**: Basic understanding of Python and web development

## Step 1: Prepare Your Repository

### 1.1 Create a GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Name it something like `congress-indexes` or `congress-trading-dashboard`
3. Make it public or private (your choice)

### 1.2 Upload Your Code

```bash
# Clone your repository locally
git clone https://github.com/YOUR_USERNAME/congress-indexes.git
cd congress-indexes

# Copy all the files from your current directory
# Make sure you have these files:
# - app.py
# - congress_buys_index.py
# - congress_equity_exposure_index.py
# - requirements.txt
# - vercel.json
# - templates/ (directory with HTML files)
# - All other supporting files

# Add and commit your files
git add .
git commit -m "Initial commit: Congress Indexes web application"
git push origin main
```

## Step 2: Deploy to Vercel

### 2.1 Connect to Vercel

1. Go to [vercel.com](https://vercel.com) and sign in
2. Click "New Project"
3. Import your GitHub repository
4. Select the repository you just created

### 2.2 Configure the Project

Vercel should automatically detect that this is a Python project. The configuration is already set up in `vercel.json`.

**Project Settings:**
- **Framework Preset**: Other
- **Root Directory**: `./` (default)
- **Build Command**: Leave empty (Vercel will auto-detect)
- **Output Directory**: Leave empty (Vercel will auto-detect)
- **Install Command**: `pip install -r requirements.txt`

### 2.3 Deploy

1. Click "Deploy"
2. Wait for the build to complete (usually 2-3 minutes)
3. Your application will be live at a URL like: `https://your-project-name.vercel.app`

## Step 3: Test Your Deployment

### 3.1 Check the Main Dashboard

Visit your Vercel URL and you should see:
- Main dashboard with both indexes
- Interactive charts and tables
- Real-time data loading

### 3.2 Test API Endpoints

Test these endpoints:
- `https://your-project.vercel.app/api/health` - Health check
- `https://your-project.vercel.app/api/congress-buys` - Congress Buys Index
- `https://your-project.vercel.app/api/congress-equity-exposure` - Equity Exposure Index

### 3.3 Test Individual Pages

- `https://your-project.vercel.app/congress-buys` - Congress Buys detailed page
- `https://your-project.vercel.app/congress-equity-exposure` - Equity Exposure detailed page

## Step 4: Customize and Enhance

### 4.1 Add Real API Keys

To use real data instead of sample data:

1. **Get QuiverQuant API Key**:
   - Sign up at [QuiverQuant](https://quiverquant.com)
   - Get your API key

2. **Add Environment Variables in Vercel**:
   - Go to your Vercel project dashboard
   - Click "Settings" → "Environment Variables"
   - Add: `QUIVERQUANT_API_KEY` = your_api_key_here

3. **Update the Code**:
   - Modify the index classes to use the environment variable
   - Add error handling for API rate limits

### 4.2 Custom Domain (Optional)

1. In Vercel dashboard, go to "Settings" → "Domains"
2. Add your custom domain
3. Follow the DNS configuration instructions

### 4.3 Set Up Automatic Deployments

- Every push to the `main` branch will automatically deploy
- You can also set up preview deployments for pull requests

## Step 5: Monitor and Maintain

### 5.1 Monitor Performance

- Use Vercel Analytics to track performance
- Monitor API response times
- Check for errors in the Vercel dashboard

### 5.2 Update Data Sources

- Keep your sample data updated
- Add more realistic scenarios
- Implement caching for better performance

### 5.3 Security Considerations

- The current implementation uses sample data (safe for public deployment)
- If using real API keys, ensure they're properly secured
- Consider rate limiting for API endpoints

## Troubleshooting

### Common Issues

1. **Build Failures**:
   - Check that all dependencies are in `requirements.txt`
   - Ensure Python version compatibility
   - Check Vercel build logs for specific errors

2. **Import Errors**:
   - Make sure all Python files are in the root directory
   - Check that `vercel.json` has the correct `PYTHONPATH`

3. **API Errors**:
   - Verify API endpoints are working
   - Check CORS settings if needed
   - Ensure proper error handling

4. **Performance Issues**:
   - Optimize data loading
   - Implement caching
   - Consider using Vercel Edge Functions for better performance

### Getting Help

- **Vercel Documentation**: [vercel.com/docs](https://vercel.com/docs)
- **Flask Documentation**: [flask.palletsprojects.com](https://flask.palletsprojects.com)
- **GitHub Issues**: Create issues in your repository for bugs

## File Structure

Your repository should look like this:

```
congress-indexes/
├── app.py                          # Main Flask application
├── congress_buys_index.py          # Congress Buys Index implementation
├── congress_equity_exposure_index.py # Equity Exposure Index implementation
├── requirements.txt                # Python dependencies
├── vercel.json                     # Vercel configuration
├── templates/                      # HTML templates
│   ├── index.html                  # Main dashboard
│   ├── congress_buys.html          # Congress Buys page
│   └── congress_equity_exposure.html # Equity Exposure page
├── DEPLOYMENT_GUIDE.md             # This file
└── README.md                       # Project documentation
```

## Next Steps

1. **Add Real Data Integration**: Connect to actual congressional trading APIs
2. **Implement Caching**: Add Redis or similar for better performance
3. **Add Authentication**: If needed for private data
4. **Mobile Optimization**: Improve mobile experience
5. **Analytics**: Add usage tracking and analytics
6. **Automated Updates**: Set up cron jobs for data updates

## Support

For deployment issues:
1. Check Vercel build logs
2. Verify all files are committed to GitHub
3. Ensure `vercel.json` is properly configured
4. Test locally before deploying

For application issues:
1. Check browser console for JavaScript errors
2. Verify API endpoints are responding
3. Test with different browsers
4. Check network connectivity

---

**Happy Deploying! 🚀**

Your Congress Indexes dashboard will be live and accessible to anyone with the URL once deployed successfully. 