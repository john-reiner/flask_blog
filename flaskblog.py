from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm, RegistraionForm
app = Flask(__name__)


app.config['SECRET_KEY'] = '9ab3b25512034e50d031ee2d91bbaa3c'

posts = [
    {
        'author': 'John Reiner',
        'title': 'flask for beginners',
        'content': 'First post content',
        'last_updated': '8/22/2021'
    },
        {
        'author': 'Django Reiner',
        'title': 'flask is flask',
        'content': 'Second post content',
        'last_updated': '8/12/2021'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistraionForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)