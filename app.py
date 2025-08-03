#!/usr/bin/env python3
"""
Congress Indexes Web Application
Deployable to Vercel with both Congress Buys and Congress Equity Exposure indexes
"""

from flask import Flask, render_template, jsonify, request
import pandas as pd
import json
from datetime import datetime, timedelta
import os

# Import our index classes
from congress_buys_index import CongressBuysIndex
from congress_equity_exposure_index import CongressEquityExposureIndex

app = Flask(__name__)

@app.route('/')
def index():
    """Main page with both indexes"""
    return render_template('index.html')

@app.route('/api/congress-buys')
def congress_buys_api():
    """API endpoint for Congress Buys Index"""
    try:
        # Get parameters
        days_back = request.args.get('days_back', 100, type=int)
        
        # Generate index
        index = CongressBuysIndex()
        
        # Set API key from environment variable if available
        api_key = os.environ.get('QUIVERQUANT_API_KEY')
        if api_key:
            index.set_api_key(api_key)
        
        result_df = index.generate_index(days_back=days_back)
        
        # Convert to JSON
        result = {
            'index_name': 'Congress Buys Index',
            'methodology': 'Top 10 stocks by total dollars purchased by Congress in last 100 days',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'parameters': {
                'days_back': days_back
            },
            'constituents': result_df.to_dict('records'),
            'summary': {
                'total_weight': float(result_df['weight'].sum()),
                'total_value': float(result_df['dollar_amount'].sum()),
                'constituent_count': len(result_df)
            }
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/congress-equity-exposure')
def congress_equity_exposure_api():
    """API endpoint for Congress Equity Exposure Index"""
    try:
        # Get parameters
        quarter_end = request.args.get('quarter_end', None)
        
        # Generate index
        index = CongressEquityExposureIndex()
        
        # Set API key from environment variable if available
        api_key = os.environ.get('QUIVERQUANT_API_KEY')
        if api_key:
            index.set_api_key(api_key)
        
        result_df = index.generate_index(quarter_end_date=quarter_end)
        
        # Convert to JSON
        result = {
            'index_name': 'Congress Equity Exposure Index',
            'methodology': 'Top 10 stocks by largest total congressional net holding value at quarter end',
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'parameters': {
                'quarter_end': quarter_end or 'Latest'
            },
            'constituents': result_df.to_dict('records'),
            'summary': {
                'total_weight': float(result_df['weight'].sum()),
                'total_value': float(result_df['dollar_value'].sum()),
                'constituent_count': len(result_df)
            }
        }
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health')
def health_check():
    """Health check endpoint for Vercel"""
    api_key_configured = bool(os.environ.get('QUIVERQUANT_API_KEY'))
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'indexes': ['congress-buys', 'congress-equity-exposure'],
        'api_key_configured': api_key_configured,
        'data_source': 'real_data' if api_key_configured else 'sample_data'
    })

@app.route('/congress-buys')
def congress_buys_page():
    """Congress Buys Index page"""
    return render_template('congress_buys.html')

@app.route('/congress-equity-exposure')
def congress_equity_exposure_page():
    """Congress Equity Exposure Index page"""
    return render_template('congress_equity_exposure.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5000))) 