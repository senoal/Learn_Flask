import pandas as pd
from flask import render_template

def show_purch(data):
    data = pd.read_csv('Purch_report.csv')
    return render_template('purchased_view.html',tables=[data.to_html(classes='Data')],
    titles = ['Purchased Report'])