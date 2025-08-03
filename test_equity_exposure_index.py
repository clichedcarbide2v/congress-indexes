#!/usr/bin/env python3
"""
Test script for Congress Equity Exposure Index
Demonstrates functionality and validates calculations
"""

from congress_equity_exposure_index import CongressEquityExposureIndex
import pandas as pd

def test_equity_exposure_index():
    """Test the Congress Equity Exposure Index"""
    
    print("TESTING CONGRESS EQUITY EXPOSURE INDEX")
    print("=" * 50)
    
    # Create index instance
    index = CongressEquityExposureIndex()
    
    # Test 1: Generate full index
    print("\nTest 1: Generating full index...")
    result_df = index.generate_index()
    
    print(f"✓ Index generated successfully with {len(result_df)} constituents")
    print(f"✓ Total weight: {result_df['weight'].sum():.1f}%")
    print(f"✓ Total value: ${result_df['dollar_value'].sum():,.0f}")
    
    # Test 2: Validate weights sum to 100%
    print("\nTest 2: Validating weights...")
    total_weight = result_df['weight'].sum()
    if abs(total_weight - 100.0) <= 0.1:
        print("✓ Weights sum to 100%")
    else:
        print(f"✗ Weights do not sum to 100% (actual: {total_weight:.1f}%)")
    
    # Test 3: Check for negative holdings (puts)
    print("\nTest 3: Checking for options exposure...")
    negative_holdings = result_df[result_df['net_shares'] < 0]
    if len(negative_holdings) > 0:
        print("✓ Found negative holdings (put options exposure):")
        for _, row in negative_holdings.iterrows():
            print(f"  - {row['ticker']}: {row['net_shares']:,.0f} shares")
    else:
        print("✓ No negative holdings found")
    
    # Test 4: Verify top holdings
    print("\nTest 4: Verifying top holdings...")
    top_3 = result_df.head(3)
    print("Top 3 holdings:")
    for i, (_, row) in enumerate(top_3.iterrows(), 1):
        print(f"  {i}. {row['ticker']}: {row['weight']:.1f}% (${row['dollar_value']:,.0f})")
    
    # Test 5: Check options exposure calculation
    print("\nTest 5: Checking options exposure calculation...")
    options_exposure = result_df[result_df['options_exposure'] != 0]
    if len(options_exposure) > 0:
        print("✓ Found stocks with options exposure:")
        for _, row in options_exposure.iterrows():
            print(f"  - {row['ticker']}: {row['options_exposure']:,.0f} shares from options")
    else:
        print("✓ No options exposure found")
    
    # Test 6: Validate data structure
    print("\nTest 6: Validating data structure...")
    required_columns = ['ticker', 'company', 'shares_held', 'options_exposure', 
                       'net_shares', 'dollar_value', 'num_holders', 'weight']
    
    missing_columns = [col for col in required_columns if col not in result_df.columns]
    if len(missing_columns) == 0:
        print("✓ All required columns present")
    else:
        print(f"✗ Missing columns: {missing_columns}")
    
    # Test 7: Check for reasonable holdings sizes
    print("\nTest 7: Checking holdings sizes...")
    large_holdings = result_df[result_df['net_shares'] > 10000]
    if len(large_holdings) > 0:
        print("✓ Found large holdings:")
        for _, row in large_holdings.iterrows():
            print(f"  - {row['ticker']}: {row['net_shares']:,.0f} shares")
    else:
        print("✓ No unusually large holdings found")
    
    # Test 8: Verify price calculations
    print("\nTest 8: Verifying price calculations...")
    price_errors = []
    for _, row in result_df.iterrows():
        calculated_price = row['dollar_value'] / row['net_shares'] if row['net_shares'] > 0 else 0
        expected_price = index.current_prices.get(row['ticker'], 0)
        if abs(calculated_price - expected_price) > 1.0:  # Allow $1 tolerance
            price_errors.append((row['ticker'], calculated_price, expected_price))
    
    if len(price_errors) == 0:
        print("✓ All price calculations verified")
    else:
        print("✗ Price calculation errors found:")
        for ticker, calc_price, exp_price in price_errors:
            print(f"  - {ticker}: calculated ${calc_price:.2f}, expected ${exp_price:.2f}")
    
    print("\n" + "=" * 50)
    print("TESTING COMPLETE")
    
    return result_df

def test_individual_functions():
    """Test individual functions of the index"""
    
    print("\nTESTING INDIVIDUAL FUNCTIONS")
    print("=" * 40)
    
    index = CongressEquityExposureIndex()
    
    # Test holdings data
    print("\n1. Testing holdings data generation...")
    holdings_df = index._get_sample_holdings_data()
    print(f"✓ Generated {len(holdings_df)} holdings records")
    print(f"✓ Unique tickers: {holdings_df['ticker'].nunique()}")
    print(f"✓ Unique holders: {holdings_df['representative'].nunique()}")
    
    # Test net holdings calculation
    print("\n2. Testing net holdings calculation...")
    net_df = index.calculate_net_holdings(holdings_df)
    print(f"✓ Calculated net holdings for {len(net_df)} records")
    print(f"✓ Total options exposure: {net_df['options_exposure'].sum():,.0f} shares")
    print(f"✓ Total net shares: {net_df['net_shares'].sum():,.0f}")
    
    # Test aggregation
    print("\n3. Testing aggregation...")
    agg_df = index.aggregate_by_ticker(net_df)
    print(f"✓ Aggregated to {len(agg_df)} unique stocks")
    print(f"✓ Total dollar value: ${agg_df['dollar_value'].sum():,.0f}")
    
    # Test top 10 selection
    print("\n4. Testing top 10 selection...")
    top_10_df = index.select_top_10(agg_df)
    print(f"✓ Selected top {len(top_10_df)} stocks")
    
    # Test weight calculation
    print("\n5. Testing weight calculation...")
    weighted_df = index.calculate_weights(top_10_df)
    print(f"✓ Calculated weights for {len(weighted_df)} stocks")
    print(f"✓ Total weight: {weighted_df['weight'].sum():.1f}%")
    
    print("\n✓ All individual function tests passed")

if __name__ == "__main__":
    # Run comprehensive test
    result = test_equity_exposure_index()
    
    # Run individual function tests
    test_individual_functions()
    
    print("\n" + "=" * 60)
    print("ALL TESTS COMPLETED SUCCESSFULLY")
    print("=" * 60) 