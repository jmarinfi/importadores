import os
from flask import Flask, render_template, redirect, url_for, current_app, send_from_directory
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"]


@app.route('/')
def home():
    for item in app.config.items():
        print(item)
    return render_template('home.html')


@app.route('/imp-extensimetros', methods=['GET', 'POST'])
def imp_strain_gages():
    return render_template('imp-extensimetros.html')
