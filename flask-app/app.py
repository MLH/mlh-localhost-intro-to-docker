from flask import Flask, render_template
import random

app = Flask(__name__)

images = [
  "https://media.giphy.com/media/nNxT5qXR02FOM/giphy.gif",
  "https://media.giphy.com/media/10dU7AN7xsi1I4/giphy.gif",
  "https://media.giphy.com/media/t7MWRoExDRF72/giphy.gif"
]

@app.route('/')
def index():
  url = random.choice(images)
  return render_template("index.html", url=url)

if __name__ == "__main__":
  app.run(host="0.0.0.0")
