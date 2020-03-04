import pytest
from app.core.paginator import pagenation

"""
In order to test behavior of pagenation function
"""


def test_pagenation_400_initial_default():

    d = pagenation(1, 20, 400, list(range(0, 400)))
    print(d["listings"])
    print(list(range(0, 20)))
    assert d["listings"] == list(range(0, 20))


def test_pagenation_400_10th_page():

    d = pagenation(10, 20, 400, list(range(0, 400)))
    print(d["listings"])
    print(list(range(180, 200)))
    assert d["listings"] == list(range(180, 200))


def test_pagenation_400_start_0():

    d = pagenation(19, 20, 400, list(range(0, 400)), start_page_as_1=False)
    print(d["listings"])
    print(list(range(380, 400)))
    assert d["listings"] == list(range(380, 400))


def test_pagenation_400_start_1():

    d = pagenation(20, 20, 400, list(range(0, 400)))
    print(d["listings"])
    print(list(range(380, 400)))
    assert d["listings"] == list(range(380, 400))


def test_pagenation_400_set_start_1_equals_True_and_init_as_pagenumber_as_0():
    """Exception case
    """
    with pytest.raises(Exception, match=r".* starts > 0. *"):
        d = pagenation(0, 20, 400, list(range(0, 400)))
