from typing import KeysView
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from . import db
import os
import json

views = Blueprint('views', __name__)

@login_required
@views.route('/upload/')
def home():
    return render_template('home.html')

@login_required
@views.route('/upload/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(os.path.join('static/data', 'data'))
    return redirect(url_for('views.home'))

