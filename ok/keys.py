from importlib import import_module
# from . import types


def keygen(*args, **kwargs):
    """Joins strings together by a colon (default)

    This function doesn't include empty strings in the final output.
    """

    kwargs['sep'] = ':'

    cleaned_list = [arg for arg in args if arg != '']

    return kwargs['sep'].join(cleaned_list)


def import_class(name):
    module = '.'.join(name.split('.')[:-1])
    class_name = name.split('.')[-1]
    mod = import_module(module)
    return getattr(mod, class_name)


class Key(object):
    fields = []
    subkeys = []

    def __init__(self, id='', prefix='', class_key=''):
        self.id = id
        self.prefix = prefix
        self.class_key = class_key or type(self).__name__
        self.key = keygen(self.prefix, self.class_key, self.id)

    def __call__(self, id='', prefix=''):
        if not id:
            id = self.id

        if not prefix:
            prefix = self.prefix

        return type(self)(id, prefix)

    def __getattr__(self, attr):
        # Access fields
        if attr in self.fields:
            return keygen(self.key, attr)

        # Access subkeys
        string_subkeys = [subkey for subkey in self.subkeys
                          if type(subkey) == str]
        subkeys = [subkey for subkey in self.subkeys
                   if type(subkey) != str and issubclass(subkey, Key)]

        for subkey in string_subkeys:
            subkeys.append(import_class(subkey))

        if attr in [subkey.__name__ for subkey in subkeys]:
            return next(subkey for subkey in subkeys
                        if subkey.__name__ == attr)(prefix=self.key)