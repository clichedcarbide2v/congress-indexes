#!/usr/bin/env python3
"""
Data Freshness Demo for Congress Buys Index
Shows how the index gets the latest data each time it runs
"""

from datetime import datetime, timedelta
from congress_buys_index import CongressBuysIndex

def show_data_window():
    """Show the current data window"""
    print("📅 CONGRESS BUYS INDEX - DATA FRESHNESS")
    print("=" * 60)
    
    # Calculate the data window
    today = datetime.now()
    start_date = today - timedelta(days=100)
    
    print(f"Current Date: {today.strftime('%Y-%m-%d')}")
    print(f"Data Window: {start_date.strftime('%Y-%m-%d')} to {today.strftime('%Y-%m-%d')}")
    print(f"Days Back: 100 calendar days")
    print()
    
    print("📊 How Data Freshness Works:")
    print("-" * 40)
    print("✅ Dynamic Date Range: Always uses last 100 days from today")
    print("✅ Real-time Updates: Each run uses current date as endpoint")
    print("✅ Rolling Window: Old data drops out, new data comes in")
    print("✅ No Caching: Fresh calculation every time")
    print()

def show_sample_data_dates():
    """Show the dates in our sample data"""
    print("📋 SAMPLE DATA DATES (for demonstration):")
    print("-" * 40)
    
    index = CongressBuysIndex()
    df = index._get_sample_data()
    
    # Extract dates and show range
    dates = pd.to_datetime(df['date'])
    min_date = dates.min()
    max_date = dates.max()
    
    print(f"Sample Data Range: {min_date.strftime('%Y-%m-%d')} to {max_date.strftime('%Y-%m-%d')}")
    print(f"Total Days in Sample: {(max_date - min_date).days} days")
    print()
    
    # Show distribution by month
    print("Sample Data Distribution by Month:")
    monthly_counts = df.groupby(df['date'].str[:7]).size()
    for month, count in monthly_counts.items():
        print(f"  {month}: {count} transactions")

def demonstrate_freshness():
    """Demonstrate how freshness works"""
    print("\n🔄 DATA FRESHNESS DEMONSTRATION")
    print("=" * 60)
    
    print("Scenario: Running the index multiple times over time")
    print()
    
    # Simulate running the index on different dates
    dates_to_test = [
        datetime.now() - timedelta(days=30),  # 30 days ago
        datetime.now() - timedelta(days=15),  # 15 days ago  
        datetime.now(),                       # today
        datetime.now() + timedelta(days=15),  # 15 days from now
    ]
    
    for i, test_date in enumerate(dates_to_test, 1):
        start_date = test_date - timedelta(days=100)
        print(f"Run #{i} (Date: {test_date.strftime('%Y-%m-%d')}):")
        print(f"  Data Window: {start_date.strftime('%Y-%m-%d')} to {test_date.strftime('%Y-%m-%d')}")
        print(f"  Would include: Latest 100 days of congressional trades")
        print()

def show_real_data_usage():
    """Show how real data would work"""
    print("\n🌐 REAL DATA USAGE (with QuiverQuant API)")
    print("=" * 60)
    
    print("When you have a QuiverQuant API key:")
    print()
    print("1. **API Call**: System fetches latest congressional trading data")
    print("2. **Date Filter**: Automatically filters to last 100 days")
    print("3. **Real-time**: Gets the most recent disclosures available")
    print("4. **Fresh Index**: Calculates index with latest data")
    print()
    
    print("Example API calls:")
    print("- House trades: https://api.quiverquant.com/beta/congresstrading/house")
    print("- Senate trades: https://api.quiverquant.com/beta/congresstrading/senate")
    print("- Date parameters: start_date and end_date")
    print()

def show_usage_instructions():
    """Show how to get the latest picture"""
    print("\n📈 HOW TO GET THE LATEST PICTURE")
    print("=" * 60)
    
    print("To get the most current Congress Buys Index:")
    print()
    print("1. **Run the index**: python3 congress_buys_index.py")
    print("   → Automatically uses last 100 days from today")
    print()
    print("2. **With real data**: Set up QuiverQuant API key")
    print("   → Fetches actual congressional trading disclosures")
    print()
    print("3. **Schedule updates**: Run daily/weekly for fresh data")
    print("   → Index automatically updates with new disclosures")
    print()
    print("4. **Custom timeframes**: Modify days_back parameter")
    print("   → Change from 100 days to any period you want")
    print()

def show_custom_timeframes():
    """Show how to use custom timeframes"""
    print("\n⚙️  CUSTOM TIMEFRAMES")
    print("=" * 60)
    
    index = CongressBuysIndex()
    
    timeframes = [
        ("Last 30 days", 30),
        ("Last 60 days", 60), 
        ("Last 100 days", 100),
        ("Last 6 months", 180),
        ("Last year", 365)
    ]
    
    print("You can modify the data window:")
    print()
    for name, days in timeframes:
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        print(f"{name:15}: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}")
    
    print()
    print("To use custom timeframe:")
    print("  result = index.generate_index(days_back=60)  # Last 60 days")

def main():
    """Main demonstration function"""
    show_data_window()
    show_sample_data_dates()
    demonstrate_freshness()
    show_real_data_usage()
    show_usage_instructions()
    show_custom_timeframes()
    
    print("\n🎯 SUMMARY")
    print("=" * 60)
    print("✅ The index is ALWAYS calculated with the latest available data")
    print("✅ Each run uses a rolling 100-day window from today")
    print("✅ No caching - fresh calculation every time")
    print("✅ Ready for real-time congressional trading data")
    print("✅ Customizable timeframes available")

if __name__ == "__main__":
    import pandas as pd
    main() 