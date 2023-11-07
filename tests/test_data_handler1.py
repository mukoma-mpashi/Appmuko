# import unittest
# import requests
#
# class TestIntegration(unittest.TestCase):
#     def setUp(self):
#         # Set the base URL for your Flask server (update this with your server's URL)
#         self.base_url = "http://192.168.137.153:5000"
#
#     def test_update_data_valid(self):
#         data = "25.00,60.00"
#         response = requests.post(f"{self.base_url}/update_data", data=data)
#         self.assertEqual(response.status_code, 200)  # Expect a successful response
#         self.assertEqual(response.text, "Sensor data updated")
#
#     def test_update_data_invalid_format(self):
#         data = "25.00"
#         response = requests.post(f"{self.base_url}/update_data", data=data)
#         self.assertEqual(response.status_code, 400)  # Expect a bad request response
#
#     def test_update_data_invalid_values(self):
#         data = "110.00,60.00"
#         response = requests.post(f"{self.base_url}/update_data", data=data)
#         self.assertEqual(response.status_code, 400)  # Expect a bad request response
#
#     def test_control_pump(self):
#         response = requests.get(f"{self.base_url}/control_pump")
#         self.assertEqual(response.status_code, 200)  # Expect a successful response
#         self.assertTrue("Pump" in response.text)  # Expect a response containing "Pump"
#
# if __name__ == '__main__':
#     unittest.main()
