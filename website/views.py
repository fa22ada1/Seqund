from typing import KeysView
from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify, send_file
from flask_login import login_required, current_user
from . import db
import os, subprocess,json

from .sffextract import sfftofasta

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html', user=current_user)

@views.route('/extract/')
def extract():
    return render_template('extract.html', user=current_user)

@views.route('/extract/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        ID = str(current_user.get_id())
        inputfl = "website/files/uploads/upload" + ID + ".sff"
        outputfl = "website/files/outputs/output" + ID + ".fasta"
        uploaded_file.save(inputfl)
        sfftofasta(inputfl,outputfl)
    return redirect(url_for('views.downloadFile'))

@views.route('download')
def downloadFile():
    ID = str(current_user.get_id())
    path = "files/outputs/output" + ID + ".fasta"
    return send_file(path, as_attachment=True)