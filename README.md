# Congress Trading Indexes Dashboard

A modern web application that tracks and visualizes congressional trading activity through two sophisticated indexes:

- **Congress Buys Index**: Top 10 stocks by total dollars purchased by Congress in the last 100 days
- **Congress Equity Exposure Index**: Top 10 stocks by largest total congressional net holding value at quarter end

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)
```bash
# Run the automated setup script
./setup_github.sh
```

### Option 2: Manual Setup
1. Create a GitHub repository named `congress-indexes`
2. Follow the [GITHUB_SETUP_GUIDE.md](GITHUB_SETUP_GUIDE.md)
3. Deploy to Vercel using [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

## 📊 Features

- **Interactive Dashboard**: Real-time data with charts and tables
- **Two Indexes**: Congress Buys and Equity Exposure
- **Configurable Timeframes**: 30-180 days for buys, quarter-end for holdings
- **CSV Export**: Download data for analysis
- **Responsive Design**: Works on all devices
- **Modern UI**: Built with Tailwind CSS and Chart.js

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Frontend**: HTML5, JavaScript, Tailwind CSS
- **Charts**: Chart.js
- **Deployment**: Vercel
- **Data**: Sample data (ready for real API integration)

## 📁 Project Structure

```
congress-indexes/
├── app.py                          # Main Flask application
├── congress_buys_index.py          # Congress Buys Index
├── congress_equity_exposure_index.py # Equity Exposure Index
├── requirements.txt                # Python dependencies
├── vercel.json                     # Vercel configuration
├── templates/                      # HTML templates
├── setup_github.sh                 # Automated GitHub setup
├── GITHUB_SETUP_GUIDE.md           # GitHub setup instructions
└── DEPLOYMENT_GUIDE.md             # Vercel deployment guide
```

## 🚀 Deployment

1. **Set up GitHub repository** using `./setup_github.sh`
2. **Deploy to Vercel** following [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
3. **Your app will be live** at `https://your-project.vercel.app`

## 📈 Sample Data

The application includes realistic sample data for demonstration:

### Congress Buys Index
```
Rank  Ticker  Company              Weight  Value
1     NVDA    NVIDIA Corporation   42.3%   $17.0M
2     AVGO    Broadcom Inc.        35.1%   $14.1M
3     MSFT    Microsoft Corporation 9.7%   $3.9M
```

### Congress Equity Exposure Index
```
Rank  Ticker  Company              Weight  Net Shares  Value
1     NVDA    NVIDIA Corporation   35.4%   2,055      $1.7M
2     AVGO    Broadcom Inc.        28.1%   1,160      $1.4M
3     MSFT    Microsoft Corporation 23.9%  2,960      $1.2M
```

## 🔧 Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally (use different port if 5000 is busy)
python3 app.py --port 5001

# Open browser to http://localhost:5001
```

## 📚 Documentation

- [GITHUB_SETUP_GUIDE.md](GITHUB_SETUP_GUIDE.md) - Complete GitHub setup
- [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) - Vercel deployment instructions
- [API Documentation](#api-endpoints) - Available endpoints

## 🔌 API Endpoints

- `GET /api/congress-buys` - Congress Buys Index data
- `GET /api/congress-equity-exposure` - Equity Exposure Index data
- `GET /api/health` - Health check

## ⚠️ Disclaimer

This application is for educational and research purposes. The sample data is fictional and does not represent actual congressional trading activity.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

**Made with ❤️ for transparent congressional trading data**

[![Deploy to Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/YOUR_USERNAME/congress-indexes) 