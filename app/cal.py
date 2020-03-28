from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('cal.html')

# Form submission route
@app.route('/send', methods=['POST'])
def send():
    if request.method=='POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']
        # calculation if statements
        if operation == 'add':
            sum = float(num1) + float(num2)
            return render_template('cal.html', sum=sum)
        elif operation == 'subtract':
            sum = float(num1)-float(num2)
            return render_template('cal.html', sum=sum)
        elif operation == 'multiply':
            sum = float(num1)*float(num2)
            return render_template('cal.html', sum=sum)
        elif operation == 'divide':
            sum = float(num1)/float(num2)
            return render_template('cal.html', sum=sum)
        else:
            return render_template('cal.html')

app.run()