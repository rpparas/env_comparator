import pytest
from file_reader import read_file_contents

def test_read_env_file():
    test_file = ".env"
    contents = read_file_contents(test_file)
    assert len(contents) > 0

def test_read_invalid_file_path():
    test_file = "invalid_path/.env"
    with pytest.raises(FileNotFoundError):
        read_file_contents(test_file)
