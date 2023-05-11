from flask import Flask, jsonify, render_template, request
import datetime
from pydantic import BaseModel, EmailStr, validator
import re


class FormData(BaseModel):
    name: str
    email: EmailStr
    password: str
    speciality: str

    @validator('email')
    def check_email(cls, value):
        regex = "^\w+@\w+.\w{2,5}$"
        if re.match(regex, value):
            return value
        else:
            raise ValueError('email must be in format test@gmail.com')

app = Flask(__name__)



@app.route('/', methods=["GET", "POST"])
def greeting():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        name = request.form["name"]
        return render_template('greeting.html', name=name)


@app.route('/register', methods=["POST"])
def register():
    data = {
        'name': request.form.get('name'),
        'email': request.form.get('email'),
        'password': request.form.get('password'),
        'speciality': request.form.get('speciality'),
    }
    form_data_validator = FormData(**data)
    if form_data_validator:
        return jsonify(data)




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


@app.route('/test-1', methods=["GET"])
def test_function():
    data = {
        'message': 'New Test Message'
    }
    return jsonify(data)

app.run(debug=True)
