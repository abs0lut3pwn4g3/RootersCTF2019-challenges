import os
import jwt
from path import Path
from flask import Flask, render_template, request, flash, redirect, url_for, make_response, send_from_directory
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_sslify import SSLify


app = Flask(__name__)
app.secret_key = "p3d5c6cd65752b6fab43lc3f32705a58"
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///site.db'  #os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['STATIC_FOLDER'] = 'static'
app.config['ALLOWED_EXTENSIONS'] = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # maximum file size = 1mb
project_dir = os.path.dirname(os.path.abspath(__file__))

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

if 'DYNO' in os.environ:  # only trigger SSLify if the app is running on Heroku
	sslify = SSLify(app)

''' Models '''

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    images = db.relationship('Image', back_populates='user', uselist=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.images}')"


class Image(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, index=True)
    user_id = db.Column(db.ForeignKey('user.id'),
                        nullable=False, index=True, unique=False)
    user = db.relationship('User', foreign_keys=[
                           user_id], back_populates='images')


''' views / routes '''


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
	cookie = request.cookies.get('session_id')
	if not cookie:
		return render_template('home.html')
	key = 'you-will-never-guess'
	username = (jwt.decode(cookie, key=key))['user']
	user = User.query.filter_by(username=username).first()
	if not user:
		return render_template('home.html')
	if request.method == 'POST':
	# check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
			# if user does not select file, browser also
			# submit an empty part without filename
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)
		if file:
			filename = secure_filename(file.filename)
			hashed_username = h(username.encode('utf-8'))
			with Path(os.path.join(project_dir, app.config['STATIC_FOLDER'])) as cwd:
				file.save(os.path.join(hashed_username, filename))
			img = Image(name=filename, user_id=user.id)
			db.session.add(img)
			db.session.commit()
			return redirect(request.url)
	else:
		user_hash = h(username.encode('utf-8'))
		return render_template('home.html', user=username, user_hash=user_hash, images=user.images)


@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')
		if auth(username, password):
			key = 'you-will-never-guess'
			cookie = jwt.encode({"user": username}, key=key, algorithm="HS256")#.decode('utf-8', errors='ignore')
			response = make_response(redirect('/'))
			response.set_cookie('session_id', cookie)
			flash('Login Successful.', 'success')
			return response
		else:
			flash('Login Unsuccessful. Please check username and password', 'danger')
			return render_template('login.html', title='Login')
	else:
		return render_template('login.html', title='Login')


@app.route('/logout')
def logout():
	resp = make_response(redirect('/'))
	resp.delete_cookie('session_id')
	flash('Logout Successful.', 'info')
	return resp


@app.route('/register', methods=['GET', 'POST'])
def register():
	if request.method == 'POST':
		username = request.form.get('username')
		password = request.form.get('password')

		if not is_valid(username):
			flash("Invalid username. Length: 4-20 only.")
			return render_template('register.html', title='Register')

		if user_exists(username):
			flash("A user already exists with this username.")
			return render_template('register.html', title='Register')

		try: 
			hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
			hashed_username = h(username.encode('utf-8'))
			user = User(username=username, password=hashed_password)
			db.session.add(user)
			db.session.commit()
			with Path(os.path.join(project_dir, app.config['STATIC_FOLDER'])) as cwd:
				os.mkdir(hashed_username)
			flash('Registration Successful. You can now login.', 'success')
			return redirect(url_for('login'))
		except Exception as e: 
			return make_response(e)
	else:
		return render_template('register.html', title='Register')


def is_valid(username):
    import re
    if not re.match(r"\A[0-9a-zA-Z]{4,20}\Z", username):
        return False
    else:
        return True


def user_exists(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return True
    else:
        return False


def auth(username, password):
    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        return True
    else:
        return False


def h(s):
	from hashlib import md5
	salt=b"veryrandomstring"
	return md5(s+salt).hexdigest()


if __name__ == "__main__":
    app.run(debug=False)
