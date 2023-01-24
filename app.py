from flask import Flask, jsonify
from importlib import import_module

def register_blueprints(app):
    for module_name in ['Users', 'Devices', 'Domains', 'Groups', 'Panels']:
        module = import_module('routes.{}'.format(module_name))
        app.register_blueprint(module.blueprint)

# inicia a aplicação
def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    return app

app = create_app()

@app.route('/')
def home():
    return "A API tá funcionando!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)