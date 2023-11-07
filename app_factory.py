import firebase_admin
from firebase_admin import credentials, db
from flask_caching import Cache
from flask_restx import Api
from flask import Flask, request
import time
from azure_monitor import log_custom_event, log_operation_duration, log_exception
from data_handler import is_valid_sensor_data, process_sensor_data
from error_handling import handle_error

def create_app():
    app = Flask(__name__)

    # Initialize Firebase
    cred = credentials.Certificate("secrets.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': "https://arcus-c9ae1-default-rtdb.firebaseio.com/"
    })

    root_ref = db.reference('/')

    # Configure Flask-Caching
    cache = Cache(app, config={'CACHE_TYPE': 'simple'})

    api = Api(app, version='1.0', title='MukoApi', description='Arcus API', doc='/apidocs/')

    app.errorhandler(Exception)(handle_error)

    @cache.cached(timeout=300)  # Cache the result for 300 seconds 
    @app.route('/update_data', methods=['POST'])
    def update_data():
        try:
            data = request.data.decode("utf-8")

            if not is_valid_sensor_data(data):
                log_custom_event('InvalidSensorData', properties={'data': data})
                return "Invalid sensor data format", 400

            start_time = time.time()

            sensors_data = process_sensor_data(data)

            # Log the duration of this operation
            log_operation_duration('UpdateDataDuration', start_time)

            root_ref.update(sensors_data)
            log_custom_event('SensorDataUpdated', properties={'data': data})

            return "Sensor data updated"
        except Exception as e:
            log_exception()
            raise e

    @cache.cached(timeout=300)  # Cache the result for 300 seconds 
    @app.route('/control_pump', methods=['GET'])
    def control_pump():
        try:
            
            pump_status = root_ref.child("sensor1").child("pump_status").get()

            if pump_status is not None:
                pump_status = pump_status == "on"  # Convert to a boolean

                # Depending on the "pump_status" value, take appropriate actions to control the pump

                response_message = ""
                if pump_status:
                    response_message = "Pump turned on"
                else:
                    response_message = "Pump turned off"
            else:
                response_message = "Pump status not found in the database"

            return response_message
        except Exception as e:
            log_exception()
            raise e

    return app
