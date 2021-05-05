from line_parser import line_matches_pattern, extract_key

def test_line_matches_pattern_happy_path1():
    assert line_matches_pattern("ABC=val")

def test_line_matches_pattern_happy_path2():
    assert line_matches_pattern("ABC = val")

def test_line_matches_pattern_happy_path3():
    assert line_matches_pattern("ABC = val 460")

def test_line_matches_pattern_happy_path4():
    assert line_matches_pattern("ABC = 'val 180 100;'")

def test_line_matches_pattern_happy_path5():
    assert line_matches_pattern("  ABC =  lots   of   spaces   ")

def test_line_matches_pattern_happy_path6():
    assert line_matches_pattern('_b544 = "multiple words";')

def test_line_matches_pattern_sad_path1():
    assert not line_matches_pattern('')

def test_line_matches_pattern_sad_path2():
    assert not line_matches_pattern(' =  ')

def test_line_matches_pattern_sad_path3():
    assert not line_matches_pattern(None)

def test_line_matches_pattern_sad_path4():
    assert not line_matches_pattern(' no key  ')

def test_extract_key_happy_path1():
    assert extract_key('a=b') == "a"

def test_extract_key_happy_path2():
    assert extract_key('   abc123 = "xyz"') == "abc123"

def test_extract_key_happy_path3():
    assert extract_key('ABC_DE_f = b') == "ABC_DE_f"

def test_extract_key_happy_path4():
    assert extract_key('a  =  special_chars') == "a"

def test_extract_key_sad_path1():
    assert not extract_key(' = == =  ')

def test_extract_key_sad_path2():
    assert not extract_key('   ')

def test_extract_key_sad_path3():
    assert not extract_key(' separated words = value ')

def test_extract_key_sad_path4():
    assert not extract_key(' no key  ')
