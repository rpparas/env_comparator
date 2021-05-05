from compare_env_files import find_missing_keys

def test_find_missing_keys_happy_path1():
    set1 = set(["KEY1", "KEY2"])
    set2 = set(["KEY2", "KEY3"])
    assert find_missing_keys(set1, set2) == set(["KEY1"])

def test_find_missing_keys_sad_path1():
    set1 = set([])
    set2 = set(["KEY2", "KEY3"])
    assert find_missing_keys(set1, set2) is None
