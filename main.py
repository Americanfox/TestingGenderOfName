from flask import Flask, render_template
import random
from datetime import datetime
import requests
response = requests.get(url="https://api.genderize.io?name=luke")
dict = response.text



print(response)
def convert(function):
    def wrap_function():
        response
        guess = function()




app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(1,10)
    current_year = datetime.now().strftime("%Y")
    return render_template("index.html", num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess(name):
    response = requests.get(url=f"https://api.genderize.io?name={name}")
    gender_data = response.json()
    gender = gender_data["gender"]
    age_response = requests.get(url=f"https://api.agify.io?name={name}")
    age_data = age_response.json()
    age = age_data["age"]
    return render_template("guess.html", gen=gender, age=age, guess=name)

@app.route("/blog")
def blog():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("bolg.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)


