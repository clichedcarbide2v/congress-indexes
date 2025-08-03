import pandas as pd
import requests
import yfinance as yf
from datetime import datetime, timedelta
import json
from typing import Dict, List, Tuple
import re

class CongressBuysIndex:
    """
    Congress Buys Equity Index following QuiverQuant methodology
    """
    
    def __init__(self):
        self.base_url = "https://api.quiverquant.com/beta"
        self.api_key = None  # Will be set by user
        self.dollar_ranges = {
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
        }
    
    def set_api_key(self, api_key: str):
        """Set the QuiverQuant API key"""
        self.api_key = api_key
    
    def get_congressional_trades(self, days_back: int = 100) -> pd.DataFrame:
        """
        Fetch congressional stock trades from QuiverQuant API
        """
        if not self.api_key:
            print("No API key provided. Using sample data for demonstration.")
            return self._get_sample_data()
        
        # Calculate date range
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days_back)
        
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        # Fetch House trades
        house_url = f"{self.base_url}/congresstrading/house"
        house_params = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }
        
        try:
            house_response = requests.get(house_url, headers=headers, params=house_params)
            house_response.raise_for_status()
            house_data = house_response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching House data: {e}")
            house_data = []
        
        # Fetch Senate trades
        senate_url = f"{self.base_url}/congresstrading/senate"
        senate_params = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }
        
        try:
            senate_response = requests.get(senate_url, headers=headers, params=senate_params)
            senate_response.raise_for_status()
            senate_data = senate_response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching Senate data: {e}")
            senate_data = []
        
        # Combine data
        all_data = house_data + senate_data
        
        if not all_data:
            print("No data received from API. Using sample data for demonstration.")
            return self._get_sample_data()
        
        return pd.DataFrame(all_data)
    
    def _get_sample_data(self) -> pd.DataFrame:
        """Generate sample data for demonstration purposes"""
        sample_data = [
            # NVDA - Multiple large purchases (AI boom, realistic for current market)
            {"transaction_id": "1", "ticker": "NVDA", "company": "NVIDIA Corporation", "transaction_type": "buy", 
             "amount": "$250,001-$500,000", "date": "2024-01-15", "representative": "John Doe"},
            {"transaction_id": "2", "ticker": "NVDA", "company": "NVIDIA Corporation", "transaction_type": "buy", 
             "amount": "$500,001-$1,000,000", "date": "2024-01-20", "representative": "Jane Smith"},
            {"transaction_id": "3", "ticker": "NVDA", "company": "NVIDIA Corporation", "transaction_type": "buy", 
             "amount": "$100,001-$250,000", "date": "2024-01-25", "representative": "Bob Johnson"},
            {"transaction_id": "4", "ticker": "NVDA", "company": "NVIDIA Corporation", "transaction_type": "buy", 
             "amount": "$250,001-$500,000", "date": "2024-02-01", "representative": "Alice Brown"},
            
            # AVGO (Broadcom) - Multiple large purchases (AI/semiconductor boom)
            {"transaction_id": "5", "ticker": "AVGO", "company": "Broadcom Inc.", "transaction_type": "buy", 
             "amount": "$250,001-$500,000", "date": "2024-02-05", "representative": "Charlie Wilson"},
            {"transaction_id": "6", "ticker": "AVGO", "company": "Broadcom Inc.", "transaction_type": "buy", 
             "amount": "$100,001-$250,000", "date": "2024-02-10", "representative": "Diana Davis"},
            {"transaction_id": "7", "ticker": "AVGO", "company": "Broadcom Inc.", "transaction_type": "buy", 
             "amount": "$500,001-$1,000,000", "date": "2024-02-15", "representative": "Edward Miller"},
            {"transaction_id": "8", "ticker": "AVGO", "company": "Broadcom Inc.", "transaction_type": "buy", 
             "amount": "$100,001-$250,000", "date": "2024-02-20", "representative": "Frank Garcia"},
            
            # MSFT - Multiple purchases (AI leader)
            {"transaction_id": "9", "ticker": "MSFT", "company": "Microsoft Corporation", "transaction_type": "buy", 
             "amount": "$100,001-$250,000", "date": "2024-02-25", "representative": "Grace Lee"},
            {"transaction_id": "10", "ticker": "MSFT", "company": "Microsoft Corporation", "transaction_type": "buy", 
             "amount": "$250,001-$500,000", "date": "2024-03-01", "representative": "Henry Taylor"},
            {"transaction_id": "11", "ticker": "MSFT", "company": "Microsoft Corporation", "transaction_type": "buy", 
             "amount": "$50,001-$100,000", "date": "2024-03-05", "representative": "Ivy Chen"},
            
            # AMD - AI/semiconductor play
            {"transaction_id": "12", "ticker": "AMD", "company": "Advanced Micro Devices", "transaction_type": "buy", 
             "amount": "$250,001-$500,000", "date": "2024-03-10", "representative": "Jack Wilson"},
            {"transaction_id": "13", "ticker": "AMD", "company": "Advanced Micro Devices", "transaction_type": "buy", 
             "amount": "$100,001-$250,000", "date": "2024-03-15", "representative": "Kate Davis"},
            
            # AAPL - Multiple smaller purchases
            {"transaction_id": "14", "ticker": "AAPL", "company": "Apple Inc.", "transaction_type": "buy", 
             "amount": "$15,001-$50,000", "date": "2024-03-20", "representative": "Liam Brown"},
            {"transaction_id": "15", "ticker": "AAPL", "company": "Apple Inc.", "transaction_type": "buy", 
             "amount": "$50,001-$100,000", "date": "2024-03-25", "representative": "Mia Johnson"},
            {"transaction_id": "16", "ticker": "AAPL", "company": "Apple Inc.", "transaction_type": "buy", 
             "amount": "$15,001-$50,000", "date": "2024-03-30", "representative": "Noah Smith"},
            
            # AMZN - Medium purchases
            {"transaction_id": "17", "ticker": "AMZN", "company": "Amazon.com Inc.", "transaction_type": "buy", 
             "amount": "$100,001-$250,000", "date": "2024-04-01", "representative": "Olivia Taylor"},
            {"transaction_id": "18", "ticker": "AMZN", "company": "Amazon.com Inc.", "transaction_type": "buy", 
             "amount": "$50,001-$100,000", "date": "2024-04-05", "representative": "Paul Anderson"},
            
            # GOOGL - Medium purchases
            {"transaction_id": "19", "ticker": "GOOGL", "company": "Alphabet Inc.", "transaction_type": "buy", 
             "amount": "$100,001-$250,000", "date": "2024-04-10", "representative": "Quinn Miller"},
            {"transaction_id": "20", "ticker": "GOOGL", "company": "Alphabet Inc.", "transaction_type": "buy", 
             "amount": "$50,001-$100,000", "date": "2024-04-12", "representative": "Rachel Wilson"},
            
            # META - Medium purchases
            {"transaction_id": "21", "ticker": "META", "company": "Meta Platforms Inc.", "transaction_type": "buy", 
             "amount": "$100,001-$250,000", "date": "2024-04-15", "representative": "Sam Chen"},
            {"transaction_id": "22", "ticker": "META", "company": "Meta Platforms Inc.", "transaction_type": "buy", 
             "amount": "$50,001-$100,000", "date": "2024-04-18", "representative": "Tom Wilson"},
            
            # TSLA - Smaller purchases
            {"transaction_id": "23", "ticker": "TSLA", "company": "Tesla Inc.", "transaction_type": "buy", 
             "amount": "$50,001-$100,000", "date": "2024-04-20", "representative": "Sarah Johnson"},
            {"transaction_id": "24", "ticker": "TSLA", "company": "Tesla Inc.", "transaction_type": "buy", 
             "amount": "$15,001-$50,000", "date": "2024-04-25", "representative": "David Brown"},
            
            # JPM - Medium purchases
            {"transaction_id": "25", "ticker": "JPM", "company": "JPMorgan Chase & Co.", "transaction_type": "buy", 
             "amount": "$100,001-$250,000", "date": "2024-04-28", "representative": "Emma Wilson"},
            
            # JNJ - Smaller purchases
            {"transaction_id": "26", "ticker": "JNJ", "company": "Johnson & Johnson", "transaction_type": "buy", 
             "amount": "$50,001-$100,000", "date": "2024-05-01", "representative": "Michael Davis"},
            
            # V - Smaller purchases
            {"transaction_id": "27", "ticker": "V", "company": "Visa Inc.", "transaction_type": "buy", 
             "amount": "$15,001-$50,000", "date": "2024-05-05", "representative": "Lisa Anderson"},
            
            # Exclude this sell transaction
            {"transaction_id": "28", "ticker": "AAPL", "company": "Apple Inc.", "transaction_type": "sell", 
             "amount": "$15,001-$50,000", "date": "2024-05-10", "representative": "Robert Chen"},
        ]
        return pd.DataFrame(sample_data)
    
    def filter_buys_only(self, df: pd.DataFrame) -> pd.DataFrame:
        """Filter to only include buy transactions"""
        return df[df['transaction_type'].str.lower() == 'buy'].copy()
    
    def deduplicate_trades(self, df: pd.DataFrame) -> pd.DataFrame:
        """Remove duplicate trades based on transaction_id"""
        return df.drop_duplicates(subset=['transaction_id']).copy()
    
    def convert_dollar_ranges_to_midpoints(self, df: pd.DataFrame) -> pd.DataFrame:
        """Convert dollar ranges to midpoint values"""
        df = df.copy()
        df['dollar_amount'] = df['amount'].map(self.dollar_ranges)
        
        # Handle any unmapped ranges
        unmapped = df[df['dollar_amount'].isna()]
        if not unmapped.empty:
            print(f"Warning: Found unmapped dollar ranges: {unmapped['amount'].unique()}")
        
        return df
    
    def aggregate_by_ticker(self, df: pd.DataFrame) -> pd.DataFrame:
        """Sum all buys by ticker"""
        return df.groupby(['ticker', 'company'])['dollar_amount'].sum().reset_index()
    
    def select_top_10(self, df: pd.DataFrame) -> pd.DataFrame:
        """Select top 10 tickers by total dollars purchased"""
        return df.nlargest(10, 'dollar_amount').copy()
    
    def calculate_weights(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calculate pro-rata weights based on dollar amounts"""
        df = df.copy()
        total_dollars = df['dollar_amount'].sum()
        
        # Calculate raw weights
        raw_weights = (df['dollar_amount'] / total_dollars * 100)
        
        # Round to 1 decimal place
        rounded_weights = raw_weights.round(1)
        
        # Adjust the largest weight to ensure total equals 100%
        total_rounded = rounded_weights.sum()
        if abs(total_rounded - 100.0) > 0.01:
            # Find the largest weight and adjust it
            max_idx = rounded_weights.idxmax()
            adjustment = 100.0 - total_rounded
            rounded_weights[max_idx] += adjustment
        
        df['weight'] = rounded_weights
        return df
    
    def get_current_prices(self, tickers: List[str]) -> Dict[str, float]:
        """Get current stock prices for validation"""
        prices = {}
        for ticker in tickers:
            try:
                stock = yf.Ticker(ticker)
                current_price = stock.info.get('regularMarketPrice', 0)
                prices[ticker] = current_price
            except Exception as e:
                print(f"Error getting price for {ticker}: {e}")
                prices[ticker] = 0
        return prices
    
    def generate_index(self, days_back: int = 100) -> pd.DataFrame:
        """Generate the complete Congress Buys index"""
        print("Step 1: Fetching congressional trades...")
        df = self.get_congressional_trades(days_back)
        
        print("Step 2: Filtering buy transactions only...")
        df = self.filter_buys_only(df)
        
        print("Step 3: Deduplicating trades...")
        df = self.deduplicate_trades(df)
        
        print("Step 4: Converting dollar ranges to midpoints...")
        df = self.convert_dollar_ranges_to_midpoints(df)
        
        print("Step 5: Aggregating by ticker...")
        df = self.aggregate_by_ticker(df)
        
        print("Step 6: Selecting top 10 tickers...")
        df = self.select_top_10(df)
        
        print("Step 7: Calculating weights...")
        df = self.calculate_weights(df)
        
        # Sort by weight descending
        df = df.sort_values('weight', ascending=False).reset_index(drop=True)
        
        return df
    
    def print_methodology(self):
        """Print the index methodology"""
        methodology = """
        CONGRESS BUYS EQUITY INDEX - METHODOLOGY
        
        1. Data Window: All STOCK-Act purchase disclosures (House + Senate, including spouses/dependents) 
           from the last 100 calendar days, excluding sales and short positions.
        2. Dollar Sizing: Convert reported dollar ranges to midpoints and sum all buys by ticker.
        3. Constituent Selection: Rank tickers by total dollars purchased and select top 10.
        4. Weighting Rule: Weight each stock pro-rata to its share of total dollars purchased.
        5. Output: Table with ticker, company name, and index weight (rounded to 1 decimal place).
        """
        print(methodology)
    
    def print_assumptions(self):
        """Print assumptions and dollar range mappings"""
        print("\nASSUMPTIONS AND DOLLAR RANGE MAPPINGS:")
        print("=" * 50)
        for range_str, midpoint in self.dollar_ranges.items():
            print(f"{range_str:20} → ${midpoint:>10,.0f}")
        print("\nNote: For ranges above $50M, using conservative estimate of $75M midpoint.")
        print("Data gaps: Using sample data if API is unavailable or returns no results.")

def main():
    """Main function to run the Congress Buys index"""
    index = CongressBuysIndex()
    
    # For demonstration, we'll use sample data
    # In production, you would set your API key:
    # index.set_api_key("your_api_key_here")
    
    print("CONGRESS BUYS EQUITY INDEX")
    print("=" * 50)
    
    # Print methodology
    index.print_methodology()
    
    # Generate index
    result_df = index.generate_index()
    
    # Display results
    print("\nCONGRESS BUYS INDEX CONSTITUENTS")
    print("=" * 50)
    print(f"{'Ticker':<8} {'Company':<30} {'Weight (%)':<12} {'Total $':<15}")
    print("-" * 65)
    
    for _, row in result_df.iterrows():
        print(f"{row['ticker']:<8} {row['company'][:28]:<30} {row['weight']:<12.1f} ${row['dollar_amount']:>12,.0f}")
    
    # Verify weights sum to 100%
    total_weight = result_df['weight'].sum()
    print(f"\nTotal Weight: {total_weight:.1f}%")
    
    if abs(total_weight - 100.0) > 0.1:
        print(f"Warning: Weights do not sum to 100% (difference: {total_weight - 100.0:.1f}%)")
    else:
        print("✓ Weights sum to 100%")
    
    # Print assumptions
    index.print_assumptions()
    
    # Save to CSV
    result_df.to_csv('congress_buys_index.csv', index=False)
    print(f"\nIndex saved to 'congress_buys_index.csv'")

if __name__ == "__main__":
    main() 