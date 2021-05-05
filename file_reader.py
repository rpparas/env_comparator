import os
import logging

ONE_MEGABYTE = 1000000

def read_file_contents(filepath, file_size_limit=ONE_MEGABYTE):
    """
    Open file and split newline delimeter
    If size is too big based on bytes specified, then output error message
    """
    # TODO: optimize by introducing buffering (read as a streams)
    # TODO: get filesize first & warn if above threshold & confirm before loading into memory
    # TODO: identify if file is serializable (textual) and not binary (e.g. images)

    if file_size_limit and get_file_size(filepath) > file_size_limit:
        logging.error(f"File is too big to process. Limit of {file_size_limit}")
        exit(1)

    try:
        if not is_file_serializable(filepath):
            logging.error("File is not readable as text")
            exit(1)
    except:
        # TODO: only raise exception for ImportError and specific errors
        logging.warning(f"Unable to check filetype of {filepath}")

    with open(filepath) as f:
        contents = f.readlines()
    return contents

def get_file_size(filepath):
    """ Calculates the filesize in bytes without opening/loading it into memory """
    return os.path.getsize(filepath)

def is_file_serializable(filepath):
    blob = open(filepath, "rb").read()

    import magic
    m = magic.Magic(mime_encoding=True)
    encoding = m.from_buffer(blob)
    return encoding in ["utf-8", "us-ascii"]
