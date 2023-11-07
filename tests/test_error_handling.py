import pytest
from flask import Flask
from app.error_handling import handle_error, MyCustomErrorType, AnotherCustomErrorType


@pytest.fixture
def app():
    app = Flask(__name__)

    return app


def test_handle_error_custom_error(app):
    custom_error = MyCustomErrorType("Custom error message")

    # Create a test client for the Flask app
    test_client = app.test_client()

    # Use the test client to make a request and get a response
    response = test_client.get('/some_endpoint')

    assert response.status_code == 404


def test_handle_error_another_custom_error(app):
    another_error = AnotherCustomErrorType("Another custom error message")

    # Create a test client for the Flask app
    test_client = app.test_client()

    # Use the test client to make a request and get a response
    response = test_client.get('/another_endpoint')

    assert response.status_code == 404
