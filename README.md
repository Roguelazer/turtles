It's turtles all the way down

Usage
=====

Make your coding so easy!

```
from turtles import Turtle


def main():
    db = Turtle('db')
    record = db.get_me_a_sweet_record()
    record.name = "foo"
    record.cities[1] = "San Francisco"
    db.insert(record)
    db.commit()
    assert db.is_persistently_stored()
```
