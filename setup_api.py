#!/usr/bin/env python3
"""
Setup script for QuiverQuant API to get real congressional trading data
"""

import os
from congress_buys_index import CongressBuysIndex

def setup_api_key():
    """Guide user through API key setup"""
    print("🔑 QUIVERQUANT API SETUP")
    print("=" * 50)
    print()
    print("To get REAL congressional trading data (including Broadcom, etc.),")
    print("you need a QuiverQuant API key.")
    print()
    print("Steps to get your API key:")
    print("1. Visit: https://quiverquant.com/")
    print("2. Sign up for an account")
    print("3. Subscribe to their congressional trading data")
    print("4. Get your API key from your dashboard")
    print()
    
    api_key = input("Enter your QuiverQuant API key (or press Enter to skip): ").strip()
    
    if api_key:
        # Save to config file
        config_content = f'''# Configuration file for Congress Buys Index

# QuiverQuant API Configuration
QUIVERQUANT_API_KEY = "{api_key}"  # Your API key

# Index Configuration
DEFAULT_DAYS_BACK = 100  # Number of days to look back for trades
TOP_N_CONSTITUENTS = 10  # Number of top stocks to include in index

# Dollar Range Mappings (midpoints)
DOLLAR_RANGES = {{
    "$1,001-$15,000": 8000.5,
    "$15,001-$50,000": 32500.5,
    "$50,001-$100,000": 75000.5,
    "$100,001-$250,000": 175000.5,
    "$250,001-$500,000": 375000.5,
    "$500,001-$1,000,000": 750000.5,
    "$1,000,001-$5,000,000": 3000000.5,
    "$5,000,001-$25,000,000": 15000000.5,
    "$25,000,001-$50,000,000": 37500000.5,
    "$50,000,001+": 75000000.5  # Conservative estimate for upper bound
}}

# Output Configuration
OUTPUT_CSV_FILE = "congress_buys_index.csv"
OUTPUT_EXCEL_FILE = "congress_buys_index.xlsx"
'''
        
        with open("config.py", "w") as f:
            f.write(config_content)
        
        print("✅ API key saved to config.py")
        print()
        print("Now you can run the index with real data:")
        print("python3 congress_buys_index.py")
        
        return api_key
    else:
        print("⏭️  Skipping API setup. Will use sample data.")
        return None

def test_with_api_key(api_key):
    """Test the API with the provided key"""
    print("\n🧪 TESTING API CONNECTION")
    print("=" * 50)
    
    index = CongressBuysIndex()
    index.set_api_key(api_key)
    
    try:
        print("Fetching real congressional trading data...")
        df = index.get_congressional_trades(days_back=30)  # Test with 30 days
        
        if len(df) > 0:
            print(f"✅ Success! Found {len(df)} transactions")
            print("\nSample of real data:")
            print(df.head())
            
            # Show unique tickers
            tickers = df['ticker'].unique()
            print(f"\n📊 Found {len(tickers)} unique stocks:")
            print(", ".join(sorted(tickers)))
            
            # Check if Broadcom is in the data
            if 'AVGO' in tickers:
                print("\n🎯 Found Broadcom (AVGO) in the data!")
            else:
                print("\nℹ️  Broadcom (AVGO) not found in this sample")
                
        else:
            print("⚠️  No data returned from API")
            
    except Exception as e:
        print(f"❌ Error testing API: {e}")
        print("This might be due to:")
        print("- Invalid API key")
        print("- No data for the specified time period")
        print("- API rate limits")

def main():
    """Main setup function"""
    api_key = setup_api_key()
    
    if api_key:
        test_with_api_key(api_key)
    else:
        print("\n📋 CURRENT STATUS: Using Sample Data")
        print("=" * 50)
        print("The index is currently using artificial sample data.")
        print("To see real congressional purchases (including Broadcom),")
        print("you need to set up the QuiverQuant API key.")
        print()
        print("Run this script again when you have an API key.")

if __name__ == "__main__":
    main() 