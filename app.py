from flask import Flask, request, jsonify, render_template, flash, redirect, session, url_for
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
    return render_template('index.html') 

if __name__ == '__main__':
    app.run(debug=True)
