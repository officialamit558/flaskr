from flask import Flask , request ,redirect , url_for , render_template
from flask import make_response , session

app = Flask(__name__)
app.secret_key = "234AMit456"

@app.route('/')
def index():
    username = session.get('username', None)
    if username:
        return 'Logged in as ' + username + '<br>' + \
               "<b><a href='/logout'>Click for logout</a></b>"
    return "You are not logged in <br><a href='/login'>Click here to login</a>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('session.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)