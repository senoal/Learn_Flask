import pandas as pd
from flask import request, redirect
from .clean_nan import clean_nan
from .clean_nanup import clean_nanup
from .clean_nannor import clean_nannor
from .clean_upnor import clean_upnor
from .clean_nor import clean_nor
from .clean_up import clean_up
from .clean_all import clean_all

def clean_process(csv_input):
    # ubah ke dalam bentuk array jika tidak bisa langsung ke dataframe
    tes_1 = []
    for i in range(len(csv_input)):
        tes_1.append([])
        for j in range(len(csv_input[i])):
            try:
                v = int(csv_input[i][j])
                tes_1[i].append(v)
            except:
                v = csv_input[i][j]
                if v == '':
                    tes_1[i].append(None)
                else:
                    tes_1[i].append(v)
    csv_input = tes_1
    csv_input = pd.DataFrame()
    csv_input['Customer']=tes_1[0]
    csv_input['Type']=tes_1[1]
    csv_input['Price']=tes_1[2]
    csv_input = csv_input.drop(csv_input.index[0])
    if request.method == 'POST':
        # total
        if request.form.get('check_nan'):
            # nan & normalize
            if request.form.get('check_nor'):
                csv_input = clean_nannor(csv_input)
                return csv_input                
            # nan & uppercase
            if request.form.get('check_up'):
                csv_input = clean_nanup(csv_input)
                return csv_input
            # nan
            csv_input = clean_nan(csv_input)
            return csv_input

        # uppercase
        if request.form.get('check_up'):
            # uppercase & normalize
            if request.form.get('check_nor'):
                csv_input = clean_upnor(csv_input)
                return csv_input
            # uppercase
            csv_input = clean_up(csv_input)
            return csv_input

        # normalize
        if request.form.get('check_nor'):
            csv_input = clean_nor(csv_input)
            return csv_input
        # all in one
        if request.form.get('check_all'):
            csv_input = clean_all(csv_input)
            return csv_input

    return redirect('/')