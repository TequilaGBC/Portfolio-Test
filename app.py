from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/services')
def services_page():
    return render_template('services.html')


@app.route('/login')
def login_page():
    return render_template('login.html')


@app.route('/register')
def register_page():
    return render_template('register.html')


@app.route('/about')
def about_page():
    return render_template('about.html')


if __name__ == '__main__':
    app.run()
