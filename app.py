#imports 
from flask import Flask
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy


#My app
app=Flask(__name__)


@app.route("/")
def index():
    return "This is Desalegn Deribe"

if __name__ == "__main__":
  app.run(debug=True)
