import os
import pytest
from datetime import datetime
from unittest.mock import MagicMock
from lambda_function import save_metadata

@pytest.fixture
def dynamodb_table():
    os.environ['DYNAMODB_TABLE'] = 'Ebike-image-metadata'
    dynamodb_mock = MagicMock()
    table_mock = MagicMock()
    dynamodb_mock.Table.return_value = table_mock
    yield table_mock

def test_save_metadata(dynamodb_table):
    # Mocking the DynamoDB table
    key = 'test_image.jpg'
    size = 1024
    upload_time = datetime.now().isoformat()

    # Call the save_metadata function
    response = save_metadata(key, size, upload_time)

    # Assert that put_item method is called with correct arguments
    dynamodb_table.put_item.assert_called_once_with(
        Item={
            'key': key,
            'size': size,
            'upload_time': upload_time
        }
    )

    # Assert the response
    assert response == {
        'statusCode': 200,
        'body': f'Metadata saved for {key}'
    }
