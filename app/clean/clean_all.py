from flask import redirect

def clean_all(csv_input):
    csv_input.sort_values(by=['Customer'], inplace=True)
    csv_input['Customer'] = csv_input['Customer'].str.upper()
    csv_input['Price'] = csv_input['Price']/csv_input['Price'].max()
    def set_value (row_number, assigned_value):
        return assigned_value[row_number]
    new ={'avanza' : 500000, 'fortuner' : 1000000, 'pajero' : 1500000}
    csv_input['Rupiah'] = csv_input.iloc[:,1].apply(set_value, args=(new, ))
    dft = csv_input.T
    dft['Total']=dft.iloc[2:,:].sum(axis=1)
    dft = dft.fillna("-")
    csv_input = dft.fillna('-').T
    csv_input['Type'] = csv_input['Type'].str.upper()

    val=csv_input['Type'].value_counts()
    print(val)

    csv_input = csv_input.set_index('Customer')
    csv_input.to_csv('result.csv')
    return redirect('/showdata')