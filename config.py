# Configuration file for Congress Buys Index

# QuiverQuant API Configuration
QUIVERQUANT_API_KEY = ""  # Add your API key here

# Index Configuration
DEFAULT_DAYS_BACK = 100  # Number of days to look back for trades
TOP_N_CONSTITUENTS = 10  # Number of top stocks to include in index

# Dollar Range Mappings (midpoints)
DOLLAR_RANGES = {
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

# Output Configuration
OUTPUT_CSV_FILE = "congress_buys_index.csv"
OUTPUT_EXCEL_FILE = "congress_buys_index.xlsx" 