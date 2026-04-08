#!/usr/bin/env python3
"""
Ultra-simple Flask app for CI/CD demo
"""

from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <html>
    <head>
        <title>CI/CD Demo</title>
        <style>
            body { font-family: Arial; text-align: center; padding: 50px; background: #f0f0f0; }
            h1 { color: #333; }
            .status { background: green; color: white; padding: 10px; border-radius: 5px; display: inline-block; }
        </style>
    </head>
    <body>
        <h1>🚀 CI/CD is Working!</h1>
        <div class="status">✅ App is LIVE</div>
        <p>Your GitHub Actions workflow deployed this successfully.</p>
    </body>
    </html>
    '''

@app.route('/api/health')
def health():
    return jsonify({'status': 'ok', 'message': 'App is running'})

@app.route('/api/test')
def test():
    return jsonify({'test': 'passed', 'version': '1.0'})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
