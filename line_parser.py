import re

KEY_VALUE_PATTERN = r".+=.*"
KEY_NAME_PATTERN = r"^[a-zA-Z0-9_]+$"

def line_matches_pattern(line, pattern=KEY_VALUE_PATTERN):
    """
    Checks whether line meets KEY=PAIR pattern.
    This method trims whitespaces before and after strings,
    ignores distinction uppercase/lowercase,
    """
    if not line:
        return False

    return re.match(pattern, line.strip())

def extract_key(line, delimiter="="):
    """
    If there are multiple equality symbols, assume the first all chars before that is the key,
    then apply another regex check to see if naming is valid (alphanumeric + underscores)
    """

    if not line:
        return None

    potential_key = line.split("=")[0].strip()
    if re.match(KEY_NAME_PATTERN, potential_key):
        return potential_key
    return None
