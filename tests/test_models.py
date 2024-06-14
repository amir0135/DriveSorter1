import pytest
from api.models import File

@pytest.mark.django_db
def test_file_model():
    file = File.objects.create(name="Test File")
    assert file.name == "Test File"
