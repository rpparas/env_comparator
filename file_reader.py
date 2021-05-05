def read_file_contents(filepath):
    """ Open file and split newline delimeter """
    # TODO: optimize by introducing buffering (read as a streams)
    # TODO: get filesize first & warn if above threshold & confirm before loading into memory
    # TODO: identify if file is serializable (textual) and not binary (e.g. images)

    with open(filepath) as f:
        contents = f.readlines()
    return contents
