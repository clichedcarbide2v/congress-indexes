#!/usr/bin/env python3
"""
Test script for Congress Buys Index
Demonstrates the functionality with sample data
"""

from congress_buys_index import CongressBuysIndex
import pandas as pd

def test_index_generation():
    """Test the index generation process"""
    print("Testing Congress Buys Index Generation...")
    print("=" * 60)
    
    # Initialize index
    index = CongressBuysIndex()
    
    # Generate index (will use sample data since no API key)
    result_df = index.generate_index(days_back=100)
    
    # Display results
    print("\nCONGRESS BUYS INDEX RESULTS")
    print("=" * 60)
    print(f"{'Ticker':<8} {'Company':<30} {'Weight (%)':<12} {'Total $':<15}")
    print("-" * 65)
    
    for _, row in result_df.iterrows():
        print(f"{row['ticker']:<8} {row['company'][:28]:<30} {row['weight']:<12.1f} ${row['dollar_amount']:>12,.0f}")
    
    # Verify weights
    total_weight = result_df['weight'].sum()
    print(f"\nTotal Weight: {total_weight:.1f}%")
    
    if abs(total_weight - 100.0) <= 0.1:
        print("✓ Weights sum to 100%")
    else:
        print(f"⚠ Warning: Weights do not sum to 100% (difference: {total_weight - 100.0:.1f}%)")
    
    # Save results
    result_df.to_csv('test_congress_buys_index.csv', index=False)
    print(f"\nResults saved to 'test_congress_buys_index.csv'")
    
    return result_df

def test_individual_steps():
    """Test individual processing steps"""
    print("\nTesting Individual Processing Steps...")
    print("=" * 60)
    
    index = CongressBuysIndex()
    
    # Step 1: Get sample data
    print("Step 1: Loading sample data...")
    df = index._get_sample_data()
    print(f"   Loaded {len(df)} transactions")
    
    # Step 2: Filter buys only
    print("Step 2: Filtering buy transactions...")
    df_buys = index.filter_buys_only(df)
    print(f"   Found {len(df_buys)} buy transactions")
    
    # Step 3: Deduplicate
    print("Step 3: Deduplicating trades...")
    df_dedup = index.deduplicate_trades(df_buys)
    print(f"   After deduplication: {len(df_dedup)} transactions")
    
    # Step 4: Convert dollar ranges
    print("Step 4: Converting dollar ranges to midpoints...")
    df_converted = index.convert_dollar_ranges_to_midpoints(df_dedup)
    print("   Dollar range conversions:")
    for _, row in df_converted.iterrows():
        print(f"     {row['amount']} → ${row['dollar_amount']:,.0f}")
    
    # Step 5: Aggregate by ticker
    print("Step 5: Aggregating by ticker...")
    df_agg = index.aggregate_by_ticker(df_converted)
    print("   Aggregated amounts by ticker:")
    for _, row in df_agg.iterrows():
        print(f"     {row['ticker']}: ${row['dollar_amount']:,.0f}")
    
    # Step 6: Select top 10
    print("Step 6: Selecting top 10 tickers...")
    df_top10 = index.select_top_10(df_agg)
    print(f"   Selected top {len(df_top10)} tickers")
    
    # Step 7: Calculate weights
    print("Step 7: Calculating weights...")
    df_weighted = index.calculate_weights(df_top10)
    print("   Final weights:")
    for _, row in df_weighted.iterrows():
        print(f"     {row['ticker']}: {row['weight']:.1f}%")

if __name__ == "__main__":
    # Run full index generation test
    result = test_index_generation()
    
    # Run individual steps test
    test_individual_steps()
    
    print("\n" + "=" * 60)
    print("Test completed successfully!")
    print("Check the generated CSV files for detailed results.") 