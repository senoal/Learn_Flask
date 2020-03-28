from flask import *
import pandas as pd
import numpy as np
from .clean_condition import clean_condition
from flask import redirect
import io
import csv
import requests

def trans(f):
    f = request.files['data_file']
    if not f:
        return redirect('/cleaning')
    stream = io.StringIO(f.stream.read().decode("UTF8"), newline=None)
    csv_input = csv.reader(stream)
    csv_input = pd.DataFrame(csv_input)
    csv_input = np.array(csv_input)
    csv_input = csv_input.T

    tes_1 = []                                  # transform dari dataframe ke array
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
    print(tes_1)
    csv_input = tes_1
    csv_input = pd.DataFrame()
    csv_input['Customer']=tes_1[0]
    csv_input['Type']=tes_1[1]
    csv_input['Price']=tes_1[2]
    csv_input = csv_input.drop(csv_input.index[0])

    csv_input = clean_condition(csv_input)
    return csv_input    # konek ke cleaning menggunakan return csv_input