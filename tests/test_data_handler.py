# from data_handler import is_valid_sensor_data, process_sensor_data
# from data_handler import is_valid_sensor_data, process_sensor_data
from mukoApp.data_handler import is_valid_sensor_data, process_sensor_data

def test_is_valid_sensor_data():
    assert is_valid_sensor_data("25.5,60.0") == True
    assert is_valid_sensor_data("25.5") == False
    assert is_valid_sensor_data("25.5,abc") == False


def test_process_sensor_data():
    data = "25.5,60.0"
    expected_result = {
        "sensor1": {
            "temperature": "25.5°C",
            "moisture": "60.0%"
        }
    }
    assert process_sensor_data(data) == expected_result
