#!/usr/bin/env python3
"""
Get Latest Congress Buys Index
Shows how to get the most current index with different timeframes
"""

from datetime import datetime, timedelta
from congress_buys_index import CongressBuysIndex

def get_latest_index(days_back=100):
    """Get the latest index with specified timeframe"""
    print(f"📊 GETTING LATEST CONGRESS BUYS INDEX")
    print(f"Timeframe: Last {days_back} days")
    print("=" * 60)
    
    # Calculate date range
    today = datetime.now()
    start_date = today - timedelta(days=days_back)
    
    print(f"Data Window: {start_date.strftime('%Y-%m-%d')} to {today.strftime('%Y-%m-%d')}")
    print(f"Current Date: {today.strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Generate index
    index = CongressBuysIndex()
    result_df = index.generate_index(days_back=days_back)
    
    # Display results
    print("LATEST INDEX CONSTITUENTS:")
    print("-" * 60)
    print(f"{'Rank':<4} {'Ticker':<6} {'Company':<25} {'Weight':<8} {'Total $':<12}")
    print("-" * 60)
    
    for i, (_, row) in enumerate(result_df.iterrows(), 1):
        print(f"{i:<4} {row['ticker']:<6} {row['company'][:24]:<25} {row['weight']:<7.1f}% ${row['dollar_amount']:>10,.0f}")
    
    # Summary
    total_weight = result_df['weight'].sum()
    total_dollars = result_df['dollar_amount'].sum()
    
    print("-" * 60)
    print(f"Total Weight: {total_weight:.1f}%")
    print(f"Total Purchased: ${total_dollars:,.0f}")
    print(f"Constituents: {len(result_df)} stocks")
    
    return result_df

def compare_timeframes():
    """Compare different timeframes"""
    print("\n🔄 COMPARING DIFFERENT TIMEFRAMES")
    print("=" * 60)
    
    timeframes = [
        ("Last 30 days", 30),
        ("Last 60 days", 60),
        ("Last 100 days", 100),
        ("Last 6 months", 180)
    ]
    
    results = {}
    
    for name, days in timeframes:
        print(f"\n{name.upper()}:")
        print("-" * 40)
        
        try:
            df = get_latest_index(days)
            results[name] = df
            
            # Show top 3
            print("Top 3 positions:")
            for i, (_, row) in enumerate(df.head(3).iterrows(), 1):
                print(f"  {i}. {row['ticker']}: {row['weight']:.1f}%")
                
        except Exception as e:
            print(f"Error with {name}: {e}")
    
    return results

def show_real_data_setup():
    """Show how to set up for real data"""
    print("\n🌐 SETTING UP FOR REAL DATA")
    print("=" * 60)
    
    print("To get the LATEST congressional trading data:")
    print()
    print("1. **Get QuiverQuant API Key**:")
    print("   - Visit: https://quiverquant.com/")
    print("   - Sign up and subscribe to congressional trading data")
    print("   - Get your API key from dashboard")
    print()
    
    print("2. **Configure API Key**:")
    print("   - Edit config.py or use setup_api.py")
    print("   - Add your API key: QUIVERQUANT_API_KEY = 'your_key_here'")
    print()
    
    print("3. **Run with Real Data**:")
    print("   python3 congress_buys_index.py")
    print("   → Will fetch actual congressional disclosures")
    print()
    
    print("4. **Schedule Regular Updates**:")
    print("   - Run daily: python3 get_latest_index.py")
    print("   - Run weekly: python3 get_latest_index.py --days 7")
    print("   - Run monthly: python3 get_latest_index.py --days 30")
    print()

def show_automation_example():
    """Show automation example"""
    print("\n🤖 AUTOMATION EXAMPLE")
    print("=" * 60)
    
    print("Create a script to automatically get the latest index:")
    print()
    print("```python")
    print("#!/usr/bin/env python3")
    print("import schedule")
    print("import time")
    print("from congress_buys_index import CongressBuysIndex")
    print()
    print("def update_index():")
    print("    print(f'Updating index at {datetime.now()}')")
    print("    index = CongressBuysIndex()")
    print("    result = index.generate_index()")
    print("    result.to_csv(f'congress_buys_index_{datetime.now().strftime(\"%Y%m%d\")}.csv')")
    print("    print('Index updated successfully')")
    print()
    print("# Schedule daily updates")
    print("schedule.every().day.at('09:00').do(update_index)")
    print()
    print("while True:")
    print("    schedule.run_pending()")
    print("    time.sleep(60)")
    print("```")
    print()

def main():
    """Main function"""
    import sys
    
    # Check command line arguments
    if len(sys.argv) > 1:
        try:
            days = int(sys.argv[1])
            get_latest_index(days)
        except ValueError:
            print("Usage: python3 get_latest_index.py [days_back]")
            print("Example: python3 get_latest_index.py 60")
    else:
        # Default: show latest 100-day index
        get_latest_index(100)
        
        # Show additional options
        show_real_data_setup()
        show_automation_example()
        
        print("\n🎯 QUICK COMMANDS:")
        print("=" * 60)
        print("Latest 30 days:  python3 get_latest_index.py 30")
        print("Latest 60 days:  python3 get_latest_index.py 60")
        print("Latest 100 days: python3 get_latest_index.py 100")
        print("Latest 6 months: python3 get_latest_index.py 180")
        print()
        print("✅ The index is ALWAYS fresh - each run gets the latest data!")

if __name__ == "__main__":
    main() 