from turtles import turtle
from turtles import Turtle

import itertools
import pytest
import operator


def test_basic():
    assert repr(turtle(1)) == 'turtle(1)'
    assert repr(turtle[turtle]) == 'turtle[turtle]'
    assert repr(turtle(1) + turtle(foo=2)) == '(turtle(1) + turtle(foo=2))'
    assert repr(turtle(1) - turtle(foo=2)) == '(turtle(1) - turtle(foo=2))'
    assert repr(turtle.turtle) == 'turtle.turtle'


def test_unorderable():
    for op in ('ge', 'le', 'gt', 'lt'):
        with pytest.raises(TypeError):
            getattr(operator, op)(turtle.foo, turtle.bar)


def test_equal_by_name():
    assert turtle(1) == turtle(1)
    assert turtle(1) != turtle
    assert not (turtle(1) == turtle)


def test_hashable():
    assert {turtle.foo: 1}[turtle.foo] == 1
    assert set([turtle.foo]) == set([turtle.foo])


def test_iterable():
    some_turtles = list(itertools.islice(iter(turtle), 0, 3))
    assert [repr(t) for t in some_turtles] == [
        'next(turtle)',
        'next(next(turtle))',
        'next(next(next(turtle)))',
    ]


def test_custom_ninja_turtles():
    ninja = Turtle('ninja')
    assert repr(ninja[ninja](ninja)) == 'ninja[ninja](ninja)'


def test_readme_example():
    db = Turtle('db')
    record = db.get_me_a_sweet_record()
    record.name = "foo"
    record.cities[1] = "San Francisco"
    db.insert(record)
    db.commit()
    assert db.is_persistently_stored()
