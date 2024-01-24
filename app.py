from database import db
from config import Config
from model.userModel import User
from user_services.userService import UserService
from flask import Flask, request, jsonify, render_template, flash, redirect, session, url_for, send_from_directory
from flask_login import LoginManager, login_user, current_user, logout_user, login_required

app = Flask(__name__, static_url_path='/static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + Config.DB_USER + ':' + Config.DB_PASS + '@' + Config.DB_HOST + ':' + Config.DB_PORT + '/' + Config.DB_NAME
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = Config.SECRET_KEY

# Inisialisasi database dan login manager
db = db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Route untuk halaman login
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Menangani pengiriman formulir login
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = UserService.login(email, password)
        if user is None:
            return render_template('login.html', error='Email atau password salah')
        login_user(user)
        return redirect(url_for('index'))
    return render_template('login.html') 

# Route untuk halaman registrasi
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        password_confirm = request.form['password_confirm']
        email = request.form['email']
        
        if password != password_confirm:
            return render_template('register.html', error='Konfirmasi password tidak sesuai')
        
        # Instansiasi UserService
        user_service = UserService()

        # Periksa apakah email sudah terdaftar
        user = user_service.getUser(email)
        if user is not None:
            return render_template('register.html', error='Email sudah terdaftar')

        # Buat pengguna baru
        user_service.createUser(name, password, email)
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/')
@login_required
def index():
    active_page = 'index'
    return render_template('index.html', active_page=active_page) 

@app.route('/data-latih') 
@login_required
def trainingDataPage():
    active_page = 'data'
    return render_template('trainingDataPage.html', active_page=active_page) 

@app.route('/data-uji') 
@login_required
def testingDataPage():
    active_page = 'data'
    return render_template('testingDataPage.html', active_page=active_page) 

@app.route('/hasil-preprocessing') 
@login_required
def preprocessingResultsPage():
    active_page = 'data'
    return render_template('preprocessingResultsPage.html', active_page=active_page) 

@app.route('/klasifikasi') 
@login_required
def classificationPage():
    active_page = 'classification'
    return render_template('classificationPage.html', active_page=active_page) 

@app.route('/hasil-analisis') 
@login_required
def analysisResultsPage():
    active_page = 'analysisResults'
    return render_template('analysisResultsPage.html', active_page=active_page) 

# Route untuk logout
@app.route('/logout')
@login_required
def logout(): 
    logout_user()
    return redirect(url_for('login'))

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
