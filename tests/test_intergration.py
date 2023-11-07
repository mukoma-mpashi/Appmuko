# import unittest
# from app_factory import create_app  # Import create_app from app_factory.py
#
# class TestIntegration(unittest.TestCase):
#     def setUp(self):
#         self.app = create_app().test_client()  # Create the Flask app for testing
#
#     def test_update_data_valid(self):
#         response = self.app.post('/update_data', data="29.0,60.0")
#         self.assertEqual(response.status_code, 200)
#
#     def test_update_data_invalid(self):
#         response = self.app.post('/update_data', data="25.0")
#         self.assertEqual(response.status_code, 400)
#
# if __name__ == '__main__':
#     unittest.main()
