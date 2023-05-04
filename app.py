from flask import Flask, jsonify, render_template
import datetime

app = Flask(__name__)


@app.route('/', methods=["GET"])
def hello():
    return 'Hello, World!'


@app.route('/api', methods=["GET"])
def get_api_endpoints():
    info = [
        {
            'method': 'GET',
            'endpoint': '/',
            'description': 'Return message "Hello, World!"'
        },
        {
            'method': 'GET',
            'endpoint': '/api',
            'description': 'Return all API endpoints'
        },
        {
            'method': 'GET',
            'endpoint': '/api/data',
            'description': 'Return some data'
        }
    ]
    return jsonify(info)


@app.route('/api/data', methods=["GET"])
def get_api_data():
    data = {
        'username': 'NurikN999',
        'email': 'test@test.com',
        'address': 'Shalyapin street',
        'date_of_login': datetime.datetime.now()
    }
    return jsonify(data)


@app.route('/test', methods=["GET"])
def index():
    context = {
        "name": "Nurmukhamed",
        "surname": "Nurkamal",
        "email": "test@gmail.com",
        "date_of_login": datetime.datetime.now()
    }
    return render_template('index.html', context=context)

app.run(debug=True)
