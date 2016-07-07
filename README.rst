ok |latest-version|
==============================

|build-status| |python-support| |downloads| |license|

Object-Key Mapper for Redis

If you’ve used redis on python, you’ve had to deal with redis keys.
Sometimes, *lots* of redis keys. With so many keys, it’s easy to make
mistakes, especially since keys are just strings. I built ``ok`` so that
I didn’t have to work with strings for redis keys.

Here’s how you use it:

.. code:: python

    import ok
    import redis


    class User(ok.Key):
        fields = ['timeline', 'followers', 'following']


    # Get user mixxorz' timeline
    r = redis.StrictRedis()
    r.zrevrange(User('mixxorz').timeline, 0, 50)
    # ZREVRANGE User:mixxorz:timeline 0 50

Managing your keys just became a lot less fragile.

Installation
------------

Install it from pypi

::

    $ pip install ok-redis

Usage
-----

Access fields.

.. code:: python

    class User(ok.Key):
        fields = ['timeline', 'followers', 'following']


    print(User('mixxorz').timeline)
    # User:mixxorz:timeline

Chain keys.

.. code:: python

    class City(ok.Key):
        fields = ['tweets_hll']


    class Country(ok.Key):
        subkeys = [City]


    print(Country('PH').City('Manila').tweets_hll)
    # Country:PH:City:Manila:tweets

Subkeys can be an absolute or relative path to a key.

.. code:: python

    # mod_one.py
    class Refer(Key):
        fields = ['elements']


    # mod_two.py
    class Parent(Key):
        subkeys = ['..mod_one.Refer']


    print(Parent('foo').Refer('bar').elements)
    # Parent:foo:Refer:bar:elements

The string representation of a `Key` instance is the key, so you can use it like
this:

.. code:: python

    class User(ok.Key):
        pass


    r.get(User('mixxorz'))

But you can also access the key explicitly.

.. code:: python

    User('mixxorz').key
    # >>> User:mixxorz

IDs are optional.

.. code:: python

    class User(ok.Key):
        fields = ['rankings']


    print(User().rankings)
    # User:rankings

IDs don't have to be strings

.. code:: python

    class User(ok.Key)
        pass

    print(User(123))
    # User:123

You can change the string used for the key.

.. code:: python

    class Facebook(ok.Key):
        fields = ['all_posts']
        class_key = 'fb'


    print(Facebook().all_posts)
    # fb:all_posts

License
-------

MIT

.. |latest-version| image:: https://img.shields.io/pypi/v/ok-redis.svg
    :target: https://pypi.python.org/pypi/ok-redis/
    :alt: Latest version
.. |build-status| image:: https://img.shields.io/travis/mixxorz/ok-redis/master.svg
    :target: https://travis-ci.org/mixxorz/ok-redis
    :alt: Build status
.. |python-support| image:: https://img.shields.io/pypi/pyversions/ok-redis.svg
   :target: https://pypi.python.org/pypi/ok-redis
   :alt: Python versions
.. |downloads| image:: https://img.shields.io/pypi/dm/ok-redis.svg
    :target: https://pypi.python.org/pypi/ok-redis/
    :alt: Monthly downloads
.. |license| image:: https://img.shields.io/pypi/l/ok-redis.svg
    :target: https://github.com/behave/ok-redis/blob/master/LICENSE
    :alt: Software license
