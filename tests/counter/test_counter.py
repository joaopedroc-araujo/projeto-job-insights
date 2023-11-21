import pytest
from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"
    word = "Python"

    assert count_ocurrences(path, word) == 1639

    word = "python"

    assert count_ocurrences(path, word) == 1639

    word = "xablau"

    assert count_ocurrences(path, word) == 0

    path = "data/empty.csv"
    with pytest.raises(FileNotFoundError):
        count_ocurrences(path, word)
