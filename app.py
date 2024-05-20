from flask import Flask
from flask_cors import CORS
from config import Config
from models import db
from label_controller import label_bp

app = Flask(__name__)
CORS(app, origins=["*"])

app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(label_bp)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
