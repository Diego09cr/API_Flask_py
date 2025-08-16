from flask import Flask
from myapi.routes import bp

app = Flask(__name__)
app.register_blueprint(bp)