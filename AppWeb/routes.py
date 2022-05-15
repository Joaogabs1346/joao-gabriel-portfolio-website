from flask import render_template
from AppWeb import app

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/About')
def about():
    return render_template('Sobremim.html')

@app.route('/About/cv')
def cv():
    return

@app.route('/Resume')
def resume():
    return  render_template('Resume.html')


@app.route('/Services')
def servicos():
    return render_template('Services.html')

@app.route('/Portfolio')
def portfolio():
    return render_template('Portfolio.html')

