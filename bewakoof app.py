from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Fake user data for demonstration purposes
users = {
    "nagendra": "123456789",
    "radha": "123456789",
}

@app.route('/')
def login():
    return render_template('ram.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        # Successful login, redirect to home page
        return redirect(url_for('bewakoo.html'))
    else:
        # Login failed, redirect back to login page with an error message
        return redirect(url_for('login', error='Login failed. Please try again.'))

@app.route('/home')
def home():
   return render_template('bewakoo.html')

if __name__ == '__main__':
   app.run(debug=True)
