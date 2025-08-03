#!/usr/bin/env python3
"""
CapitolTrades API Integration
Free alternative to QuiverQuant for congressional trading data
"""

import requests
import pandas as pd
from datetime import datetime, timedelta
from typing import Dict, List, Optional
import time

class CapitolTradesAPI:
    """
    Free API integration for congressional trading data
    Website: https://capitoltrades.com/
    """
    
    def __init__(self):
        self.base_url = "https://api.capitoltrades.com"
        self.api_key = None
        self.session = requests.Session()
        
    def set_api_key(self, api_key: str):
        """Set the CapitolTrades API key"""
        self.api_key = api_key
        if api_key:
            self.session.headers.update({
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            })
    
    def get_recent_trades(self, days_back: int = 100) -> pd.DataFrame:
        """
        Get recent congressional trades from CapitolTrades
        """
        if not self.api_key:
            print("No CapitolTrades API key provided. Using sample data.")
            return self._get_sample_data()
        
        # Calculate date range
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days_back)
        
        try:
            # Fetch recent trades
            url = f"{self.base_url}/trades"
            params = {
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "limit": 1000  # Adjust based on API limits
            }
            
            response = self.session.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            if not data or 'data' not in data:
                print("No data received from CapitolTrades API. Using sample data.")
                return self._get_sample_data()
            
            # Convert to DataFrame
            df = pd.DataFrame(data['data'])
            
            # Standardize column names
            df = self._standardize_columns(df)
            
            return df
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching CapitolTrades data: {e}")
            print("Falling back to sample data.")
            return self._get_sample_data()
    
    def get_holdings(self, quarter_end_date: str = None) -> pd.DataFrame:
        """
        Get current congressional holdings from CapitolTrades
        """
        if not self.api_key:
            print("No CapitolTrades API key provided. Using sample holdings data.")
            return self._get_sample_holdings_data()
        
        if not quarter_end_date:
            quarter_end_date = self._get_latest_quarter_end()
        
        try:
            # Fetch holdings data
            url = f"{self.base_url}/holdings"
            params = {
                "as_of_date": quarter_end_date,
                "limit": 1000
            }
            
            response = self.session.get(url, params=params)
            response.raise_for_status()
            
            data = response.json()
            
            if not data or 'data' not in data:
                print("No holdings data received from CapitolTrades API. Using sample data.")
                return self._get_sample_holdings_data()
            
            # Convert to DataFrame
            df = pd.DataFrame(data['data'])
            
            # Standardize column names
            df = self._standardize_holdings_columns(df)
            
            return df
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching CapitolTrades holdings: {e}")
            print("Falling back to sample holdings data.")
            return self._get_sample_holdings_data()
    
    def _standardize_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Standardize column names to match our expected format"""
        column_mapping = {
            'ticker': 'ticker',
            'company_name': 'company',
            'representative': 'representative',
            'transaction_date': 'transaction_date',
            'transaction_type': 'transaction_type',
            'amount': 'dollar_amount',
            'chamber': 'chamber',
            'transaction_id': 'transaction_id'
        }
        
        # Rename columns that exist
        existing_columns = {k: v for k, v in column_mapping.items() if k in df.columns}
        df = df.rename(columns=existing_columns)
        
        # Add missing columns with defaults
        if 'dollar_amount' not in df.columns:
            df['dollar_amount'] = df.get('amount', 0)
        
        if 'transaction_type' not in df.columns:
            df['transaction_type'] = 'buy'  # Default assumption
        
        return df
    
    def _standardize_holdings_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Standardize holdings column names"""
        column_mapping = {
            'ticker': 'ticker',
            'company_name': 'company',
            'representative': 'representative',
            'shares': 'shares_held',
            'options_contracts': 'options_contracts',
            'options_type': 'options_type',
            'options_delta': 'options_delta',
            'quarter_end': 'quarter_end_date',
            'chamber': 'chamber'
        }
        
        # Rename columns that exist
        existing_columns = {k: v for k, v in column_mapping.items() if k in df.columns}
        df = df.rename(columns=existing_columns)
        
        # Add missing columns with defaults
        if 'options_contracts' not in df.columns:
            df['options_contracts'] = 0
        
        if 'options_type' not in df.columns:
            df['options_type'] = None
        
        if 'options_delta' not in df.columns:
            df['options_delta'] = 0
        
        return df
    
    def _get_latest_quarter_end(self) -> str:
        """Get the latest quarter end date"""
        now = datetime.now()
        current_quarter = (now.month - 1) // 3
        quarter_end_month = (current_quarter + 1) * 3
        
        if quarter_end_month > now.month:
            # Previous quarter
            if current_quarter == 0:
                year = now.year - 1
                month = 12
            else:
                year = now.year
                month = current_quarter * 3
        else:
            year = now.year
            month = quarter_end_month
        
        # Get last day of month
        if month == 12:
            next_month = datetime(year + 1, 1, 1)
        else:
            next_month = datetime(year, month + 1, 1)
        
        last_day = next_month - timedelta(days=1)
        return last_day.strftime("%Y-%m-%d")
    
    def _get_sample_data(self) -> pd.DataFrame:
        """Generate sample trading data for demonstration"""
        # Import sample data from existing index
        from congress_buys_index import CongressBuysIndex
        index = CongressBuysIndex()
        return index._get_sample_data()
    
    def _get_sample_holdings_data(self) -> pd.DataFrame:
        """Generate sample holdings data for demonstration"""
        # Import sample data from existing index
        from congress_equity_exposure_index import CongressEquityExposureIndex
        index = CongressEquityExposureIndex()
        return index._get_sample_holdings_data()
    
    def test_connection(self) -> bool:
        """Test if the API connection works"""
        if not self.api_key:
            return False
        
        try:
            # Simple test call
            url = f"{self.base_url}/trades"
            params = {"limit": 1}
            
            response = self.session.get(url, params=params)
            response.raise_for_status()
            
            return True
            
        except requests.exceptions.RequestException:
            return False

def main():
    """Test the CapitolTrades integration"""
    print("🧪 Testing CapitolTrades API Integration")
    print("=" * 50)
    
    # Initialize API
    api = CapitolTradesAPI()
    
    # Test without API key (should use sample data)
    print("\n1. Testing without API key:")
    trades_df = api.get_recent_trades(days_back=30)
    print(f"   Retrieved {len(trades_df)} trades (sample data)")
    
    # Test holdings without API key
    holdings_df = api.get_holdings()
    print(f"   Retrieved {len(holdings_df)} holdings (sample data)")
    
    # Test connection (should be False without key)
    print(f"   API connection test: {api.test_connection()}")
    
    print("\n2. To use real data:")
    print("   - Sign up at https://capitoltrades.com/")
    print("   - Get your free API key")
    print("   - Set it with: api.set_api_key('your_key_here')")
    
    print("\n3. Integration with existing indexes:")
    print("   - Replace QuiverQuant calls with CapitolTrades")
    print("   - Same data format, different source")
    print("   - Free tier available")

if __name__ == "__main__":
    main() 