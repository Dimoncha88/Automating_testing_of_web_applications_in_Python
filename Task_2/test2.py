import pytest
from checkPost import get_post, create_post

id_check = 91749
descript_check = 'Post made by pycharm'


def test_1(token):
    output = get_post(token)['data']
    res = []
    for item in output:
        res.append(item['id'])
    assert id_check in res


def test_2(token):
    output = get_post(token)['data']
    res = []
    for item in output:
        res.append(item['description'])
    assert descript_check in res
