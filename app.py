from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import Finance_Yahoo

app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/stocks_app")

@app.route("/")
def home():
    covid_finance = mongo.db.finance.find_one()
    return render_template("webscraper.html", covid_finance = covid_finance)


@app.route("/scrape")
def scrape():
    stock_data = Finance_Yahoo.scrape()
    mongo.db.finance.update({}, stock_data, upsert = True)
    return redirect("/", code=302)

if __name__ == "__main__":
    app.run(debug=True)