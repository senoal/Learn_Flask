from flask import request, redirect
from .clean_nan import clean_nan
from .clean_nanup import clean_nanup
from .clean_nannor import clean_nannor
from .clean_upnor import clean_upnor
from .clean_nor import clean_nor
from .clean_up import clean_up
from .clean_all import clean_all

def clean_condition(csv_input):
    if request.method == 'POST':
        if request.form.get('check_nan'):       # nan
            if request.form.get('check_nor'):   # nan & normalize
                csv_input = clean_nannor(csv_input)
                return csv_input                
            if request.form.get('check_up'):    # nan & uppercase
                csv_input = clean_nanup(csv_input)
                return csv_input
            csv_input = clean_nan(csv_input)    # nan
            return csv_input
        if request.form.get('check_up'):        # uppercase
            if request.form.get('check_nor'):   # uppercase & normalize
                csv_input = clean_upnor(csv_input)
                return csv_input
            csv_input = clean_up(csv_input)     # uppercase
            return csv_input
        if request.form.get('check_nor'):       # normalize
            csv_input = clean_nor(csv_input)
            return csv_input
        if request.form.get('check_all'):       # all in one
            csv_input = clean_all(csv_input)
            return csv_input

    return redirect('/')                        # back to home