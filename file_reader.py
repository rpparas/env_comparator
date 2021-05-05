import os
import logging

def read_file_contents(filepath, file_size_limit=None):
    """
    Open file and split newline delimeter
    If size is too big based on bytes specified, then output error message
    """
    # TODO: optimize by introducing buffering (read as a streams)
    # TODO: get filesize first & warn if above threshold & confirm before loading into memory
    # TODO: identify if file is serializable (textual) and not binary (e.g. images)

    if file_size_limit and get_file_size(filepath) > file_size_limit:
        logging.error("File is too big to process")
        exit(1)

    with open(filepath) as f:
        contents = f.readlines()
    return contents

def get_file_size(filepath):
    return os.path.getsize(filepath)
