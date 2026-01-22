from katas.nth_char.nth_char import nth_char


def test_basic_case():
    words = ["yoda", "best", "has"]
    assert nth_char(words) == "yes"


def test_single_word():
    words = ["python"]
    assert nth_char(words) == "p"


def test_empty_list():
    words = []
    assert nth_char(words) == ""


def test_longer_words():
    words = ["code", "kata", "tests", "pass"]
    # c[0] + a[1] + s[2] + s[3]
    assert nth_char(words) == "cass"
