from flask import redirect

def clean_upnor(csv_input):
    csv_input.sort_values(by=['Customer'], inplace=True)
    csv_input['Customer'] = csv_input['Customer'].str.upper()
    csv_input['Price'] = csv_input['Price']/csv_input['Price'].max()
    csv_input['Type'] = csv_input['Type'].str.upper()
    csv_input = csv_input.set_index('Customer')
    csv_input.to_csv('result.csv')
    return redirect('/showdata')