import os
from flask import Flask, render_template, redirect, url_for, current_app, send_from_directory

from dao.dao_td import dao_td

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/imp-extensimetros', methods=['GET', 'POST'])
def imp_strain_gages():
    return render_template('imp-extensimetros.html', dao_td=dao_td)
