#all the imports
"""
For projection: we want to create an entire layout where a series of prompts/questions 
is preented to the user. Robot photo, can it climb, can it do gears?
Next we want to create an algorithm which calculates a score depending on the robot's 
ability to preform.
"""
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from wtforms import Form
from passlib.hash import sha256_crypt

#create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

#Load default config and override config from an enviroment variable
app.config.update(dict(
    DATABASE = os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY = 'development key',
    USERNAME = 'admin',
    PASSWORD = 'default'

    
))
app.config.from_envvar('FLASKR_SETTINGS', silent = True)

def connect_db():
    """Connects to the specfific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode = 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    
@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print 'Initialized the database.'
    
def get_db():
    """Opens a new database if there is none yet for the current
    application context."""
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()
        
@app.route('/', methods=['GET', 'POST'])
def show_entries():
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries = entries)
"""
    if request.form['checkbox'] == 'robotClimb':
        print 'Robot climb was found!'
    else:
        print 'Hi!'
"""

    
    
@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
                   [request.form['title'], request.form['text']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form.get('check'):
            print 'lmao'
        else:
            print 'Nothing was found.'
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)
    
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

def contact(methods=['GET', 'POST']):
    if request.method == 'POST':
        if request.form['checkbox'] == 'robotClimb':
            print 'Found Something'
        elif request.form['checkbox'] == 'Do Something Else':
            print 'Found something else' # do something else
        else:
            print 'Found nothing'# unknown
    elif request.method == 'GET':
        return render_template('contact.html', form=form)

#Method to create an account for posting/access to other parts of the site
@app.route('/createaccount', methods=["CREATEACCOUNT"])
def createaccount():
    error = None
    if request.form == 'CREATEACCOUNT':
        if request.form['screenname']:
            app.config.update(request.form['screenname'])
        else:
            print('Did not recieve a screenname.')
        if request.form['passcode']:
            app.config.update(request.form['passcode'])
        else:
            print('Did not recieve a request for passcode')
    return render_template('login.html', error=error)
"""
class RegistrationForm(form):
    username = TextField(Username, [validators.Length(min=4, max=20)])
    email = TextField(Email, [validators.Length(min=6, max=30)])
    password = PasswordField('Password', [validators.Required(), validators.EqualTo('confirm', message="Passwords must match")])
    confirm = PasswordField('repeat password')
    accept_tos = BooleanField('I accept the terms of service and the privacy notice.', validators.Required())
"""
@app.route('/register/', methods=["GET", "POST"])
def register_page():
    try:
        form = RegistrationForm(request.form)
        if request.method == "POST" and form.validate():
            username = form.username.data 
            email = form.username.data
            password = sha256.encrypt((str(form.password.data)))

    except Exception as e:
        return str(e)
print 'Hello!'
#value = request.form.getlist('check')
#print value
"""
:0
"""
