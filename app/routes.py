from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {"username": "Lucjan"}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful Day in Portland!'
        },
        {   'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Randy'},
            'body': 'I badly want a cheeseburger'
        },
        {
            'author': {'username': 'Sheriff'},
            'body': 'Bla bli bla'
        },
        {
            'author': {'username': 'Mike'},
            'body': 'Da di doo'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)