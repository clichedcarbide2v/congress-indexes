# 🚀 Vercel Real Data Setup Guide

## 📊 Current Status: Sample Data

Your Vercel deployment is currently running with **sample data** (realistic but fictional congressional trading data). This is why the "Refresh Data" button works but doesn't pull new real data.

## 🔑 To Enable Real Data

### Step 1: Get QuiverQuant API Key
1. Sign up at [QuiverQuant](https://www.quiverquant.com/)
2. Get your API key from your dashboard
3. Note: This is a paid service

### Step 2: Configure Environment Variable in Vercel

1. **Go to your Vercel dashboard**
2. **Select your project** (congress-indexes)
3. **Go to Settings → Environment Variables**
4. **Add new variable:**
   - **Name**: `QUIVERQUANT_API_KEY`
   - **Value**: Your actual API key
   - **Environment**: Production (and Preview if desired)
5. **Save the variable**

### Step 3: Redeploy

1. **Go to Deployments tab**
2. **Click "Redeploy"** on your latest deployment
3. **Wait for deployment to complete**

## ✅ Verification

After setup, check the health endpoint:
```
https://your-app.vercel.app/api/health
```

You should see:
```json
{
  "status": "healthy",
  "api_key_configured": true,
  "data_source": "real_data"
}
```

## 🔄 How Refresh Works

### With Real Data (API Key Configured):
- ✅ **Real congressional trading data** from QuiverQuant
- ✅ **Live market prices** from Yahoo Finance
- ✅ **Dynamic date ranges** (last 100 days, latest quarter)
- ✅ **Fresh data on every refresh**

### With Sample Data (No API Key):
- ✅ **Realistic sample data** (always works)
- ✅ **Sample market prices** (consistent)
- ✅ **Dynamic date ranges** (last 100 days, latest quarter)
- ✅ **UI updates** (charts, tables refresh)

## 💰 Cost Considerations

- **QuiverQuant API**: Paid service (check their pricing)
- **Vercel**: Free tier should be sufficient for this app
- **Yahoo Finance**: Free (with rate limits)

## 🛠️ Troubleshooting

### If Real Data Doesn't Work:
1. **Check API key** is correctly set in Vercel
2. **Verify QuiverQuant subscription** is active
3. **Check Vercel logs** for API errors
4. **Test API key** locally first

### Fallback Behavior:
- If API fails, the app automatically falls back to sample data
- No downtime or errors for users
- Health endpoint shows current data source

## 📈 Benefits of Real Data

1. **Actual congressional trading patterns**
2. **Real-time market prices**
3. **Historical accuracy**
4. **Professional-grade data**

## 🎯 Recommendation

For **demonstration/prototype**: Sample data is perfect
For **production use**: Configure real API key for actual data 