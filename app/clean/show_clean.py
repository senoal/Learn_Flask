from flask import render_template
import pandas as pd

def show_clean(data):
    data = pd.read_csv('result.csv')
    return render_template('view.html',tables=[data.to_html(classes='Data')],
    titles = ['Hasil Data'])