from flask import Flask

from src.application.planet_controller import planet_controller

app = Flask(__name__)

app.register_blueprint(planet_controller, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
