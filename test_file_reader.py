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

def test_big_env_file():
    test_file = ".env"
    with pytest.raises(SystemExit):
        # For testing, assume that any file size greater than 1 is big
        read_file_contents(test_file, file_size_limit=1)
