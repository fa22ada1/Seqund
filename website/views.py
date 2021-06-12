from typing import KeysView
from flask import Blueprint, render_template, request, redirect, url_for
import os

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Test</h1>"

@views.route('/upload/')
def home():
    return render_template('home.html')

@views.route('/upload/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(os.path.join('static/data', 'data'))
    return redirect(url_for('views.home'))

