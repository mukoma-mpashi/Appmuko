def is_valid_sensor_data(data):
    """
    Validate the sensor data format.

    This function validates that the data is in the expected format. It checks that 'data' is a string
    containing two numeric values separated by a comma.

    Args:
        data (str): The sensor data to validate.

    Returns:
        bool: True if the data is valid; otherwise, False.
    """
    if not isinstance(data, str):
        return False

    data_parts = data.split(',')
    if len(data_parts) != 2:
        return False

    temperature, moisture = data_parts

    if not (temperature.replace('.', '', 1).isdigit() and moisture.replace('.', '', 1).isdigit()):
        return False

    return True


def process_sensor_data(data):
    """
    Process sensor data.

    This function processes the validated sensor data. It can perform additional operations, data transformation,
    or save it to a database.

    Args:
        data (str): The validated sensor data.

    Returns:
        dict: A structured dictionary of sensor data.
    """
    temperature, moisture = data.split(',')

    # Create a structured dictionary with sensor data
    sensors_data = {
        "sensor1": {
            "temperature": f"{temperature}°C",
            "moisture": f"{moisture}%"
        }
    }

    return sensors_data
