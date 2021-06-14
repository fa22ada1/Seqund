from flask import Blueprint, render_template, request, redirect, url_for, send_file
from flask_login import current_user
from .sffextract import sfftofasta, sfftofastq
from wtforms import validators, RadioField
from flask_wtf import Form

views = Blueprint('views', __name__)

class TestForm(Form):
    choice_switcher = RadioField(
        'Choice?',
        [validators.Required()],
        choices=[('choice1', 'Choice One'), ('choice2', 'Choice Two')], default='choice1'
    )

@views.route('/')
def home():
    return render_template('home.html', user=current_user)

@views.route('/extract/')
def extract():
    return render_template('extract.html', user=current_user)

@views.route('/extract/', methods=['POST'])
def upload_file():
    option = request.form.get('match')

    print(option)
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        ID = str(current_user.get_id())
        inputfl = "website/files/uploads/upload" + ID + ".sff"
        outputfl = "website/files/outputs/output" + ID
        uploaded_file.save(inputfl)
        if option:
            outputfl = outputfl + '.fastq'
            sfftofastq(inputfl,outputfl)
            suf = 'fastq'
        else :
            outputfl = outputfl + '.fasta'
            sfftofasta(inputfl,outputfl)
            suf = 'fasta'
        return redirect(url_for('views.downloadFile', flsuf = suf))
    return render_template('extract.html', user=current_user)

@views.route('download/<flsuf>')
def downloadFile(flsuf):
    ID = str(current_user.get_id())
    file = "files/outputs/output" + ID + '.' + flsuf
    return send_file(file, as_attachment=True)
