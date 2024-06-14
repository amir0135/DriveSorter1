import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_file_upload(mocker):
    client = APIClient()
    mocker.patch('api.views.suggest_file_name', return_value='Test Name')
    mocker.patch('api.views.suggest_file_category', return_value='Test Category')
    mocker.patch('api.views.suggest_file_tags', return_value=['tag1', 'tag2'])

    with open('test_file.txt', 'w') as f:
        f.write('Dummy content')

    with open('test_file.txt', 'rb') as f:
        response = client.post('/files/', {'file': f}, format='multipart')

    assert response.status_code == 201
    assert response.data['name'] == 'Test Name'
    assert response.data['category'] == 'Test Category'
    assert response.data['tags'] == ['tag1', 'tag2']
