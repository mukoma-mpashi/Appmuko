import requests

# Define the server URL
server_url = "https://mukoapi.azurewebsites.net"  # Replace with your server's URL

# Define the endpoints
update_data_endpoint = "/update_data"
control_pump_endpoint = "/control_pump"

# Sample sensor data as a string
sensor_data = "20.00,62.00"  # Replace with your sensor data

# Perform a POST request to update sensor data
response = requests.post(f"{server_url}{update_data_endpoint}", data=sensor_data, headers={"Content-Type": "text/plain"})
print("POST Response:")
print(response.text)

# Perform a GET request to retrieve the pump status
response = requests.get(f"{server_url}{control_pump_endpoint}")
print("\nGET Response (Pump Status):")
print(response.text)
