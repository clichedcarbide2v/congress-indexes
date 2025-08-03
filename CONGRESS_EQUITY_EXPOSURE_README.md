# Congress Equity Exposure Index - Top 10 Held

## Overview

The **Congress Equity Exposure Index** tracks the top 10 individual stocks most heavily held by members of the US Congress (including spouses and dependent children) at the end of the latest quarter. This index represents a snapshot of Congressional net equity exposure, including both direct stock holdings and options exposure.

## Key Features

- **Holdings-Based**: Tracks actual holdings rather than just purchases
- **Options Integration**: Includes net stock-equivalent exposure from options (calls minus puts)
- **Quarter-End Snapshot**: Uses end-of-quarter holdings data
- **Net Position Calculation**: Accounts for both buys and sells during the quarter
- **Real-Time Pricing**: Uses current market prices for valuation
- **Comprehensive Coverage**: Includes House and Senate members

## Methodology

### 1. Data Source
- STOCK Act disclosure filings covering both House and Senate
- Includes transactional and periodic reports
- Aggregates data from multiple sources (QuiverQuant, UnusualWhales, CapitolTrades)

### 2. Holdings Calculation
For each congressperson and immediate family:
- **Total shares bought minus total shares sold** during the quarter
- **Net stock-equivalent options exposure**:
  - Add exercised call options
  - Subtract exercised put options
  - Convert net call/put options held into notional share exposure using delta-adjusted values

### 3. Screening and Inclusion
- US-listed equities only (no ETFs, mutual funds, bonds)
- Both direct stock holdings and net options exposure
- Top 10 stocks by largest total congressional net holding value

### 4. Weighting Methodology
- Proportional to share of total notional Congressional equity exposure
- No cap applied - weights may reflect concentration
- Weights sum to 100%

## Sample Results

```
CONGRESS EQUITY EXPOSURE INDEX - TOP 10 HELD
============================================================
Rank Ticker Company                   Weight   Net Shares   Value          
------------------------------------------------------------
1    NVDA   NVIDIA Corporation        42.3%    20,000      $17,000,000
2    AVGO   Broadcom Inc.             35.1%    11,750      $14,100,000
3    MSFT   Microsoft Corporation     9.7%     9,700       $3,880,000
4    AAPL   Apple Inc.                5.1%     11,400      $2,052,000
5    META   Meta Platforms Inc.       2.9%     2,550       $1,147,500
6    AMZN   Amazon.com Inc.           1.7%     4,450       $667,500
7    AMD    Advanced Micro Devices    1.4%     4,650       $558,000
8    GOOGL  Alphabet Inc.             1.1%     3,100       $434,000
9    JPM    JPMorgan Chase & Co.      0.5%     1,200       $216,000
10   TSLA   Tesla Inc.                0.2%     500         $100,000
```

## Installation

1. Install required packages:
```bash
pip install pandas requests yfinance beautifulsoup4 lxml python-dateutil openpyxl
```

2. Set up API key (optional):
   - Get a QuiverQuant API key
   - Add it to `congress_equity_exposure_config.py`

## Usage

### Basic Usage
```python
from congress_equity_exposure_index import CongressEquityExposureIndex

# Create index instance
index = CongressEquityExposureIndex()

# Set API key (optional)
index.set_api_key("your_api_key_here")

# Generate index
result = index.generate_index()

# Display results
print(result)
```

### Command Line
```bash
python3 congress_equity_exposure_index.py
```

### Custom Quarter End Date
```python
# Generate index for specific quarter end
result = index.generate_index(quarter_end_date="2024-09-30")
```

## Options Exposure Calculation

The index includes sophisticated options exposure calculation:

### Delta-Adjusted Options Exposure
- **Call Options**: Positive exposure (delta * contracts * 100 shares)
- **Put Options**: Negative exposure (delta * contracts * 100 shares)
- **Net Exposure**: Sum of all options positions per stock

### Sample Options Deltas
- Deep ITM Call: 0.95
- ITM Call: 0.75
- ATM Call: 0.50
- OTM Call: 0.25
- Deep OTM Call: 0.05
- (Similar for puts with negative values)

## Data Sources

### Primary Sources
- **QuiverQuant API**: Congressional trading data
- **STOCK Act Filings**: Official disclosure documents
- **Yahoo Finance**: Current stock prices

### Sample Data
When API access is unavailable, the system uses realistic sample data that demonstrates:
- Multiple holders per stock
- Various options positions
- Realistic holdings sizes
- Current market prices

## Output Files

- **CSV**: `congress_equity_exposure_index.csv`
- **Excel**: `congress_equity_exposure_index.xlsx` (if openpyxl installed)

## Key Differences from "Congress Buys" Index

| Feature | Congress Buys Index | Congress Equity Exposure Index |
|---------|-------------------|--------------------------------|
| **Focus** | Recent purchases only | Total holdings at quarter end |
| **Time Window** | Last 100 days | Quarter-end snapshot |
| **Options** | Excluded | Included with delta adjustment |
| **Sells** | Excluded | Netted against buys |
| **Valuation** | Purchase amounts | Current market prices |
| **Methodology** | Flow-based | Stock-based |

## Validation Features

- **Weight Verification**: Ensures weights sum to 100%
- **Data Quality Checks**: Validates holdings calculations
- **Options Exposure Validation**: Confirms delta calculations
- **Price Verification**: Uses reliable price sources

## Assumptions and Limitations

### Assumptions
- Options deltas are approximated based on moneyness
- Current prices used for valuation (not historical)
- Standard 100-share options contracts
- All holdings are US-listed equities

### Limitations
- Sample data used when API unavailable
- Options delta approximations may not be exact
- Limited to disclosed holdings (some may be confidential)
- Quarterly reporting lag

## API Requirements

### QuiverQuant API
- Endpoint: `https://api.quiverquant.com/beta`
- Required for real data access
- Rate limits may apply

### Alternative Data Sources
- UnusualWhales
- CapitolTrades
- Direct STOCK Act filings

## Future Enhancements

- Real-time data updates
- Historical index tracking
- Sector breakdown analysis
- Performance attribution
- Risk metrics calculation

## Support

For questions or issues:
1. Check the sample data output
2. Verify API key configuration
3. Review error messages in console output
4. Ensure all dependencies are installed

---

**Note**: This index is for educational and research purposes. Always verify data accuracy and consult multiple sources for investment decisions. 