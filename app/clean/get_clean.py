import pandas as pd
from flask import Response, redirect, render_template

def get_clean(df):
    df = pd.read_csv('result.csv')
    csv = df.to_string()
    return Response(
        csv,
        mimetype="text/csv",
        headers={"Content-disposition":
                 "attachment; filename=new_result.csv"}) 