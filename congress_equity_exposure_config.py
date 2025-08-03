# Configuration file for Congress Equity Exposure Index

# QuiverQuant API Configuration
QUIVERQUANT_API_KEY = ""  # Add your API key here

# Index Configuration
DEFAULT_QUARTER_END = None  # Will auto-calculate latest quarter end
TOP_N_CONSTITUENTS = 10  # Number of top stocks to include in index

# Sample Stock Prices (for demonstration when API is unavailable)
SAMPLE_PRICES = {
    "NVDA": 850.00,   # NVIDIA Corporation
    "AVGO": 1200.00,  # Broadcom Inc.
    "MSFT": 400.00,   # Microsoft Corporation
    "AAPL": 180.00,   # Apple Inc.
    "AMZN": 150.00,   # Amazon.com Inc.
    "GOOGL": 140.00,  # Alphabet Inc.
    "META": 450.00,   # Meta Platforms Inc.
    "TSLA": 200.00,   # Tesla Inc.
    "AMD": 120.00,    # Advanced Micro Devices
    "JPM": 180.00,    # JPMorgan Chase & Co.
}

# Options Delta Mappings (for calculating options exposure)
OPTIONS_DELTAS = {
    "deep_itm_call": 0.95,    # Deep in-the-money call
    "itm_call": 0.75,         # In-the-money call
    "atm_call": 0.50,         # At-the-money call
    "otm_call": 0.25,         # Out-of-the-money call
    "deep_otm_call": 0.05,    # Deep out-of-the-money call
    "deep_itm_put": -0.95,    # Deep in-the-money put
    "itm_put": -0.75,         # In-the-money put
    "atm_put": -0.50,         # At-the-money put
    "otm_put": -0.25,         # Out-of-the-money put
    "deep_otm_put": -0.05,    # Deep out-of-the-money put
}

# Output Configuration
OUTPUT_CSV_FILE = "congress_equity_exposure_index.csv"
OUTPUT_EXCEL_FILE = "congress_equity_exposure_index.xlsx"

# API Endpoints
QUIVERQUANT_BASE_URL = "https://api.quiverquant.com/beta"
HOUSE_HOLDINGS_ENDPOINT = "/congresstrading/house"
SENATE_HOLDINGS_ENDPOINT = "/congresstrading/senate"

# Data Processing Settings
OPTIONS_CONTRACT_SIZE = 100  # Standard options contract size
DEFAULT_STOCK_PRICE = 100.0  # Default price for unknown stocks 