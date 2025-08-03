#!/usr/bin/env python3
"""
Setup script for Congress Buys Index
Helps users install dependencies and configure the system
"""

import subprocess
import sys
import os

def install_dependencies():
    """Install required Python packages"""
    print("Installing required dependencies...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ Dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"✗ Error installing dependencies: {e}")
        return False
    return True

def create_config_template():
    """Create a configuration template"""
    config_content = '''# Configuration file for Congress Buys Index

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
'''
    
    with open("config.py", "w") as f:
        f.write(config_content)
    print("✓ Configuration template created!")

def run_test():
    """Run a quick test to verify installation"""
    print("\nRunning quick test...")
    try:
        result = subprocess.run([sys.executable, "test_index.py"], 
                              capture_output=True, text=True, timeout=30)
        if result.returncode == 0:
            print("✓ Test completed successfully!")
            return True
        else:
            print(f"✗ Test failed: {result.stderr}")
            return False
    except subprocess.TimeoutExpired:
        print("✗ Test timed out")
        return False
    except Exception as e:
        print(f"✗ Test error: {e}")
        return False

def main():
    """Main setup function"""
    print("Congress Buys Index - Setup")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not os.path.exists("congress_buys_index.py"):
        print("✗ Error: Please run this script from the project directory")
        return
    
    # Install dependencies
    if not install_dependencies():
        print("Setup failed. Please check the error messages above.")
        return
    
    # Create config template
    create_config_template()
    
    # Run test
    if run_test():
        print("\n" + "=" * 40)
        print("Setup completed successfully!")
        print("\nNext steps:")
        print("1. Edit config.py to add your QuiverQuant API key")
        print("2. Run 'python3 congress_buys_index.py' to generate the index")
        print("3. Check the generated CSV file for results")
    else:
        print("\nSetup completed with warnings. Please check the test output above.")

if __name__ == "__main__":
    main() 