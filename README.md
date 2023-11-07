# Flask Server for IoT Data Handling

Developed by Mukoma Mpashi

This Flask server serves as an intermediary for handling IoT sensor data and controlling a pump connected to an IoT hub. The server communicates with a Firebase Realtime Database and receives sensor data from the hub, allowing control of the pump status.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

To run the Flask server locally or in a production environment, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-flask-server.git
   cd your-flask-server
2. install dependicies:
    ```bash
    pip install -r requirements.txt


3. Create a Firebase Realtime Database and obtain the necessary credentials file (secrets.json). Place it in the root directory of the project

4. Run the server:
     ```bash
     python app.py


                            Usage
Once the server is up and running, you can interact with it using the following endpoints:

. /update_data (POST): Send sensor data to update the database.
. /control_pump (GET): Get or set the status of the pump.