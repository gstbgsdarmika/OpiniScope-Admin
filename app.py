from flask import Flask, request, jsonify, render_template, flash, redirect, session, url_for, send_from_directory
from database import db
from config import Config
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from model.userModel import User

app = Flask(__name__, static_url_path='/static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + Config.DB_USER + ':' + Config.DB_PASS + '@' + Config.DB_HOST + ':' + Config.DB_PORT + '/' + Config.DB_NAME
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = Config.SECRET_KEY

@app.route('/')
def index():
    active_page = 'index'
    return render_template('index.html', active_page=active_page) 

@app.route('/data-latih') 
def trainingDataPage():
    active_page = 'data'
    return render_template('trainingDataPage.html', active_page=active_page) 

@app.route('/data-uji') 
def testingDataPage():
    active_page = 'data'
    return render_template('testingDataPage.html', active_page=active_page) 

@app.route('/hasil-preprocessing') 
def preprocessingResultsPage():
    active_page = 'data'
    return render_template('preprocessingResultsPage.html', active_page=active_page) 

@app.route('/klasifikasi') 
def classificationPage():
    active_page = 'classification'
    return render_template('classificationPage.html', active_page=active_page) 

@app.route('/hasil-analisis') 
def analysisResultsPage():
    active_page = 'analysisResults'
    return render_template('analysisResultsPage.html', active_page=active_page) 

@app.route("/preline.js")
def serve_preline_js():
    return send_from_directory("node_modules/preline/dist", "preline.js")

@app.route("/apexcharts.min.js")
def serve_apexcharts_js():
    return send_from_directory("node_modules/apexcharts/dist", "apexcharts.min.js")

@app.route("/lodash.min.js")
def serve_lodash_js():
    return send_from_directory("node_modules/lodash", "lodash.min.js")

@app.route("/apexcharts.min.js")
def serve_apexcharts_css():
    return send_from_directory("node_modules/apexcharts/dist", "apexcharts.css")

if __name__ == '__main__':
    app.run(debug=True)
