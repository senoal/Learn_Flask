from app import app
from flask import render_template
from .clean.trans import trans
from .purchased.purchased import purchased
from .clean.get_clean import get_clean
from .purchased.get_purch import get_purch
from .clean.show_clean import show_clean
from .purchased.show_purch import show_purch

@app.route('/')
def home():
    return render_template('home.html')
# cleaning page
@app.route('/cleaning')
def cleaning():
    return render_template('cleaning.html')    
# download cleaning
@app.route("/getPlotCSV")
def getPlotCSV():
    df = get_clean('result.csv')
    return df
# display cleaning
@app.route("/showdata")
def show_tables():
    data = show_clean('result.csv')
    return data
# Get file for cleaning
@app.route('/transform', methods=["GET","POST"])
def transform_view():
    f = trans('data_file')
    return f
# Purchased page
@app.route('/purchased')
def purchase():
    return render_template('purchased.html')  
# Purchased post from purchased page
@app.route('/purch', methods=['POST'])
def purch():
    p = purchased('POST')
    return p
# Download Purch
@app.route("/getPurch")
def getPurch():
    df = get_purch('Purch_report.csv')
    return df
# Display purch
@app.route("/showPurch")
def showPurch():
    data = show_purch('Purch_report.csv')
    return data