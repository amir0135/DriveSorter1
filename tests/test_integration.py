import pytest
from rest_framework.test import APIClient

@pytest.mark.django_db
def test_search_files(mocker):
    client = APIClient()
    mocker.patch('api.views.suggest_file_name', return_value='Test Name')
    mocker.patch('api.views.suggest_file_category', return_value='Test Category')
    mocker.patch('api.views.suggest_file_tags', return_value=['tag1', 'tag2'])

    # Upload a file
    with open('test_file.txt', 'w') as f:
        f.write('Dummy content')

    with open('test_file.txt', 'rb') as f:
        client.post('/files/', {'file': f}, format='multipart')

    # Search for the file
    response = client.get('/search/', {'q': 'Test Name'})
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == 'Test Name'
