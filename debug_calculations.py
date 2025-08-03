#!/usr/bin/env python3
"""
Debug script to trace calculation discrepancies in Congress Buys Index
"""

import pandas as pd
from congress_buys_index import CongressBuysIndex

def debug_step_by_step():
    """Debug the calculation process step by step"""
    print("🔍 DEBUGGING CALCULATION PROCESS")
    print("=" * 60)
    
    index = CongressBuysIndex()
    
    # Step 1: Get raw data
    print("STEP 1: Raw sample data")
    print("-" * 40)
    df = index._get_sample_data()
    print(f"Total transactions: {len(df)}")
    print(f"Buy transactions: {len(df[df['transaction_type'].str.lower() == 'buy'])}")
    print(f"Sell transactions: {len(df[df['transaction_type'].str.lower() == 'sell'])}")
    
    # Step 2: Filter buys
    print("\nSTEP 2: After filtering buys only")
    print("-" * 40)
    df_buys = index.filter_buys_only(df)
    print(f"Buy transactions: {len(df_buys)}")
    
    # Step 3: Deduplicate
    print("\nSTEP 3: After deduplication")
    print("-" * 40)
    df_dedup = index.deduplicate_trades(df_buys)
    print(f"Transactions after dedup: {len(df_dedup)}")
    
    # Step 4: Convert dollar ranges
    print("\nSTEP 4: Dollar range conversion")
    print("-" * 40)
    df_converted = index.convert_dollar_ranges_to_midpoints(df_dedup)
    
    # Show each transaction with its conversion
    print("Transaction conversions:")
    for _, row in df_converted.iterrows():
        print(f"  {row['ticker']:6} {row['amount']:20} → ${row['dollar_amount']:>10,.0f}")
    
    # Step 5: Aggregate by ticker
    print("\nSTEP 5: Aggregation by ticker")
    print("-" * 40)
    df_agg = index.aggregate_by_ticker(df_converted)
    
    print("Aggregated amounts:")
    total_system = 0
    for _, row in df_agg.iterrows():
        print(f"  {row['ticker']:6} ${row['dollar_amount']:>10,.0f}")
        total_system += row['dollar_amount']
    
    print(f"\nSystem total: ${total_system:,.0f}")
    
    # Step 6: Select top 10
    print("\nSTEP 6: Top 10 selection")
    print("-" * 40)
    df_top10 = index.select_top_10(df_agg)
    
    print("Top 10 amounts:")
    total_top10 = 0
    for _, row in df_top10.iterrows():
        print(f"  {row['ticker']:6} ${row['dollar_amount']:>10,.0f}")
        total_top10 += row['dollar_amount']
    
    print(f"\nTop 10 total: ${total_top10:,.0f}")
    
    # Step 7: Calculate weights
    print("\nSTEP 7: Weight calculation")
    print("-" * 40)
    df_weighted = index.calculate_weights(df_top10)
    
    print("Final weights:")
    total_weight = 0
    for _, row in df_weighted.iterrows():
        print(f"  {row['ticker']:6} ${row['dollar_amount']:>10,.0f} → {row['weight']:>5.1f}%")
        total_weight += row['weight']
    
    print(f"\nTotal weight: {total_weight:.1f}%")
    
    return df_weighted, total_top10

def manual_calculation_check():
    """Manual calculation to verify"""
    print("\n🔢 MANUAL CALCULATION CHECK")
    print("=" * 60)
    
    # Manual calculation based on sample data
    manual_data = {
        'NVDA': [375000.5, 750000.5, 175000.5, 375000.5],  # 4 transactions
        'AVGO': [375000.5, 175000.5, 750000.5, 175000.5],  # 4 transactions
        'MSFT': [175000.5, 375000.5, 75000.5],             # 3 transactions
        'AMD': [375000.5, 175000.5],                        # 2 transactions
        'AMZN': [175000.5, 75000.5],                        # 2 transactions
        'GOOGL': [175000.5, 75000.5],                       # 2 transactions
        'META': [175000.5, 75000.5],                        # 2 transactions
        'JPM': [175000.5],                                  # 1 transaction
        'AAPL': [32500.5, 75000.5, 32500.5],               # 3 transactions
        'TSLA': [75000.5, 32500.5],                         # 2 transactions
        'JNJ': [75000.5],                                   # 1 transaction
        'V': [32500.5]                                      # 1 transaction
    }
    
    print("Manual calculation by ticker:")
    manual_totals = {}
    grand_total = 0
    
    for ticker, amounts in manual_data.items():
        total = sum(amounts)
        manual_totals[ticker] = total
        grand_total += total
        print(f"  {ticker:6} ${total:>10,.0f} ({len(amounts)} transactions)")
    
    print(f"\nManual grand total: ${grand_total:,.0f}")
    
    # Calculate manual weights
    print("\nManual weight calculations:")
    manual_weights = {}
    for ticker, total in manual_totals.items():
        weight = (total / grand_total) * 100
        weight_rounded = round(weight, 1)
        manual_weights[ticker] = weight_rounded
        print(f"  {ticker:6} ${total:>10,.0f} → {weight:>6.3f}% → {weight_rounded:>5.1f}%")
    
    total_manual_weight = sum(manual_weights.values())
    print(f"\nTotal manual weight: {total_manual_weight:.1f}%")
    
    return manual_totals, manual_weights, grand_total

def compare_system_vs_manual():
    """Compare system vs manual calculations"""
    print("\n🔄 SYSTEM VS MANUAL COMPARISON")
    print("=" * 60)
    
    # Get system results
    df_weighted, system_total = debug_step_by_step()
    
    # Get manual results
    manual_totals, manual_weights, manual_total = manual_calculation_check()
    
    print("\nComparison:")
    print("-" * 60)
    print(f"{'Ticker':<6} {'System $':<12} {'Manual $':<12} {'Diff $':<10} {'System %':<8} {'Manual %':<8}")
    print("-" * 60)
    
    for _, row in df_weighted.iterrows():
        ticker = row['ticker']
        system_dollars = row['dollar_amount']
        system_weight = row['weight']
        manual_dollars = manual_totals.get(ticker, 0)
        manual_weight = manual_weights.get(ticker, 0)
        diff_dollars = system_dollars - manual_dollars
        
        print(f"{ticker:<6} ${system_dollars:<11,.0f} ${manual_dollars:<11,.0f} ${diff_dollars:<9,.0f} {system_weight:<7.1f}% {manual_weight:<7.1f}%")
    
    print("-" * 60)
    print(f"{'TOTAL':<6} ${system_total:<11,.0f} ${manual_total:<11,.0f} ${system_total - manual_total:<9,.0f}")
    
    # Identify the discrepancy
    if abs(system_total - manual_total) > 1:
        print(f"\n❌ DISCREPANCY FOUND: ${system_total - manual_total:,.0f}")
        print("This suggests there's an issue in the data processing pipeline.")
    else:
        print(f"\n✅ NO DISCREPANCY: Totals match within $1")

if __name__ == "__main__":
    compare_system_vs_manual() 