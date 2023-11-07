from flask import request
from flask_restx import Resource, fields

from application import api, root_ref
from data_handler import is_valid_sensor_data, process_sensor_data

# Define data models
sensor_data_model = api.model('SensorData', {
    'data': fields.String(description='The sensor data to update (e.g., "25.5,60.0")', required=True)
})

response_model = api.model('Response', {
    'message': fields.String(description='The status message ("Pump turned on" or "Pump turned off")')
})

@api.route('/update_data')
class UpdateData(Resource):
    @api.expect(sensor_data_model)
    @api.response(200, 'Sensor data successfully updated')
    @api.response(400, 'Invalid sensor data format')
    @api.response(500, 'An error occurred')
    def post(self):
        data = api.payload['data']
        try:
            if not is_valid_sensor_data(data):
                return "Invalid sensor data format", 400

            sensors_data = process_sensor_data(data)

            root_ref.update(sensors_data)

            return "Sensor data updated", 200
        except Exception as e:
            raise e

@api.route('/control_pump')
class ControlPump(Resource):
    @api.response(200, 'Successfully retrieved pump status', response_model)
    @api.response(400, 'An error occurred or invalid request')
    def get(self):
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

            return {'message': response_message}, 200
        except Exception as e:
            raise e
