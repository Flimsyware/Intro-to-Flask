from flask import render_template # needed to render HTML templates
from app import app 

################################################################################

# localhost:5000/ or localhost:5000/index displays "Hello, World"
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World"

################################################################################
# localhost:5000/welcome displays some static HTML,
# followed by "Hello, {user}"
# uses flask's render_template to render HTML
    # needs import render_template 

@app.route('/welcome')
def welcome():
    user = { 'username': 'You' }
    return render_template('index.html', title='Home', user=user) 
    
################################################################################
# localhost:5000/

