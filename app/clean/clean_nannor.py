from flask import redirect

def clean_nannor(csv_input):
    csv_input.sort_values(by=['Customer'], inplace=True)
    csv_input['Customer'] = csv_input['Customer'].str.upper()
    csv_input['Price'] = csv_input['Price']/csv_input['Price'].max()
    def set_value (row_number, assigned_value):
        return assigned_value[row_number]
    new ={'avanza' : 500000, 'fortuner' : 1000000, 'pajero' : 1500000}
    csv_input['cleaning'] = csv_input.iloc[:,1].apply(set_value, args=(new, ))
    csv_input = csv_input.T
    csv_input['Total']=csv_input.iloc[2:,:].sum(axis=1)
    csv_input = csv_input.fillna("-")
    csv_input = csv_input.fillna('-').T
    csv_input = csv_input.set_index('Customer')
    csv_input.to_csv('result.csv')
    return redirect('/showdata')