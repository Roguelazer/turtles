class Turtle(object):
    """It's turtles all the way down."""

    __slots__ = ['name']

    def __init__(self, name='Turtle'):
        self.name = name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, Turtle):
            return other.name == self.name
        return False

    def __ne__(self, other):
        if isinstance(other, Turtle):
            return other.name != self.name
        return True

    def __gt__(self, other):
        raise TypeError('turtles are incomparable to all other matter')

    def __lt__(self, other):
        raise TypeError('turtles are incomparable to all other matter')

    def __ge__(self, other):
        raise TypeError('turtles are incomparable to all other matter')

    def __le__(self, other):
        raise TypeError('turtles are incomparable to all other matter')

    def __add__(self, other):
        return Turtle('({0!r} + {1!r})'.format(self, other))

    def __sub__(self, other):
        return Turtle('({0!r} - {1!r})'.format(self, other))

    def __hash__(self):
        return hash(self.name)

    def __nonzero__(self):
        return True

    def __getitem__(self, item):
        return Turtle('{0}[{1!r}]'.format(self.name, item))

    def __setitem__(self, key, value):
        return None

    def __delitem__(self, key):
        return None

    def __getattr__(self, attr):
        if attr == 'name':
            return object.__getattr__(self, attr)
        else:
            return Turtle(self.name + '.' + attr)

    def __setattr__(self, key, value):
        if key == 'name':
            object.__setattr__(self, key, value)
        else:
            return None

    def __call__(self, *args, **kwargs):
        if not args and not kwargs:
            return Turtle('{0}()'.format(self.name))
        elif args and not kwargs:
            return Turtle('{0}({1})'.format(
                self.name,
                ', '.join(repr(a) for a in args)
            ))
        elif kwargs and not args:
            return Turtle('{0}({1})'.format(
                self.name,
                ', '.join('{0}={1}'.format(k, repr(v)) for k, v in kwargs.items())
            ))
        else:
            return Turtle('{0}(*{1!r}, **{2!r})'.format(
                self.name,
                args,
                kwargs,
            ))

    def __enter__(self, *args, **kwargs):
        return Turtle('{0}.__enter__(*{1!r}, **{2!r})'.format(
            self.name,
            args,
            kwargs,
        ))

    def __exit__(self, *args, **kwargs):
        return None

    def __iter__(self):
        i = 0
        while True:
            yield self[i]
            i += 1


turtle = Turtle('turtle')
