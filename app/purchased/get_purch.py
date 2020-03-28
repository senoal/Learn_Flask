import pandas as pd
from flask import Response, redirect, render_template

def get_purch(df):
    df = pd.read_csv('Purch_report.csv')
    purch_csv = df.to_string()
    return Response(
        purch_csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                "attachment; filename=new_purch.csv"})