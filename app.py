#!/usr/bin/env python3
"""
Document Parser Web Application
"""
from flask import Flask, render_template

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/legal')
def legal():
    return render_template('legal.html')

@app.route('/medical')
def medical():
    return render_template('medical.html')

@app.route('/pulse')
def pulse():
    return render_template('pulse.html')

if __name__ == '__main__':
    app.run(debug=True)
