from api.views import suggest_file_name, suggest_file_category, suggest_file_tags

def test_suggest_file_name(mocker):
    mocker.patch('openai.Completion.create', return_value={'choices': [{'text': 'Test Name'}]})
    result = suggest_file_name("Dummy content")
    assert result == "Test Name"

def test_suggest_file_category(mocker):
    mocker.patch('openai.Completion.create', return_value={'choices': [{'text': 'Test Category'}]})
    result = suggest_file_category("Dummy content")
    assert result == "Test Category"

def test_suggest_file_tags(mocker):
    mocker.patch('openai.Completion.create', return_value={'choices': [{'text': 'tag1, tag2, tag3'}]})
    result = suggest_file_tags("Dummy content")
    assert result == ["tag1", "tag2", "tag3"]
