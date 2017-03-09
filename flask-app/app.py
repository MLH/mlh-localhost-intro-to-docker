from flask import Flask, render_template
import random

app = Flask(__name__)

images = [
  "http://bit.ly/docker-cat-1",
  "http://bit.ly/docker-cat-2",
  "http://bit.ly/docker-cat-3"
]

@app.route('/')
def index():
  url = random.choice(images)
  return render_template("index.html", url=url)

if __name__ == "__main__":
  app.run(host="0.0.0.0")
