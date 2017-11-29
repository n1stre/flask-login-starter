import os
from flask import jsonify
from app import create_app

config_name = os.getenv('APP_ENV') # config_name = "development"
app = create_app(config_name)

@app.route("/")
def home():
  return jsonify({ "works": True })
  

if __name__ == '__main__':
    app.run()