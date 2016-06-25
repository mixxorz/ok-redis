# ok

Object-Key Mapper for Redis

If you've used redis on python, you've had to deal with redis keys. Sometimes,
_lots_ of redis keys. With so many keys, it's easy to make typos, especially
since keys are just strings. I built `ok` so that I didn't have to work with
strings for redis keys.

Here's how you use it:

```python
import redis
from ok import Key


class User(Key):
    fields = ['timeline', 'followers', 'following']


# Get user mixxorz' timeline
r = redis.StrictRedis()
r.zrevrange(User('mixxorz').timeline, 0, 50)
# ZREVRANGE User:mixxorz:timeline 0 50
```

You can even chain keys.

```python
class City(Key):
    fields =  ['tweets_hll']


class Country(Key):
    subkeys = ['City']


r.pfcount(Country('PH').City('Manila').tweets_hll)
# pfcount Country:PH:City:Manila:tweets
```

Simple as that.
