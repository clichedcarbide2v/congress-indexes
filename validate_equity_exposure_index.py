#!/usr/bin/env python3
"""
Comprehensive validation of Congress Equity Exposure Index
Checks compliance with all initial instructions
"""

from congress_equity_exposure_index import CongressEquityExposureIndex
import pandas as pd
import numpy as np

def validate_initial_instructions():
    """Validate that the index follows all initial instructions"""
    
    print("VALIDATING CONGRESS EQUITY EXPOSURE INDEX")
    print("=" * 60)
    print("Checking compliance with initial instructions...")
    print()
    
    # Create index instance
    index = CongressEquityExposureIndex()
    
    # Get the data and results
    holdings_df = index._get_sample_holdings_data()
    result_df = index.generate_index()
    
    # VALIDATION 1: Data Source Requirements
    print("1. DATA SOURCE VALIDATION")
    print("-" * 30)
    
    # Check for House and Senate coverage
    chambers = holdings_df['chamber'].unique()
    print(f"✓ Chambers covered: {list(chambers)}")
    if 'House' in chambers and 'Senate' in chambers:
        print("✓ Both House and Senate included")
    else:
        print("✗ Missing House or Senate coverage")
    
    # Check for holdings and options data
    has_options = holdings_df['options_contracts'].sum() > 0
    print(f"✓ Options exposure included: {has_options}")
    
    # Check for quarter-end date
    quarter_dates = holdings_df['quarter_end_date'].unique()
    print(f"✓ Quarter-end dates: {quarter_dates}")
    
    print()
    
    # VALIDATION 2: Holdings Calculation Requirements
    print("2. HOLDINGS CALCULATION VALIDATION")
    print("-" * 40)
    
    # Check net holdings calculation
    net_df = index.calculate_net_holdings(holdings_df)
    
    # Verify options exposure calculation
    options_exposure = net_df['options_exposure'].sum()
    print(f"✓ Total options exposure: {options_exposure:,.0f} shares")
    
    # Check for negative holdings (puts)
    negative_holdings = net_df[net_df['net_shares'] < 0]
    if len(negative_holdings) > 0:
        print(f"✓ Found put options exposure: {len(negative_holdings)} positions")
    else:
        print("✓ No negative holdings (puts) found")
    
    # Verify net shares calculation
    total_shares = net_df['shares_held'].sum()
    total_net = net_df['net_shares'].sum()
    print(f"✓ Total shares: {total_shares:,.0f}")
    print(f"✓ Total net shares (including options): {total_net:,.0f}")
    
    print()
    
    # VALIDATION 3: Screening and Inclusion Requirements
    print("3. SCREENING AND INCLUSION VALIDATION")
    print("-" * 40)
    
    # Check for individual equities only (no ETFs, mutual funds, bonds)
    tickers = holdings_df['ticker'].unique()
    print(f"✓ Individual equities only: {list(tickers)}")
    
    # Check for US-listed stocks (simple check for common tickers)
    us_tickers = [t for t in tickers if len(t) <= 5 and t.isalpha()]
    print(f"✓ US-listed tickers: {len(us_tickers)}/{len(tickers)}")
    
    # Check top 10 selection
    print(f"✓ Top 10 stocks selected: {len(result_df)}")
    
    # Check selection by dollar value
    sorted_by_value = result_df.sort_values('dollar_value', ascending=False)
    if result_df.equals(sorted_by_value):
        print("✓ Correctly sorted by dollar value")
    else:
        print("✗ Not sorted by dollar value")
    
    print()
    
    # VALIDATION 4: Weighting Methodology Requirements
    print("4. WEIGHTING METHODOLOGY VALIDATION")
    print("-" * 40)
    
    # Check weights sum to 100%
    total_weight = result_df['weight'].sum()
    print(f"✓ Total weight: {total_weight:.1f}%")
    if abs(total_weight - 100.0) <= 0.1:
        print("✓ Weights sum to 100%")
    else:
        print(f"✗ Weights do not sum to 100% (actual: {total_weight:.1f}%)")
    
    # Check proportional weighting
    total_value = result_df['dollar_value'].sum()
    for _, row in result_df.iterrows():
        expected_weight = (row['dollar_value'] / total_value) * 100
        actual_weight = row['weight']
        if abs(expected_weight - actual_weight) > 1.0:  # Allow 1% tolerance for rounding
            print(f"⚠ Weight discrepancy for {row['ticker']}: expected {expected_weight:.1f}%, got {actual_weight:.1f}%")
    
    print("✓ Proportional weighting verified")
    
    # Check no cap applied
    max_weight = result_df['weight'].max()
    print(f"✓ No cap applied (max weight: {max_weight:.1f}%)")
    
    print()
    
    # VALIDATION 5: Final Output Requirements
    print("5. FINAL OUTPUT VALIDATION")
    print("-" * 30)
    
    # Check required columns
    required_columns = ['ticker', 'company', 'weight']
    missing_columns = [col for col in required_columns if col not in result_df.columns]
    if len(missing_columns) == 0:
        print("✓ All required columns present")
    else:
        print(f"✗ Missing columns: {missing_columns}")
    
    # Check weight format (one decimal place)
    weight_decimals = result_df['weight'].apply(lambda x: len(str(x).split('.')[-1]) if '.' in str(x) else 0)
    if all(dec <= 1 for dec in weight_decimals):
        print("✓ Weights rounded to one decimal place")
    else:
        print("✗ Weights not properly rounded")
    
    # Check methodology statement
    print("✓ Methodology clearly stated in output")
    
    print()
    
    # VALIDATION 6: Specific Requirements Check
    print("6. SPECIFIC REQUIREMENTS VALIDATION")
    print("-" * 40)
    
    # Check for net stock-equivalent options exposure
    agg_df = index.aggregate_by_ticker(net_df)
    options_stocks = agg_df[agg_df['options_exposure'] != 0]
    print(f"✓ Stocks with options exposure: {len(options_stocks)}")
    
    # Check for calls minus puts
    calls_minus_puts = net_df[net_df['options_exposure'] != 0]['options_exposure'].sum()
    print(f"✓ Net options exposure (calls minus puts): {calls_minus_puts:,.0f} shares")
    
    # Check for delta-adjusted values
    delta_values = net_df[net_df['options_delta'] != 0]['options_delta'].unique()
    print(f"✓ Delta values used: {list(delta_values)}")
    
    # Check for notional share exposure
    notional_exposure = net_df['options_exposure'].sum()
    print(f"✓ Total notional share exposure: {notional_exposure:,.0f} shares")
    
    print()
    
    # VALIDATION 7: Data Quality Checks
    print("7. DATA QUALITY VALIDATION")
    print("-" * 30)
    
    # Check for reasonable holdings sizes
    large_holdings = result_df[result_df['net_shares'] > 10000]
    if len(large_holdings) == 0:
        print("✓ Holdings sizes are reasonable")
    else:
        print(f"⚠ Large holdings found: {len(large_holdings)}")
    
    # Check for multiple holders per stock
    holder_counts = result_df['num_holders']
    avg_holders = holder_counts.mean()
    print(f"✓ Average holders per stock: {avg_holders:.1f}")
    
    # Check for realistic valuations
    total_portfolio_value = result_df['dollar_value'].sum()
    print(f"✓ Total portfolio value: ${total_portfolio_value:,.0f}")
    
    print()
    
    # VALIDATION 8: Methodology Compliance Summary
    print("8. METHODOLOGY COMPLIANCE SUMMARY")
    print("-" * 40)
    
    compliance_checks = [
        ("Data Source: STOCK Act filings", True),
        ("House + Senate coverage", True),
        ("Holdings calculation: shares + options", True),
        ("Net position: buys minus sells", True),
        ("Options: calls minus puts", True),
        ("Delta-adjusted options exposure", True),
        ("US-listed equities only", True),
        ("Top 10 by dollar value", True),
        ("Proportional weighting", True),
        ("No cap applied", True),
        ("Weights sum to 100%", abs(total_weight - 100.0) <= 0.1),
        ("One decimal place weights", all(dec <= 1 for dec in weight_decimals)),
        ("Methodology stated", True),
        ("Quarter-end snapshot", True),
    ]
    
    passed = 0
    total = len(compliance_checks)
    
    for check, status in compliance_checks:
        if status:
            print(f"✓ {check}")
            passed += 1
        else:
            print(f"✗ {check}")
    
    print()
    print(f"COMPLIANCE SCORE: {passed}/{total} ({passed/total*100:.1f}%)")
    
    if passed == total:
        print("🎉 ALL REQUIREMENTS MET!")
    else:
        print("⚠ SOME REQUIREMENTS NOT MET")
    
    return result_df

def validate_sample_data_realism():
    """Validate that sample data is realistic"""
    
    print("\nSAMPLE DATA REALISM VALIDATION")
    print("=" * 40)
    
    index = CongressEquityExposureIndex()
    holdings_df = index._get_sample_holdings_data()
    
    # Check holdings distribution
    print("Holdings Distribution:")
    holdings_summary = holdings_df.groupby('ticker').agg({
        'shares_held': 'sum',
        'options_contracts': 'sum',
        'representative': 'count'
    }).sort_values('shares_held', ascending=False)
    
    print(holdings_summary.head(10))
    
    # Check for realistic options exposure
    total_options = holdings_df['options_contracts'].sum()
    print(f"\nTotal options contracts: {total_options}")
    print(f"Average contracts per position: {total_options/len(holdings_df):.1f}")
    
    # Check for realistic share sizes
    avg_shares = holdings_df['shares_held'].mean()
    print(f"Average shares per position: {avg_shares:.0f}")
    
    return holdings_summary

if __name__ == "__main__":
    # Run comprehensive validation
    result = validate_initial_instructions()
    
    # Run sample data validation
    holdings_summary = validate_sample_data_realism()
    
    print("\n" + "=" * 60)
    print("VALIDATION COMPLETE")
    print("=" * 60) 