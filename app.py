# Tax brackets (progressive):
# Bracket 1: $0 - $5,000       taxed at 5%
# Bracket 2: $5,000 - $10,000  taxed at 15%
# Bracket 3: over $10,000      taxed at 20%

from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    income_text = request.form.get("income", "")
    income = float(income_text)

    if income <= 5000:
        tax = income * 0.05
    elif income <= 10000:
        tax = (5000 * 0.05) + ((income - 5000) * 0.15)
    else:
        tax = (5000 * 0.05) + (5000 * 0.15) + ((income - 10000) * 0.20)

    if income < 0:
        return render_template('error.html', message="Income cannot be negative")
    
    income_display = f"${income:.2f}"
    tax_display = f"${tax:.2f}"

    return render_template('result.html', income=income_display, tax=tax_display)
    

if __name__ == '__main__':
    app.run(debug=True)
    