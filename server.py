from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key="Brandon"

@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 0
    else:
        session['count'] += 1
    return render_template('index.html')

@app.route('/reset')
def increment():
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True, host='localhost', port=5001)