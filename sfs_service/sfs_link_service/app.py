from flask import Flask, render_template,request,make_response, request

from models import Links
import json

model_obj = Links()

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/links")
def links():
    global model_obj
    datas=model_obj.all()
    return json.dumps(datas)

@app.route("/search")
def search():
  global model_obj
  print(request.args)

  category = request.args['cat']
  content = request.args['content']

  searched_data = model_obj.search(cat=category, content=content)
  print(searched_data)
  return searched_data

if __name__ == "__main__":
  app.run(host="0.0.0.0",debug=True)
