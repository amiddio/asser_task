from ma import *
from mb import B


def test():
    a = A()
    b = B(5)

    assert a.i == 3
    assert a.fnc(2) == 2 * 2 * 3
    assert b.fnc(10, 4) == 10 * 4 * 5
    assert a.isFirst() == 1
    assert a.isSecond == 0
    assert b.isFirst() == 0
    assert b.isSecond == 1

    assert isinstance(a, First)
    assert isinstance(a, Parent)
    assert isinstance(b, Second)
    assert isinstance(b, Parent)

    try:
        a.fnc(7)
    except MyError as e:
        if str(e) != 'Error text':
            assert 0
    else:
        assert 0


if __name__ == '__main__':
    test()
    print('done')
