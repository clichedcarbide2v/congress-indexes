#!/usr/bin/env python3
"""
Manual verification of Congress Buys Index calculations
Double-checks the math step by step
"""

import pandas as pd
from congress_buys_index import CongressBuysIndex

def manual_calculation_verification():
    """Manually verify the calculations step by step"""
    print("🔢 MANUAL CALCULATION VERIFICATION")
    print("=" * 50)
    
    index = CongressBuysIndex()
    
    # Get the raw data
    df = index._get_sample_data()
    df_buys = index.filter_buys_only(df)
    df_converted = index.convert_dollar_ranges_to_midpoints(df_buys)
    df_agg = index.aggregate_by_ticker(df_converted)
    
    print("Raw data by ticker:")
    print("-" * 40)
    for _, row in df_agg.iterrows():
        print(f"{row['ticker']:6} ${row['dollar_amount']:>10,.0f}")
    
    # Calculate total manually
    total_dollars = df_agg['dollar_amount'].sum()
    print(f"\nTotal dollars: ${total_dollars:,.0f}")
    
    # Calculate weights manually
    print("\nManual weight calculations:")
    print("-" * 40)
    manual_weights = {}
    
    for _, row in df_agg.iterrows():
        ticker = row['ticker']
        dollar_amount = row['dollar_amount']
        weight = (dollar_amount / total_dollars) * 100
        weight_rounded = round(weight, 1)
        manual_weights[ticker] = weight_rounded
        
        print(f"{ticker:6} ${dollar_amount:>10,.0f} → {weight:>6.3f}% → {weight_rounded:>5.1f}%")
    
    # Verify total weight
    total_weight = sum(manual_weights.values())
    print(f"\nTotal manual weight: {total_weight:.1f}%")
    
    # Compare with system calculation
    df_top10 = index.select_top_10(df_agg)
    df_weighted = index.calculate_weights(df_top10)
    
    print("\nSystem vs Manual comparison:")
    print("-" * 40)
    print(f"{'Ticker':<6} {'System':<6} {'Manual':<6} {'Match':<5}")
    print("-" * 40)
    
    all_match = True
    for _, row in df_weighted.iterrows():
        ticker = row['ticker']
        system_weight = row['weight']
        manual_weight = manual_weights.get(ticker, 0)
        match = "✅" if abs(system_weight - manual_weight) < 0.01 else "❌"
        
        print(f"{ticker:<6} {system_weight:<6.1f} {manual_weight:<6.1f} {match:<5}")
        
        if match == "❌":
            all_match = False
    
    print(f"\nAll calculations match: {'✅ YES' if all_match else '❌ NO'}")
    
    return all_match

def verify_nvda_calculation():
    """Specifically verify NVDA calculation"""
    print("\n🎯 NVDA CALCULATION VERIFICATION")
    print("=" * 50)
    
    # NVDA transactions from sample data
    nvda_transactions = [
        {"amount": "$250,001-$500,000", "midpoint": 375000.5},
        {"amount": "$500,001-$1,000,000", "midpoint": 750000.5},
        {"amount": "$100,001-$250,000", "midpoint": 175000.5},
        {"amount": "$250,001-$500,000", "midpoint": 375000.5}
    ]
    
    print("NVDA transactions:")
    for i, trans in enumerate(nvda_transactions, 1):
        print(f"  {i}. {trans['amount']} → ${trans['midpoint']:,.0f}")
    
    nvda_total = sum(trans['midpoint'] for trans in nvda_transactions)
    print(f"\nNVDA total: ${nvda_total:,.0f}")
    
    # Calculate total from all tickers
    index = CongressBuysIndex()
    df = index._get_sample_data()
    df_buys = index.filter_buys_only(df)
    df_converted = index.convert_dollar_ranges_to_midpoints(df_buys)
    df_agg = index.aggregate_by_ticker(df_converted)
    
    total_dollars = df_agg['dollar_amount'].sum()
    nvda_weight = (nvda_total / total_dollars) * 100
    nvda_weight_rounded = round(nvda_weight, 1)
    
    print(f"Total market: ${total_dollars:,.0f}")
    print(f"NVDA weight: {nvda_weight:.3f}% → {nvda_weight_rounded:.1f}%")
    
    # Verify against system
    df_top10 = index.select_top_10(df_agg)
    df_weighted = index.calculate_weights(df_top10)
    system_nvda_weight = df_weighted[df_weighted['ticker'] == 'NVDA']['weight'].iloc[0]
    
    print(f"System NVDA weight: {system_nvda_weight:.1f}%")
    print(f"Match: {'✅' if abs(system_nvda_weight - nvda_weight_rounded) < 0.01 else '❌'}")
    
    return abs(system_nvda_weight - nvda_weight_rounded) < 0.01

def verify_broadcom_calculation():
    """Specifically verify Broadcom calculation"""
    print("\n🎯 BROADCOM CALCULATION VERIFICATION")
    print("=" * 50)
    
    # Broadcom transactions from sample data
    avgo_transactions = [
        {"amount": "$250,001-$500,000", "midpoint": 375000.5},
        {"amount": "$100,001-$250,000", "midpoint": 175000.5},
        {"amount": "$500,001-$1,000,000", "midpoint": 750000.5},
        {"amount": "$100,001-$250,000", "midpoint": 175000.5}
    ]
    
    print("Broadcom (AVGO) transactions:")
    for i, trans in enumerate(avgo_transactions, 1):
        print(f"  {i}. {trans['amount']} → ${trans['midpoint']:,.0f}")
    
    avgo_total = sum(trans['midpoint'] for trans in avgo_transactions)
    print(f"\nBroadcom total: ${avgo_total:,.0f}")
    
    # Calculate total from all tickers
    index = CongressBuysIndex()
    df = index._get_sample_data()
    df_buys = index.filter_buys_only(df)
    df_converted = index.convert_dollar_ranges_to_midpoints(df_buys)
    df_agg = index.aggregate_by_ticker(df_converted)
    
    total_dollars = df_agg['dollar_amount'].sum()
    avgo_weight = (avgo_total / total_dollars) * 100
    avgo_weight_rounded = round(avgo_weight, 1)
    
    print(f"Total market: ${total_dollars:,.0f}")
    print(f"Broadcom weight: {avgo_weight:.3f}% → {avgo_weight_rounded:.1f}%")
    
    # Verify against system
    df_top10 = index.select_top_10(df_agg)
    df_weighted = index.calculate_weights(df_top10)
    system_avgo_weight = df_weighted[df_weighted['ticker'] == 'AVGO']['weight'].iloc[0]
    
    print(f"System Broadcom weight: {system_avgo_weight:.1f}%")
    print(f"Match: {'✅' if abs(system_avgo_weight - avgo_weight_rounded) < 0.01 else '❌'}")
    
    return abs(system_avgo_weight - avgo_weight_rounded) < 0.01

def main():
    """Run all manual verifications"""
    print("🔍 MANUAL VERIFICATION OF CONGRESS BUYS INDEX")
    print("=" * 60)
    
    # Run verifications
    calc_ok = manual_calculation_verification()
    nvda_ok = verify_nvda_calculation()
    broadcom_ok = verify_broadcom_calculation()
    
    print("\n📋 MANUAL VERIFICATION SUMMARY")
    print("=" * 60)
    print(f"General calculations: {'✅ PASSED' if calc_ok else '❌ FAILED'}")
    print(f"NVDA calculation: {'✅ PASSED' if nvda_ok else '❌ FAILED'}")
    print(f"Broadcom calculation: {'✅ PASSED' if broadcom_ok else '❌ FAILED'}")
    
    all_passed = calc_ok and nvda_ok and broadcom_ok
    print(f"\nOverall: {'✅ ALL VERIFICATIONS PASSED' if all_passed else '❌ SOME VERIFICATIONS FAILED'}")
    
    if all_passed:
        print("\n🎉 Manual verification confirms the index is mathematically correct!")
        print("   - All weight calculations are accurate")
        print("   - NVDA and Broadcom positions are verified")
        print("   - Ready for production use")

if __name__ == "__main__":
    main() 