from flask import Flask, render_template, request

app = Flask(__name__)

balance = 5000

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/withdraw', methods=['POST'])
def withdraw():
    global balance
    amount = int(request.form['amount'])
    if amount > balance:
        return "Insufficient funds!"
    else:
        balance -= amount
        return f"Withdrawal successful! Remaining balance: ${balance}"

if __name__ == '__main__':
    app.run(debug=True)
