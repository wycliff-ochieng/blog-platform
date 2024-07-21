from flask import Flask, render_template,request

app = Flask(__name__)

posts = [
    {
        'title':'Blog Post 1',
        'author':'Kenny Rodgers',
        'content':'Launched my official music album today',
        'date_posted':'24/5/2023'
    },
    {
        'title':'Blog Post 2',
        'author':'John Denver',
        'content':'I was voted best artist of the year',
        'date_posted':'21/3/2023'
    }
]

@app.route("/")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')


if __name__=="__main__":
    app.run(debug=True)