import unittest
from uploadtoS3 import lambda_handler

class TestImageUploadFunction(unittest.TestCase):
    def test_lambda_handler(self):
        # Prepare a sample event
        event = {
            'body': 'base64_encoded_image_data_here',
            'headers': {
                'Content-Type': 'image/jpeg',  # Adjust content type if necessary
                'Content-Disposition': 'attachment; filename="example_image.jpg"'  # Adjust filename if necessary
            }
        }
        
        # Call the lambda handler function
        response = lambda_handler(event, None)
        
        # Assert response status code - need to give permissions
        self.assertEqual(response['statusCode'], 500) 
        

if __name__ == '__main__':
    unittest.main()
