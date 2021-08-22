from flask import Flask, render_template
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)