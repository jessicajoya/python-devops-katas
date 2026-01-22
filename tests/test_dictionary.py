import pytest
from katas.dictionary.dictionary import Dictionary


def test_add_and_lookup_word():
    d = Dictionary()
    d.newentry("Apple", "A fruit that grows on trees")

    result = d.look("Apple")

    assert result == "A fruit that grows on trees"


def test_lookup_is_case_insensitive():
    d = Dictionary()
    d.newentry("Apple", "A fruit that grows on trees")

    assert d.look("apple") == "A fruit that grows on trees"
    assert d.look("APPLE") == "A fruit that grows on trees"


def test_word_not_found():
    d = Dictionary()

    result = d.look("Banana")

    assert result == "Can't find entry for Banana"


def test_overwrite_existing_entry():
    d = Dictionary()
    d.newentry("Apple", "First definition")
    d.newentry("apple", "Updated definition")

    assert d.look("APPLE") == "Updated definition"
