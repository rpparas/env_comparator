import argparse
import logging

from setup_logging import define_log_settings
from file_reader import read_file_contents
from line_parser import line_matches_pattern, extract_key

def compare_keys_in_files(contents_file1, contents_file2):
    """ Extract keys from both file contents and identify missing keys """

    keys_file1 = extract_unique_keys(contents_file1)
    keys_file2 = extract_unique_keys(contents_file2)
    keys_not_in_file2 = find_missing_keys(keys_file1, keys_file2)

    if keys_not_in_file2:
        logging.warning(f"Keys missing in {args.file2}: {keys_not_in_file2}")
    else:
        logging.info(f"There are no keys missing in {args.file2}")

def extract_unique_keys(contents):
    """
    Based on file contents, extract the unique keys matching desired pattern
    Valid patterns include:
    KEY=VALUE
    key = value
    key == 'val'
    key ==
    """

    unique_keys = set()
    for line in contents:
        if line_matches_pattern(line):
            key = extract_key(line, "=")
            if key:
                unique_keys.add(key)

    return unique_keys

def find_missing_keys(set1, set2):
    """
    Subtracts set2 from set1 and returns the values that only exist in set1
    This method is case-sensitive where it treats ABC & abc as different keys
    """
    return set1.difference(set2) if set1 else None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file1', type=str, help='Path to first file')
    parser.add_argument('file2', type=str, help='Path to second file')
    # TODO: what if there's a third file, is it compared against the first file?
    # TODO: make max filesize customizable as a parameter
    args = parser.parse_args()

    define_log_settings()

    try:
        contents_file1 = read_file_contents(args.file1)
    except FileNotFoundError:
        logging.error(f"Unable to read {args.file1} file. Check path & file permission")
        exit(1)

    try:
        contents_file2 = read_file_contents(args.file2)
    except FileNotFoundError:
        logging.error(f"Unable to read {args.file2} file. Check path & file permission")
        exit(1)

    compare_keys_in_files(contents_file1, contents_file2)
