from typing import KeysView
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, current_user
from . import db
import os, subprocess,json

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/extract/')
def extract():
    return render_template('extract.html')

@views.route('/extract/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(''.join(["website/static/uploads/upload", current_user.get_id(), '.sff']))
        comande = ["python2 sffextract/sff_extract.py -o outputs/output", current_user.get_id(), " uploads/upload", current_user.get_id(), ".sff"]
        s = subprocess.check_call(''.join(comande), shell = False)
    return redirect(url_for('views.upload_file'))
